# Prueba de manipulación web por MCP con Chrome

*2026-09-04. Sitio: `https://aplicada.somee.com/ingreso`. Chrome headless en el host Linux,
manejado por `chrome-devtools-mcp`.*

## Qué se buscaba

Demostrar dos cosas distintas, porque son distintas:

1. Que puedo **capturar** una pantalla.
2. Que puedo **manipular** el sitio —escribir en campos, hacer clic— y **entender** lo que la
   aplicación responde.

Lo segundo es lo que importa: sacar una foto de una URL lo hace cualquier cosa; recorrer un sitio
autenticado, no.

## Qué se hizo, paso por paso

| # | Acción | Resultado |
|---|---|---|
| 1 | `new_page` a `/ingreso` | Chrome abrió la página. Título leído: «Ingreso» |
| 2 | `take_screenshot` | `01-ingreso.png`, 77.975 bytes |
| 3 | `take_snapshot` | Mapa de elementos con identificadores estables (`uid=1_8` correo, `1_10` contraseña, `1_11` botón) |
| 4 | `fill_form` con un usuario **inventado** | «Successfully filled out the form» |
| 5 | `take_screenshot` | `02-formulario-completado.png`, 83.451 bytes |
| 6 | `click` sobre `Ingresar` | «Successfully clicked on the element» |
| 7 | `take_screenshot` | `03-resultado-del-ingreso.png`, 87.506 bytes |

Credenciales usadas: `prueba.mcp@ejemplo.test` / `claveInventada123`. **Inventadas a propósito**:
la intención era ejercitar el camino de error, no entrar.

## Qué pasó, y qué entendí de lo que vi

**La pantalla de ingreso** (`01`) es de «Fábrica de Geometría», titulada «Ingresar al
laboratorio». Tarjeta centrada sobre fondo gris claro, dos campos —Correo y Contraseña—, un botón
verde oscuro a todo el ancho, un enlace «Registrarte» y una nota explicando que la clave la resetea
el docente. Al pie, «VERSIÓN NO IDENTIFICADA» y los banners de publicidad del hosting de Somee.

**Después del envío** (`03`) la aplicación **rechazó las credenciales** y lo dijo bien:

> El correo o la contraseña no corresponden.

En un recuadro rosa pálido con texto rojo, **arriba del formulario**, donde se lee sin buscarlo.
Dos detalles que sólo se ven manipulando y que hablan bien del formulario:

- **el correo quedó escrito** —no obliga a retipear—;
- **la contraseña se limpió**, que es el comportamiento correcto tras un intento fallido.

El mensaje además **no revela** si el que no existe es el correo o la clave, que es lo que
corresponde en una pantalla de ingreso.

## Conclusión

El puente hacia Chrome funciona de punta a punta: **navega, mapea, escribe, hace clic, captura, y
lo capturado se puede leer y juzgar**. Queda habilitado el trabajo de revisión de interfaces sobre
sitios que exigen sesión.

El procedimiento para reproducir esto desde cero está en
[`../Iniciar-MCP-Con-Chrome.md`](../Iniciar-MCP-Con-Chrome.md).

## Capturas

| Archivo | Momento |
|---|---|
| `01-ingreso.png` | La pantalla como llega |
| `02-formulario-completado.png` | Con los campos escritos por el agente |
| `03-resultado-del-ingreso.png` | La respuesta de la aplicación al usuario inventado |
