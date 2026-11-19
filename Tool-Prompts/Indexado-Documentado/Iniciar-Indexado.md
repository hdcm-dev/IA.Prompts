# Tool-Prompt — Iniciar Indexado

> **Invocación**:
> - Un proyecto: `Lee y ejecuta /IA/IA.Prompts/Tool-Prompts/Indexado-Documentado/Iniciar-Indexado.md en {proyecto}`
> - Varios proyectos: `Lee y ejecuta /IA/IA.Prompts/Tool-Prompts/Indexado-Documentado/Iniciar-Indexado.md de {proyecto-a} y {proyecto-b} y deja la indexación en {destino}`

---

# Parámetros de invocación

| Parámetro | Descripción | Si no se indica |
|-----------|-------------|-----------------|
| `{proyectos}` | Uno o más repositorios o carpetas del workspace a indexar (también proyectos no versionados) | Solicitarlo al usuario antes de comenzar |
| `{destino}` | Dónde generar la ia-db | Un proyecto → `<proyecto>/ia-db` · Varios proyectos o «en la raíz» → `/ia-db` en la raíz del workspace (modo federado) |
| `{modelo-verificacion}` | Tier de modelo de la verificación adversarial y de la crítica | Mayor (`Rule-Agents.md`, «Modelo y esfuerzo por rol») |
| `{esfuerzo}` | Esfuerzo de la escritura, si se quiere subir o bajar | El de la tabla de etapas del Profile |

---

# Contexto

Los proyectos indicados no disponen de base de conocimiento `ia-db` (o debe regenerarse). Cada conversación nueva obliga a releer código y documentación completa, con alto consumo de tokens.

---

# Objetivo

Generar la ia-db de `{proyectos}` en `{destino}` conforme a la estructura canónica del Profile — incluido el **manifiesto de generación**, que captura la génesis de la base y permite regenerarla o actualizarla con este mismo prompt.

---

# Solicitudes

- Resolver `{destino}` según la tabla de parámetros y confirmar el modo (proyecto o workspace federado).
- Si ya existe una ia-db en `{destino}`, informarlo y preguntar si se regenera o conviene ejecutar `Actualizar-Indexado.md`.
- Analizar cada proyecto: dominios de conocimiento e inventario de fuentes. En modo federado, indexar los proyectos en paralelo con subagentes (uno por proyecto).
- Generar el punto de entrada `README.md` y los índices temáticos en `{destino}/indexes/` según la estructura canónica del Profile.
- Si un proyecto ya posee su propia ia-db, referenciarla desde el índice federado en lugar de duplicarla.
- Completar el manifiesto de generación: prompt generador, alcance, fuentes, fecha, versión 1.0 (o la mayor siguiente si se regenera una base existente) y la línea «Ejecución».
- Ejecutar por las etapas del Profile («Etapas, modelo y esfuerzo»): inventario y verificación mecánica por script; escritura, verificación adversarial, consolidación, entrada, crítica y corrección con el tier y el esfuerzo de esa tabla, salvo que la invocación los fije.

---

# Restricciones

- No modificar los proyectos indexados: solo se agregan archivos dentro de `{destino}`.
- No hacer commit, push ni pull request.
- No inventar información: toda entrada del índice debe ser trazable a una fuente.
- Respetar el presupuesto de tamaño por índice definido en el Profile.
- No escanear ni indexar las carpetas excluidas por el Profile (`.git`, dependencias, artefactos de build, binarios, la propia `ia-db`) ni lo ignorado por el `.gitignore` del proyecto.

---

# Framework

## Profile

Aplicar:

- `/IA/IA.Prompts/PromptFramework/Profiles/Knowledge-Indexing.md`

---

# Verificación de finalización

- [ ] Un agente puede responder «¿de qué trata y con qué stack?» leyendo solo `README.md`.
- [ ] `verificar_ia_db.py` sobre la base entera termina sin problemas graves (citas rotas o fuera de rango, remisiones rotas, secretos) y con la cobertura de «Fuentes» declarada en el manifiesto.
- [ ] Cada índice cubre un único dominio, referencia sus fuentes y nada está duplicado.
- [ ] El manifiesto permite regenerar (`Iniciar-Indexado`) y actualizar (`Actualizar-Indexado`) la base sin información externa.
