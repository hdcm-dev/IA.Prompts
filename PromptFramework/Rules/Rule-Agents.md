# Rule — Agents

## Objetivo

Definir cómo asignar subagentes, ajustando la estructura de delegación al tamaño y la naturaleza real de la tarea.

Los límites (usar subagentes, paralelismo máximo, modelo y esfuerzo de cada rol) pueden indicarse en el propio prompt; en su ausencia, ajustarlos a la naturaleza de la tarea.

---

# Cuándo delegar

Delegar en subagentes cuando:

- la tarea se descompone en partes **independientes** ejecutables en paralelo (varios repos, varios dominios, varios documentos);
- una exploración amplia produciría más contexto del que la conversación necesita conservar (el subagente lee mucho, devuelve poco);
- se requieren perspectivas independientes (revisión, verificación adversarial).

No delegar cuando la tarea es secuencial, pequeña o depende del contexto ya cargado en la conversación: el costo de traspasar contexto superaría el beneficio.

---

# Autoajuste al tamaño de la tarea

Dimensionar la delegación según el trabajo real, no según un número fijo:

| Tarea | Asignación |
|-------|------------|
| Puntual o secuencial | Sin subagentes; ejecutar en la conversación |
| Pocas unidades independientes (2–4) | Un subagente por unidad |
| Muchas unidades homogéneas | Lotes por subagente, respetando el paralelismo máximo configurado |
| Resultado crítico | Agregar un subagente verificador independiente |

Cada subagente recibe **una única responsabilidad** y el contexto mínimo autocontenido para cumplirla: objetivo, alcance, restricciones, rutas exactas y formato del resultado esperado.

---

# Decidir, convocar o consultar

El subagente no ve lo que el agente principal sabe de la persona. Por eso el prompt de cada subagente declara:

- `OBJETIVO`: qué tiene que lograr el trabajo, con su fuente.
- `DECIDE`: qué clases de decisión toma solo. Por defecto, todo lo aditivo y reversible sin efecto externo.
- `LÍMITES`: lo que siempre se eleva: producción, dinero, datos personales, credenciales, obligaciones con terceros, lo irreversible.
- `ZONAS-DEL-USUARIO`: rutas que no se tocan.

Antes de devolver una pregunta, el subagente mide si el cambio es aditivo o estructural, si es reversible, si pone en riesgo el objetivo y de quién es la norma que choca. Si el cambio es aditivo y reversible, decide y lo declara. Si es complejo, lo dice para que se convoque una mesa. Cuando pregunta, lo hace con una recomendación y con lo que rige si nadie responde.

Si falta un acceso o falla un paso que la persona prescribió, lo dice en una línea en el mismo momento, sin rodearlo por otro camino. La primera delegación en un destino que no la tiene escrita (por ejemplo, el primer merge automático de un repositorio nuevo) se consulta con propuesta.

---

# Modelo y esfuerzo por rol

El modelo y el esfuerzo de razonamiento de cada subagente se eligen por la **naturaleza de su rol**, no por el dominio
ni por el modelo de la conversación. Un subagente sin modelo ni esfuerzo explícitos los hereda de la conversación, y
eso iguala para arriba: lo mecánico se paga como juicio. Por eso cada rol los declara.

**Primero, lo mecánico no va a un modelo.** Listar, contar, leer historia de versiones, comprobar que una ruta o un
rango de líneas existe, buscar patrones: si un script lo resuelve de forma determinista, lo corre el agente principal
una vez y entrega el resultado a los subagentes. Un subagente que rehace ese trabajo con decenas de llamadas relee
todo su contexto en cada una, y ese releer es el grueso del consumo.

| Naturaleza del rol | Ejemplos | Tier de modelo | Esfuerzo |
|---|---|---|---|
| Mecánico y determinista | Inventario, conteos, historia git, verificación de citas y enlaces, cobertura | Ninguno: script | — |
| Aplicar lo ya especificado | Correctores que aplican hallazgos concretos, reformateo, traslado de texto | Rápido | bajo |
| Relevar y buscar | Barridos de búsqueda, extracción de datos con criterio simple | Rápido | medio |
| Ejecutar o escribir | Escritores de un dominio, constructores, editores, integradores | Mayor | medio |
| Verificar | Verificador adversarial, revisión de un entregable, consolidación entre resultados | Mayor | alto |
| Juzgar el conjunto o concluir | Crítico de completitud, mesa, jurado, conclusiones que relacionan resultados con lo hecho | Mayor (o el de razonamiento superior, si el prompt lo pide) | máximo disponible |

**Tiers, no nombres.** La regla nombra tiers para no envejecer con cada versión de modelo. Correspondencia vigente
(se actualiza acá, en un solo lugar):

| Tier | Modelo vigente |
|---|---|
| Rápido | Sonnet |
| Mayor | Opus |
| Razonamiento superior | Fable (sólo por pedido explícito del prompt; si su cupo se agota, el rol sigue en el tier mayor y se declara) |

**Cuándo subir o bajar un escalón.** Se sube cuando el error del rol es caro de detectar después (seguridad,
producción, lo irreversible, un veredicto que otros consumen sin revisar). Se baja cuando el resultado lo revisa otro
rol más arriba en la tabla, o cuando la tarea es reversible y barata de repetir. La verificación no baja de alto:
un verificador barato aprueba lo que debía rechazar.

**Override del prompt.** Un tool-prompt puede fijar el modelo o el esfuerzo de un rol con parámetros de invocación
(por ejemplo, `{modelo-verificacion}` o `{esfuerzo}`); lo que fija prevalece sobre esta tabla. Un prompt que sólo
dice «subagentes» aplica esta tabla.

**Medir.** Cuando una tarea se repite (indexados, auditorías, lotes), se registra el consumo por rol —llamadas,
contexto releído, contexto nuevo y salida— y un indicador de calidad del resultado, para recalibrar esta tabla con
datos y no por intuición.

---

# Especialización

Cuando las subtareas requieran conocimientos distintos (arquitectura, seguridad, redes, documentación, etc.), formular cada prompt de subagente desde la especialidad correspondiente.

---

# Agregación de resultados

El agente principal:

- consolida los resultados verificando consistencia entre sí y con el objetivo;
- no acepta resultados sin evidencia (aplica `Rule-Evidences.md`);
- resuelve o reporta los conflictos entre resultados;
- integra todo en el reporte final según `Rule-Workflow.md`.
