# Rule — Agents

## Objetivo

Definir cómo asignar subagentes, ajustando la estructura de delegación al tamaño y la naturaleza real de la tarea.

Los límites (usar subagentes, paralelismo máximo) pueden indicarse en el propio prompt; en su ausencia, ajustarlos a la naturaleza de la tarea.

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

# Especialización

Cuando las subtareas requieran conocimientos distintos (arquitectura, seguridad, redes, documentación, etc.), formular cada prompt de subagente desde la especialidad correspondiente.

---

# Agregación de resultados

El agente principal:

- consolida los resultados verificando consistencia entre sí y con el objetivo;
- no acepta resultados sin evidencia (aplica `Rule-Evidences.md`);
- resuelve o reporta los conflictos entre resultados;
- integra todo en el reporte final según `Rule-Workflow.md`.
