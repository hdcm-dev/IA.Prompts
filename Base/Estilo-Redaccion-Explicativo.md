# Base — Estilo de redacción explicativo

> **Invocación**: Leer `/IA/PROMPTs/IA.Prompts/Base/Estilo-Redaccion-Explicativo.md` cuando haya que producir un documento cuyo propósito sea **formar criterio** en quien lo lee —una guía, un documento de caso, una explicación de por qué algo está construido como está— y no solo registrar qué se hizo.
>
> **Overview**: Este documento no fija un formato de plantilla: fija **una forma de explicar**. Su tesis es que un documento técnico sirve cuando el lector queda en condiciones de decidir por su cuenta en una situación que el documento no cubre, y que eso se consigue con tres cosas: exponer por preguntas antes que por afirmaciones, contrastar siempre lo que cumple contra lo que no, y declarar los límites de lo que se afirma con la misma precisión que lo afirmado.
>
> Se declaran cuatro capas. La **estructura** —cómo se ordena un documento y por qué las definiciones van antes que todo—. El **patrón de exposición** —pregunta guía, respuesta en una línea, explicación, ejemplos contrastados—, que es el núcleo y el que más cambia el resultado. La **voz** —qué se pone en negrita, cómo se cita, qué construcciones se evitan—. Y la **postura**, que es lo que separa un documento confiable de uno persuasivo: qué se afirma, con qué evidencia, y qué se deja explícitamente sin afirmar.
>
> Está escrito aplicándose a sí mismo. Cada sección es una pregunta, cada respuesta cabe en una línea, y hay una sección que declara lo que este documento deliberadamente no cubre. Un agente que lo lea puede tomarlo también como el ejemplo.

---

## Índice

- **[1. Qué problema resuelve este estilo](#1-que-problema-resuelve-este-estilo)**
- **[2. El patrón de exposición](#2-el-patron-de-exposicion)** — el núcleo
- **[3. La estructura del documento](#3-la-estructura-del-documento)** — el orden, la jerarquía numerada y el índice
- **[4. La voz](#4-la-voz)** — negrita, metáforas, evidencia literal y anclaje de definiciones
- **[5. La postura](#5-la-postura)** — qué se afirma y con qué evidencia
- **[6. Anti-patrones](#6-anti-patrones)**
- **[7. Lista de verificación](#7-lista-de-verificacion)**
- **[8. Lo que este documento no cubre](#8-lo-que-este-documento-no-cubre)**

---

## 1. Qué problema resuelve este estilo

### 1.1 ¿Qué distingue a un documento que forma criterio?

**Respuesta: que el lector puede decidir bien en un caso que el documento no menciona.**

Hay dos clases de documento técnico, y se confunden todo el tiempo:

| Clase | Qué deja | Cuándo falla |
| --- | --- | --- |
| **Registro** | Qué se hizo y cómo quedó | Cuando aparece un caso distinto |
| **Formativo** | Con qué criterio se decidió | — |

Un registro responde «¿qué hicimos?». Un documento formativo responde «¿cómo decido yo
lo mismo mañana?». Los dos son legítimos, pero solo el segundo sobrevive al cambio de
las circunstancias.

**La prueba práctica:** tapá la solución que el documento propone. Si lo que queda
alcanza para reconstruirla, el documento forma criterio. Si lo que queda es una
introducción, es un registro con prólogo.

### 1.2 ¿Por qué no alcanza con explicar bien?

**Respuesta: porque una explicación se lee, y un criterio se ejercita.**

Un texto expositivo bien escrito produce asentimiento —«claro, tiene sentido»— y ese
asentimiento se evapora. Una pregunta produce otra cosa: el lector intenta responderla
antes de leer la respuesta, y ahí es donde queda algo.

Por eso el patrón de la §2 no es una preferencia de formato. Es el mecanismo.

---

## 2. El patrón de exposición

Es el núcleo de este estilo. Si solo se adopta una cosa de este documento, que sea esta.

### 2.1 ¿Cuál es la unidad de exposición?

**Respuesta: pregunta → respuesta en una línea → por qué → ejemplos contrastados.**

La forma completa:

```markdown
### 3.2 ¿Desde dónde parte el caso?

**Respuesta: de un estado conocido, y declararlo es parte del caso —no un trámite—.**

<explicación: por qué esa respuesta y no otra>

| | |
| --- | --- |
| ✅ | «Abierta la pantalla y con el circuito ya establecido» |
| ⚠️ | «Abierta la pantalla» — cierto, pero insuficiente |
| ❌ | «Abierta la pantalla, y además ya escribí la frase» — eso ya es actuar |

<opcional: la regla práctica, o qué hacer cuando no se puede>
```

Cada parte tiene un trabajo:

| Parte | Su trabajo | Si falta |
| --- | --- | --- |
| **La pregunta** | Que el lector intente responder antes de leer | Vuelve a ser prosa expositiva |
| **La respuesta en una línea** | Que sea citable y recordable | El criterio se diluye en el párrafo |
| **El porqué** | Que se pueda extrapolar | Queda una regla que se obedece sin entender |
| **Los ejemplos** | Que se reconozca el caso en la vida real | El lector coincide pero no sabe aplicarlo |

### 2.2 ¿Cómo tiene que ser la pregunta?

**Respuesta: la que el lector ya se está haciendo, con sus palabras.**

| | |
| --- | --- |
| ✅ | «¿Y si igual hago clic antes de tiempo?» |
| ✅ | «¿Por qué una pantalla que se ve lista puede no estarlo?» |
| ❌ | «¿Cuál es la importancia del estado inicial?» |
| ❌ | «Consideraciones sobre la hidratación» |

Las dos primeras son preguntas que alguien realmente hace. La tercera es un título
disfrazado de pregunta. La cuarta ni siquiera lo intenta.

**Señal de alarma:** si la pregunta empieza con «¿Cuál es la importancia de…» o
«¿Qué debemos considerar…», es un encabezado con signos de interrogación pegados.

**Truco que funciona:** escribí primero la objeción o la duda que tendría alguien que
está en desacuerdo. Esa es la pregunta.

### 2.3 ¿Cómo tiene que ser la respuesta?

**Respuesta: una línea, afirmativa, en negrita, y que se sostenga sola fuera de contexto.**

| | |
| --- | --- |
| ✅ | **«Respuesta: la persona. Nunca el sistema.»** |
| ✅ | **«Respuesta: no es que "no pasa nada". Pasa otra cosa.»** |
| ❌ | «Respuesta: depende de varios factores que se detallan a continuación» |
| ❌ | Un párrafo de cinco líneas en negrita |

Una respuesta que necesita el párrafo siguiente para entenderse **no es la respuesta**:
es el comienzo de la explicación. Cuando pase eso, la señal es que la pregunta estaba
mal recortada —abarcaba dos—.

### 2.4 ¿Por qué siempre ejemplos contrastados?

**Respuesta: porque un ejemplo solo enseña dónde está el límite si se lo compara con
algo que queda del otro lado.**

Un ejemplo correcto aislado deja la pregunta abierta: *¿por qué ese y no otro?* El par
✅/❌ responde eso sin explicarlo.

Tres formas, de menor a mayor potencia:

| Forma | Cuándo |
| --- | --- |
| ✅ / ❌ | La mayoría de los casos |
| ✅ / ⚠️ / ❌ | Cuando existe el caso *cierto pero insuficiente*, que es el más traicionero |
| Tabla de escenarios | Cuando lo que importa es **cuándo aplica**, no cómo se ve |

El ⚠️ merece atención: casi siempre el error real no es hacer lo contrario de lo
correcto, sino hacer *algo parcialmente correcto* y detenerse ahí.

### 2.5 ¿Cuántos ejemplos?

**Respuesta: los suficientes para cubrir las formas de equivocarse, no las de acertar.**

Acertar tiene una forma; equivocarse tiene varias. Un buen bloque de ejemplos suele
tener **un** ✅ y **dos o tres** ❌, cada uno con un modo de falla distinto.

Y cuando el tema lo justifica —como «qué superficies cumplen y cuáles no»—, conviene una
sección entera de casos, cada uno con: **el ejemplo**, **qué falla**, **qué hacer**. Las
tres partes. Un catálogo de errores sin la tercera columna es un catálogo de quejas.

### 2.6 ¿Se aplica el patrón a todo el documento?

**Respuesta: no. Solo donde hay una decisión que tomar.**

| Va con pregunta | Va sin pregunta |
| --- | --- |
| Un criterio que se puede aplicar mal | Una definición |
| Una decisión que tiene alternativas | Un listado de referencia |
| Algo contraintuitivo | El código completo, al final |
| Una objeción previsible | Los metadatos del encabezado |

Forzar el patrón donde no hay decisión produce preguntas huecas —«¿Qué es un
identificador de prueba?»— que son definiciones con disfraz. **Las definiciones se
declaran, no se preguntan.**

---

## 3. La estructura del documento

### 3.1 ¿Qué va primero?

**Respuesta: las definiciones. Antes de usar un término, se fija.**

El orden que funciona:

| # | Sección | Por qué ahí |
| --- | --- | --- |
| 0 | Metadatos y overview | Qué es esto y si me sirve, en diez segundos |
| 0.5 | Índice *(si supera ~200 líneas)* | Sin él, un documento largo se lee una vez y nunca más |
| 1 | **Definiciones** | Un término sin fijar se lee con el significado que cada uno le trae |
| 2 | **Qué promete / de qué se trata** | El objeto del documento, en una frase |
| 3.. | Los criterios, uno por pregunta | El cuerpo |
| n-3 | El artefacto entero | Ver junto lo que se explicó en partes |
| n-2 | **Lo que deliberadamente no se cubre** | §5.3 |
| n-1 | Cómo se corre / cómo se usa | Lo operativo |
| n | **El criterio, en una línea** | Lo único que se va a recordar dentro de un mes |

Las definiciones al principio no son un trámite académico: son lo que permite que el
resto sea preciso sin ser pesado. Una vez fijado «superficie», se puede usar cien veces
sin volver a explicarlo.

### 3.2 ¿Por qué las secciones van numeradas y jerarquizadas?

**Respuesta: porque un criterio se cita, y lo que no tiene número no se puede citar.**

La numeración no es ornamento. Es lo que permite escribir «el problema que trata la
§4.6» dentro del propio documento, en su hermano, en un comentario del código y en una
conversación —sin repetir el contenido y sin que la referencia envejezca cuando alguien
reordene el texto—.

| | |
| --- | --- |
| ✅ | `## 4. Los criterios de diseño` → `### 4.3 ¿A qué elementos les pongo data-testid?` |
| ❌ | `## Criterios` → `### Identificadores` *(no hay cómo citarlo)* |

**Los tres niveles, y qué significa cada uno:**

| Nivel | Qué es | Cuántos |
| --- | --- | --- |
| `##` **`n.`** | Una parte del documento: un tema que se puede leer solo | 5 a 9 |
| `###` **`n.m`** | **Una decisión**: acá vive el patrón pregunta–respuesta | 3 a 6 por sección |
| `####` | Un caso enumerado dentro de una decisión | Solo cuando hay una serie |

**Cuándo aparece el cuarto nivel:** solo cuando la subsección contiene **una serie de
ítems paralelos** que merecen navegarse —las cinco preguntas de una checklist, los seis
casos de un catálogo—. Se los rotula con letra o número propio (`#### a. El tablero de
inicio`, `#### Pregunta 3 — …`) para que no compitan con la numeración de secciones.

**Si hace falta un quinto nivel, la sección está mal recortada.** Un `#####` es casi
siempre el síntoma de que un `###` estaba tratando dos decisiones distintas.

**Regla de tamaño:** un `##` que pasa de ~150 líneas quiere partirse; un `###` de tres
líneas quiere fusionarse con su vecino. La numeración hace visible ese desbalance de un
vistazo —lo que en un documento sin numerar pasa desapercibido—.

**Y la regla que se olvida:** cuando se inserta una sección en el medio, **hay que
renumerar y revisar las referencias cruzadas**. Es el costo de la numeración, y es
barato comparado con lo que compra.

### 3.3 ¿Cuándo lleva índice, y cómo se arma?

**Respuesta: pasadas unas 200 líneas, y con una glosa por entrada —no solo el título—.**

Sin índice, un documento largo se lee entero una vez y después nunca más, porque volver
a buscar algo cuesta más que preguntarle a alguien.

**La forma:**

```markdown
## Índice

- **[1. Definiciones](#1-definiciones)**
- **[2. Qué promete esta superficie](#2-que-promete-esta-superficie)** — las cinco preguntas
  que se le hacen a una promesa. Es la parte que **no depende de este proyecto**.
- **[4. El criterio propio de una superficie interactiva](#4-el-criterio-propio…)** — el
  testigo de hidratación, y cuándo hace falta
```

| | |
| --- | --- |
| ✅ | Entrada con glosa: qué voy a encontrar ahí y por qué me importaría |
| ⚠️ | Entrada con el título solo: sirve para navegar, no para decidir si entrar |
| ❌ | Índice generado que repite los tres niveles enteros |

**Qué profundidad:** solo el nivel `##`. Un índice que replica todos los `###` es tan
largo como el documento y deja de ser un mapa. Lo que sí conviene es que la glosa
nombre lo que hay adentro —«el testigo de hidratación»— para que el `###` se encuentre
igual con la búsqueda del navegador.

**La glosa hace un trabajo que el título no puede:** marcar qué secciones son de
alcance general y cuáles son específicas de este caso. Esa es exactamente la
información que necesita alguien que llega de otro proyecto.

**Cuidado con las anclas.** El ancla se deriva del título —minúsculas, espacios por
guiones, se cae la puntuación—, y **los caracteres acentuados se conservan** en los
renders de GitHub. Un título con tilde produce un ancla con tilde. Conviene generarlas
del título exacto y **verificar en el render publicado**, no de memoria: un índice con
anclas rotas es peor que no tener índice, porque promete una navegación que no cumple.

### 3.4 ¿Cómo se cierra?

**Respuesta: con una sola frase que valga por todo el documento.**

> **Lo que la prueba necesita nombrar, se declara en el marcado.**

> **Una promesa se escribe desde el lado de quien la recibe, y tiene que poder ser falsa.**

Debe cumplir dos cosas: **derivarse** de todo lo anterior, y **sostenerse sola** para
quien no leyó nada. Si no se deriva, es un eslogan pegado al final. Si no se sostiene
sola, no va a sobrevivir a la cita de pasillo, que es como estos documentos se propagan
en realidad.

### 3.5 ¿Cuándo conviene partir en varios documentos?

**Respuesta: cuando dos temas se explican mejor por su diferencia que por separado.**

Dos documentos hermanos que se referencian entre sí superan a uno solo cuando **el
contraste es la enseñanza**. En el caso que originó este estilo, la superficie
interactiva y la superficie estática se explican una a la otra: casi todo lo que cambia
entre ellas se deriva de una sola diferencia, y eso solo se ve teniéndolas al lado.

**La regla para no duplicar:** el criterio compartido vive en **uno** de los dos, y el
otro lo enlaza con una línea que diga qué va a encontrar allá. Repetirlo garantiza que
las dos copias diverjan.

---

## 4. La voz

### 4.1 ¿Qué se pone en negrita?

**Respuesta: la afirmación que el lector debería poder citar. Nada más.**

| | |
| --- | --- |
| ✅ | **«Nunca se fabrica el estado que la prueba debería obtener actuando.»** |
| ❌ | «Es **muy importante** tener en cuenta que…» |

La negrita marca **qué frase es la carga del párrafo**, no qué palabras son intensas.
Un párrafo con cuatro fragmentos en negrita no tiene ninguno: el lector deja de verlos.

**Regla de densidad:** como mucho una frase en negrita por párrafo, y muchos párrafos
sin ninguna.

### 4.2 ¿Cómo se explica un mecanismo?

**Respuesta: la metáfora para retenerlo, el mecanismo literal para poder actuar.**

Las dos, en ese orden, y sin que la primera reemplace a la segunda:

> Eso es *hidratar*: el HTML llega deshidratado —con la forma correcta pero sin nada
> corriendo adentro— y el circuito lo rehidrata.

La metáfora hace que se recuerde. Pero sola no alcanza para depurar nada, así que
inmediatamente después va lo literal: qué corre, dónde, en qué orden, qué observa el
que mira.

**Anti-patrón:** quedarse en la metáfora. «El componente cobra vida» no le sirve a nadie
a las tres de la mañana.

### 4.3 ¿Cómo se citan los errores y la evidencia?

**Respuesta: literales. El mensaje exacto, el número exacto.**

| | |
| --- | --- |
| ✅ | `Locator expected to have text '…' But was: '<element(s) not found>'` |
| ✅ | «1 de 8 corridas en rojo» |
| ❌ | «a veces falla» |
| ❌ | «la prueba puede dar error de localización» |

El mensaje literal es lo que alguien va a **pegar en un buscador** cuando le pase. El
número exacto es lo que hace que una afirmación sea comprobable en vez de creíble.

### 4.4 ¿Cómo se hace concreta una definición abstracta?

**Respuesta: anclando cada parte de la definición a su correspondencia física, línea por línea.**

Una definición se entiende cuando se puede señalar. La técnica es descomponerla en sus
partes y darle a cada una **su lugar en el artefacto real**:

```markdown
| La definición dice | En el archivo es | Líneas |
| --- | --- | --- |
| **lo que la persona ve** | El encabezado: el título y la bajada | [19–24](…#L19-L24) |
| **lo que puede hacer** | El formulario: un campo y un botón | [38–81](…#L38-L81) |
| **en qué estados puede quedar** | El bloque de estados, excluyentes | [87–110](…#L87-L110) |
```

**Por qué funciona:** una definición abstracta se lee y se olvida porque no deja rastro
sensorial. Con el anclaje, el lector la vuelve a encontrar cada vez que abre el archivo,
y el archivo pasa a ser el recordatorio.

**Y hace un segundo trabajo, más silencioso:** obliga a quien escribe a comprobar que la
definición **describe algo que existe**. Una parte de la definición que no se puede
anclar a ninguna línea es, casi siempre, una parte que sobra.

**Los rangos se verifican, no se estiman.** Una cita que apunta tres líneas más abajo
destruye la confianza en todas las demás, y es el error más fácil de cometer porque las
líneas se corren con cada edición.

**Su complemento obligado — anclar también lo que la definición excluye:**

| No es X | Qué es | Dónde se ve |
| --- | --- | --- |

Sin esa segunda tabla, el lector sabe reconocer el concepto pero no sabe **dónde
termina**, que es lo que hace falta para aplicarlo en un caso nuevo.

### 4.5 ¿Qué se hace cuando el lector propone una idea mejor que la escrita?

**Respuesta: se adopta con sus palabras, y se le busca la correspondencia física.**

Una guía viva recibe formulaciones de quien la lee, y suelen ser mejores que las del
autor porque nacen del intento de entender. La forma de incorporarlas:

1. **Adoptar la formulación**, no parafrasearla. Si alguien dice «la superficie es un
   marco estructurado donde se ordenan esas representaciones», esa frase entra tal cual.
2. **Buscarle el anclaje** (§4.4). Casi siempre la idea ya está realizada en el código
   sin que nadie la hubiera nombrado —y encontrarla es la confirmación de que la
   formulación era correcta—.
3. **Dejar la pregunta que la originó** como encabezado, porque otro lector va a llegar
   por el mismo camino.

**El indicio de que la idea era buena:** que al buscarle el anclaje aparezca sola. Una
formulación que no se puede anclar a nada es elegante y probablemente falsa.

### 4.6 ¿Qué tono?

**Respuesta: el de alguien que explica algo que le costó entender, a un par.**

- **Segunda persona para las reglas prácticas.** «Tapate el código y preguntate si…»
- **Frases cortas.** Cuando una frase necesita dos comas y un paréntesis, son dos frases.
- **Rayas —así— para el inciso que aclara**, no paréntesis, que se leen como opcionales.
- **Comillas angulares «así»** para poner en boca de alguien una frase que no es del documento.
- **Sin adjetivos de entusiasmo.** «Elegante», «potente», «robusto» no informan.
- **Sin condescendencia.** Nada de «simplemente», «basta con», «obviamente»: si fuera
  obvio, el documento no existiría.

---

## 5. La postura

Esto es lo que separa un documento confiable de uno persuasivo, y es la parte que más
fácil se pierde.

### 5.1 ¿Qué se puede afirmar?

**Respuesta: lo que se verificó. Lo demás se marca como lo que es.**

Tres registros, y hay que poder distinguirlos en el texto:

| Registro | Cómo se escribe |
| --- | --- |
| **Verificado** | «16 de 16 en verde, en `evidencia/2026-09-03-…`» |
| **Razonado** | «El patrón calza: la primera corrida paga el arranque frío» |
| **Supuesto** | «No puedo afirmar el mecanismo exacto de la traza secundaria» |

El tercero es el que se omite, y es el que más confianza construye. Un documento que
nunca dice «esto no lo comprobé» obliga al lector a desconfiar de todo por igual.

**Y el matiz honesto que casi siempre falta:** «16 corridas no prueban que la
intermitencia esté extinguida —una intermitencia nunca se demuestra ausente contando
corridas—». Decirlo no debilita el documento: es lo que hace creíble el resto.

### 5.2 ¿Qué se hace con un hallazgo que aparece mientras se escribe?

**Respuesta: se anota, se explica, y no se arregla de contrabando.**

Escribir un documento formativo destapa problemas —es una de sus mejores propiedades—.
La tentación es corregirlos en silencio. La forma correcta:

1. **Anotarlo donde apareció**, con el síntoma literal.
2. **Explicar por qué es así**, si se puede determinar.
3. **Decir qué se hizo** —y si no se resolvió, **por qué no**.

> «Las pruebas se ajustaron a lo que la aplicación hace, no al revés: corregir el
> comportamiento es una decisión de diseño, y no la toma la prueba.»

Esa última frase es el modelo. **Dice quién decide**, que casi siempre es la información
que falta.

### 5.3 ¿Por qué declarar lo que no se hizo?

**Respuesta: porque una ausencia sin explicar se lee como olvido, y con razón.**

Y hay tres ausencias distintas, que se resuelven distinto:

| Tipo | Significa | Qué hacer |
| --- | --- | --- |
| **Pendiente** | Debería estar y todavía no está | Anotarlo como deuda |
| **No aplica** | La situación no puede ocurrir | Explicar por qué no puede |
| **Otra herramienta** | Se hace, pero no acá | Decir con qué se hace |

Confundir «no aplica» con «pendiente» hace crecer una lista de deudas con cosas que
nunca hubo que hacer. Al revés —llamar «no aplica» a un pendiente— es la forma educada
de barrerlo abajo de la alfombra.

### 5.4 ¿Se documenta lo que salió mal en el camino?

**Respuesta: sí, cuando el error enseña algo que el resultado final ya no muestra.**

El código terminado no conserva las huellas de por qué es así. Si en el camino se
probó algo que no funcionó —y el motivo es instructivo— eso vale más que la solución:

> «El caso se escribió primero afirmando `/login?estado=sesion-requerida`. **Falló.** Lo
> que la aplicación produce de verdad es `/login?returnurl=%2FHolaMundo`.»

Ahí se ve la restricción real, que en el resultado final quedó invisible.

**Dónde no:** un error trivial —un `using` que faltaba— no enseña nada. El criterio es
si alguien podría volver a cometerlo por la misma razón.

---

## 6. Anti-patrones

Cada uno con el síntoma por el que se lo reconoce.

| Anti-patrón | Se reconoce por | Qué hacer |
| --- | --- | --- |
| **Preguntas huecas** | «¿Cuál es la importancia de…?» | Es una definición: declarala |
| **Respuesta larga** | La negrita ocupa tres líneas | La pregunta abarcaba dos; partila |
| **Ejemplo sin contraejemplo** | Solo ✅ | Agregá el ❌ que marca el límite |
| **Catálogo de quejas** | Errores listados sin «qué hacer» | Sin la salida, no forma criterio |
| **Metáfora sola** | «Cobra vida», «se despierta» | Agregá el mecanismo literal |
| **Definición sin anclaje** | Se entiende al leerla y no se sabe aplicarla | Señalá cada parte en el artefacto real |
| **Cita de línea estimada** | El rango no coincide con lo que dice | Verificala; una falla desacredita todas |
| **Negrita decorativa** | Cuatro fragmentos por párrafo | Dejá el que se pueda citar |
| **Relleno introductorio** | «En el mundo actual del software…» | Borralo entero |
| **Frase de transición vacía** | «Es importante notar que…» | Borrala; lo que sigue se sostiene solo |
| **Certeza uniforme** | Todo afirmado con el mismo peso | Marcá qué verificaste y qué no |
| **Ausencia sin declarar** | El documento simplemente no lo menciona | §5.3 |
| **Bullets sin verbo** | «Rendimiento», «Seguridad», «Escalabilidad» | Cada punto afirma algo o se va |
| **Estructura por herramienta** | Secciones que copian el índice del framework | Ordená por decisión del lector |
| **Secciones sin numerar** | No se puede escribir «ver §4.2» | Numerá: un criterio que no se cita no se usa |
| **Índice sin glosa** | Lista de títulos repetidos | Agregá qué hay adentro y para quién |
| **Anidamiento de cuatro niveles** | Aparece un `#####` | El `###` trataba dos decisiones |

---

## 7. Lista de verificación

Para pasar antes de dar un documento por terminado.

**Del patrón**

- [ ] Cada sección con decisión abre con una pregunta que alguien realmente haría.
- [ ] Cada respuesta cabe en una línea y se sostiene fuera de contexto.
- [ ] Cada criterio aplicable tiene ✅ y al menos un ❌.
- [ ] Las definiciones **no** están disfrazadas de pregunta.

**De la estructura**

- [ ] Los términos se definen antes de usarse.
- [ ] Las secciones están numeradas, y cada decisión es un `###` citable.
- [ ] Ningún `#####`; ningún `##` de más de ~150 líneas.
- [ ] Hay índice si supera ~200 líneas, con glosa por entrada y solo del nivel `##`.
- [ ] Las anclas del índice se verificaron en el render, no de memoria.
- [ ] Las referencias cruzadas (§n.m) apuntan a la sección que existe hoy.
- [ ] Hay una sección de lo que deliberadamente no se cubre.
- [ ] Cierra con una frase que se sostiene sola.

**De la postura**

- [ ] Lo verificado se distingue de lo razonado y de lo supuesto.
- [ ] La evidencia se cita con números y mensajes literales.
- [ ] Los hallazgos no resueltos dicen **quién** decide.
- [ ] No hay ninguna afirmación que no pueda ser falsa.

**De la voz**

- [ ] Ningún párrafo con más de una frase en negrita.
- [ ] Ninguna metáfora sin su mecanismo al lado.
- [ ] Toda definición abstracta anclada a su correspondencia física, y a lo que excluye.
- [ ] Los rangos de línea citados se verificaron contra el archivo, no se estimaron.
- [ ] Ningún «simplemente», «basta con», «obviamente».
- [ ] Ningún adjetivo de entusiasmo.

---

## 8. Lo que este documento no cubre

| No cubre | Por qué |
| --- | --- |
| **Documentación de referencia de API** | Su valor es la completitud y la búsqueda, no la formación de criterio. El patrón de preguntas ahí estorba. |
| **Registros de cambios y bitácoras** | Son registros por definición (§1.1). Necesitan precisión y fecha, no pedagogía. |
| **Prompts de sistema para agentes** | Comparten la exigencia de precisión, pero optimizan para el cumplimiento, no para la comprensión. |
| **La estructura de carpetas y nombres de archivo** | Es convención de cada repositorio. |
| **El idioma** | Los ejemplos están en español rioplatense porque el corpus de origen lo está. El patrón no depende del idioma; la §4.4 sí. |

---

## 9. El criterio, en una línea

> **Explicá lo que costó entender, mostrá dónde está el límite con un contraejemplo, y
> decí qué no comprobaste.**

Lo demás de este documento son formas de sostener esas tres cosas.

---

## Anexo — El corpus de referencia

El estilo está destilado de dos documentos que se pueden leer como ejemplo completo:

| Documento | Qué muestra especialmente bien |
| --- | --- |
| `LAB/Lab-E2E.WebBlazor.Base/Guides/Caso-HolaMundo-Page.MD` | El patrón de preguntas sostenido; el catálogo de casos que cumplen y no cumplen (§2.3–2.4); la explicación de un mecanismo contraintuitivo con metáfora **y** literal (§4) |
| `LAB/Lab-E2E.WebBlazor.Base/Guides/Caso-Login-Page.md` | Dos documentos hermanos que se explican por su diferencia; el hallazgo anotado y no resuelto (§6); la sección de ausencias con su porqué (§7) |
