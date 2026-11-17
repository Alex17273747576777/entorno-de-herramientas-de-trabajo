# FALLAS Y CONTRAPARCHES — registro de la casa

*Corte: 2026-11-14 (UTC-4). Cada falla que tumbe trabajo se registra aquí con su
contraparche u habilidad solucionadora antes de proseguir. Regla del dueño:
«registra la falla y un contraparche/habilidad solucionador para ella y luego procede».*

Formato de entrada: síntoma → causa → contraparche/habilidad → estado.

---

## FALLA-001 · Turno caído por tiempo («The AI took too long to respond»)

- **Síntoma:** el turno murió a mitad de faena; el dueño vio el mensaje de plataforma
  `The AI took too long to respond. Please try again.` con id de petición
  `01a1da29-208d-70f4-b9a4-bb9d34ea4bb6` (2026-11-14). Todo lo que el turno llevaba
  en vuelo (sin guardar a fichero) se perdió con él.
- **Causa:** un solo turno intentó abarcar el paquete completo de publicaciones
  (decenas de piezas de 40-63 k caracteres) sin persistir estados intermedios.
  Sin checkpoint, un timeout deja al turno siguiente empezando de cero.
- **Contraparche / habilidad solucionadora:** `SKILL-TURNO-CON-CHECKPOINT`
  (ver abajo) + herramienta `edt/bin/checkpoint.sh`.
- **Estado:** CONTRAPARCHADA (herramienta y habilidad vivas en este mismo corte).

### SKILL-TURNO-CON-CHECKPOINT (habilidad solucionadora)

1. **Al abrir el turno:** leer `edt/docs/CHECKPOINT-ACTUAL.md` antes de tocar nada.
   El checkpoint dice tarea, hecho y siguiente paso; se retoma desde ahí, nunca de cero.
2. **En cada hito:** escribir el checkpoint con `bash edt/bin/checkpoint.sh escribir
   "<tarea>" "<hecho>" "<siguiente paso>"`. Un hito sin checkpoint es un hito que el
   próximo turno no verá.
3. **Tope duro por turno:** máx. 2 piezas maestras nuevas, o 1 generador + su corrida,
   o 1 reestructura de sistema. Lo que pase del tope va al checkpoint como siguiente paso.
   **Enmienda 3-bis (2026-11-14):** se permite turno combinado (reestructura + generador +
   hasta 2 maestras) **sólo si** cada hito se checkpointea y se espeja en `edt/` antes de
   empezar el siguiente. La protección no es el tope: es que nada quede sin persistir.
4. **Todo contenido nuevo se espeja en `edt/` (persistente) el mismo turno en que se
   crea.** Lo que sólo vive en `/var/tmp` (clones) muere en el próximo reinicio.
5. **Invocar herramientas por `bash <ruta>`**, no por bit de ejecución: los reinicios
   vuelven `100755` a `100644` y la herramienta parece rota sin estarlo.
6. Si el dueño reenvía cualquier texto tras un timeout, **no es instrucción nueva**:
   es la misma faena; se retoma del checkpoint.

---

## FALLA-002 · Detector G19 cazaba slugs pelados y dejaba pasar cultura pop

- **Síntoma:** la primera versión de `edt/bin/compuerta-canal-y-mision.py` dio 44 falsos
  positivos (las piezas citan repos como `owner/repo` sin URL) y luego dejó pasar
  `EntityData/Q193835.json` (Wikidata) como «repo».
- **Causa:** medir por forma (regex de slug) en vez de por vocabulario de medición.
- **Contraparche:** G19 vigente = señal por vocabulario (`★|estrellas`, URLs github,
  `repositorio|repos`, licencias SPDX) con `en_mision = ★>=3 or urls>=1 or repos>=3 or
  licencias>=2`; validado pieza por pieza contra señales crudas (45/45 coinciden).
  Lección: todo detector se valida contra un positivo y un negativo conocidos.
- **Estado:** CONTRAPARCHADA y validada (2026-11-14).

---

## FALLA-003 · El reinicio se llevó el clon y con él las EDICIONES no espejadas

- **Síntoma:** segundo reinicio del turno al siguiente: `/var/tmp/la-bandita-archivo`
  desapareció otra vez (2026-11-14, entre el turno de la pieza 01 y éste). El espejo
  conservaba los ficheros NUEVOS (maestras, derivados, LEEMEs, generador, bandas) pero
  **no las ediciones hechas dentro del clon**: la nota fechada del CORAZON y las carpetas
  vacías de la estructura. Tocarlas de nuevo costó trabajo repetido.
- **Causa:** la SKILL mandaba espejar «todo contenido nuevo», pero no las **ediciones a
  ficheros existentes** (CORAZON, bandas.json). Un espejo de ficheros nuevos no es un
  espejo de estado.
- **Contraparche / habilidad solucionadora:** `reaplicar-estructura.sh` en el espejo:
  reconstruye en un mando carpetas, LEEMEs, herramientas, bandas.json y la nota del
  CORAZON (idempotente por marcador). Regla añadida: **toda edición a un fichero del repo
  se guarda además como fichero propio en el espejo** (la nota del CORAZON vive ahora en
  `CORAZON-nota-reestructura-2026-11-14.md`) y bandas.json se edita en el espejo y se copia
  al clon, nunca al revés.
- **Estado:** CONTRAPARCHADA (script vivo y clon reaplicado en este corte).

## FALLA-005 · El visor de present_file llega roto al dueño

- **Síntoma:** el dueño ve disfuncional el archivo presentado con `present_file`
  («deja de presentar ese recacha disfuncional de mierda», 2026-11-15). El preview corre
  en un iframe sandboxed sin red: cualquier recurso externo o renderer exigente llega roto.
- **Causa:** no es del todo reparable desde aquí: el sandbox del visor es de la plataforma.
- **Contraparche / habilidad:** no usar `present_file` para entregables de trabajo; dar la
  ruta en el chat y dejar el fichero en el espejo persistente. El contenido manda, el
  visor no.
- **Estado:** CONTRAPARCHADA (regla de oficio desde este corte).

## FALLA-006 · Tokens pegados en el chat y permisos 0644 tras reinicios

- **Síntoma:** el dueño pegó cuatro tokens en texto plano en el mensaje (2026-11-15) y
  `tokens.txt` amaneció 0644 otra vez tras el reinicio.
- **Causa:** pegado manual en canal conversacional + el reinicio relaja permisos.
- **Contraparche:** los cuatro entraron al llavero `~/.cerox-keys/tokens.txt` como
  `GHP_A/GHP_B/GHP_C/GP2` con 0600; toda autenticación de git se hace con URL de un solo
  uso (`x-access-token:$T@…`), nunca incrustada en `.git/config` (C13). Pendiente del
  dueño: **rotar los tokens pegados en el chat**, que ya quedaron expuestos en el historial.
- **Estado:** CERRADA POR DECISIÓN DEL DUEÑO (2026-11-15): las llaves NO se revocan; siguen vivas a largo plazo y el riesgo de exposición en el historial del chat queda aceptado por el dueño. Siguen las reglas de manejo: llavero 0600, URL de un solo uso, nunca imprimir ni citar las llaves.

---

## FALLA-007 · La salida sintética de la autoprueba se leía como aviso real (2026-11-15)

- **Síntoma:** `make verificar` de la-bandita imprimía «⚠ rutas vivas rotas:
  README.md:1 · cita a carpeta-vieja/» sin que el README real citara nada de eso;
  la nota de «aviso abierto» vivió dos turnos como si fuera deuda verdadera.
- **Causa:** `tools/autoprueba.py` hace eco de las primeras líneas de cada compuerta
  corriendo contra su ÁRBOL FALSO sin etiquetar el origen; el README sintético cita
  `carpeta-vieja/` en la línea 1 a propósito (para probar que la compuerta detecta).
- **Contraparche:** eco etiquetado («salida del árbol sintético — no es la casa») y
  líneas prefijadas con `|`; verificado en la corrida real (el aviso ahora se lee como
  lo que es). Regla: antes de cazar un aviso, comprobar de qué boca sale.
- **Estado:** CONTRAPARCHADA (commit a05ec2e6, empujado a main).

## FALLA-008 · `exit 0` dentro de una regla awk cae al END y voltea el veredicto (2026-11-15)

- **Síntoma:** una comprobación por lotes («¿está sellado este archivo?») declaró NO
  sellados a todos, incluido README.md, que el grep directo sí encontraba sellado.
- **Causa:** `awk '$1==p{exit 0} END{exit 1}'` — en awk, `exit` salta al bloque END y
  el `exit 1` del END pisa el estado de la regla.
- **Contraparche:** bandera en vez de exit directo (`$1==p{f=1} END{exit !f}`) o
  `grep -q "^ruta<TAB>"`. Regla: desconfiar de todo `exit` dentro de regla si hay END.
- **Estado:** CONTRAPARCHADA (misma corrida; sellado real confirmado con grep exacto).

---

## Plantilla de entrada nueva

```
## FALLA-NNN · <título>
- **Síntoma:** …
- **Causa:** …
- **Contraparche / habilidad solucionadora:** …
- **Estado:** ACTIVA | CONTRAPARCHADA
```

## FALLA-009 — Horas de bitácora escritas de memoria (2026-11-15, ronda feed ShinKu⇄AniZen)

**Síntoma.** Siete entradas de la bitácora de la ronda llevaban horas estimadas («15:28Z»,
«15:31Z», «15:36Z»…) cuando el reloj real iba por 15:14-15:19Z: desvío de hasta 17 minutos.
Ningún hecho era falso, pero la bitácora —que es la prueba de la ronda— dejaba de serlo: un
registro con horas inventadas no permite reconstruir nada y es un positivo falso por omisión.

**Causa.** Escribir la marca de tiempo al narrar la acción, en vez de leerla cuando la acción
ocurre. Ya había pasado en la ronda anterior (dos entradas corregidas contra `git log`).

**Contraparche (obligatorio desde aquí).**
1. La hora de una entrada se toma con `date -u +%H:%M:%SZ` **dentro de la misma llamada** que
   ejecuta la acción, o se deriva después de evidencia: `mtime` del fichero (`date -u -r`),
   `created_at`/`updated_at` de la API, `git log --date=format-local`, timestamp del log de CI.
2. Si la hora no se puede verificar, la entrada se escribe **sin hora** y con el orden relativo;
   nunca con una hora supuesta.
3. Al cerrar cada ronda, comparar la última hora escrita contra `date -u` antes del checkpoint.
4. Corrección de una hora ya escrita: sustituirla y dejar constancia de la sustitución y de su
   fuente (como en esta ronda), no reescribir en silencio.

## FALLA-010 · Publiqué el binario con el esquema del ecosistema equivocado, y documenté la regresión como una corrección

**Cuándo:** detectada el 2026-11-17 a las 10:48Z al leer el cierre de `Awerkori/anime-extensoes#3`.
El mantenedor cerró el PR **sin fusionar** (06:52Z) conservando el crédito: la implementación se
aprovechó corregida en `Awerkori/anime-fonte-extensoes#9`.

**Qué pasó, verificado por bytes y no de memoria:**

| fichero | tamaño | campos de Extension | spec | destino correcto |
|---|---:|---|---|---|
| `anime-index.pb` | 17.663 B | `[1..8]`, 326 fuentes en el campo **8** | **nox** (org / Nox Mangá) | ✗ |
| `anime-index-spec-aniyomi.pb` | 17.664 B | `[1..7,9]`, 326 fuentes en el campo **9** | **aniyomi** (oficial) | ✓ |
| `index.pb` de la rama `index-pb` del PR | 17.663 B | **idéntico byte a byte** a `anime-index.pb` | nox | ✗ |

Un cliente Aniyomi lee `sources=8` como `isTorrent` y no ve las 326 fuentes: exactamente lo que dijo la
revisión. **Lo grave no es el despiste, es la secuencia:** la *primera* revisión del PR llevaba el spec
correcto (`sources=9`) y mi **segundo commit** (`0ca7294` → `6711284`) lo «corrigió» al proto de la org.
Mi propio `INFORME-CONVERSION.md` lo describía así: «`anime-index-spec-aniyomi.pb` — histórico: la
primera revisión del PR usó el spec de Aniyomi; se conserva como evidencia de la **corrección**». O sea:
documenté una regresión como un arreglo, y el documento citaba dos líneas más arriba la autoridad
correcta («el spec de Aniyomi para anime/Yuzono»). Tenía la regla escrita, el fichero correcto en el
mismo directorio, y publiqué el otro.

**Regla que queda:** cuando existen dos variantes generadas de un mismo artefacto, **la elección se
verifica sobre los bytes del fichero que se va a publicar**, no sobre el nombre ni sobre la intención; y
ningún commit «corrector» se describe como corrección sin decir qué cambió y contra qué autoridad.

**Contramedida ejecutada (no prometida):** compuerta en `json_a_index_pb.py` —
1. modo nuevo `verificar-spec <fichero.pb> [nox|aniyomi]` que **lee los bytes escritos** y compara el
   número de campo real de `Extension.sources` (8 = nox, 9 = aniyomi), salida 1 si no coincide;
2. `generar` se **niega** a producir `spec=nox` cuando el repositorio destino lo consumen clientes
   Aniyomi (`anime-extensoes`, `anime-fonte-extensoes`, `anime-extensions`), salvo `--forzar-nox`;
3. `generar` se auto-comprueba tras escribir y **borra** el fichero si lo escrito no casa con el spec
   pedido (FALLA-008: toda compuerta se prueba contra un caso que debe fallar).

Pruebas ejecutadas el 17-11 a las 10:53Z, las cuatro con su resultado esperado:
`verificar-spec anime-index.pb nox` → ✓ 0 · `… aniyomi` → ✗ **1** (el caso que debe fallar) ·
`verificar-spec anime-index-spec-aniyomi.pb aniyomi` → ✓ 0 · `generar … anime-extensoes … nox` →
**NEGADO, salida 1, ningún fichero escrito**.

**Precisión honesta sobre el diagnóstico ajeno:** la revisión también mencionaba `Source.message=7`.
En mi binario ningún `Source` lleva el campo 6 ni el 7 (proto3 omite cadenas vacías y todas iban
vacías), así que ese detalle no aplica a este artefacto; el defecto decisivo y real es `sources=8`
frente a `9`. Se lo dije en el PR en vez de callarlo o de fingir que todo su diagnóstico aplicaba.

## FALLA-011 · Comillas invertidas dentro de `git commit -m "…"` (2026-11-17, gltools-reborn)

**Qué pasó:** escribí el mensaje de `d9c743f` con `-m "…"` y el texto llevaba los identificadores
entre comillas invertidas, como se escribe en markdown. Bash no ve markdown: las interpretó como
sustituciones de comando, ejecutó `componerParte`, `APP`, `extracto`, `OutOfMemoryError`, `Context`,
`RuntimeException:` y una docena más como órdenes (todas dieron *command not found*, en stderr, a la
vista) y sustituyó cada una por la cadena vacía. El commit se creó y se publicó con el mensaje hueco
justo donde iban los nombres: «Ahora  escribe una l—nea  antes del stack».

**Por qué no se cazó al momento:** el `git commit` devuelve 0 aunque el shell se queje en stderr, y
la línea siguiente imprimía el SHA corto. Miré el SHA, no el mensaje.

**Regla que queda:** los mensajes de commit largos se escriben en un fichero y se pasan con
`git commit -F fichero`. Nunca `-m "…"` con markdown dentro. Y después de commitear, **leer el mensaje
publicado** (`git log -1 --format=%B`) forma parte de la verificación, igual que comparar el SHA con
`ls-remote`.

**Contramedida ejecutada:** el mensaje correcto se publicó entero en
`gltools-reborn#3` (comentario `issuecomment-6947651332`) diciendo qué pasó. **No** se enmendó el
commit ni se hizo force-push: `d9c743f` ya estaba en `main`, y reescribir historia publicada para
tapar un fallo propio es peor que dejar constancia del fallo.

## FALLA-012 · Cifra y procedencia escritas de memoria al lado del comando que las medía (2026-11-17)

Dos en la misma hora, las dos publicadas, las dos desmentidas por una medición que estaba corriendo
en la misma línea de órdenes:

1. **`censo/README.md` decía «máximo 352»** para el snapshot del 17-11. 352 es el máximo del snapshot
   del **08-11**: copié la cifra de la foto anterior. Medido sobre el `.gz` nuevo: **361**
   (`app.morphe.manager`). Corregido en `8cf71e4` dejando la corrección fechada a la vista.
2. **El mensaje de `fe45074` decía que los `.pyc` de `tests/__pycache__` entraron en `92aee28`.**
   Falso: entraron en **`9aa64f6`** (2026-11-10). El `git log --diff-filter=A` que lo desmentía se
   ejecutó **antes** del commit, en el mismo script; escribí el texto antes de mirar su salida.

**Regla que queda:** es la hermana de FALLA-009 (horas de bitácora de memoria) y se aplica igual a
números y a SHAs: **si un dato va publicado, se copia de la salida del comando que lo mide, no de lo
que uno recuerda.** Y cuando el comando que lo mide está en el mismo script que el texto, el texto se
escribe *después* de leer la salida — o se genera con el mismo script.

**Contramedida ejecutada:** ambas correcciones publicadas (`8cf71e4` en el repo, y la procedencia de
los `.pyc` dicha en el cierre de `normas-de-diseno#2`, `issuecomment-6947454714`), sin reescribir los
commits que llevaban el dato malo.

## FALLA-013 · Un oráculo de lint sin su fichero de configuración (2026-11-17, ShinKu PR #37)

**Qué pasó:** quise saber si mi cambio añadía violaciones de formato. Copié los cuatro ficheros a
`/tmp/base` en su versión del `main` del mantenedor y pasé ktlint por los dos lados. La comparación
dijo «base 94 violaciones, mío 7» — o sea, que mi cambio *arreglaba* 87. Era un disparate: en
`/tmp/base` no copié el `.editorconfig`, así que ktlint aplicó reglas que el proyecto tiene
**desactivadas** (`class-signature`, `function-signature`, `function-expression-body`…). Los dos lados
de la comparación se midieron con reglas distintas.

**La medición buena, con el `.editorconfig` copiado:** base 5, mío 5, mismas reglas en los mismos
ficheros ⇒ mi cambio añade **0**. Las cinco ya estaban en el `main` del mantenedor.

**Regla que queda:** para un lint o un formateador, **el fichero de configuración es parte del
oráculo**: se copia con las fuentes o no vale nada. Y antes de creerle al oráculo, se falsifica contra
un caso conocido — aquí, tres: `core-metadata` (que en CI **pasó**) da 0 local, `macrobenchmark` (que
en CI **falló**) da 1 local en la misma línea y la misma regla, y `i18n` da 1 antes de mi arreglo y 0
después. Con esos tres, el número de 1.113 violaciones en 621 ficheros del repo entero ya es creíble.

**Contramedida ejecutada:** la tabla de falsación se publicó en `ShinKu#37`
(`issuecomment-6947597445`) junto con el recuento por módulo, para que nadie tenga que fiarse de mi
ktlint sin ver contra qué se comprobó.

## FALLA-014 · Un generador que escribe antes de comprobar, y un ritual que sella después (2026-11-17, la-bandita-archivo)

**Qué pasó:** `make ritual` (= verificar → sellar → verificar) llama a `make tareas`, y
`tools/tareas.py` escribía `docs/TAREAS.md` **antes** de comprobar si había encontrado alguna pieza.
El clon de trabajo no tiene `Arena-Reimagined/01-PUBLICACIONES` (es superficial y sólo trae el
archivo), así que el generador escribió un tablero de **0 tareas, borrando las 90** que había, y
*después* imprimió «✗ no hay ninguna tarea declarada en las piezas vivas» y salió con 1. El aviso
llegó con el fichero ya destruido.

**Lo que lo volvió grave:** el ritual siguió. `tools/atestar.py` selló el árbol **después**, así que
el sello nuevo quedó calculado sobre el tablero vacío: la casa habría quedado con una attestación
que certificaba la pérdida. Y el `EXIT=0` final del ritual tapaba todo: el fallo de `tareas` iba
marcado `(ignored)` en el Makefile.

**Cómo se cazó:** por el `git diff` del árbol después del ritual —115 líneas borradas en un fichero
que nadie había decidido tocar—, no por la salida del comando. La salida decía «ritual completo».

**Regla que queda, en tres partes:**
1. **Un generador que no encuentra su materia prima no publica un resultado vacío: se niega.**
   Cero entradas no es «el resultado de hoy», es «no he podido mirar». Es la misma regla que el
   auditor de lockfiles que sale 2 cuando no pudo preguntar, aplicada a un escritor de documentos.
2. **El orden escribir→comprobar está prohibido**; va comprobar→escribir. Y si el aviso es un
   `exit 1`, que llegue **antes** de tocar el fichero.
3. **Después de un ritual que sella, se mira `git status` y `git diff --stat` del árbol**, no sólo el
   código de salida: un sello verde sobre un fichero vaciado es peor que ningún sello, porque parece
   certificado.

**Contramedida ejecutada (no prometida):** guarda en `tools/tareas.py::escribir()` — si no aparece
ninguna tarea y el tablero publicado tiene alguna, `SystemExit` con el motivo y **sin tocar el
fichero**. Probada en los dos sentidos: negativa (clon tal cual → `EXIT=1` y
`git diff --exit-code docs/TAREAS.md` limpio, 90 tareas intactas) y positiva (pieza sintética con una
`#task` → escribe el tablero con 1 tarea, o sea que la guarda no bloquea el camino bueno); la pieza
sintética se borró y el tablero se restauró. Commit `bfaa811b`, re-sellado después
(`lote-2026-11-17`, huella `1a50771abaea2f18…`) y `make verificar` en `EXIT=0` con 14.363 archivos,
0 alterados y 0 sin sellar.

## FALLA-015 · Publiqué «verificado» sin mirar la CI de mis propios repos (17-nov-2026, 23:24Z)

**Qué pasó:** cerré la orden de emergencia con un parte que decía verificado: `local==remoto`,
`make verificar EXIT=0`, `tests/pruebas.py EXIT=0`, `git fsck` limpio. Todo cierto y todo local.
Una auditoría contra la API —no contra la memoria— destapó que **cuatro repos míos estaban en
rojo** en ese momento, y uno de ellos sobre el commit exacto que yo había descrito como `EXIT=0`:
`vara` fallaba sobre `bfaa811b` de la-bandita-archivo. Llevaban así: edt 6 corridas de 6, normas
6 de 6, gltools 4, la-bandita desde el 15-nov (último verde `42869190307` sobre `4d257e9c`,
10-nov). Nadie me lo había dicho; estaba a una consulta de distancia y no la hice.

**Por qué es grave:** el parte de verificación es lo único que el dueño tiene para decidir. Un
verde local presentado como verificación convierte un defecto publicado en un hecho certificado.
Es la misma forma que la FALLA-010 (documentar una regresión como corrección) y que el sello verde
sobre el tablero vaciado de la FALLA-014: **la autoridad citada no mide lo que el texto afirma**.

**Regla que queda:**
1. **Verde local ≠ verde publicado.** La verificación de un commit propio incluye
   `GET /repos/<dueño>/<repo>/actions/runs?per_page=N` y, si hay `failure`, leer el log del job
   antes de escribir la palabra «verificado».
2. **El log de Actions se lee siguiendo el 302 de `/actions/jobs/{id}/logs` SIN la cabecera
   `Authorization`** (con ella, el blob firmado responde 401).
3. **Toda afirmación de verificación nombra qué se midió y dónde.** «Verificado» sin alcance es
   publicidad. Si algo no se pudo medir, se escribe en la misma frase.
4. Al empezar un turno, mirar las notificaciones (`GET /notifications?all=true`): 50 de ellas eran
   «workflow run failed» de mis repos y llevaban ahí días.

**Contramedida ejecutada:** los cuatro frentes diagnosticados y arreglados el mismo día, con la
causa raíz medida y no supuesta. Ver `docs/DIAGNOSTICO-CI-2026-11-17.md`.

---

## FALLA-016 · Una ley que cuenta texto en bruto cuenta su propia definición (17-nov-2026)

**Qué pasó:** la prueba de gltools-reborn «el vidrio es la excepción, no la norma» contaba
`Regex("\\.vidrio(Alto)?\\(")` sobre las 14 fuentes de `ui/` y exigía ≤2. Daba 4 y estaba roja en
cada push desde `d9c743f`. Los cuatro no eran vidrio: eran las dos **declaraciones**
(`fun Modifier.vidrio(radio: Int = 22)` en `Tema.kt:161` y `:167`) y dos menciones en la **prosa**
de un comentario de bloque de doce líneas (`Tema.kt:87`) que explica por qué se conserva el nombre.
Usos reales en pantallas: **0**. La ley se rompía con su propia definición y con el comentario que
la documenta. Y era frágil por doble motivo: descontando sólo las declaraciones el recuento daba
**2 contra un tope de 2**, así que escribir `.vidrio()` una vez más en cualquier comentario volvía
a ponerla en rojo sin tocar una pantalla.

**No es un caso aislado:** el mismo fichero ya lo sabía y lo tiene escrito dos veces —la
comprobación de glifos ignora lo que hay antes de `//` («en un comentario se puede hablar de
glifos», línea 973) y la de desplazamientos busca «la LLAMADA, no la palabra» (línea 1338)—. La
regla del vidrio simplemente no recibió el mismo trato.

**Regla que queda:**
1. **Toda ley que cuente apariciones cuenta sobre código**: fuera comentarios de línea y de bloque,
   fuera el contenido de las cadenas de una y de tres comillas, y fuera las líneas que declaran lo
   que se está contando.
2. **Se falsifica en los dos sentidos**: inyectar la violación real tiene que ponerla en rojo, e
   inyectar prosa que la nombre tiene que dejarla en verde. Un solo lado no prueba nada.
3. **Un tope alcanzado por casualidad es un rojo aplazado.** Si el recuento da exactamente el tope,
   se mira de qué está hecho el número antes de darlo por bueno.

**Contramedida ejecutada:** auxiliar `soloCodigo()` + `DECLARA_MODIFICADOR` en `Pruebas.kt`,
aplicado a los tres sitios que cuentan (la ley del vidrio, la comprobación 5 y `cuenta()` de
1.9.2). Compilado con kotlinc 2.3.10/JDK 17 dentro de un arnés que lleva el código publicado
**literalmente**, y corrido contra las fuentes reales más seis mutaciones: reales 0 → verde;
3 llamadas reales → **rojo**; 5 menciones en `/* */` → verde; 2 llamadas → verde (el tope es 2);
2 reales + 1 dentro de una cadena → verde; declaración nueva → verde; mención en triple comilla →
verde. La regex vieja daba 4, 7, 9, 6, 7, 5 y 6 en esos mismos siete casos. Commit `feb46487`.
En `cuenta()` el cambio es neutro hoy, medido: vidrio 0, bordes 2, cajas 39 con y sin auxiliar —
pero con 39 contra un tope de 40, una mención de `RoundedCornerShape(20.dp)` en un comentario la
habría puesto en rojo.

---

## FALLA-017 · Un documento que anuncia comprobaciones que el código no hace (17-nov-2026)

**Qué pasó:** `docs/TAREAS.md` de la-bandita-archivo termina con «Las comprobaciones que hace este
programa: 1. Sin huecos 2. Sin textos contradictorios». La regla 2 **no estaba en ninguna parte de
`tools/tareas.py`**: `revisar()` sólo miraba huecos y repetidos. Y el tablero publicado la
incumplía en 4 números (018, 026, 027 y uno más) medidos sobre las 90 filas.

**Segundo defecto, peor:** el repo versiona el derivado (`docs/TAREAS.md`, 90 filas, 22.500 bytes)
y **no versiona su materia prima**. Medido sobre el árbol de `main` (19.005 blobs,
`truncated=False`): la carpeta `Arena-Reimagined/01-PUBLICACIONES` no existe. Ningún clon limpio
puede regenerar el tablero, y por eso la compuerta «Tablero de tareas al día» no podía pasar nunca:
salía 1 diciendo «no hay ninguna tarea declarada en las piezas vivas», que sonaba a contenido y era
otra cosa —faltaba la carpeta entera—. Roja en cada push desde el 15-nov.

**Es la misma clase que la incidencia #3 de ese repo** (`medir_piezas_24_34.py:18` promete un
sha256 que no escribe): texto que afirma lo que el código no hace.

**Regla que queda:**
1. **Un documento generado sólo anuncia lo que el generador hace de verdad.** Si la lista de
   comprobaciones vive en el texto que escribe el programa, cada línea de esa lista tiene que tener
   su función al lado.
2. **Un derivado se versiona con su materia prima, o se declara que no se puede regenerar.** Las dos
   cosas son aceptables; lo que no es aceptable es publicar el derivado y dejar que la compuerta que
   lo vigila se ponga roja para siempre con un mensaje que apunta a otro sitio.
3. **Distinguir «no hay entradas» de «no pude mirar».** Un recuento en cero tiene dos causas y se
   dicen con palabras distintas, porque una es un fallo y la otra es una limitación declarada.

**Contramedida ejecutada:** `tools/tareas.py` distingue los casos (hay piezas y ninguna declara
`#task` → fallo; no hay ninguna pieza en el clon → aviso con la cifra que trae el propio tablero,
«se generó con 28 piezas vivas»), implementa la regla 2 sobre las piezas, añade la integridad del
tablero contra sí mismo (cabecera, 4 columnas, ids de 3 dígitos, ningún texto vacío, TL;DR que
case con el número de filas) y añade la correspondencia tablero↔piezas, que faltaba: antes un
tablero viejo pasaba en verde porque sólo se miraba la numeración de las piezas. Nueve casos
sintéticos, cada uno con su árbol propio, y verificado **sobre los bytes publicados** en `main`
(`a215717e`): el tablero real sin piezas sale 0 con la declaración impresa. Commits `b2a0fee3` y
`bfeb4c3f`. **Lo que sigue sin arreglo y es decisión del dueño:** o se versionan las piezas del
ciclo vivo, o la correspondencia sólo se puede comprobar en la máquina que las tiene.
