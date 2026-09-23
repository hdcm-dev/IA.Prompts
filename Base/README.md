# Base

Marcos de orquestación de propósito general: piezas que definen **cómo se organiza un conjunto de agentes** para trabajar sobre un artefacto, con independencia del dominio y del contenido del artefacto.

Se mantienen fuera de `PromptFramework` porque no son componentes componibles de la jerarquía `Prompt → Profile → RuleSet → Rules`: no describen el comportamiento de *un* agente, sino el protocolo de un colectivo —quién se convoca, quién juzga, quién corrige y quién aprueba— y su condición de corte.

---

## Cómo se usan

Se invocan por ruta absoluta desde la raíz del workspace, igual que un Tool-Prompt, y el marco se aplica sobre el artefacto que indique el pedido:

```
Lee y ejecuta /IA/IA.Prompts/Base/Mesa-Evaluadora.md sobre <artefacto>
```

El marco no reemplaza al prompt del caso: fija el procedimiento del ciclo. Qué se revisa, con qué objetivo y bajo qué restricciones lo aporta el contrato de entrada que el propio marco exige antes de arrancar.

---

## Marcos disponibles

| Marco | Qué aporta | Usar cuando |
|-------|------------|-------------|
| [Mesa-Evaluadora.md](Mesa-Evaluadora.md) | Ciclo cerrado de revisión, veredicto, corrección y verificación sobre artefactos de especificación (`spec → plan → tareas → código/pruebas`): panel armado por señales observables, informes a ciegas, escala de evidencia E1–E4, jurado de cinco funciones objetivo, cuerpo auditor separado de quien aprueba, reparación en la capa de origen, escalada al humano por lista cerrada de disparadores y criterios de parada con bloque de cierre. | Hay que someter una especificación —o cualquier artefacto derivado de ella— a una revisión con autonomía decisoria acotada, y se necesita que el resultado quede trazable: qué se detectó, quién lo juzgó, qué se corrigió, qué se verificó y qué deuda se asumió deliberadamente. |

---

## Documentos transversales

No son marcos de orquestación —no definen quién se convoca ni cómo se decide— pero cualquier marco puede apoyarse en ellos.

| Documento | Qué aporta | Usar cuando |
|-----------|------------|-------------|
| [Medios.md](Medios.md) | Declaración de los medios de observación disponibles en este entorno: navegador Chromium sin escritorio para interfaces web —alcanzando servicios internos y públicos, con registro de errores de consola— y dispositivo Android físico por USB, mediado por el contenedor dueño del recurso. Incluye la regla de exclusividad del dispositivo, el alcance y los límites de cada medio, y cómo se cita lo observado según la escala de evidencia. | El ciclo tiene que juzgar una interfaz que se ejecuta y no solo el texto que la describe. Sin medio declarado, todo juicio sobre el comportamiento de una interfaz es conjetura y no funda correcciones. |
| [Estilo-Redaccion-Explicativo.md](Estilo-Redaccion-Explicativo.md) | La forma de redactar un documento cuyo propósito es **formar criterio** y no solo registrar qué se hizo: el patrón de exposición por pregunta guía, respuesta en una línea y ejemplos contrastados (✅/❌); la estructura —definiciones primero, secciones numeradas y citables, índice con glosa, cierre en una frase—; la voz; y la postura, que distingue lo verificado de lo razonado y de lo supuesto, declara las ausencias con su motivo y anota los hallazgos diciendo quién decide. Incluye anti-patrones con su síntoma y una lista de verificación. | Hay que producir una guía, un documento de caso o una explicación de por qué algo está construido como está, y se quiere que quien la lea quede en condiciones de decidir por su cuenta en una situación que el documento no cubre. |
