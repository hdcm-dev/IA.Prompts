# Iniciar MCP con Chrome

> Manejar un navegador de verdad —navegar, escribir, hacer clic, capturar— desde un agente, en un
> host Linux sin pantalla. Escrito el 2026-09-04 después de hacerlo funcionar; lo que sigue es lo
> que pasó, no lo que debería pasar.

---

## 1. El escenario, que condiciona todo

```
Windows  ──►  VS Code  ──►  Remote-SSH  ──►  host Linux  ──►  Claude Code
                                                              └─► servidor MCP + Chrome headless
```

Lo que hay que tener claro y suele confundirse: **el navegador corre en el host Linux, no en la
máquina de escritorio**. No hay `DISPLAY` ni servidor gráfico, y no hace falta: Chrome corre
`--headless` y renderiza fuera de pantalla. Que VS Code esté en Windows es irrelevante para el
navegador; sólo importa para dónde se leen los archivos.

Corolario práctico: **las capturas se guardan en el host Linux**, dentro del árbol del proyecto, y
se leen desde ahí.

---

## 2. Evaluar el escenario antes de tocar nada

Cinco comprobaciones, en este orden. Cada una descarta una causa distinta.

```bash
# 1. ¿Hay un servidor MCP declarado, y para qué proyecto?
python3 -c "
import json; d=json.load(open('$HOME/.claude.json'))
print('globales:', list((d.get('mcpServers') or {}).keys()))
for p,v in (d.get('projects') or {}).items():
    m=v.get('mcpServers') or {}
    if m: print(p,'->',list(m.keys()))
"
ls -la ./.mcp.json 2>/dev/null      # el del proyecto, si existe

# 2. ¿Está el binario del navegador que la config declara?
ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome

# 3. ¿Están node y npx?
node --version; which npx

# 4. ¿El agente TIENE las herramientas en su sesión?
#    (buscar en el toolset: click, take_screenshot, navigate_page, new_page…)

# 5. ¿Está deshabilitado por configuración?
python3 -c "
import json; d=json.load(open('$HOME/.claude.json'))
p=d['projects']['$PWD']
print({k:p[k] for k in p if 'cp' in k.lower() and k!='mcpServers'})
"
```

### La distinción que decide todo

| Síntoma | Significado | Qué hacer |
|---|---|---|
| El servidor no arranca a mano | Problema **real**: falta el binario, node, o permisos | Arreglar lo que falte |
| Arranca a mano pero el agente no tiene las herramientas | El servidor está sano; **la sesión no lo conectó** | Sección 4: el puente |

**No confundir una con otra.** Es el error que cuesta más tiempo.

---

## 3. Probar el servidor de verdad (no a medias)

> **El sondeo que engaña.** Mandar sólo `initialize` y ver que responde **no prueba nada**: el
> servidor contesta el saludo aunque Chrome no pueda arrancar. Hay que llegar hasta la captura.

La secuencia mínima que sí prueba: `initialize` → `notifications/initialized` → `tools/list` →
`new_page` → `take_screenshot`.

Dos detalles del contrato que hacen perder tiempo si no se saben:

- **`navigate_page` y `take_screenshot` exigen `pageId`.** Sin página abierta fallan con
  `Required at pageId`. Primero `new_page`.
- **`pageId` es un NÚMERO, no una cadena.** `"pageId":"2"` devuelve
  `Expected number, received string`. Va `"pageId":2`.

---

## 4. Cuando el servidor anda pero la sesión no lo conectó

Claude Code engancha los servidores MCP **al arrancar**. Si uno quedó afuera, desde adentro de la
sesión no se puede forzar la conexión. Dos caminos:

### 4.1 El que depende de la persona

`/mcp` en la sesión interactiva y conectar el servidor, o reiniciar Claude Code en el directorio
del proyecto. Es lo correcto, pero **requiere a alguien del otro lado**.

### 4.2 El puente, que no depende de nadie

`tools/medios/chrome_mcp.py` habla JSON-RPC por stdio con el mismo servidor y expone **las mismas
29 herramientas**. Con eso el agente trabaja igual, sin esperar a nadie.

```bash
M=tools/medios/chrome_mcp.py
python3 $M arrancar                       # deja el proceso VIVO
python3 $M herramientas
python3 $M llamar new_page '{"url":"https://ejemplo/ingreso"}'
python3 $M llamar take_snapshot '{"pageId":2}'
python3 $M llamar fill_form '{"pageId":2,"elements":[{"uid":"1_8","value":"correo@x"},{"uid":"1_10","value":"clave"}]}'
python3 $M llamar click '{"pageId":2,"uid":"1_11"}'
python3 $M captura 2 ./OUTPUTs/01.png
python3 $M parar
```

#### Las dos trampas de implementar el puente

Las dos cuestan una tarde si no se saben:

1. **El proceso tiene que quedar vivo entre llamadas.** Un script que abre y cierra el servidor en
   cada comando pierde la pestaña, las cookies y la sesión: sirve para una foto y para nada más.
   Ninguna prueba con inicio de sesión funciona así.
2. **Hay que mantener la FIFO abierta para escritura.** Si el único escritor cierra, el servidor ve
   EOF y se apaga apenas termina el primer comando. Se resuelve con un proceso que sostenga el
   descriptor: `exec 3>fifo; sleep 86400`.

---

## 5. Manipular y entender

Es el objetivo real; la captura sola no alcanza.

1. **`take_snapshot` antes de tocar.** Devuelve el árbol de accesibilidad con identificadores
   estables (`uid=1_8`) y el rol de cada elemento. **Nunca adivinar coordenadas**: los `uid` no se
   mueven cuando cambia el diseño.
2. **`fill_form` para varios campos de una** — un solo viaje, y el resultado dice si funcionó.
3. **`click` por `uid`**, no por posición.
4. **Capturar antes y después** de cada acción que cambie estado. Un antes sin después no prueba
   nada, y un después sin antes tampoco.
5. **Leer la captura y decir qué se ve.** Si el agente no puede describir lo que capturó, no lo
   capturó: lo archivó.

### Formato de la captura

Pedir **PNG**, no WebP (`--screenshotFormat png`). En un host pelado puede no haber con qué
convertir WebP —ni `dwebp`, ni `convert`, ni `ffmpeg`, ni PIL—, y una captura que no se puede abrir
no es evidencia. Verificado: en este host no había ninguno de los cuatro.

---

## 6. Dejarlo configurado para la próxima

```jsonc
// .mcp.json, en la raíz del proyecto: queda versionado y no depende del perfil personal
{
  "mcpServers": {
    "chrome": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y","chrome-devtools-mcp@latest",
               "--headless","--isolated",
               "--executablePath","<ruta al chrome de playwright>",
               "--viewport","1440x900",
               "--screenshotFormat","png","--screenshotMaxWidth","1440"]
    }
  }
}
```

`--isolated` da un perfil limpio por corrida: lo que se prueba es el sitio, no lo que quedó de la
vez anterior.

---

## 7. Lista de verificación

- [ ] El binario de Chrome existe en la ruta que declara la config
- [ ] `node` y `npx` responden
- [ ] El servidor llega **hasta la captura** a mano, no sólo hasta `initialize`
- [ ] El agente tiene las herramientas; si no, puente
- [ ] `pageId` numérico, y `new_page` antes de navegar o capturar
- [ ] Formato PNG
- [ ] Se hizo **una acción** sobre el sitio, no sólo una foto
- [ ] El agente **describió** lo que vio en la captura

---

## 8. Prueba de referencia

`OUTPUTs/nuevo.md` — ingreso a `https://aplicada.somee.com/ingreso` con un usuario inventado:
navegación, mapa de elementos, escritura, clic, y la aplicación respondiendo «El correo o la
contraseña no corresponden». Tres capturas, con el antes y el después.
