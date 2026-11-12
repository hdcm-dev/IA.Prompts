# Profile — Study Guide Documentation Con Ilustraciones

> Este Profile contiene **íntegro** el contenido de `Study-Guide-Documentation` (secciones *Objetivo* a *Resultado esperado*) y suma el aprendizaje de una guía de estudio extensa redactada por una mesa en cinco rondas: el **estilo formal-narrativo**, las **respuestas explicativas** a preguntas guía, propuestas y temas abiertos, la **evidencia con marcas**, las **ilustraciones como evidencia**, las **fórmulas** y el **proceso por rondas**. Lo agregado empieza en [Estilo formal-narrativo](#estilo-formal-narrativo).

## Objetivo

Configurar el agente para construir una **guía de estudio**: un cuerpo documental formativo sobre una temática, organizado como recorrido de aprendizaje y no como colección de fichas sueltas. El lector debe terminar entendiendo cada tema y con criterio para intervenir en él: elegir, producir y evaluar los artefactos del dominio.

La temática, el alcance y el destino los aporta el Prompt. Este Profile define cómo se estructura, se redacta y se valida la guía, cualquiera sea el tema.

Esta variante se elige cuando la guía, además, debe **leerse con gusto por un humano sin perder los atajos de un agente**: cada bloque formal queda intacto y lo continúa un tramo narrativo; las preguntas, propuestas y temas abiertos llevan respuesta explicada; toda afirmación lleva marca de evidencia; y las imágenes (capturas anotadas, esquemas propios, renders 3D, diagramas) funcionan como evidencia visual.

## De dónde sale lo agregado

Cada regla nueva declara su origen:

- **[Pedido]**: pedido literal del dueño del proyecto donde nació el estilo. Los pedidos que lo fundan, textuales:
  - P-1, respuestas explicativas: «a las preguntas guías que sirven para formar criterio les agregaria respuestas explicativas, explicando no solo lo que se pregunta, sino porque y que significa, de alguna manera es una retroalimentación al cuerpo del texto».
  - P-2, propuestas y atajos: «ok decis una propuesta, y que esperaria o para que»; «como lector como agente humano es un texto dificil de leer, muy sintetico - y como agente IA, esta bien que le inserte los atajos que ayudan a los agentes IA a encontrar y razonar mejor».
  - P-3, evidencia y abiertos: «incluya frases y extractos evidenciando y defendiendo y proponiendo, explicando que se espera o que se pretende, - dejando abierto temas como interrogantes y supuestos que se especulan sobre el tema como para abrir puntos futuros de trabajo».
  - P-4, formato narrativo: «uno va dando formalidad al concepto, pero tambien esta bien construir un formato narrativo que continue y complemente a la formalidad, y con eso se va nutriendo de recursos, como un texto explicativo, puede que lo combine con un ejemplo para dar contexto y salir de la estructura y formar la idea, plantear una pregunta y seguir con la respuesta que responda explicando desde un formato mas ameno y práctico ayudando al lector a encontrar los fundamentos y al mismo tiempo formando una imagen de la idea».
  - P-5, ilustraciones: «ir incluyendo imagenes, e incluso podes remarcar hallazgos en dichas imagenes»; capturas «como evidencia visual»; «crear esquemas personalizados, y capturar imagenes 3d».
  - P-6, fórmulas: «mejorar la escrituda de las formulas y revisarlas».
  - Reglas que el dueño repite: secciones jerárquicas, definiciones, ejemplos claros, mermaid cuando haga falta, autocontenido, con índices; no inventar; toda afirmación con evidencia verificable.
- **[Mesa]**: práctica de la mesa de redacción, asentada en sus registros (revisión explicativa, auditorías académica y editorial por parte, verificación, armonía, láminas, fórmulas).

Los **casos de origen** citados (sección y extracto breve) vienen de esa guía, un tratado de modelos de un proyecto de investigación (versión 1.5, ~8300 líneas). Sólo ilustran: las reglas valen para cualquier tema. Donde dice «corpus», léase «las fuentes primarias del tema: expedientes, actas, código, datos, testimonios».

---

# Framework

## Rule Set

Aplicar:

- `/IA/IA.Prompts/PromptFramework/RuleSets/RuleSet-Study-Guide-Con-Ilustraciones.md`

(= `RuleSet-Study-Guide`, que ya incluye `Rule-Math-Formulas`, más `Rule-Illustrations`.)

---

# Enfoque

Diseñar el mapa antes de escribir las piezas. Primero se fija el **marco de referencia** de la guía —el vocabulario común que después reaparece en todos los documentos—, y recién entonces se desarrolla cada tema sobre ese marco.

El marco de referencia se compone de tres ejes que el Prompt instancia según la temática:

| Eje | Qué fija | Rol en la guía |
|-----|----------|----------------|
| Escenarios | Situaciones típicas en las que se aplica el tema | Cada documento explica qué aporta el tema en cada escenario |
| Contextos | Entornos o variantes donde cambian las respuestas | Diferencian el tratamiento dentro de un mismo escenario |
| Actores | Roles que intervienen, con responsabilidades y alcance | Ubican al lector: qué le toca decidir y qué no |

Los ejes se definen una sola vez, en documentos propios, y el resto de la guía los referencia. Un tema que no se cruza con ningún escenario ni contexto sobra o está mal delimitado.

Ir de lo general a lo particular: mapa conceptual → ejes → un documento por tema → anexos.

---

# Objetivos específicos

Producir, cuando corresponda a la temática:

| Pieza | Contenido |
|-------|-----------|
| Marco de referencia | Escenarios, contextos y actores del dominio, definidos y nombrados de forma estable |
| Mapa conceptual | Tablas de entrada por escenario, por contexto y por artefacto: «estoy acá → qué aplico» |
| Documentos por tema | Un documento por unidad temática del dominio, todos con la misma estructura interna |
| Métodos y marcos | Enfoques alternativos del dominio: en qué consiste cada uno, en qué se diferencian, criterios para elegir |
| Anexos | Plantillas comentadas, listas de verificación y glosario |
| README | Tabla de contenido de todo lo generado, con la ruta de lectura sugerida |

---

# Estructura de cada documento temático

Todos los documentos temáticos siguen el mismo patrón, para que el lector aprenda una sola forma de leer:

1. **Definición** — qué es, qué problema resuelve, qué no es.
2. **Aplicación por escenario** — qué aporta en cada escenario del marco, y qué cambia según el contexto.
3. **Ejemplos concretos** — casos reales del dominio, no descripciones abstractas.
4. **Preguntas guía** — las que el lector debe poder responder para producir o evaluar el artefacto tratado.
5. **Criterios de calidad** — cómo se distingue una versión buena de una pobre.
6. **Anexo** — plantilla comentada, con las preguntas que guían cada campo.

En esta variante, cada pieza formal de esa estructura (definición, propuesta, tema abierto, bloque de preguntas guía) lleva **debajo** su bloque explicativo y su tramo narrativo, con marcador invisible; y los temas que lo necesitan cierran con **Propuestas** y **Temas abiertos** explicados. Ver [Estilo formal-narrativo](#estilo-formal-narrativo) y [Respuestas explicativas](#respuestas-explicativas-preguntas-propuestas-y-abiertos).

---

# Criterios de calidad

- **Formativo, no enciclopédico**: cada sección deja al lector en condiciones de decidir, no solo de reconocer términos.
- **Trazable**: definiciones y prácticas se anclan a estándares o fuentes de la industria; lo que es criterio propio se declara como tal (`Rule-Evidences.md`).
- **Consistente**: la misma terminología, la misma estructura y los mismos escenarios en toda la guía; una sola voz de autor (`Rule-Narrative-Voice.md`).
- **Interconectado**: cada documento enlaza con los que lo preceden y lo continúan; ningún documento queda huérfano del mapa conceptual.
- **Verificable**: al cerrar, se revisa la guía completa contra el mapa buscando huecos, solapamientos y contradicciones, y se corrigen.

---

# Diagramas típicos

Mapa conceptual del dominio, relación entre escenarios y artefactos, flujos por rol, líneas de tiempo de un proceso, taxonomías. Diagramas como código (`Rule-Dual-Audience.md`). Las fórmulas matemáticas siguen `Rule-Math-Formulas.md`: sintaxis LaTeX en Markdown, cada símbolo definido y cada fórmula acompañada de su lectura en palabras.

En esta variante las imágenes son evidencia y siguen `Rule-Illustrations.md`: capturas anotadas de lo que produjo el sistema estudiado, esquemas propios, renders 3D del objeto físico y diagramas como código, con pie, marca, manifiesto y verificación visual. Ver [Ilustraciones como evidencia](#ilustraciones-como-evidencia) y [Fórmulas](#fórmulas).

---

# Resultado esperado

Un conjunto documental navegable desde su README, que permita a un lector sin conocimiento previo recorrer la temática de forma ordenada, ubicarse en un escenario concreto y saber qué producir, y formar criterio suficiente para intervenir como uno de los actores del dominio.

En esta variante, además, cada concepto queda dicho dos veces sin contradecirse: una en forma formal, citable por un agente, y otra en un tramo narrativo que un lector humano recorre con gusto, sale con los fundamentos ubicados y con una imagen de la idea. Ninguna explicación agrega evidencia que la forma formal no tenga.

---

# Estilo formal-narrativo

La forma formal (definiciones con id, marcas, tablas, remisiones) es el atajo del agente; el tramo narrativo es el camino del lector. Ninguno reemplaza al otro. [Pedido P-2, P-4]

## Cómo se ve

Un bloque formal y su continuación. Ejemplo genérico (una guía sobre colas de mensajes); la fecha, la cifra, la fuente y las marcas son **ficticias**, sólo muestran la forma: en una guía real, FN-4 exige que salgan del corpus.

```markdown
**Def. 4.2 (Entrega al menos una vez).** El broker reintenta hasta recibir confirmación;
el consumidor puede ver un mensaje más de una vez. `[DOC]` (manual del broker §3.1)

<!-- RE:NARR -->
**En palabras llanas: el pedido que llegó dos veces.**
En la corrida del 12 de marzo, el registro de pagos muestra dos cobros con el mismo
identificador (informe de incidentes, l. 88) `[MED]`. ¿Falló el broker? No: cumplió
exactamente lo que promete la Def. 4.2. Lo que faltaba era que el consumidor
reconociera el identificador repetido.

La imagen: un cartero que, si no le firman el acuse, vuelve a tocar el timbre
(imagen de la guía, no de la fuente). Queda abierto si el costo de deduplicar en el
consumidor supera al de una entrega exactamente una vez `[ESP]`.
```

## Reglas

| Id | Regla | Caso de origen (sección: extracto) | Origen |
|----|-------|------------------------------------|--------|
| FN-1 | **Primero lo formal, intacto; debajo el tramo narrativo.** Nunca al revés ni mezclados. Explicar no borra ids, marcas, tablas ni remisiones: conservar y sumar. | I.2.4: tras los campos de la Pr. 1, «**Pr. 1, contado con un caso.** Quien abra el código del programa se encuentra con dos archivos que no se conocen.» | [Pedido P-4: «continue y complemente a la formalidad»]; [Mesa] regla «conservar y sumar» de la revisión explicativa |
| FN-2 | **Marcador invisible único** antes de cada tramo y bloque explicativo (`<!-- RE:NARR -->`, `RE:PG`, `RE:PROP`, `RE:TA`…), de una **lista única** declarada una sola vez en el capítulo «cómo leer». Una sola grafía por marcador. | I.1.2.4: «Ésta es la **lista única** de marcadores de toda la obra». La mesa unificó 14 `RE:NAR` en `RE:NARR`. | [Pedido P-2: atajos para agentes]; [Mesa] corrección de coherencia y armonía |
| FN-3 | **Rótulo de apertura de un repertorio cerrado y declarado**, con subtítulo que ya dice la idea: «En palabras llanas: ‹idea›», «Contado de otra manera», «Para formarse la imagen», «‹id›, contado con un caso». | III.2.7: «**En palabras llanas: un diez por ciento que no es un hecho.**» (en la obra: 22, 19, 11 y 5 usos de cada forma) | [Mesa] |
| FN-4 | **Anclar en un caso concreto del propio corpus**, citado: una cifra, una corrida, una escena, una frase literal. Nunca un ejemplo inventado presentado como dato. | II.2.9: «"Con σ_h = σ_e = 0,1 sale **0,98 contra 0,98: indistinguibles**"» con su fuente y marca heredada. | [Pedido P-4: «un ejemplo para dar contexto y salir de la estructura»] |
| FN-5 | **Pregunta del lector, respondida en la oración siguiente**, en llano. Puede encadenarse pregunta → respuesta corta → pregunta hasta llegar al fundamento. | III.2.7: «¿Es un hecho sobre la mente? No: es el punto donde se clava el termostato.» III.1.8: «¿Qué regla? La B […]. ¿Qué lazo? De ganancia […]. ¿Estructura o pesos? Pesos.» | [Pedido P-4: «plantear una pregunta y seguir con la respuesta»] |
| FN-6 | **Traducir el dato a lo que significa** para quien lee, sin tecnicismo. | II.2.9: «¿Qué dice eso, en llano? Que si uno sólo mira cuánto se parecen dos señales, un eco bien hecho y un hecho real se parecen igual.» | [Pedido P-1: «porque y que significa»] |
| FN-7 | **Cerrar con una imagen retenible** (analogía o escena, una o dos frases). Si no viene de la fuente, se rotula como imagen de la guía. | II.2.9: «La imagen: dos testigos que cuentan lo mismo con las mismas palabras no son más creíbles por eso». I.3.6: «La escena, imagen de la mesa, …». | [Pedido P-4: «formando una imagen de la idea»]; [Mesa] auditoría editorial |
| FN-8 | **El tramo no agrega cifra, marca ni fuente** que el bloque formal no tenga; si toma una de otra sección, la remite. | I.1.2.4: «cuando toma una de otra sección, la remite (por ejemplo, I.3.3 o I.2.1)». | [Pedido: «no inventar»]; [Mesa] auditoría editorial de la Parte I |
| FN-9 | **No afirmar más que la fuente.** Bajar el registro no sube la marca ni cambia quién dijo qué. | VI.1.11: «¿Qué enseña el caso? No que el sello tardío cause el fallo: es un solo caso». | [Mesa] auditoría editorial de la Parte VI («dos revisores» donde la fuente tenía uno) |
| FN-10 | **Una escena puede ordenar varios ítems**: ante una lista de abiertos, elegir el caso que los explica y recorrerlos como preguntas que esa escena deja. | II.1.8: «Los otros cuatro temas se entienden como preguntas que ese mismo experimento dejaría sin contestar aun si saliera bien.» | [Mesa] |
| FN-11 | **Tres párrafos**: caso → pregunta y respuesta → abierto o imagen. Ningún tramo en un solo bloque de más de ~1500 caracteres. | II.2.9: párrafo del caso y la medida; aparte, «La imagen: …». | [Mesa] auditoría editorial de la Parte I |
| FN-12 | **Terminar con lo que no se sabe**, como interrogante fértil o supuesto marcado `[ESP]`, con la condición que lo decidiría. | VI.2.6: «La salida que la mesa deja como supuesto es la más interesante: que el desacuerdo sea la medida». | [Pedido P-3: «dejando abierto temas como interrogantes y supuestos»] |
| FN-13 | **Una sola voz.** El tramo baja el registro, no cambia de narrador ni de convenciones de marcas, citas y nombres (`Rule-Narrative-Voice`). | VIII.2.2: «La reacción fácil sería descartar la frase por la palabra "cuántico". El registro hace otra cosa: traduce.» | [Mesa] |
| FN-14 | **Cobertura y paridad.** Toda parte que lea un humano lleva tramos; la que no (un catálogo), se justifica por escrito. Se miden palabras por bloque y se trata como hallazgo una asimetría de factor ≥ 3 entre partes. | Una parte quedó con 0 tramos y otra con bloques de ≈170 palabras contra ≈930 en otra; se niveló. | [Mesa] revisión de armonía |
| FN-15 | **El índice o el capítulo «cómo leer» anuncia** los tramos y su marcador. | Una línea al pie del índice de la Parte VI. | [Mesa] auditoría editorial |

---

# Respuestas explicativas: preguntas, propuestas y abiertos

Las tres piezas formales que más forman criterio llevan, debajo, una respuesta en campos fijos. Los campos son **guía, no plantilla rígida que se rellena**: ordenan la respuesta, y la prosa de cada campo explica. [Pedido P-1, P-2, P-3; lectura del gestor: «NO es una plantilla rígida»]

## Preguntas guía (`RE:PG`)

| Id | Regla | Caso de origen | Origen |
|----|-------|----------------|--------|
| PG-1 | Todo capítulo y todo tema puente lleva preguntas guía, y **cada una tiene respuesta**. La lista formal queda arriba; las respuestas, debajo de `<!-- RE:PG -->`. | II.1.9 conserva su lista numerada de cuatro preguntas y debajo el bloque `RE:PG`. | [Pedido P-1]; [Mesa] verificación de legibilidad |
| PG-2 | Cuatro campos, en orden: *Qué pregunta y por qué importa* · *Respuesta según lo que se sabe* · *Qué significa* · *Queda abierto*. Cierra con *Fuente:* (ruta y línea). | III.1.8: «**¿Este lazo lleva contenido o ganancia?** — *Qué pregunta y por qué importa.* Pide que cada "lazo" del texto diga qué baja por él». | [Pedido P-1: «no solo lo que se pregunta, sino porque y que significa»] |
| PG-3 | En *por qué importa*, nombrar **el error de lectura** que la pregunta previene. | II.1.9: «Quien no las separe lee mal toda la Parte III». | [Mesa] |
| PG-4 | La respuesta trae **extracto textual con fuente localizada y marca**, separando la letra del dueño, el código y la medida. | II.1.9: «"a = np.abs(x - self._x_anterior)" (`unidad.py` l.80) `[COD]` […] La letra del PO ya tenía el par: "todo aquello que se diferencia del resto lo separa o agrupa" `[LIT]`». | [Pedido P-3: «frases y extractos evidenciando»] |
| PG-5 | *Qué significa* da **una consecuencia de lectura o de uso** («quien lea X tiene que…»), y retroalimenta el cuerpo. | III.1.8: «Quien lea una cifra tiene que ubicarla en la línea que la produjo». | [Pedido P-1: «retroalimentación al cuerpo del texto»] |
| PG-6 | *Queda abierto* remite a un id de tema abierto o laguna y nombra **un supuesto no medido `[ESP]`**. | III.1.8: «*Queda abierto.* TA 5.2 […] Supuesto `[ESP]`: …». | [Pedido P-3] |
| PG-7 | Un resumen «en una línea» se admite **además** de los cuatro campos, nunca en su lugar. | VI.1.13: «En una línea cada una: …». | [Mesa] observado en la muestra; no decidido por la mesa |

## Propuestas (`RE:PROP`)

| Id | Regla | Caso de origen | Origen |
|----|-------|----------------|--------|
| PR-1 | Propuesta formal compacta (id, enunciado, marca `[PRO]`) y debajo seis campos: *Qué se espera y para qué* · *Cómo se sabría si funciona* · *Qué defiende y qué supone* · *Extracto* · *Lo que ya existe para correrla* · *Abre*. | III.2.5, Prop. 6.1: «*Qué se espera y para qué.* Un número, la fracción de elementos de borde-A que forman cadenas, con intervalo». | [Pedido P-2: «que esperaria o para que»] |
| PR-2 | *Qué se espera* nombra **un entregable concreto** (un número, un instrumento, una decisión) y la pregunta que contesta. | IV.2.10, Prop. 9.1: «Una segunda cifra por cada gestación […] Sirve para TA 9.13». | [Pedido P-2] |
| PR-3 | *Cómo se sabría* da **criterio de éxito y controles (positivo y negativo) sellados antes de correr**; si el umbral no está sellado, se dice o se marca la laguna en el lugar. | III.2.5, Prop. 6.3: «AUC ≥ 0,9 […] y AUC ≈ 0,5 con el observador quieto (control). Umbral de la propuesta, no sellado en acta.» | [Mesa] |
| PR-4 | *Qué defiende y qué supone*: la idea fuente que protege y **el supuesto que podría tumbarla**. | IV.2.10: «Supone `[PRO]` que dos varas independientes que coinciden descartan el sobreajuste; podrían compartir el mismo artefacto». | [Pedido P-3: «defendiendo y proponiendo»] |
| PR-5 | *Abre*: al menos **dos desenlaces** («si sale X…; si sale Y…») y un supuesto futuro `[ESP]`. | III.2.5, Prop. 6.2: «Si las regiones […] son cadenas, […]. Si no lo son […], el operador local hay que cambiarlo.» | [Pedido P-3: «abrir puntos futuros de trabajo»] |
| PR-6 | *Lo que ya existe*: datos, código e instrumentos disponibles, con remisión al programa de experimentos. | III.2.5: «el capítulo 18 la lista como X-02 con Prop. 6.2, costo bajo». | [Mesa] |

## Temas abiertos y lagunas (`RE:TA`)

| Id | Regla | Caso de origen | Origen |
|----|-------|----------------|--------|
| TA-1 | Distinguir **tema abierto** (pregunta que nadie resolvió) de **laguna** (contenido que la guía todavía no trajo), con marcas distintas (`[ABIERTO]`, `[LAGUNA id: qué falta; de dónde saldría]`). | VII.3.7: «Si se confunden, una deuda de lectura parece un misterio del modelo, o un misterio del modelo se "llena" con prosa». | [Pedido: «tolerar esas lagunas y avanzar sobre un esquema general, para luego volver»] |
| TA-2 | Todo tema abierto: id, eje o familia, y cinco campos: **pregunta única · rivales con nombre · lo ya medido · camino · qué cuenta como avance** (declarado antes de correr). Ninguno sin camino. | V, TA 11.4: «Rivales: ángulo verdadero […] Lo medido: el MG946R no informa posición `[DOC]`. Camino: Prop. 11.3. Avance: …». | [Pedido P-3]; [Mesa] formato del capítulo «cómo leer» |
| TA-3 | Forma completa **en un solo lugar**; en los demás, forma breve con remisión. Un id, un texto. | III.1.7: «La forma completa, con rivales y extractos, es TA 17.1 (VII.1.3)». | [Mesa] |
| TA-4 | Cada tema abierto, **su propio bloque** titulado con su id y *Por qué importa* en una frase llana. Nunca un bloque agrupado que explica sólo el último. | III.1.7: «**TA 5.3.** *Por qué importa.* …». | [Mesa] auditoría editorial (36 sin explicación propia) |
| TA-5 | Los abiertos se reúnen en un **capítulo por familias**; los duplicados se funden conservando todos los ids de origen. | VII.1.1, Def. 17.2: «se funden en uno cuando tienen la misma pregunta, los mismos rivales y un camino que los decide a la vez». | [Mesa] |
| TA-6 | Toda laguna tiene **fila en un capítulo de lagunas** con destino: llenada · fusionada · puenteada · abierta. Una laguna sin fila es falla grave; ninguna se «llena» con prosa. | VII.3.1: «Una laguna sin fila es hallazgo P1 de toda verificación». | [Pedido: lagunas]; [Mesa] |
| TA-7 | Cerrar cada bloque con **interrogante fértil, nunca con objeción**. Una metáfora de la fuente sin mecanismo se registra con la pregunta que la convertiría en mecanismo. | I.1.2.4: «lo no resuelto se plantea como pregunta fértil, no como objeción». | [Pedido P-3] |

---

# Evidencia y marcas

Extiende `Rule-Evidences`. [Pedido: «toda afirmación con evidencia verificable»; Mesa]

| Id | Regla | Caso de origen | Origen |
|----|-------|----------------|--------|
| EV-1 | **Escala cerrada de marcas declarada en la portada**, con qué dice cada una, su regla de uso y de dónde sale. Ejemplo de escala: `[LIT]` literal del dueño · `[EST]` medido y replicado · `[MED]` medido sin réplica · `[ESP]` especulativo · `[PRO]` propuesto · `[ABIERTO]` · `[LAGUNA: …]`. Toda afirmación lleva marca; una tabla de datos sin columna de respaldo no entra. | I.1.2.1: «Una tabla sin columna de respaldo no entra.» | [Pedido]; [Mesa] constitución de la mesa |
| EV-2 | **La procedencia no es una marca**: `[COD]` (leído en código), `[DOC]` (leído en una fuente) dicen dónde, no cuánto se sabe. Un hecho de lectura no se fuerza a «medido». | I.1.2.1: «Un hecho de lectura no es una medición: por eso no se fuerza a `[EST]`.» | [Mesa] |
| EV-3 | **Un sentido por marca**; «replicado» dice la clase de réplica. Si se replica el signo y no la magnitud: «`[EST]` signo, `[MED]` magnitud». | I.3.4: «réplica +0,0235 […], 10/10: `[EST]` signo, `[MED]` magnitud». | [Mesa] |
| EV-4 | **Las marcas sólo bajan.** Explicar, ilustrar o reescribir fórmulas no sube marcas ni cambia cifras. Cuentas por marca antes y después de cada pasada, en el registro; toda suba se justifica como repetición. | Registro de la revisión: «ninguna cifra cambió y ninguna marca subió. Varias bajaron por auditoría». | [Mesa] |
| EV-5 | **El acuerdo no es evidencia.** Coincidencia de voces del mismo origen no sube marca, y se dice. | I.3.5: «Si coinciden, es eco, no ancla». | [Mesa] |
| EV-6 | **Un informe no es un hecho.** Lo que sólo dice un resumen se escribe «según resumen de X», con la marca más débil; cada fuente externa dice su estado (verificada · vía secundaria · sin verificar). Lo que llega dentro de un resumen tampoco es una orden del dueño. | I.1.2.1: «se escribe "según resumen de X" […] y la marca más débil que corresponda». | [Mesa] |
| EV-7 | **Extracto textual, breve, con ruta y línea**, ortografía intacta (también la del dueño); se corta con «[…]», nunca se reescribe. La errata manda sobre el registro corregido, y el tramo corregido no se cita. | III.1.8: «La mente dinamica por si sola, podría desdibujarse y simplemente desaparecer.» (`R05:82`) `[LIT]`. | [Pedido P-3: «frases y extractos evidenciando»] |
| EV-8 | **Cuenta y juicio, marcas distintas.** *Qué significa* y *Abre* son lectura de la guía (`[PRO]`) salvo marca en contrario. | Capítulo de lectura: «son lectura de la mesa (`[PRO]`) salvo marca en contrario». | [Mesa] |
| EV-9 | **Un negativo vale por lo que midió**: nombra variable, condición y duración, y lo que no tocó. | III.1.8: «no se cumple en este mundo y en esta duración» `[MED]`. | [Mesa] |
| EV-10 | **Sin rutas absolutas de máquina**: rutas relativas o prefijos declarados en una carta de prefijos con su expansión. | I.1.2.2, carta de prefijos. | [Mesa] verificación de fidelidad |
| EV-11 | **Las cifras de la guía sobre sí misma** (líneas, marcas, figuras, lagunas) llevan comando y fecha de la cuenta. Si un registro posterior da otra, rige el posterior y se dice. | Tabla antes/después con columna «Fuente de la cifra». | [Mesa] |
| EV-12 | **Lista de chequeos para leer una cifra** en el capítulo de lectura: unidad de n, controles, sello previo, errata posterior, cuenta o juicio, alcance del negativo, clase de réplica, vara, modelo o realidad, informe o fuente. | I.3.5: «**Unidad de n.** ¿n cuenta semillas, pares, imágenes o pasos?». | [Mesa] |

---

# Ilustraciones como evidencia

Las reglas completas están en `Rule-Illustrations.md` (IL-01 a IL-24). Lo esencial para este Profile: [Pedido P-5; Mesa]

- **Tipo por lo que prueba**: captura anotada, esquema propio, render 3D (sólo si el texto habla del objeto físico) o diagrama como código.
- **Original intacto** con sha256; derivado anotado por script reproducible; **ningún número a mano**.
- **Remarcar el hallazgo** (recuadro, flecha, ①②③) donde la fuente dice que está.
- **Pie en cinco tiempos**: qué se ve → qué significa → marca → fuente → abierto. Ninguna lámina sube una marca; si falla en algo, lo confiesa. Caso de origen, F3-24: «234 objetos visibles […] `[MED]`, sin cotejo pieza a pieza […] En violeta, el soporte de ensayo, que no es parte del robot».
- **La lámina dentro del relato**: antes de cada una, «Mirá la Figura X», una pregunta y su respuesta. Caso de origen, V.1.6: «¿Por qué la inmediata casi nunca se aplica? Porque su caducidad queda a la izquierda de la franja de latencia».
- **Lista de figuras** con anclas, **manifiesto** `Imagenes/README.md` y **verificación visual** por una voz distinta del autor.

---

# Fórmulas

Siguen `Rule-Math-Formulas.md`. Lo que esta variante agrega, aprendido al revisar las fórmulas de la guía de origen: [Pedido P-6; Mesa]

| Id | Regla | Caso de origen |
|----|-------|----------------|
| FO-1 | Toda relación matemática en LaTeX; nada de pseudo-ASCII en el cuerpo. En línea con dos o más `_` o con `*`, usar `` $`…`$ ``. | III.1.2: «con $`W = w_s + w_f`$» (15 fórmulas corregidas por render) |
| FO-2 | Todo bloque con rótulo numerado por capítulo `(Ec. c.k)`, cláusula «Donde…» que glosa cada símbolo en el orden en que aparece, y lectura «En palabras». | II.1.2: «**(Ec. II.1)** En palabras: la actividad del elemento $i$ es cuánto cambió su valor desde la muestra anterior, sin signo.» |
| FO-3 | Homónimos declarados donde chocan. | V, Ec. 11.1: «dos símbolos distintos con la misma letra». |
| FO-4 | Cada fórmula se **coteja contra su fuente** (archivo y línea). Si el texto da una forma corta, se escribe la completa y se dice qué omitía. Una discrepancia no se arregla en silencio: id `D-n`, nota o `[ABIERTO]`. | IV, Def. 8.7 → Ec. 8.1: «en el código el paso completo […] también olvida, replica y recorta». |
| FO-5 | Lo que la fuente no implementa se marca como postulado `[PRO]`. Reescribir en LaTeX no cambia cifras ni sube marcas. | II.1.4, Ec. II.5: «no está cableado […] Es un postulado de composición». |
| FO-6 | Verificación por comando: 0 errores KaTeX con `throwOnError`, 0 `$` en mermaid, 0 barras verticales sin escapar en tablas. | 400 expresiones, 0 errores. |

---

# Proceso por rondas

Cómo se produce una guía de este tipo cuando es extensa. [Mesa, salvo lo marcado]

1. **Relevar antes de escribir**: inventario de fuentes y de piezas a tratar (secciones, preguntas, propuestas, imágenes, fórmulas).
2. **Descomponer en núcleos chicos**, redactarlos y criticar cada uno con su evidencia.
3. **Cohesión global y decisión de arquitectura** antes de integrar (propuestas rivales, decisión escrita, plan).
4. **Redactar por partes y auditar cada parte** con un especialista académico y un editor. [Pedido: «que lo evaluen los especialistas academicos y editores bibliograficos»]
5. **Verificar por lentes independientes** (fidelidad y evidencia, legibilidad, coherencia, visual, render), con hallazgos P1/P2/P3 y su estado.
6. **Verificación mecánica por comando**, no a ojo: anclas, rutas absolutas, imágenes, mermaid, KaTeX, marcadores fuera de la lista.
7. **Armonía al cierre de cada ronda**: densidad pareja entre partes, una grafía, los mismos campos.
8. **Una ronda por objetivo, sobre la versión cerrada de la anterior**, subiendo la versión de la guía (por ejemplo: explicativa → láminas → fórmulas → estilo). [Pedido: «termina la rondas, y luego en otra»]
9. **Respaldo antes de toda edición por script** y ensamblado idempotente con modo de comprobación.
10. **README de ronda**: tabla antes/después con la fuente de cada cifra y la lista de lo que quedó abierto.

---

# Anti-patrones observados y corregidos

| Anti-patrón | Corrección |
|-------------|------------|
| Texto «muy sintetico»: sólo ids y campos | Bloques explicativos + tramo narrativo (FN-1) |
| Pregunta guía sin respuesta | Bloque `RE:PG` de cuatro campos (PG-2) |
| Propuesta sin «qué se espera o para qué» | Bloque `RE:PROP` (PR-1) |
| Temas abiertos telegráficos o agrupados | Un bloque por id, paridad entre partes (TA-4, FN-14) |
| El tramo trae cifras o citas que el bloque formal no tiene | Quitar o remitir (FN-8) |
| El tramo dramatiza y altera la fuente | Volver a la letra (FN-9) |
| Tramo de un solo párrafo con preguntas retóricas encadenadas | Caso / pregunta-respuesta / abierto (FN-11) |
| Imagen de la guía leída como si fuera de la fuente | Rotularla (FN-7) |
| Marcadores con grafías distintas | Lista única (FN-2) |
| Marca inflada; figura que sube una marca | Bajar en toda la obra (EV-4, `Rule-Illustrations` IL-11) |
| Fórmula «arreglada» en silencio | Discrepancia con id (FO-4) |
| Laguna sin fila de destino | Capítulo de lagunas (TA-6) |
| Respuesta remitida a un registro de trabajo fuera de la guía | La respuesta vive en la guía |
| Ruta absoluta en el cuerpo | Ruta relativa o descripción (EV-10) |

---

# Criterios de aceptación de esta variante

Además de los [Criterios de calidad](#criterios-de-calidad), verificables por `grep` o lectura dirigida:

1. Cada definición, propuesta, tema abierto con forma completa y bloque de preguntas guía tiene debajo su tramo o bloque con marcador de la lista única; partes exentas, justificadas por escrito.
2. 0 marcadores fuera de la lista única; lista declarada una sola vez y anunciada en el índice o «cómo leer».
3. Cada tramo abre con un rótulo del repertorio, contiene un caso del corpus citado, al menos una pregunta respondida en la oración siguiente, y termina en lo abierto o en la imagen; ningún párrafo de más de ~1500 caracteres.
4. Toda cifra, marca o fuente de un tramo está en su bloque formal o lleva remisión; ninguna analogía ajena a la fuente sin rótulo.
5. Preguntas = bloques respondidos con los cuatro campos; propuestas con los seis campos; temas abiertos con los cinco campos y bloque propio.
6. Cada `[LAGUNA]` tiene fila con destino (n de n).
7. Cuentas de marcas antes/después de cada ronda en el registro; ninguna sube sin justificación; ninguna cifra cambió.
8. Láminas conforme a los criterios de `Rule-Illustrations`; fórmulas con 0 errores de render, «Donde…» y «En palabras».
9. 0 anclas rotas; 0 rutas absolutas de máquina.
10. Paridad: palabras medias por bloque entre partes dentro de un factor 3, o el motivo registrado.

---

# Queda abierto

- El repertorio de rótulos de apertura (FN-3) no está unificado en la guía de origen; este Profile lo admite como lista cerrada en lugar de fijar uno solo.
- El criterio de exención de tramos para partes de catálogo (FN-14) no tiene definición operativa.
- PG-7 sale de la muestra y no de una decisión registrada.
