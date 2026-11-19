"""Inventario previo de un indexado (etapa 0 del Profile Knowledge-Indexing).

Recorre los archivos versionados de un repositorio en una revisión, sin tocar su árbol de trabajo, aplica las
exclusiones del Profile y deja, en la carpeta de salida:

- inventario.md      totales, carpetas de primer nivel, binarios por extensión, historia git (commits, merges, etiquetas);
- dominio-<NN>.md    por cada índice del mapa: sus archivos con líneas y la historia git de esas rutas;
- sin-dominio.md     los archivos de texto que ningún dominio reclama (el mapa se corrige antes de escribir);
- inventario.json    lo mismo, para máquinas.

Lo que hoy cada subagente rehace con decenas de llamadas (listar, contar, git log) se calcula una vez y se entrega.

Uso:
    python3 -I inventario.py --repo <ruta> [--rev HEAD] --salida <carpeta> [--mapa mapa.json]

mapa.json: {"01_arquitectura.md": ["GDA.Core.APP/*.cs", "GDA.Core.APP/Platforms/**", ...], ...}
Patrones estilo glob; `**` cruza carpetas. Un archivo puede caer en más de un dominio (se avisa).
"""
import argparse, collections, fnmatch, json, os, pathlib, re, subprocess, sys

EXCLUIR_CARPETAS = {".git", ".svn", ".hg", ".vs", ".vscode", ".idea", "node_modules", "packages", "vendor",
                    ".venv", "__pycache__", "bin", "obj", "dist", "build", "target", "out", "publish", "ia-db"}
BINARIOS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".ico", ".icns", ".webp", ".svg", ".ttf", ".otf", ".woff",
            ".woff2", ".zip", ".gz", ".7z", ".rar", ".tar", ".jar", ".apk", ".aab", ".ipa", ".dll", ".exe", ".so",
            ".dylib", ".a", ".lib", ".pdb", ".p12", ".pfx", ".cer", ".der", ".mobileprovision", ".keystore", ".jks",
            ".pdf", ".docx", ".xlsx", ".pptx", ".mp4", ".mov", ".mp3", ".wav", ".db", ".sqlite", ".bin"}


def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], check=True, capture_output=True, text=True).stdout


def excluido(ruta):
    return any(p in EXCLUIR_CARPETAS for p in pathlib.PurePosixPath(ruta).parts[:-1])


def glob_a_regex(patron):
    patron = patron.strip().rstrip("/")
    partes, i = [], 0
    while i < len(patron):
        if patron.startswith("**", i):
            partes.append(".*"); i += 2
            if i < len(patron) and patron[i] == "/":
                i += 1
        elif patron[i] == "*":
            partes.append("[^/]*"); i += 1
        elif patron[i] == "?":
            partes.append("[^/]"); i += 1
        else:
            partes.append(re.escape(patron[i])); i += 1
    return re.compile("^" + "".join(partes) + "(/.*)?$")


def leer_blobs(repo, rev, rutas):
    """Devuelve {ruta: (es_texto, lineas)} leyendo los blobs con una sola llamada a git cat-file."""
    proc = subprocess.Popen(["git", "-C", repo, "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out = {}
    for ruta in rutas:
        proc.stdin.write(f"{rev}:{ruta}\n".encode()); proc.stdin.flush()
        cab = proc.stdout.readline().split()
        if len(cab) < 3 or cab[1] != b"blob":
            out[ruta] = (False, 0); continue
        datos = proc.stdout.read(int(cab[2])); proc.stdout.read(1)
        texto = b"\0" not in datos[:8000] and pathlib.PurePosixPath(ruta).suffix.lower() not in BINARIOS
        out[ruta] = (texto, datos.count(b"\n") + (1 if datos and not datos.endswith(b"\n") else 0) if texto else 0)
    proc.stdin.close(); proc.wait()
    return out


def historia(repo, rev, rutas, n=40):
    if not rutas:
        return []
    lineas = git(repo, "log", "--format=%h %ad %s", "--date=short", f"-n{n}", rev, "--", *rutas).splitlines()
    return lineas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--rev", default="HEAD")
    ap.add_argument("--salida", required=True)
    ap.add_argument("--mapa")
    a = ap.parse_args()
    sal = pathlib.Path(a.salida); sal.mkdir(parents=True, exist_ok=True)
    rev = git(a.repo, "rev-parse", "--short", a.rev).strip()

    todas = [r for r in git(a.repo, "ls-tree", "-r", "--name-only", rev).splitlines()]
    rutas = [r for r in todas if not excluido(r)]
    blobs = leer_blobs(a.repo, rev, rutas)
    texto = [r for r in rutas if blobs[r][0]]
    binarios = collections.Counter(pathlib.PurePosixPath(r).suffix.lower() or "(sin ext.)" for r in rutas if not blobs[r][0])

    primer = collections.defaultdict(lambda: [0, 0, 0])
    for r in rutas:
        k = r.split("/", 1)[0] + ("/" if "/" in r else "")
        primer[k][0] += 1
        if blobs[r][0]:
            primer[k][1] += 1; primer[k][2] += blobs[r][1]

    commits = git(a.repo, "rev-list", "--count", rev).strip()
    merges = git(a.repo, "rev-list", "--count", "--merges", rev).strip()
    etiquetas = git(a.repo, "for-each-ref", "--merged", rev, "--sort=creatordate",
                    "--format=%(refname:short) %(creatordate:short)", "refs/tags").splitlines()
    total_etiquetas = len(git(a.repo, "tag").splitlines())
    ultimo = git(a.repo, "log", "-1", "--format=%h %ad %s", "--date=short", rev).strip()

    md = [f"# Inventario — {pathlib.Path(a.repo).name} @ {rev}", "",
          f"- Último commit: {ultimo}",
          f"- Commits: {commits} · merges: {merges} · etiquetas alcanzables: {len(etiquetas)} de {total_etiquetas}",
          f"- Archivos versionados: {len(todas)} · tras exclusiones del Profile: {len(rutas)} "
          f"· de texto: {len(texto)} · líneas de texto: {sum(blobs[r][1] for r in texto)}", "",
          "## Primer nivel", "", "| Ruta | Archivos | De texto | Líneas |", "|---|---:|---:|---:|"]
    md += [f"| `{k}` | {v[0]} | {v[1]} | {v[2]} |" for k, v in sorted(primer.items())]
    md += ["", "## Binarios por extensión (sólo nombre y metadatos)", "", "| Extensión | Archivos |", "|---|---:|"]
    md += [f"| `{k}` | {v} |" for k, v in binarios.most_common()]
    md += ["", "## Etiquetas", ""] + [f"- {t}" for t in etiquetas] + [""]
    (sal / "inventario.md").write_text("\n".join(md), encoding="utf-8")

    resumen = {"rev": rev, "commits": int(commits), "merges": int(merges), "etiquetas": etiquetas,
               "archivos": len(todas), "tras_exclusiones": len(rutas), "texto": len(texto),
               "lineas": {r: blobs[r][1] for r in texto}, "dominios": {}, "sin_dominio": [], "en_varios": []}
    if a.mapa:
        mapa = json.loads(pathlib.Path(a.mapa).read_text(encoding="utf-8"))
        regex = {d: [glob_a_regex(p) for p in pats] for d, pats in mapa.items()}
        dueños = collections.defaultdict(list)
        for r in texto:
            for d, rx in regex.items():
                if any(x.match(r) for x in rx):
                    dueños[r].append(d)
        for d in mapa:
            propios = sorted(r for r in texto if d in dueños[r])
            bin_propios = sorted(r for r in rutas if not blobs[r][0] and any(x.match(r) for x in regex[d]))
            resumen["dominios"][d] = propios
            hist = historia(a.repo, rev, sorted({str(pathlib.PurePosixPath(r).parent) if "/" in r else r for r in propios}))
            nn = d.split("_", 1)[0]
            cuerpo = [f"# Dominio {d} — {len(propios)} archivos de texto, {sum(blobs[r][1] for r in propios)} líneas",
                      "", "| Archivo | Líneas |", "|---|---:|"] + [f"| `{r}` | {blobs[r][1]} |" for r in propios]
            if bin_propios:
                cuerpo += ["", f"## Binarios del dominio ({len(bin_propios)}, sólo nombre: no se leen ni se transcriben)", ""]
                cuerpo += [f"- `{r}`" for r in bin_propios]
            cuerpo += ["", f"## Historia git de esas carpetas (últimos {len(hist)})", "", "```text", *hist, "```", ""]
            (sal / f"dominio-{nn}.md").write_text("\n".join(cuerpo), encoding="utf-8")
        resumen["sin_dominio"] = sorted(r for r in texto if not dueños[r])
        resumen["en_varios"] = sorted(f"{r}: {', '.join(v)}" for r, v in dueños.items() if len(v) > 1)
        (sal / "sin-dominio.md").write_text(
            "# Archivos de texto sin dominio\n\n" + "\n".join(f"- `{r}`" for r in resumen["sin_dominio"]) + "\n"
            + ("\n## En más de un dominio\n\n" + "\n".join(f"- {x}" for x in resumen["en_varios"]) + "\n"
               if resumen["en_varios"] else ""), encoding="utf-8")
    (sal / "inventario.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{rev}: {len(rutas)} archivos tras exclusiones, {len(texto)} de texto"
          + (f"; sin dominio: {len(resumen['sin_dominio'])}; en varios: {len(resumen['en_varios'])}" if a.mapa else ""))


if __name__ == "__main__":
    sys.exit(main())
