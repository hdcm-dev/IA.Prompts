# Conocimiento: consultar a una persona por WhatsApp Web desde el Chrome del MCP

Probado el 2026-09-30 en este mismo Linux: se envió un mensaje, la persona respondió desde el celular ("Celeste") y la respuesta se leyó y se interpretó bien. Este documento es para la sesión de Claude Code que coordina la mesa de expertos.

## Qué habilita

Los especialistas de la mesa le hacen preguntas a **una sola persona** por WhatsApp sin que el PO copie y pegue nada. Se usa WhatsApp Web dentro del Chrome que expone el MCP `chrome` (chrome-devtools-mcp).

## Límites que hay que conocer antes de empezar

1. **Cada sesión de Claude Code levanta su propio Chrome, sin ventana y con perfil descartable** (`--headless --isolated`). Una vinculación hecha en otra sesión no se ve desde esta: **hay que vincular de nuevo en esta sesión**, y la vinculación se pierde cuando la sesión termina.
2. **WhatsApp rechaza el modo sin ventana** ("WhatsApp funciona con Google Chrome 100 o versiones posteriores") porque el user agent dice `HeadlessChrome`. Se resuelve sobreescribiendo el user agent (paso 1).
3. **Un solo mensajero.** Los subagentes no usan el navegador: le pasan la pregunta al coordinador, que es quien escribe en WhatsApp. Si dos agentes manejan la misma pestaña, se pisan.
4. `take_snapshot` con `filePath` sólo escribe dentro del espacio de trabajo (`<raíz del workspace>`), no en el scratchpad.

## Paso 1: abrir WhatsApp Web

```
mcp__chrome__list_pages                      → normalmente hay una página about:blank (pageId 1)
mcp__chrome__emulate  pageId=1  userAgent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
mcp__chrome__navigate_page  pageId=1  type=url  url=https://web.whatsapp.com
mcp__chrome__wait_for  pageId=1  text=["Escanea para iniciar sesión","Chats"]  timeout=30000
```

La versión del user agent tiene que coincidir con la de Chromium; se consulta con `navigator.userAgent`. El `emulate` vale para esa página: si se abre otra con `new_page`, hay que repetirlo.

## Paso 2: vincular (lo hace el PO)

El QR se renueva cada ~20 segundos, así que **hay que avisarle al PO antes** para que tenga el celular listo:

1. Pedirle que abra en el celular WhatsApp → Dispositivos vinculados → Vincular dispositivo.
2. Recién entonces: `mcp__chrome__take_screenshot pageId=1 filePath=<raíz del workspace>/whatsapp-qr.png` y darle la ruta.
3. Si el QR venció, sacar otra captura. Alternativa: el botón "Iniciar sesión con número de teléfono" da un código de 8 caracteres que dura minutos (pide el número del PO).
4. Cuando el PO confirme, esperar con `wait_for text=["Chats"]`. Suele aparecer un diálogo "Novedades en WhatsApp Web": se cierra con su botón "Cerrar".
5. Al terminar, **borrar `whatsapp-qr.png`**.

## Paso 3: abrir el chat del destinatario, con verificación

Buscar por el nombre **exacto** que dio el PO:

```
take_snapshot → textbox "Buscar un chat o iniciar uno nuevo" → fill con el nombre → click en el resultado que coincide
```

**Probado el 2026-09-30 (consulta a un tercero):**

- `click` del MCP sobre el `gridcell` del resultado abre el chat. Un `element.click()` desde `evaluate_script` **no** lo abre; sí lo hace despachar `mousedown`, `mouseup` y `click` sobre el `gridcell` que contiene `span[title="<nombre exacto>"]`.
- **No usar `take_snapshot` completo con la lista de chats a la vista**: vuelca las vistas previas de todas las conversaciones privadas del PO. Buscar y abrir el chat con `evaluate_script` filtrando por `span[title="<nombre exacto>"]`, y dejar el snapshot para cuando ya está abierto el chat correcto.
- **Verificar el número** si el PO lo dio: clic en el encabezado del chat abre la ficha de contacto; buscar el número en `document.body.innerText` (se ve como `+<país> 9 <área> …`, sin espacios al normalizar). Ojo: `Escape` para cerrar la ficha **cierra también el chat**; hay que reabrirlo y volver a verificar.

**Antes de escribir, verificar siempre** que el chat abierto sea el correcto; si el nombre no coincide exactamente, no se envía nada:

```js
// evaluate_script, waitForStableDom=false
() => document.querySelector('#main header span[dir="auto"]')?.innerText
```

## Paso 4: enviar

```js
// evaluate_script, waitForStableDom=false: foco en el cuadro del chat abierto
() => { const b = document.querySelector('#main footer div[contenteditable="true"]'); b.focus(); return b.getAttribute('aria-label'); }
```

El `aria-label` devuelto es `"Escribir un mensaje para <nombre>"`: sirve como segunda verificación. Después:

```
mcp__chrome__type_text  pageId=1  text="🤖 ..."  submitKey=Enter
```

- `type_text` con Enter envía todo como **un solo mensaje**. **No incluir saltos de línea**: en WhatsApp Web, Enter envía, así que un `\n` probablemente lo corte en partes (no se probó). Separar las ideas con « · » o numerarlas en la misma línea.
- Para confirmar el envío, leer el último mensaje (paso 5).
- Probado: el 🤖 inicial se escribe bien con `type_text`, pero **no aparece en `innerText`** (es imagen); para confirmar el envío, comparar el resto del texto.
- Un mensaje largo (~800 caracteres o más) se envía entero; WhatsApp lo muestra plegado con «Leer más» y el `innerText` del DOM viene recortado. No es un error de envío.
- Antes de cada envío, en el mismo `evaluate_script`: verificar la cabecera, enfocar el cuadro **y leer el último mensaje**, para no pisar una respuesta que llegó mientras tanto.

## Paso 5: esperar y leer la respuesta

Esperar mensajes nuevos dentro del chat abierto (bloquea hasta 4 minutos; si no llega nada, se vuelve a llamar):

```js
// evaluate_script, waitForStableDom=false
async () => {
  const q = () => [...document.querySelectorAll('#main [data-pre-plain-text]')];
  const start = q().length, t0 = Date.now();
  while (Date.now() - t0 < 240000) {
    await new Promise(r => setTimeout(r, 3000));
    const all = q();
    if (all.length > start) return { nuevos: all.slice(start).map(e => ({ meta: e.getAttribute('data-pre-plain-text'), text: e.innerText })) };
  }
  return { nuevos: [], timeout: true };
}
```

- `meta` tiene la forma `"[09:57, 9/30/2026] Autor: "`. Si el autor es el destinatario, es una respuesta; si es el PO (su cuenta), es un mensaje propio.
- La persona suele contestar en varios mensajes seguidos: después del primero, esperar unos 30–60 s más y juntar todo antes de interpretar.
- **Sólo se lee texto.** Audios, fotos y stickers no tienen `data-pre-plain-text`. Si llega uno, pedirle con amabilidad que lo escriba. Los emojis se ven como imagen y no aparecen en `innerText`.
- Para leer el historial reciente: el mismo selector con `.slice(-N)`.

## Paso 6: que te despierte solo cuando responde (vigía + Monitor)

Esperar leyendo el chat cada 10–20 minutos cuesta un turno por revisión aunque no haya nada. Probado el 2026-09-30: un **Chrome vigía** que solo mira y la herramienta **Monitor** despiertan a la sesión únicamente cuando el destinatario escribe; mientras tanto no se consume nada.

**Por qué no alcanza con el Chrome del MCP:** `chrome-devtools-mcp` lo lanza con `--remote-debugging-pipe`, sin puerto; ningún proceso de la shell puede mirarlo.

**Armado (una vez por sesión; pide al PO escanear un segundo QR, porque es otro dispositivo vinculado):**

```bash
S=<scratchpad>/vigia; mkdir -p $S/perfil
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
nohup ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome --headless=new \
  --remote-debugging-port=9333 --remote-allow-origins=* --user-data-dir=$S/perfil \
  --user-agent="$UA" --window-size=1400,900 --no-first-run https://web.whatsapp.com >$S/chrome.log 2>&1 &
```

- El user agent se pasa por bandera (acá no hay `emulate`).
- Un cliente CDP mínimo en Node 22 (`fetch` a `http://127.0.0.1:9333/json` + `WebSocket` global, `Runtime.evaluate` y `Page.captureScreenshot`) alcanza para leer la página y sacar la captura del QR. **Avisar al PO antes de mostrar el QR**, igual que en el paso 2, y borrar la captura después.

> **Actualización (v3, 2026-09-30 tarde): el criterio del contador de «no leídos» falla.** WhatsApp marcó como leída una respuesta que llegó un minuto después de nuestro mensaje, el contador nunca subió y la respuesta se vio 3,5 h tarde. El vigía v3 **mantiene abierto en su Chrome solo el chat del destinatario** (lo abre despachando `mousedown`/`mouseup`/`click` sobre su fila si hace falta) y compara **el último mensaje del destinatario** (`data-pre-plain-text` con `] <Nombre>:` + texto) contra el último ya atendido, guardado en `ultimo-atendido.txt` junto al script. Así distingue autor, no depende de «leído» y no pierde nada al rearmar el Monitor. Después de leer y responder, se marca como atendido con `atendido.sh`. Scripts: `herramientas-vigia/` del caso T-14. Lo que sigue describe la v2 y queda como antecedente.

**El script vigía** evalúa cada 20 s, en ese Chrome, **solo la fila** del chat del destinatario en la lista (no abre el chat, no lee otras filas) y escribe una línea únicamente cuando hay algo que atender:

```js
// vigia.js (Node 22) — NUEVO-DE-<destinatario> / CANAL-CAIDO
const EXPR = `(() => {
  if (document.body.innerText.includes('Escanea para iniciar sesión')) return {estado:'deslogueado'};
  const s = [...document.querySelectorAll('#pane-side span[title]')].find(x => x.getAttribute('title') === '<Nombre del contacto>');
  if (!s) return {estado:'sin-fila'};
  const row = s.closest('[role="gridcell"],[role="listitem"],[role="row"]') || s.parentElement;
  const t = row.innerText.replace(/\\s+/g,' ').trim();
  const m = t.match(/(\\d+) mensajes? no le[ií]dos?/i);
  return {estado:'ok', texto: t, noLeidos: m ? parseInt(m[1],10) : 0};
})()`;
// bucle: si noLeidos sube respecto de la lectura anterior → console.log('NUEVO-DEL-DESTINATARIO …');
// si 'deslogueado' o no hay página → console.log('CANAL-CAIDO …') una sola vez; 3 fallos seguidos de conexión → CANAL-CAIDO.
```

- **Al arrancar o rearmar el Monitor, si el contador ya es mayor que 0, avisar enseguida.** Si no, un mensaje que llega justo en el cambio de Monitor queda como línea de base y no despierta a nadie (pasó: un «Si se puede» de las 14:01 se vio recién con el mensaje siguiente, 23 min después).
- **El criterio es el contador de «no leídos», no el cambio de la fila.** En el vigía la fila no trae la vista previa ni los íconos de enviado, así que un cambio de hora no distingue un mensaje propio de uno del destinatario (primer intento: falso aviso con el mensaje propio). El contador solo sube cuando escribe el destinatario, y vuelve a 0 cuando se le responde desde el otro Chrome. El chat abierto en el Chrome del MCP, que corre sin ventana, **no** marca los mensajes como leídos.

Scripts completos usados en la primera consulta: `<repo privado del caso>/…/Caso-T14-Consulta-Directa-Al-Jefe/herramientas-vigia/` (`vigia.js`, `cdp.js`).

**Monitor:**

```
Monitor  command="cd $S && node vigia.js 2>&1 | grep --line-buffered -E 'NUEVO-DE-|CANAL-CAIDO|Error|ERR'"
         description="WhatsApp: mensaje nuevo de <destinatario> o caída del canal"  timeout_ms=1800000
```

- **Al rearmar, envolver el script con `timeout 1790`** (`timeout 1790 node vigia.js | grep …`): al vencer el Monitor, el proceso de Node puede quedar vivo y se acumulan copias (pasó: 4 vigías a la vez).
- Dura como máximo 30 minutos: al vencer llega un aviso y se lo vuelve a armar (ese vencimiento funciona también como revisión de respaldo). Con el vigía andando, se cancela el `CronCreate` de revisión periódica.
- Al llegar `NUEVO-DE-…`, la lectura y el envío se hacen como siempre en el Chrome del MCP (pasos 3 a 5); el vigía no escribe nunca.
- Al terminar la consulta, el PO desvincula **los dos** dispositivos en el celular.

## Reglas de uso (acordadas con el PO)

1. **Un solo destinatario permitido**: el que nombró el PO. No se abre, no se lee y no se escribe en ningún otro chat. La lista de chats muestra conversaciones privadas del PO: no se leen ni se citan.
2. **Cada mensaje se identifica**: empieza con 🤖 y, en el primero, aclara que es un asistente de Fernando que consulta en nombre de la mesa. Tono llano, en español rioplatense, sin jerga del SDD ni nombres de agentes.
3. **Preguntas agrupadas y cortas**: el coordinador junta las dudas de los especialistas, saca las repetidas y manda pocas y numeradas. Nada de ráfagas.
4. **Registro**: cada pregunta enviada y cada respuesta recibida (texto tal cual, con hora) se anota en el expediente o registro de la mesa, para que el PO vea qué se preguntó.
5. **Nada sensible**: no se mandan credenciales, datos personales de terceros ni archivos sin el ok del PO.
6. Si la persona pide hablar con Fernando, o la respuesta es ambigua o sale del tema, se para y se le avisa al PO.

## Si hace falta que dure más que una sesión

Levantar un Chrome fijo con perfil persistente (`--user-data-dir=<carpeta>` y `--remote-debugging-port=9222`) y cambiar la configuración del MCP `chrome` en `~/.claude.json` para que se conecte a él con `--browserUrl http://127.0.0.1:9222`, en lugar de `--headless --isolated`. Así la vinculación sobrevive y todas las sesiones comparten el mismo WhatsApp. Pide reiniciar las sesiones y lo decide el PO.

Cuando ya no se use, el PO puede quitar el dispositivo en el celular: WhatsApp → Dispositivos vinculados.

## Control de cambios

| Fecha | Cambio |
| --- | --- |
| 2026-09-30 | Versión inicial (prueba de ida y vuelta). |
| 2026-09-30 | Tras la consulta real al jefe de un proyecto: apertura del chat sin exponer la lista, verificación del número, notas de envío (🤖, «Leer más», leer antes de enviar) y **paso 6: vigía + Monitor** para despertar solo cuando responde, con el criterio del contador de no leídos. |
| 2026-09-30 | Vigía v3: chat del destinatario abierto en el vigía y comparación por último mensaje del autor con archivo de «último atendido»; el contador de no leídos queda descartado (perdió una respuesta). |
