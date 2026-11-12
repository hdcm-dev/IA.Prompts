# Rule — Illustrations

## Objetivo

Cómo se incorporan ilustraciones a la documentación Markdown cuando la imagen funciona como **evidencia** y no como adorno: capturas anotadas de lo que produjo el sistema estudiado, esquemas propios, renders 3D de un objeto físico y diagramas como código. Fija qué tipo de lámina corresponde, cómo se preserva el original, qué se dibuja encima, qué dice el pie, cómo se integra la lámina al relato y cómo se verifica. Complementa a `Rule-Evidences` (toda afirmación con respaldo), a `Rule-Dual-Audience` (diagramas como código, texto alternativo) y a `Rule-Markdown` (formato).

Origen: práctica de una mesa de redacción que ilustró una guía de estudio extensa (25 láminas, 21 diagramas) a pedido del dueño del proyecto, que pidió «ir incluyendo imagenes, e incluso […] remarcar hallazgos en dichas imagenes», usar capturas «como evidencia visual», «crear esquemas personalizados» y renders 3D. Cada regla dice si viene del pedido del dueño (**[Pedido]**) o de la práctica de la mesa (**[Mesa]**), y trae un caso de origen breve, marcado como tal.

Vocabulario: **fuente** es cualquier registro primario (acta, informe, cuaderno de laboratorio, dataset, código); **marca** es la escala de certeza que declare la guía (por ejemplo `[MED]` medido, `[EST]` replicado, `[ESP]` especulativo).

## Índice

1. [Tipos de lámina](#tipos-de-lámina)
2. [Evidencia intacta](#evidencia-intacta)
3. [Qué se dibuja encima](#qué-se-dibuja-encima)
4. [El pie y la banda](#el-pie-y-la-banda)
5. [La lámina dentro del relato](#la-lámina-dentro-del-relato)
6. [Índice y manifiesto](#índice-y-manifiesto)
7. [Verificación](#verificación)
8. [Anti-patrones](#anti-patrones)
9. [Criterios de aceptación](#criterios-de-aceptación)

---

# Tipos de lámina

**IL-01. Elegir el tipo por lo que la figura debe probar, y declararlo.** [Pedido + Mesa]

| Tipo | Cuándo | Qué prueba |
|------|--------|------------|
| Captura anotada | El sistema estudiado produjo la imagen (gráfico, mapa de activación, pantalla) | Que el hallazgo existe en la salida real |
| Esquema propio | El mecanismo no aparece en ninguna captura | Cómo se relacionan las partes; es construcción, no dato |
| Render 3D | Sólo cuando el texto habla del objeto físico | Forma, disposición y conteo de piezas del modelo |
| Diagrama como código (mermaid) | Estructura, flujo o dependencia entre conceptos | Relaciones; se versiona como texto |

Verificable: la columna «Tipo» del manifiesto no queda vacía. Caso de origen: el plan de láminas fija «Render 3D: sólo donde el texto habla del cuerpo».

# Evidencia intacta

**IL-02. Nunca anotar sobre el original.** Copiar el original byte a byte a `Imagenes/originales/`, anotar una copia en `Imagenes/anotadas/` y registrar el sha256 de ambos. Verificable: sha256 del original = sha256 de la fuente. [Pedido, en la lectura del gestor: «en una copia anotada, conservando la original con su sha256 y origen»]

**IL-03. Anotar con un script reproducible que corre sobre el original, nunca a mano en un editor.** Cada derivado se regenera con su script; si cambia, el manifiesto registra el sha nuevo y el reemplazado. [Mesa] Caso de origen: una figura regenerada tres veces deja en el manifiesto «… reemplaza d1a040a7…, que reemplazaba 006220d5…».

**IL-04. Respaldo antes de editar por script.** Antes de ensamblar o reescribir el documento con un script, copia previa y comprobación del resultado contra ella; el script lee antes de abrir en escritura. [Mesa] Caso de origen: un script de ensamblado vació dos partes y la portada; se recuperaron desde el respaldo validado byte a byte.

# Qué se dibuja encima

**IL-05. Remarcar el hallazgo, no la imagen.** Recuadro, flecha o círculo numerado (①②③) en el lugar exacto donde la fuente dice que está el hallazgo, con un rótulo corto; cada número se explica en el pie. Ninguna anotación tapa un rótulo de la captura. [Pedido: «remarcar hallazgos en dichas imagenes»]

**IL-06. Ningún número escrito a mano.** Toda cifra anotada sale de un rótulo impreso en la captura, de una línea citada de la fuente o del árbol del modelo CAD. [Pedido: «no inventar»; Mesa] Caso de origen: «El servidor informó 234 objetos visibles al capturar».

**IL-07. Si el dibujo no coincide con el dato, no se usa.** Se corrige el modelo o el dato, nunca el dibujo; la lámina rechazada queda en el manifiesto con su motivo y no se cita. [Mesa] Caso de origen: un render en que las cámaras salían como prismas de reemplazo quedó «RECHAZADA, no citada»; una ilustración ajena que declaraba 24 grados de libertad contra 28 servos del texto, «no se usa».

**IL-08. En un esquema propio, declarar qué es dibujo y qué es dato.** Las curvas ilustrativas se rotulan como tales y las calculadas como cálculo. [Mesa] Caso de origen: «Las ondas son un dibujo del régimen descrito en el folio, no una captura».

# El pie y la banda

**IL-09. El pie es un párrafo en cinco tiempos, en este orden:** qué se ve → qué significa para el tema → marca → fuente con ruta y sección → «Abierto:». [Pedido: evidencia verificable y temas abiertos; la forma es Mesa]

Ejemplo genérico:

> **Figura F3-04.** El panel de latencias muestra la cola derecha recortada en 200 ms (① recuadro). Para el servicio: el reintento nunca ve respuestas más lentas que el timeout. `[MED]`. Fuente: `informes/carga-2026-03.md` §2 (l. 41). Abierto: una sola corrida; falta repetir con tráfico real.

**IL-10. Las marcas se separan por afirmación, no por figura.** Signo y magnitud, dato y lectura, pueden llevar marcas distintas («`[EST]` signo, `[MED]` magnitud»; cifras `[MED]`, mecanismo `[ESP]`). [Mesa]

**IL-11. Ninguna marca de una lámina sube por encima de la del texto o la fuente.** Ante conflicto gana la marca más baja, en toda la obra. [Mesa] Caso de origen: «Subir la Parte III de vuelta a `[EST]` sería subir una marca, y eso no está permitido».

**IL-12. Si la figura falla en algo, el pie lo confiesa.** Lo que no se distingue, lo no cotejado y lo que es andamiaje y no objeto se dice. [Mesa] Caso de origen: «toda la pierna se ve gris translúcida y […] los servos no se distinguen»; «En violeta, el soporte de ensayo, que no es parte del robot».

**IL-13. La lámina lleva adentro su banda: fuente, fecha, marca y leyenda de colores.** Si circula sin el texto, conserva el respaldo. [Mesa, hallazgo de la verificación visual: «Si la imagen circula sola, pierde el respaldo»]

**IL-14. El texto alternativo describe lo que se ve, con los mismos colores y valores que el pie.** [Mesa] Ejemplo genérico: «línea gris punteada del umbral 0,15, casi superpuesta a la ocre de la media 0,151».

# La lámina dentro del relato

**IL-15. Antes de cada lámina, un tramo narrativo: «Mirá la Figura X», una pregunta y la respuesta en una o dos frases.** La figura es la imagen de la idea. [Pedido: «plantear una pregunta y seguir con la respuesta […] formando una imagen de la idea»] Caso de origen: «Mirá la Figura F3-22 […] ¿Por qué la inmediata casi nunca se aplica? Porque su caducidad queda a la izquierda de la franja de latencia».

**IL-16. Si la lámina usa un código visual, antes va una lámina-clave que enseña a leerlo.** [Mesa] Caso de origen: «Antes de mirar capturas conviene saber leerlas; […] ¿qué dice el color y qué dice el brillo?».

**IL-17. Encadenar láminas como respuesta a una pregunta:** una muestra el fenómeno y la siguiente su causa. [Pedido, formato narrativo]

**IL-18. Diagramas como código con leyenda de trazo en el pie:** línea llena = existe o tiene código; punteada = falta o lo decide un experimento. Sin `$` dentro de mermaid (ver `Rule-Math-Formulas`). [Pedido: «mermaid cuando haga falta»; Mesa]

# Índice y manifiesto

**IL-19. Numerar con prefijo por origen** (`F-n` diagramas de integración, `F3-nn` láminas de una ronda) **y publicar una «Lista de figuras»** con ancla a la sección donde aparece cada una. [Pedido: «con índices»]

**IL-20. Manifiesto `Imagenes/README.md`:** una fila por figura con tipo, archivo, origen (ruta + sección), sha256 original, sha256 derivado, qué se anotó y marca. Todo archivo de `Imagenes/` tiene fila; las rechazadas también, con el motivo. [Mesa]

**IL-21. Rutas relativas a la carpeta de la guía**; ninguna ruta absoluta de máquina en el documento ni en el manifiesto. [Mesa]

# Verificación

**IL-22. Una voz distinta del autor abre cada lámina como imagen** y coteja sus cifras contra la fuente. Gravedad: P1 contenido, P2 lectura o falta de marca o leyenda, P3 detalle. Ninguna lámina entra sin veredicto OK, CORREGIDA o RECHAZADA. [Mesa] Caso de origen: 9 OK, 16 CORREGIDA, 1 RECHAZADA.

**IL-23. Diagramas compilados antes de cerrar** con un renderizador real, sin errores ni «Unsupported markdown». [Mesa]

**IL-24. Al ensamblar se comprueba por comando:** toda imagen citada existe, toda ancla resuelve, todo archivo de `Imagenes/` tiene fila, el sha del manifiesto coincide con el disco. [Mesa]

# Anti-patrones

| Anti-patrón | Corrección |
|-------------|------------|
| Leyenda que nombra mal un elemento del gráfico | Reescribir la leyenda y regenerar el derivado por script |
| Render sin banda: suelto pierde fuente y marca | Banda interna (IL-13) |
| Anotación que tapa un rótulo de la captura | Mover la anotación |
| Lectura de mecanismo con marca de medida | Bajar la lectura a especulación (IL-10) |
| Pie o lámina con marca más alta que el texto | Alinear a la más baja (IL-11) |
| Render que no coincide con el objeto | Rechazar, sin dibujarlo «como debería ser» (IL-07) |
| Pie que no menciona lo visible | Sumar al pie y a la banda (IL-12) |
| sha del manifiesto distinto del disco tras reexportar | Recalcular al ensamblar, con nota |
| Script que abre en escritura antes de leer | Respaldo y lectura previa (IL-04) |

# Criterios de aceptación

1. Cada lámina tiene tipo declarado y fila en el manifiesto con origen y sha256 de original y derivado; el original coincide con la fuente.
2. Ningún original modificado; todo derivado se regenera con un script guardado.
3. Cero cifras dibujadas sin rótulo de captura, línea de fuente o lectura del modelo, verificado por una voz distinta del autor.
4. Cada pie tiene los cinco tiempos; marcas separadas por afirmación y ninguna más alta que la del texto.
5. Capturas, esquemas y renders llevan banda interna; los esquemas declaran qué es dibujo.
6. Cada lámina va precedida por un tramo con pregunta y respuesta; un código visual nuevo tiene su lámina-clave.
7. Diagramas con leyenda de trazo y compilación sin errores.
8. Lista de figuras con anclas; 100 % de las imágenes existen; 0 anclas rotas; 0 rutas absolutas.
9. Láminas rechazadas fuera del texto y dentro del manifiesto con su motivo.
10. Verificación visual con 0 P1 abiertos y los P2 aplicados.
