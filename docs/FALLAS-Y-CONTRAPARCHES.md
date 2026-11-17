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
