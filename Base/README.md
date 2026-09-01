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
