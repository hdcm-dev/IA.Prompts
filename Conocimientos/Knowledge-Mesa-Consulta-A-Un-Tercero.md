# Mesa que consulta a un tercero: cómo dialoga una mesa de expertos con una persona real por un canal

**Alias:** Mesa-Consulta-A-Un-Tercero
**Naturaleza:** propio
**Tema:** Protocolo de conversación entre una mesa de expertos y una persona de afuera (cliente, jefe de proyecto, usuario): roles, ronda, forma del mensaje, espera, correlación de respuestas, registro y cortes. Vale para cualquier canal.
**Consumidor:** transversal
**Condicion-de-carga:** la mesa necesita respuestas de alguien que no es el PO
**Hereda-de:** —
**Sustituye:** —
**Compatible-con:** Knowledge-Mesa-De-Expertos-A-Pedido.md 1.2 · un conocimiento de canal (hoy: Knowledge-WhatsApp-Web-MCP.md)
**Versión:** 1.2
**Estado:** Vigente
**Fecha:** 2026-09-30

---

## 0. Propósito y alcance

Fija **cómo conversa la mesa con un tercero**, sin importar el medio. El medio (WhatsApp, correo, Slack, un formulario) lo cubre un **conocimiento de canal** aparte; este documento no dice cómo se envía un mensaje, sino qué se envía, quién lo arma, cuándo y qué se hace con la respuesta.

**Por qué existe.** Una mesa tiene muchos especialistas y el tercero es una sola persona, ocupada, que contesta cuando puede. Si cada especialista le pregunta por su cuenta, el tercero recibe una ráfaga de mensajes repetidos, contesta a medias y la mesa se queda esperando. El cuello de botella es la persona, no las máquinas: todo lo de este protocolo apunta a gastarle menos tiempo y a sacar más de cada respuesta.

**Fuera de alcance:** la mecánica del canal, y cómo se arma la mesa (eso está en Mesa-De-Expertos-A-Pedido).

## 1. Roles

| Rol | Hace | No hace |
|---|---|---|
| **Especialistas** | Anotan sus dudas con el porqué (qué decisión destraba la respuesta) y la prioridad. Reciben la respuesta textual y deciden si les alcanza. | No tocan el canal ni le escriben al tercero. |
| **Entrevistador** | Junta las dudas, saca las repetidas, las ordena por prioridad y las reescribe como preguntas fáciles de contestar. Decide qué entra en cada ronda. | No inventa preguntas que ningún especialista pidió. No cambia la intención de una pregunta. |
| **Coordinador (mensajero)** | Es el único que usa el canal: envía la ronda, espera, lee, reparte las respuestas y registra. | No reescribe lo que armó el entrevistador. |
| **PO** | Pone el destinatario, el canal y los límites. Se le avisa ante un corte (§6). | — |

El entrevistador puede ser un subagente de la mesa o el mismo coordinador con esa función. Lo que no se negocia es que **haya una sola mano en el canal**.

## 2. La ronda

1. **Recolección.** Cada especialista entrega sus dudas con este formato: `rol · pregunta · por qué la necesito · prioridad (alta/media/baja) · qué hago si no contesta`.
2. **Destilado (entrevistador).**
   - Une las dudas que preguntan lo mismo y conserva la lista de quién pidió cada una.
   - Descarta lo que ya se sabe (del expediente o de respuestas anteriores) o lo que la mesa puede resolver sola.
   - Deja **3 a 5 preguntas por ronda**, las de mayor prioridad. El resto queda en cola para la próxima.
   - Reescribe cada una para que se pueda contestar corto (§3).
3. **Envío (coordinador).** Un solo mensaje por ronda, con las preguntas numeradas `R<ronda>.<n>`.
4. **Espera** (§4). Mientras tanto, la mesa sigue con lo que no depende de la respuesta.
5. **Reparto.** Cada respuesta se asigna a su pregunta (§5) y se le entrega **textual** a cada especialista que la pidió, junto con la pregunta tal como salió.
6. **Cierre de la ronda.** Cada especialista marca su duda como `resuelta`, `parcial` (repregunta en la próxima ronda) o `abierta` (se aplica su "qué hago si no contesta"). Recién ahí se arma la ronda siguiente.

**Tope:** si después de 3 rondas una duda sigue abierta, no se insiste: se lleva al PO como pregunta para él.

### 2.1 Modo «de a una» (cuando el tercero lo pide)

Por un canal de chat, una persona ocupada puede preferir **una pregunta por mensaje**. Medido el 2026-09-30 con el jefe de proyecto de un organismo: contestó entera, en un solo mensaje, una primera ronda de 7 preguntas mandadas en mensajes sueltos; ante una segunda ronda de 5 preguntas en un solo mensaje largo pidió «¿podés ir haciendo las preguntas de a una por agente? para poderlas responder». Si lo pide, **manda su forma** (con el ok del PO si cambia lo acordado):

- **Una pregunta por mensaje**, firmada por el especialista que la pidió; **la siguiente sale recién cuando contesta la anterior**. Nunca dos pendientes.
- Primer mensaje del modo: un acuse corto («van de a una, contestá cuando puedas, sin apuro; el mensaje largo no hace falta contestarlo»).
- **El entrevistador guía la secuencia**, no solo destila: arma cada pregunta con el contexto justo para pensarla (por qué se pregunta, qué implica cada opción, la recomendada si corresponde, qué se toma con «no sé»), elige la próxima según lo contestado y saltea lo que dejó de aplicar. Conviene que sea **un agente persistente** (se le reenvía cada respuesta y conserva el hilo), no uno nuevo por pregunta.
- Cada mensaje nuevo **empieza confirmando en media línea lo que se hizo con la respuesta anterior** y sigue con la próxima pregunta. Si la persona entendió mal un dato (p. ej. leyó «14 y 16 h» donde decía «14 a 26 h»), se corrige ahí, con tacto.
- Cuando la respuesta es una indicación y no una opción («¿podés sacarlo del plan y dejarlo como opcional?»), es una **decisión del tercero dentro de su competencia**: se registra como tal, se confirma y se sigue; no es un corte (§6) salvo que exceda lo que el PO delegó.
- Después de las preguntas urgentes, un mensaje breve que diga que lo que falta es menos urgente y que puede seguir ahora o después.
- **El tercero no sabe lo que la mesa discutió.** Cada mensaje le cuenta en llano el porqué (qué nos llevó a preguntar y qué cambia según lo que diga) antes de la pregunta. Una pregunta que le pide una gestión o una conclusión de entrada («¿podés pedirle a legales que lo mire?») sin ese contexto queda sin respuesta: medido el 2026-09-30, más de una hora de silencio; el PO pidió «explicale algo y decile por qué le preguntás… andá dialogando». Se rehace como diálogo en pasos: primero algo que pueda contestar ya (cómo trabaja hoy), con la explicación; la gestión, recién si corresponde. Al reformular, no se le reprocha el silencio («te lo explico mejor»).

## 3. Forma del mensaje

- **Primer mensaje:** presenta al asistente y a quién representa ("asistente de <PO> que consulta en nombre de la mesa de <tema>"), dice cuántas preguntas vienen y avisa que puede contestar como le quede cómodo.
- **Cada pregunta:**
  - lleva su número y el rol que la pide: `R1.2 [Especialista SIG]`;
  - pregunta una sola cosa;
  - si la respuesta es cerrada, ofrece opciones (`¿A, B u otra?`); si es abierta, da un ejemplo de respuesta;
  - lleva el contexto justo para entenderla, en media línea, sin jerga interna ni nombres de documentos o agentes.
- **Siempre:** cierra pidiendo que conteste citando el número ("1: …, 2: …"), por texto, y aclarando que "no sé" o "después te digo" también sirven.
- **Nunca:** preguntar lo que ya contestó; más de una ronda sin respuesta; mandar datos sensibles o archivos sin ok del PO.

Ejemplo de ronda (una sola línea si el canal lo necesita):

> 🤖 R2 · Tres dudas de la mesa del plan de trabajo · R2.1 [Especialista SIG] ¿Los datos viales se editan hoy en QGIS, en planillas u otra cosa? · R2.2 [Analista de requerimientos] Para "consulta rápida", ¿pensás en el celular en campo, en una PC en la oficina o en las dos? · R2.3 [Planificador] ¿Hay una fecha del organismo que el plan tenga que respetar? · Si podés, contestá con el número (ej. "1: QGIS"). "No sé" también sirve. ¡Gracias!

## 4. Esperar sin quemar

- La persona contesta en minutos u horas. **No se queda un agente bloqueado esperando.**
- **Preferido: que el canal despierte al coordinador** solo cuando llega algo (en WhatsApp, el vigía + Monitor del conocimiento de canal, paso 6). Mientras tanto no se consume nada.
- **Respaldo:** si el canal no lo permite, el coordinador revisa cada **10–20 minutos** (`/loop`, ScheduleWakeup o CronCreate). Cada revisión es una lectura corta de lo nuevo desde la última vez; si no hay nada, vuelve a dormir. Tener en cuenta que cada revisión vacía cuesta un turno.
- Cuando llega la primera respuesta, espera **1–2 minutos más** antes de interpretar, porque la gente contesta en varios mensajes seguidos.
- Mientras tanto, lo que depende de la respuesta queda marcado `pendiente de <tercero>, R<n>.<m>` y la mesa sigue con lo demás.

**¿Workflow u orquestación multiagente?** Sirve para lo que pasa entre respuestas: redactar dudas en paralelo, destilarlas, repartir y analizar una respuesta larga entre varios especialistas. **No sirve para la espera ni para el canal**: un workflow corre sin persona en el medio y el canal admite una sola mano.

## 5. Correlación de respuestas

- Si la respuesta cita números, se asigna directo.
- Si no cita números, el coordinador la asigna por contenido y marca la asignación como **inferida**. Si hay dos lecturas posibles, se agrega a la próxima ronda una pregunta de confirmación ("¿El 'sí' era por la 1 o por la 3?").
- Una respuesta que abre un tema nuevo se reparte al especialista que corresponda, aunque nadie lo haya preguntado, y se anota como **aporte espontáneo**.
- Lo que el canal no deja leer (audio, imagen) se pide por texto, una vez y con amabilidad.

## 6. Cortes: se frena y se avisa al PO

- El tercero pide hablar con el PO, pregunta quién es el asistente con desconfianza o se molesta.
- La conversación sale del tema, o aparece algo personal, sensible o comprometedor.
- El tercero pide algo que excede consultar (que se envíe un documento, que se decida algo, que se acepte una condición). **Excepción:** lo que el PO autorizó de antemano (p. ej. «si pide el Word, generalo y mandáselo») se hace sin frenar, y se registra.
- El tercero pide cambiar la forma de la conversación (p. ej. «de a una»): se frena, se consulta al PO y, con su ok, se adopta (§2.1).
- Pasan 24 h sin respuesta a una ronda: se avisa y no se insiste.

## 7. Registro en el expediente

Por cada ronda se guarda en el expediente de la mesa:
- las dudas tal como las entregó cada especialista;
- el mensaje tal como salió, con la hora;
- las respuestas textuales, con la hora;
- la asignación de cada respuesta (directa o inferida);
- el estado final de cada duda.

Así el PO puede ver qué se preguntó y cómo se pasó de lo que pedían los especialistas a lo que se envió.

## 8. Lo que tiene que dar el conocimiento de canal

Para cambiar de canal alcanza con un conocimiento que diga cómo:

| Operación | En WhatsApp (Knowledge-WhatsApp-Web-MCP) |
|---|---|
| Abrir el canal y autenticarse | vincular WhatsApp Web (QR) en el Chrome del MCP |
| Verificar el destinatario antes de enviar | encabezado del chat + `aria-label` del cuadro |
| Enviar un mensaje, y sus límites de formato | `type_text` + Enter; sin saltos de línea |
| Leer lo nuevo desde la última lectura | `data-pre-plain-text` del chat abierto |
| Qué no puede leer | audios, imágenes, stickers |
| Cuánto dura la sesión y cómo se recupera | sólo lo que dura la sesión de Claude; re-vincular |

Si el canal y este protocolo chocan, la mecánica la decide el canal (por ejemplo, "una sola línea") y la conversación la decide este protocolo.

## 9. Anti-patrones

- Cada especialista le escribe por su cuenta al tercero.
- Rondas de 10 preguntas "para aprovechar".
- Reescribirle al especialista la respuesta del tercero en lugar de dársela textual.
- Quedarse bloqueado esperando la respuesta, o dejar a la mesa parada mientras tanto.
- Repreguntar lo que ya se contestó porque no se leyó el expediente.
- Mencionar agentes, SDD, expedientes o jerga interna en los mensajes.

## 10. Control de cambios

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-09-30 | Versión inicial, surgida de la primera consulta por WhatsApp de la mesa del plan de trabajo. |
| 1.1 | 2026-09-30 | Tras la consulta real: **§2.1 modo «de a una»** (una pregunta por mensaje, entrevistador persistente que guía la secuencia, confirmar lo anterior en media línea, indicaciones del tercero como decisiones dentro de su competencia); **§4** prefiere que el canal despierte al coordinador (vigía + Monitor) y deja la revisión periódica como respaldo; **§6** suma la excepción de lo autorizado de antemano por el PO y el cambio de forma pedido por el tercero. |
| 1.2 | 2026-09-30 | §2.1: el tercero no conoce lo que la mesa discutió; cada mensaje explica el porqué antes de preguntar y los temas delicados se tratan en diálogo por pasos (lección de la pregunta sobre Google Earth). |
