"""Verificación mecánica de una ia-db (etapa 2a del Profile Knowledge-Indexing).

Comprueba, sin modelo, lo que no requiere juicio, y deja el juicio al verificador adversarial:

1. Forma: README.md con «Manifiesto de generación»; cada índice con blockquote inicial, sección «Fuentes» y tamaño
   dentro del presupuesto.
2. Citas `ruta#Lx-Ly`: el archivo existe en la revisión y el rango cae dentro de él. Las abreviadas (sólo nombre de
   archivo) se resuelven si el nombre es único; las contextuales (`#Lx` suelto) se cuentan y no se comprueban: su
   proporción mide cuánto de la base queda fuera de la verificación mecánica.
3. Remisiones «ver NN §x»: existe el índice NN y una sección §x en él.
4. Secretos: patrones de tokens, claves privadas y ApiKey en el texto de la base.
5. Cobertura: archivos de texto de la revisión que ninguna sección «Fuentes» cubre.

Uso:
    python3 -I verificar_ia_db.py --ia-db <ruta> --repo <ruta> [--rev HEAD] [--doc-root <ruta>]
           [--doc-prefijo Documentacion:] [--min 300] [--max 550] [--indices 03_x.md,10_y.md] [--json salida.json]

Sale con 1 si hay citas rotas o fuera de rango, remisiones rotas o secretos; los avisos de forma y cobertura no cortan.
"""
import argparse, collections, json, pathlib, re, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from inventario import excluido, glob_a_regex, leer_blobs  # noqa: E402

CITA = re.compile(r"`([^`\s]*?)#L(\d+)(?:-L?(\d+))?`")
REMISION = re.compile(r"\bver (\d{2})(?:\s*§\s*(\d+(?:\.\d+)*))?")
SECRETOS = [
    ("token GitHub", re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}")),
    ("clave AWS", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("clave privada PEM", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----\s*\n\s*[A-Za-z0-9+/]{40,}")),
    ("ApiKey pd_", re.compile(r"\bpd_[A-Za-z0-9]{16,}")),
    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.")),
    ("contraseña literal", re.compile(r"(?i)\b(pass(word)?|contraseña|clave)\s*[:=]\s*[\"']?[^\s\"'`|)(]{6,}")),
]
REDACTADO = re.compile(r"(?i)redactad|\(valor|<[^>]+>|\$\{|\$[A-Z_]+|secrets\.|\*{3,}")


def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], check=True, capture_output=True, text=True).stdout


def secciones(texto):
    return {m.group(1) for m in re.finditer(r"^#{1,6}\s*§\s*(\d+(?:\.\d+)*)", texto, re.M)}


def bloque_fuentes(texto):
    m = re.search(r"^#{1,6}\s*(?:§\s*\d+\s*)?Fuentes\b.*?$(.*?)(?=^#{1,2}\s|\Z)", texto, re.M | re.S)
    return m.group(1) if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ia-db", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--rev", default="HEAD")
    ap.add_argument("--doc-root")
    ap.add_argument("--doc-prefijo", default="Documentacion:")
    ap.add_argument("--min", type=int, default=300)
    ap.add_argument("--max", type=int, default=550)
    ap.add_argument("--indices", help="lista separada por comas; por defecto todos")
    ap.add_argument("--json")
    a = ap.parse_args()

    base = pathlib.Path(a.ia_db)
    carpeta = base / "indexes" if (base / "indexes").is_dir() else base
    rev = git(a.repo, "rev-parse", "--short", a.rev).strip()
    todas = [r for r in git(a.repo, "ls-tree", "-r", "--name-only", rev).splitlines()]
    blobs = leer_blobs(a.repo, rev, [r for r in todas if not excluido(r)])
    lineas = {r: n for r, (t, n) in blobs.items()}

    def largo_doc(ruta):
        p = pathlib.Path(a.doc_root or "/nonexistent") / ruta
        return sum(1 for _ in p.open(encoding="utf-8", errors="replace")) if p.is_file() else None

    indices = sorted(carpeta.glob("[0-9][0-9]_*.md"))
    if a.indices:
        quiero = {x.strip() for x in a.indices.split(",")}
        indices = [p for p in indices if p.name in quiero]
    todos_los_indices = {p.name[:2]: p for p in sorted(carpeta.glob("[0-9][0-9]_*.md"))}
    secc = {nn: secciones(p.read_text(encoding="utf-8")) for nn, p in todos_los_indices.items()}

    rep = {"rev": rev, "indices": {}, "forma": [], "secretos": [], "sin_cubrir": []}
    readme = base / "README.md"
    if not a.indices:
        if not readme.is_file():
            rep["forma"].append("falta README.md")
        elif "Manifiesto de generación" not in readme.read_text(encoding="utf-8"):
            rep["forma"].append("README.md sin «Manifiesto de generación»")

    patrones_fuentes = []
    # El README también lleva citas (resumen, avisos): se comprueban igual, sin exigirle forma de índice.
    revisar = indices + ([readme] if not a.indices and readme.is_file() else [])
    for p in revisar:
        t = p.read_text(encoding="utf-8")
        n = t.count("\n") + 1
        c = collections.Counter(); rotas = []
        for nl, linea in enumerate(t.splitlines(), 1):
            for m in CITA.finditer(linea):
                ruta, x, y = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
                if not ruta:
                    c["contextuales"] += 1  # `#Lx` suelto: el archivo está en otra celda o en el encabezado; no se comprueba
                    continue
                if ruta.startswith(a.doc_prefijo):
                    total = largo_doc(ruta[len(a.doc_prefijo):])
                    if total is None:
                        c["rotas"] += 1; rotas.append(f"L{nl} `{m.group(0)}`: no existe"); continue
                elif ruta in lineas:
                    total = lineas[ruta]; c["completas"] += 1
                else:
                    # Abreviada: sólo el nombre, o una ruta parcial (sin las carpetas de arriba). Vale si es única.
                    candidatas = [r for r in lineas if r == ruta or r.endswith("/" + ruta)]
                    if len(candidatas) == 1:
                        ruta = candidatas[0]; total = lineas[ruta]; c["abreviadas"] += 1
                    elif candidatas:
                        c["ambiguas"] += 1; rotas.append(f"L{nl} `{m.group(0)}`: ruta ambigua ({len(candidatas)} archivos)"); continue
                    else:
                        c["rotas"] += 1; rotas.append(f"L{nl} `{m.group(0)}`: no existe en {rev}"); continue
                if x < 1 or y < x or y > total:
                    c["fuera_de_rango"] += 1; rotas.append(f"L{nl} `{m.group(0)}`: el archivo tiene {total} líneas")
            for m in REMISION.finditer(linea):
                nn, s = m.group(1), m.group(2)
                c["remisiones"] += 1
                if nn not in todos_los_indices:
                    c["remisiones_rotas"] += 1; rotas.append(f"L{nl} «{m.group(0)}»: no existe el índice {nn}")
                elif s and s not in secc[nn] and s.split(".")[0] not in secc[nn]:
                    c["remisiones_rotas"] += 1; rotas.append(f"L{nl} «{m.group(0)}»: {nn} no tiene §{s}")
            for nombre, rx in SECRETOS:
                if rx.search(linea) and not REDACTADO.search(linea):
                    rep["secretos"].append(f"{p.name} L{nl}: posible {nombre}")
        forma = []
        if p == readme:
            rep["indices"][p.name] = {"lineas": n, **c, "citas": sum(c[k] for k in ("completas", "abreviadas", "contextuales", "rotas", "ambiguas")),
                                      "problemas": rotas, "forma": []}
            continue
        if not re.search(r"^>", "\n".join(t.splitlines()[:15]), re.M):
            forma.append("sin blockquote inicial")
        fuentes = bloque_fuentes(t)
        if not fuentes:
            forma.append("sin sección «Fuentes»")
        if not (a.min <= n <= a.max):
            forma.append(f"{n} líneas, fuera de {a.min}–{a.max}")
        patrones_fuentes += [x for x in re.findall(r"`([^`\s]+)`", fuentes) if not x.startswith(a.doc_prefijo)]
        citadas = sum(c[k] for k in ("completas", "abreviadas", "contextuales"))
        rep["indices"][p.name] = {"lineas": n, **c, "citas": citadas + c["rotas"] + c["ambiguas"],
                                  "problemas": rotas, "forma": forma}

    rx = [glob_a_regex(x.split("#", 1)[0]) for x in patrones_fuentes if x.split("#", 1)[0]]
    texto = [r for r, (t, _) in blobs.items() if t]
    if not a.indices:
        rep["sin_cubrir"] = sorted(r for r in texto if not any(x.match(r) for x in rx))
    rep["cobertura"] = None if a.indices else round(100 * (1 - len(rep["sin_cubrir"]) / max(1, len(texto))), 1)

    graves = sum(v.get("rotas", 0) + v.get("fuera_de_rango", 0) + v.get("ambiguas", 0) + v.get("remisiones_rotas", 0)
                 for v in rep["indices"].values()) + len(rep["secretos"])
    print(f"ia-db {base} contra {rev}")
    print(f"{'índice':40} {'lín':>4} {'citas':>5} {'compl':>5} {'abrev':>5} {'ctx':>4} {'rotas':>5} {'rango':>5} {'remis':>5} {'r.rot':>5}  forma")
    for nombre, v in rep["indices"].items():
        print(f"{nombre:40} {v['lineas']:>4} {v['citas']:>5} {v.get('completas',0):>5} {v.get('abreviadas',0):>5} "
              f"{v.get('contextuales',0):>4} {v.get('rotas',0)+v.get('ambiguas',0):>5} {v.get('fuera_de_rango',0):>5} "
              f"{v.get('remisiones',0):>5} {v.get('remisiones_rotas',0):>5}  {'; '.join(v['forma']) or 'ok'}")
    for nombre, v in rep["indices"].items():
        for x in v["problemas"]:
            print(f"  {nombre}: {x}")
    for x in rep["forma"] + rep["secretos"]:
        print("  " + x)
    if rep["cobertura"] is not None:
        print(f"cobertura de «Fuentes»: {rep['cobertura']} % ({len(rep['sin_cubrir'])} archivos de texto sin cubrir)")
        for r in rep["sin_cubrir"][:60]:
            print("  sin cubrir:", r)
    print(f"problemas graves: {graves}")
    if a.json:
        pathlib.Path(a.json).write_text(json.dumps(rep, ensure_ascii=False, indent=1), encoding="utf-8")
    return 1 if graves else 0


if __name__ == "__main__":
    sys.exit(main())
