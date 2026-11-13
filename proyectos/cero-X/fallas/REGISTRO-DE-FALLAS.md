# cero-X · registro de fallas y sus contrapartes

*Corte 2026-11-13. Cada fila es una falla que pasó de verdad, no una categoría
teórica. La columna que importa es la última: qué la caza ahora. Una falla sin
contraparte se repite; con contraparte, deja de ser un recuerdo y pasa a ser una
comprobación.*

## La familia más repetida: el cero silencioso

Cinco de las dieciocho fallas son la misma: **una medición devuelve 0 o vacío y se lee
como «no hay nada» en vez de «lo leí mal»**. Es la clase más cara porque no falla:
produce un resultado plausible y falso.

| # | falla | cómo se detectó | contraparte |
|---|---|---|---|
| 1 | `d.get('apps')` sobre el JSON de Miyomi dio 0 coincidencias; la raíz es `{success, data}` | la corrida anterior había dado 25 | leer `data or apps` **y comprobar el recuento de la lista antes de fiarse del cruce** |
| 2 | leer `repoUrl` en el JSON propio cuando la clave es `repo` → 0 de 52 fichas | 0 exacto tras un cruce que antes daba 25 | volcar las claves reales del JSON antes de cruzar; anotado en `work/ci/catalogo-releases-miyomi-01.kotlin.txt` |
| 3 | regex sobre `aapt2 dump xmltree` que no casó → «0 componentes con exported» | `grep -c exported` dio 106 | contrastar todo recuento derivado con un `grep -c` independiente |
| 4 | comparar el APK contra `tasker/src/main/AndroidManifest.xml` en vez de `manager/` → «162 nombres ausentes de la fuente» | eran 117 y todos de librerías | comparar contra **todos** los manifiestos de la fuente, no el primero que casa |
| 5 | contar 11 `@Config(sdk = [34])` cuando eran 18 | el grep sólo cazaba la forma corta, no `@org.robolectric.annotation.Config` | `NivelDeSdkDePruebasTest` escanea `sdk\s*=\s*\[(\d+)\]`, que casa las dos formas |

## Verificadores que corrompían lo que verifican

| # | falla | cómo se detectó | contraparte |
|---|---|---|---|
| 6 | `.strip()` sobre `git status --porcelain` se comía el espacio inicial de la primera línea y el latido mostraba «M ocs/INVENTARIO…» | se leyó la salida y no cuadraba la ruta | `git(…, conservar_columnas=True)` usa `.rstrip("\n")`; el porqué está en el docstring |
| 7 | `if modos and not contenido` silenciaba el AVISO de modos perdidos cuando había otra anomalía | prueba deliberada: `chmod -x` sobre un script y comprobar que no avisaba | un AVISO no se silencia porque exista otro de tipo distinto; se probó rompiéndolo a propósito |
| 8 | creer que un cambio de modo puro da salida vacía en `--numstat` | da `0\t0\truta` | `es_solo_modo()` mira las dos cifras, no si la salida está vacía |
| 9 | `head=` del registro de respaldos completado de memoria (33 caracteres inventados) | `git cat-file -t` → «could not get object info» | `comprobar_respaldo` lo convierte en BLOQUEO; los hashes se pegan de `git rev-parse`, nunca se transcriben |
| 10 | citar la regla 7 de memoria y atribuirle una prohibición que no contiene | `grep -n "^7\." AGENTS.md` | citar las reglas con grep sobre el archivo, nunca de memoria |

## Entorno y procesos

| # | falla | cómo se detectó | contraparte |
|---|---|---|---|
| 11 | typo `$candidario` en el bucle del swap → `unbound variable`, EXIT=1 | el propio script al arrancar | `set -u` en todos los scripts del repo; nunca quitarlo |
| 12 | `pkill -f` con el patrón en la propia línea de órdenes mata al shell que lo lanza | el comando no devolvió nada y el proceso seguía | `pgrep -c java`, o `ps -eo pid,args \| grep -E '[g]radle'` |
| 13 | `> work/ci/archivo.txt` con cwd dentro del repo falla: `work/ci` cuelga de `/home/user` | «No such file or directory» | rutas absolutas en los scripts: `CI=/home/user/work/ci` |
| 14 | log de Gradle de 49,9 MB por 435.671 líneas de pila D8 | el presupuesto del workspace saltó | `comprobar_logs` avisa de crudos >1 MiB; filtrar con `grep -vE '^\s+at '` y `gzip -9` |
| 15 | `find work/ci -name '*.log' \| gzip` rompió cinco rutas citadas por los docs sin `.gz` | el latido siguiente las dio como evidencia ausente | `comprobar_evidencia` verifica que toda ruta `work/ci/…` citada exista |
| 16 | swap de 12 GiB puesto a mano, por debajo del suelo del script → un rearme lo habría reducido sin avisar | comparar `/proc/swaps` con la receta versionada | la receta elige el tamaño y lo justifica; lo ad-hoc se anota como discrepancia o se versiona |

## El verde que no ejecutó nada

Dos fallas del mismo día sobre la misma causa: una comprobación que imprime éxito sobre
un trabajo que no se hizo. La primera es la cara nueva del `UP-TO-DATE` vacío (regla 18 de
cero-X); la segunda es el verificador que se añadió para cazarla y que nació cazando de más.

| # | falla | cómo se detectó | contraparte |
|---|---|---|---|
| 17 | con `org.gradle.caching=true`, un `clean` + suite dio `> Task :app:testDebugUnitTest FROM-CACHE` y terminó en 9,6 s imprimiendo «614 pruebas, 0 fallos» sin ejecutar **una sola** prueba: la caché restauró los XML de resultados | `MemAvailable` quedó en 548 MB cuando un cierre real la baja a 29-58 MB (el fork de pruebas nunca arrancó), y `tools/medir-build.py` añadió la edad de los XML: en el cierre honesto eran de 7-14 s, en el hueco no había XML nuevos | `outputs.cacheIf { false }` en `tasks.withType(Test)` de `android/app/build.gradle`, y `medir-build.py` lee el registro de Gradle e informa `pruebas_ejecutadas` buscando `FROM-CACHE`/`UP-TO-DATE`/`SKIPPED` en las tareas de tipo `Test`. **La edad de los XML no basta**: la caché los restaura con `mtime` nuevo, así que una corrida que no ejecutó nada parece recién hecha; lo que no miente es la línea de Gradle. Validado contra 11 corridas de veredicto conocido: 11/11 |
| 18 | la primera versión de ese detector usaba `\S*[Tt]est\S*` y marcaba «no se ejecutaron» en **todas** las corridas, incluidas las verdes | al validarlo contra las 11 corridas: fallaba 8 de 11 porque el regex casaba con `kspDebugUnitTestKotlin`, `compileDebugUnitTestKotlin` y `generateDebugAndroidTestAssets`, que compilan o preparan pero nunca ejecutan una prueba | estrechar el regex a `\S*:(?:test|test\w*UnitTest)` (sólo tareas de tipo `Test`) y admitir `FAILED` como ejecutada —corrió y falló, que es lo contrario de servida de caché. Un detector que siempre grita no se lee: se valida contra casos de veredicto conocido antes de fiarse de él |

## Regla que se saca de las dieciocho

Ninguna de estas fallas la habría cazado una prueba de la aplicación. Todas son del
**proceso de medir**, y por eso las contrapartes viven en `tools/latido.py`, en
`tools/comprobar_entorno.py` y en pruebas que verifican la verificación. Cuando una
medida dé 0, vacío o «sin anomalías», la primera pregunta no es si el mundo está
limpio: es si la medición leyó lo que creía leer.
