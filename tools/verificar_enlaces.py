"""Verifica que los enlaces relativos de los .md que caen dentro del repositorio apunten a archivos existentes del repositorio."""
import pathlib, re, sys, urllib.parse

raiz = pathlib.Path(__file__).resolve().parent.parent
patron = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
rotos = []
for md in sorted(raiz.rglob("*.md")):
    if ".git" in md.parts:
        continue
    texto = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8", errors="replace"), flags=re.S)
    for destino in patron.findall(texto):
        if re.match(r"^[a-z][a-z0-9+.-]*:", destino, re.I) or destino.startswith("#"):
            continue
        ruta = urllib.parse.unquote(destino.split("#", 1)[0].strip("<>"))
        if not ruta:
            continue
        objetivo = (raiz / ruta.lstrip("/")) if ruta.startswith("/") else (md.parent / ruta)
        try:
            objetivo.resolve().relative_to(raiz)
        except ValueError:
            continue  # enlace al espacio de trabajo, fuera del repositorio: no se verifica acá
        if not objetivo.exists():
            rotos.append(f"{md.relative_to(raiz)}: {destino}")
for r in rotos:
    print("roto:", r)
print(f"enlaces rotos: {len(rotos)}")
sys.exit(1 if rotos else 0)
