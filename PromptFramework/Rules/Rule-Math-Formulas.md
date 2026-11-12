# Rule — Math-Formulas

## Objetivo

Cómo se escriben fórmulas matemáticas en la documentación Markdown, en especial en las guías de estudio: cuándo conviene una fórmula, qué sintaxis usar, dónde se ve renderizada y cómo se redacta para que la entiendan un lector humano y un agente de IA. Complementa a `Rule-Markdown` (formato) y a `Rule-Dual-Audience` (doble audiencia).

Todo dato de soporte por visor sale de la documentación oficial citada en [Fuentes](#fuentes); lo que no pudo confirmarse se marca **no confirmado**.

## Índice

1. [Cuándo usar fórmula](#cuándo-usar-fórmula)
2. [Sintaxis](#sintaxis)
3. [Soporte por visor](#soporte-por-visor)
4. [Reglas de estilo para guías](#reglas-de-estilo-para-guías)
5. [Errores comunes y verificación](#errores-comunes-y-verificación)
6. [Ejemplo completo](#ejemplo-completo)
7. [Fuentes](#fuentes)

---

# Cuándo usar fórmula

- **Sí**: cuando la relación entre magnitudes es el contenido (una ley, un cálculo, una cota) y la notación la hace más clara que la prosa.
- **No**: para un número suelto, una unidad o una comparación simple que se lee igual en texto (`el timeout es 30 s`). Tampoco como adorno.
- Si el visor destino no renderiza fórmulas (ver tabla), escribir la relación en texto o en un bloque de código sin lenguaje.

---

# Sintaxis

Las fórmulas se escriben en notación LaTeX (modo matemático) dentro del Markdown.

| Forma | Escritura | Uso |
|-------|-----------|-----|
| En línea | `$a^2 + b^2 = c^2$` | Fórmula breve dentro de una oración |
| En línea, protegida | `` $`a_1 * b_1`$ `` | Cuando la expresión contiene caracteres de la sintaxis Markdown (`*`, `_`, `` ` ``) |
| Bloque | `$$` en líneas propias, fórmula en medio | Fórmula destacada, en su propio renglón |
| Bloque `math` | bloque de código con lenguaje `math` | Igual que `$$`, sin delimitadores; preferido en GitHub/GitLab |

Ejemplo en línea: la energía es $E = mc^2$.

Ejemplo en bloque:

$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$

Ejemplo con bloque `math`:

```math
\int_0^\infty e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}
```

Entornos de uso frecuente cubiertos por KaTeX y por MathJax: `matrix`, `pmatrix`, `bmatrix`, `cases`, `aligned` (en MathJax, `aligned` viene de la extensión `ams`, cargada salvo con `input/tex-base`).

## Signo pesos literal

- Dentro de una fórmula: `\$`.
- Fuera de la fórmula, en una línea que también tiene fórmulas: en GitHub, envolver el `$` en `<span>$</span>`; en Pandoc, `\$`.
- Pandoc no toma como fórmula un `$` de cierre seguido de un dígito (`$20,000 and $30,000` queda como texto); la regla general es no confiar en eso y escapar.

---

# Soporte por visor

| Visor | En línea `$` | Bloque `$$` | ```` ```math ```` | `` $`…`$ `` | Motor | Notas |
|-------|:-:|:-:|:-:|:-:|-------|-------|
| GitHub | sí | sí | sí | sí | MathJax | El bloque `$$` empieza en una línea nueva; la fórmula va entre el `$$` de apertura y el de cierre |
| GitLab | sí | sí | sí | sí | KaTeX | En issues/MR renderiza sólo las primeras 1000 fórmulas en línea; wiki y archivos del repo no tienen ese límite |
| VS Code (vista previa integrada) | sí | sí | no confirmado | no confirmado | KaTeX | Activo desde 1.58; se apaga con `"markdown.math.enabled": false` |
| VS Code + Markdown Preview Enhanced | sí (también `\(…\)`) | sí (también `\[…\]`) | sí | no confirmado | KaTeX o MathJax (configurable) | Motor por defecto: no confirmado |
| Pandoc | sí | sí | sí (`tex_math_gfm`) | sí (`tex_math_gfm`) | según salida | `tex_math_gfm` activa por defecto sólo en `gfm`; ver abajo |
| Obsidian | sí | sí | no confirmado | no confirmado | MathJax | |
| Typora | requiere habilitarlo | sí | no confirmado | no confirmado | MathJax | `$` en línea: Preferencias → Markdown, y reiniciar |
| Visor Markdown básico | no | no | no | no | — | Se ve el texto crudo con los `$` |

**Pandoc**: `$…$` y `$$…$$` vienen de la extensión `tex_math_dollars` (activa por defecto en el markdown de Pandoc, `commonmark_x`, `gfm` e `ipynb`, entre otros; para un formato dado, `pandoc --list-extensions=FORMAT`). A HTML, sin opción usa MathML; para MathJax o KaTeX se usa `--math-method=mathjax` o `--math-method=katex` (`--mathjax` y `--katex` están marcadas como obsoletas). A PDF usa LaTeX por defecto (`pdflatex`), lo que exige un motor LaTeX instalado. En `$$…$$` no se admiten líneas en blanco dentro.

**Mermaid**: desde v10.9.0 acepta fórmulas entre `$$` en etiquetas de nodos y aristas, sólo en flowchart y sequence diagram (`A["$$x^2$$"] -->|"$$\sqrt{x+3}$$"| B`). Que GitHub lo renderice dentro de Mermaid **no está documentado**: probarlo en el repo antes de usarlo.

**KaTeX y MathJax**: interpretan sólo las funciones y extensiones que documentan; no hay `\usepackage`. KaTeX se declara más rápido; MathJax admite además MathML y AsciiMath como entrada.

---

# Reglas de estilo para guías

1. **Definir cada símbolo en su primer uso**, en la oración que sigue a la fórmula («donde $v$ es la velocidad en m/s»), y registrarlo en el glosario.
2. **Unidades explícitas** en la definición del símbolo o con `\,\mathrm{m/s}` dentro de la fórmula; nunca implícitas.
3. **Una fórmula por idea**: no encadenar en un bloque relaciones distintas; si se derivan pasos, usar `aligned` con un paso por renglón.
4. **Numerar las que se citan** con un rótulo en texto junto al bloque (`(F-1)`) y citarlas por ese rótulo; no depender de `\tag`, cuyo soporte varía por visor.
5. **Lectura en palabras**: toda fórmula en bloque va acompañada de su lectura en prosa («la suma de los primeros $n$ naturales es $n(n+1)/2$»). Sirve al lector humano, al agente que razona sobre el texto y a quien abre la guía en un visor sin render (`Rule-Dual-Audience`).
6. **Sólo comandos documentados por KaTeX y MathJax**; nada de paquetes LaTeX arbitrarios.
7. **Escapar todo `$` literal** (precios, variables de shell) según [Signo pesos literal](#signo-pesos-literal).
8. **Evitar fórmulas en tablas complejas** (el `|` puede chocar con la sintaxis de tabla de GFM y exige escaparlo como `\|`) y **dentro de Mermaid** salvo que el visor destino lo soporte comprobadamente.
9. **Preferir el bloque `math`** cuando el destino principal es GitHub o GitLab; `$$` cuando importa también VS Code u Obsidian.

---

# Errores comunes y verificación

| Síntoma | Causa | Corrección |
|---------|-------|------------|
| Se ven los `$` crudos | Visor sin soporte, o, en Pandoc, espacio después del `$` que abre o antes del que cierra | Quitar los espacios; verificar en un visor con soporte |
| Un precio se volvió fórmula | `$` literal sin escapar | `\$` o `<span>$</span>` |
| Subíndices en cursiva rara o texto en negrita dentro de la fórmula | `_` o `*` interpretados como Markdown | Usar `` $`…`$ `` o bloque `math` |
| Bloque `$$` roto en Pandoc | Línea en blanco dentro del bloque | Quitarla |
| Comando no reconocido (texto en rojo) | Comando fuera de KaTeX/MathJax | Reescribir con comandos soportados |

**Verificar el render** antes de cerrar el documento: vista previa integrada de VS Code (KaTeX) y, si el destino es GitHub, la vista del archivo en la rama o el PR (MathJax). Si los motores difieren, usar sólo construcciones que rendericen bien en ambos.

---

# Ejemplo completo

Ilustrativo.

La velocidad media de un móvil es el cociente entre el desplazamiento y el tiempo empleado, **(F-1)**:

```math
\bar{v} = \frac{\Delta x}{\Delta t}
```

donde $\bar{v}$ es la velocidad media en m/s, $\Delta x$ el desplazamiento en metros y $\Delta t$ el intervalo en segundos. En palabras: cuántos metros avanza, en promedio, por cada segundo. Con $\Delta x = 100\,\mathrm{m}$ y $\Delta t = 20\,\mathrm{s}$, (F-1) da $\bar{v} = 5\,\mathrm{m/s}$.

---

# Fuentes

Consultadas el 2026-11-12.

- GitHub — [Writing mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)
- GitLab — [Markdown, sección Math](https://docs.gitlab.com/user/markdown/)
- VS Code — [Markdown](https://code.visualstudio.com/docs/languages/markdown) y [notas de la 1.58](https://code.visualstudio.com/updates/v1_58)
- Markdown Preview Enhanced — [docs/math.md](https://raw.githubusercontent.com/shd101wyy/markdown-preview-enhanced/master/docs/math.md)
- Pandoc — [Manual](https://pandoc.org/MANUAL.html)
- Mermaid — [Math Configuration (v10.9.0+)](https://mermaid.js.org/config/math.html)
- KaTeX — [katex.org](https://katex.org/) y [funciones soportadas](https://katex.org/docs/supported)
- MathJax — [extensión ams](https://docs.mathjax.org/en/latest/input/tex/extensions/ams.html)
- MkDocs Material — [Math](https://squidfunk.github.io/mkdocs-material/reference/math/)
- Obsidian — [Advanced syntax](https://obsidian.md/help/advanced-syntax)
- Typora — [Math](https://support.typora.io/Math/)
