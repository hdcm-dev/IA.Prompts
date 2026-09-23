# Base — Medios de observación

> **Invocación**: Leer `/IA/PROMPTs/IA.Prompts/Base/Medios.md` cuando un ciclo de trabajo necesite juzgar una interfaz que se ejecuta, y no solo el texto que la describe.
>
> **Overview**: Este documento no define un procedimiento ni un panel: declara **qué puede observar un agente por sí mismo en este entorno**, con qué herramienta concreta, bajo qué restricción de exclusividad y con qué nivel de evidencia queda registrado lo observado. Existe porque la diferencia entre revisar una especificación y revisar un producto es el acceso al artefacto en ejecución: sin medio de observación, todo juicio sobre una interfaz es conjetura, y una conjetura no funda correcciones (Mesa-Evaluadora §3).
>
> Se declaran dos medios. El primero es un navegador Chromium sin escritorio, ejecutado dentro de un contenedor, que alcanza tanto las URLs públicas como los servicios internos que el host no publica; devuelve una imagen de la página y el registro de sus errores de consola. El segundo es un teléfono Android físico conectado por USB, observado a través del único contenedor que tiene ese USB asignado; devuelve la pantalla real del dispositivo y permite actuar sobre ella. Ambos entregan archivos —imagen y texto— que el agente lee directamente, sin intermediación del usuario.
>
> La restricción central es de exclusividad, y es asimétrica entre los dos medios: el navegador se instancia tantas veces como haga falta y se destruye al terminar, mientras que el teléfono es un recurso único, en disputa con el trabajo de compilación que ya lo usa, y su acceso está mediado por un contenedor dueño declarado. Un agente que ignore esa mediación no obtiene un error claro: obtiene un dispositivo arrebatado a otro proceso.
>
> Lo que un medio no puede observar se declara aquí con la misma precisión que lo que puede. Un juicio emitido fuera del alcance del medio —compatibilidad con un navegador que no se ejecutó, comportamiento en un tamaño de pantalla que no se instanció— es un hallazgo sin ancla, y este documento existe para que esa frontera sea citable.

---

## 1. Qué es un medio y qué no

Un **medio de observación** es un mecanismo que le permite a un agente producir por su cuenta un registro reproducible del artefacto en ejecución, sin pedirle al usuario que mire una pantalla y describa lo que ve.

No son medios de observación, y no habilitan juicio sobre la interfaz:

- La lectura del código fuente que *debería* producir la interfaz.
- La lectura de la especificación que *declara* cómo se ve.
- La descripción que el usuario hace de lo que observa en su propia máquina.

Las tres son entradas legítimas del ciclo, pero ninguna es evidencia de que la interfaz *se comporte* como se afirma. Esa distinción es la razón de ser del documento.

### Principios

1. **Sin medio no hay veredicto sobre la ejecución.** Un hallazgo sobre el comportamiento de una interfaz que no fue ejecutada se emite como pregunta, nunca como corrección.
2. **El registro se versiona, no se narra.** El medio produce un archivo; el hallazgo cita el archivo. "Se verificó visualmente" no es una cita.
3. **El alcance del medio es parte del hallazgo.** Lo observado en Chromium se afirma de Chromium.
4. **El recurso único se pide prestado, no se toma.** Ver §4.
5. **El medio no decide.** Produce el registro; el juicio sigue siendo del panel que corresponda.

---

## 2. Medio A — Navegador sin escritorio (web)

Chromium ejecutado dentro del contenedor `mcr.microsoft.com/playwright`. El host no necesita navegador, ni Node, ni ningún SDK: todo vive en la imagen.

```
/tools/medios/web.sh <url> [nombre] [--network <red>] [--full] [--wait <ms>] [--size <WxH>]
                     [--pasos '<verbo> ...; <verbo> ...']
```

Produce dos archivos en `/tools/medios/out/`:

| Archivo | Contenido | Para qué sirve |
|---|---|---|
| `<nombre>.png` | La página renderizada | Juicio de diseño, jerarquía visual, densidad, estados |
| `<nombre>.txt` | Código de estado HTTP, título, texto visible y **errores de consola y de JavaScript** | Juicio de funcionamiento; suele contener la causa cuando la imagen muestra el síntoma |

El archivo de texto importa tanto como la imagen: una página que se ve correcta y arroja errores de consola está rota, y la captura sola no lo revela.

### 2.1 Recorrer un flujo, no solo mirar una vista

Sin `--pasos` el medio observa **una** vista. Con `--pasos` recorre un flujo: entra con credenciales, abre una sección, completa un formulario y captura donde haya que capturar. Los verbos se separan con `;`:

| Verbo | Forma | Para qué |
|---|---|---|
| `click` | `click <selector>` — admite `text=Ingresar` | Navegar, abrir, enviar |
| `fill` | `fill <selector> = <valor>` | Completar campos |
| `press` | `press <selector> <Tecla>` | Enviar con `Enter`, atajos |
| `goto` | `goto <url>` | Saltar dentro del mismo recorrido |
| `wait` | `wait <ms>` | Dejar asentar una transición |
| `shot` | `shot <nombre>` | Captura intermedia; la final se toma siempre |

```
web.sh <url> ingreso --pasos 'fill #usuario = admin; fill #clave = ****; click text=Ingresar; wait 1500; shot autenticado; click text=Segmentos'
```

Un paso que falla **corta el recorrido, se registra con su causa y la captura final se toma igual**: ver dónde quedó el flujo es la mitad del diagnóstico. El archivo de texto lista cada paso con su resultado y la **URL final**, que es lo que permite afirmar hasta dónde se llegó sin suponerlo.

### 2.2 Cómo alcanzar cada servicio

El proyecto no expone sus servicios de una sola manera, y elegir mal la red es el modo más común de concluir que "el servicio está caído" cuando solo era inalcanzable desde donde se lo buscó.

| Dónde se ejecuta el servicio | Parámetro | Cómo se lo nombra |
|---|---|---|
| Puerto publicado en el host | *(por defecto)* | `http://127.0.0.1:<puerto>` |
| Contenedor en una red interna, sin publicar | `--network <red>` | Por **nombre de contenedor**: `http://lab-geometria-api:8080` |
| Red `macvlan` de los servicios V2 | `--network infra_vlan` | El host no los alcanza; el contenedor sí |
| Túnel público o alojamiento externo | *(por defecto)* | La URL pública, como cualquier cliente |

### 2.3 Qué observa y qué no

Observa: composición y jerarquía visual, cumplimiento de una maqueta, estados de una vista, comportamiento en un ancho de pantalla declarado, errores de ejecución del cliente, contenido efectivamente renderizado tras la carga, y el recorrido de un flujo de varias pantallas con sus estados intermedios.

No observa: comportamiento en motores distintos de Chromium, tipografías o interpolaciones propias de otro navegador, rendimiento en hardware real de usuario final, ni nada que dependa de una interacción no declarada en los pasos. El recorrido es **guionado, no exploratorio**: el medio hace lo que se le indicó, y lo que no se le indicó no quedó verificado aunque la vista final se vea bien.

---

## 3. Medio B — Dispositivo Android físico

Un teléfono conectado por USB al host, alcanzado por `adb` **a través del contenedor que tiene ese USB asignado**. Es el único medio que permite juzgar la aplicación móvil tal como la ve un usuario: pantalla real, densidad real, sistema operativo real.

```
/tools/medios/movil.sh estado                        estado del dispositivo y aplicación en foco
/tools/medios/movil.sh shot [nombre]                 captura de pantalla + ventana en foco
/tools/medios/movil.sh tap <x> <y>                   toque en coordenadas
/tools/medios/movil.sh swipe <x1> <y1> <x2> <y2> [ms]
/tools/medios/movil.sh text "<texto>"                escribe en el campo enfocado
/tools/medios/movil.sh key <KEYCODE>                 BACK, HOME, ENTER, …
/tools/medios/movil.sh log [filtro]                  últimas líneas del registro del sistema
```

`shot` deja la imagen y un texto con el identificador del dispositivo, su tamaño físico y la actividad en foco. Ese último dato es el que permite afirmar **qué pantalla** se está juzgando, y sin él una captura es una imagen sin referencia.

A diferencia del medio web, este medio **actúa sobre el dispositivo**: recorrer un flujo de varias pantallas es una secuencia de `tap`, `text` y `shot`. Las coordenadas se leen de la captura anterior, contra el tamaño físico que el propio medio informa.

### 3.1 El dispositivo también es un navegador real

El teléfono no sirve solo para la aplicación nativa: su navegador es el único **motor sobre hardware real y a ancho de pantalla móvil** disponible en el entorno, y complementa al medio A allí donde este no llega. Una URL se abre en el dispositivo con una intención del sistema, y a partir de ahí se la observa con `shot` como cualquier otra pantalla.

```
movil.sh abrir <url>                     abre la URL en el navegador del dispositivo
movil.sh espera [seg]                    pausa, hecha en el dispositivo
movil.sh shot <nombre>                   observar el resultado
```

**El direccionamiento cambia respecto del medio A**, y es la confusión más frecuente: `127.0.0.1` desde el dispositivo es el dispositivo, no el host, y un servicio publicado en el host aparece como conexión rechazada. Se lo alcanza por la dirección del host en la red local; `abrir` reescribe `127.0.0.1` y `localhost` automáticamente y avisa que lo hizo. Los túneles públicos del proyecto se abren directamente, sin depender del host. Los servicios que solo existen dentro de una red de contenedores **no son alcanzables desde el dispositivo**: para esos, el medio A es el único camino.

### 3.2 Escollos verificados

Son fallas de procedimiento, no del medio, y cada una produce un registro que parece válido y no lo es:

1. **Pantalla apagada.** Una pantalla apagada se captura en negro y se interpreta como una vista rota; `abrir` despierta el dispositivo, pero antes de un `shot` suelto conviene `key WAKEUP`.
2. **El teclado se come los toques.** Al completar un formulario hay que cerrarlo con `key BACK` **entre campo y campo**; si no, los toques siguientes caen sobre el teclado y el texto se mezcla en un solo campo. Conviene capturar antes de enviar, para confirmar lo escrito.
3. **Diálogos del navegador.** Avisos de primera vez y la propuesta de guardar contraseña se superponen a la vista bajo juicio; se descartan con un toque fuera antes de capturar.
4. **Las coordenadas caducan.** Se leen de la captura inmediatamente anterior y contra el tamaño físico que informa el propio medio; un cambio de maqueta las invalida en silencio, porque el toque no falla, simplemente cae en otro lado.
5. **La espera se hace en el dispositivo.** La pausa entre la acción y la captura corresponde al dispositivo —para eso está `espera`—, no al host.

### 3.3 Qué observa y qué no

Observa: la interfaz real de la aplicación instalada, el recorrido de un flujo completo, el comportamiento de permisos del sistema, las notificaciones tal como llegan al dispositivo, y el registro del sistema durante la interacción.

No observa: otros modelos, otras versiones del sistema operativo, otras densidades de pantalla, ni el estado de una compilación que no se instaló. La aplicación observada es la que está instalada en el momento de mirar, que no necesariamente es la del código que se está revisando: verificarlo es parte del hallazgo, no un supuesto.

---

## 4. La regla de exclusividad del dispositivo

Los dos medios no tienen el mismo régimen, y confundirlos es el error caro de este documento.

El navegador es **instanciable**: cada invocación levanta un contenedor propio, efímero, y lo destruye al terminar. Varios agentes pueden observar en paralelo sin coordinarse.

El teléfono es un **recurso único y en disputa**. El USB está asignado a un contenedor de desarrollo que también lo usa para compilar e instalar la aplicación, y `adb` es exclusivo por diseño: un segundo servidor de depuración levantado desde otro contenedor no comparte el dispositivo, se lo arrebata al primero, y el síntoma no aparece en quien lo tomó sino en la compilación ajena que falla después.

De ahí la regla:

> **No se levanta un segundo `adb`.** Toda observación del dispositivo pasa por el contenedor dueño, que es el que ya lo tiene asignado. Eso es exactamente lo que hace `movil.sh`, y es la única razón por la que ese guion existe en lugar de invocar `adb` directamente.

El contenedor dueño se declara en la variable `MEDIOS_ADB_OWNER`; su valor por defecto es el contenedor de desarrollo de la aplicación móvil. Si ese contenedor no está levantado, o si `adb` no ve el dispositivo desde adentro, el guion **falla y lo dice**, en lugar de intentar tomar el USB por su cuenta. Esa falla es una condición de escalada al usuario —el dispositivo puede estar desconectado, bloqueado o tomado—, no un problema que el agente deba resolver forzando el recurso.

Corolario para un ciclo con varios agentes: el medio B se usa **de a uno por vez**. Si el ciclo necesita observación móvil concurrente, la mesa la serializa; no la paraleliza.

---

## 5. Cómo se cita lo observado

Un registro producido por un medio se incorpora al ciclo como evidencia, y su nivel se determina por lo que el registro demuestra, no por el hecho de existir:

| Lo que se afirma | Nivel | Qué hay que adjuntar |
|---|---|---|
| La interfaz falla o arroja un error de ejecución | **E1** | El archivo de texto con el error, o el registro del sistema con la línea citada |
| La interfaz se aparta de lo que la maqueta o la especificación declara | **E2** | La captura **y** la cita literal de la regla que se incumple |
| Un caso concreto no está resuelto por la interfaz | **E3** | La secuencia de pasos que lo reproduce, con la captura del estado final |

Toda cita nombra el archivo, la URL o la pantalla observada, y el momento de la observación. Una captura sin la ruta del artefacto observado no es citable: no se puede reproducir.

El corolario práctico es que el archivo se conserva. `/tools/medios/out/` es un área de trabajo volátil; un registro que funda un hallazgo se copia junto a la documentación del hallazgo, porque la próxima invocación del medio con el mismo nombre lo sobrescribe.

---

## 6. Límites declarados del entorno

Se enuncian para que ningún agente los descubra como si fueran defectos del proyecto:

1. **El host no compila ni ejecuta las aplicaciones.** No tiene los SDK. Todo servicio corre en contenedor o detrás de un túnel, y por eso los medios también viven en contenedores.
2. **No hay escritorio gráfico.** No existe la opción de "abrir el navegador y mirar": no hay pantalla donde abrirlo. Es la razón del medio A, no una limitación a sortear.
3. **El navegador del usuario no está disponible para los agentes**, y no hace falta que lo esté. Un juicio que requiera específicamente ese navegador es una consulta al usuario, no una tarea de un agente.
4. **El único motor web disponible es Chromium**, en sus dos formas: sin escritorio en el contenedor (medio A) y sobre el dispositivo real (§3.1). Cualquier afirmación sobre otro motor está fuera del alcance de los medios y debe emitirse como pregunta.
5. **El teléfono es uno solo, de un modelo concreto.** La cobertura de dispositivos no es un objetivo alcanzable con este medio, y declararla cubierta sería falso.

---

## 7. Relación con el resto del registro

`Medios.md` es **transversal**: no compite con [Mesa-Evaluadora.md](Mesa-Evaluadora.md) ni la reemplaza, la habilita. Donde la mesa exige evidencia, este documento declara con qué se la produce.

Un ciclo que vaya a juzgar interfaces incorpora los medios en su contrato de entrada, nombrándolos como recurso disponible, y declara en su bloque de cierre qué medios usó y qué quedó sin observar. La forma más común de deuda silenciosa en un ciclo de revisión de interfaces es la aprobación de una vista que nadie ejecutó; nombrar los medios en el contrato de entrada es lo que la vuelve visible.
