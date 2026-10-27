# Entrega de unidades de trabajo

## Delegación del merge

| | |
| --- | --- |
| **Fecha** | 2026-10-27 |
| **Decidió** | El responsable del producto (PO) |
| **Responsable de ejecutarla** | El agente que conduce cada unidad de trabajo |
| **Conocimiento** | Conformacion-Pull-Request-Automatico (IA.Knowledge.Base) |
| **Techo de espera de la guarda** | 30 minutos |
| **Intervalo de relectura** | 30 segundos |
| **Control que lee la guarda (G3)** | El workflow `Verificar` (`.github/workflows/verificar.yml`) |

El agente abre el pull request de su unidad, lo fusiona cuando se cumplen G1–G4 (cabeza auditada, `mergeable_state`
`clean`, al menos una corrida de controles en éxito para ese SHA y ninguna reserva), con un merge commit atado al SHA,
y borra la rama remota. Ante una reserva el merge vuelve al PO.

**Excepción:** si hay un cuestionamiento particular sobre la unidad, se para y se hace manual. Es revocable por unidad.

### Testimonio literal

> «sobre el merge automático, esto surgió porque despues de un avance surgia preguntas y confirmaciones tontas, - nada
> que con un analisis previo no se resuelva por si solo … de esta manera el desarrollo no se para … Mi objetivo es que
> se enriquesca de tal forma el conocimiento analitico que los subagentes con este conocimiento puedan orquestar de
> forma automatica todo el proceso de desarrollo, busco una interactividad autonoma e inteligente»
>
> — PO, 2026-10-27, conversación con el agente; asentado en el registro de decisiones del PO (expediente 0002,
> folio 130).
