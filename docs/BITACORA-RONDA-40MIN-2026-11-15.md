T0=1794747715 (13:01:55Z)
# Bitácora de ronda · 40 minutos · 2026-11-15
Regla del dueño: cada acción registrada y confirmada, sin falsos positivos ni manipulación por omisión.
Formato: [minuto] acción → resultado verificado (fuente de la verificación).

[0min] T0 + estado inicial → vigilante vivo, PR head 6711284
[1min] simulacro de producción de las URLs fijadas en cero-X → ver veredicto arriba
[2min] auditoría de logs de la corrida 43712847510 → ver salida
[3min] evidencia CI (resumen de pruebas), igualdades manga JSON↔PB medidas, diagnóstico dependabot y docs

## Minuto 12 → 24 (13:13Z - 13:25Z)

- **13:13Z** · Medida la hipótesis MIXED contra datos reales (parser pb propio sobre el raw
  fijado `64d2caef` + `index.min.json`): `contentWarning==3 ⟺ min.nsfw==1` en **1702/1702**;
  las **579 MIXED** van como `nsfw=0` en el JSON; el pb nunca es más laxo (`json-nsfw ⇒
  cw>=2` = 1702/1702). Fuente: descarga real de los dos ficheros del pin.
- **13:14Z** · `write_file` `IntegracionRedRealTest.kt`: recuentos vetustos 1618/273 →
  **1702/272** (quedaba en rojo con `CEROX_NETWORK_TESTS=1`), +1 prueba nueva
  `formato_moderno_real_coincide_con_el_json_min` (mismo catálogo y mismos códigos en pb y
  JSON, sha256 cubierto, nsfw de anime exacto 272/272 y en manga la regla «más estricto,
  nunca más laxo» con 494 JSON / 1.073 pb). Verificado contra el código real: `noxModerno():
  List<ExtensionIndice>`, campos `paquete/codigo/nsfw/sha256`, y `sha256(File)` top-level en
  `RepositoriosAuditados.kt:520` (mismo paquete) → compila.
- **13:14Z** · `edit_file` `RepositoriosAuditados.kt`: la divergencia MIXED queda escrita
  donde se decide (`nsfw = aviso >= 2`), con las mediciones.
- **13:15Z** · `edit_file` ×3 en `docs/AUDITORIA-FUENTES-Y-KISARA.md`: pines
  `55b9127e…`/`d2b689f3…` → **`64d2caef…`/`51bb0521…`**, recuentos 1.618/273 → **1.702/272**,
  mención del `index.pb` como consumo preferente y del PR #3 para el pb de anime; + nota
  fechada con lo medido por API.
- **13:16Z** · **Hallazgo por API sobre las raíces reales de los pines**: manga `64d2caef`
  **no tiene carpeta `apk/`** (raíz: `icon/ index.html index.json index.min.json index.pb
  release-assets.json repo.json` + LICENSE/NOTICE/README) ⇒ los APK viven en releases, lo que
  explica `resolverUrlManga()` y `release-assets.json`. Anime `51bb052` **no tiene `index.pb`**
  (raíz: `apk/ icon/ index.html index.json index.min.json repo.json`) ⇒ el formato moderno lo
  aporta el PR #3.
- **13:17Z** · **Falso positivo propio cazado y corregido**: una primera comprobación de
  paridad dio `DIVERGENTE` porque asumí que los APK se llaman `<paquete>.apk`. La
  nomenclatura real es `aniyomi-<lang>.<slug>-v<maj>.<min>.apk` (la que genera `create-repo.py`
  de la org). Rehecha contra el campo `apk` del índice: **PARIDAD EXACTA 1:1 — 272 APK reales,
  272 citados, 0 huérfanos, 0 rotos**. Registrado aquí para no repetir el supuesto.
- **13:17Z** · `edit_file` `docs/auditoria/investigacion-fmhy-appteka.md:206`: «273 APK» se
  conserva como dato de su instantánea y se añade el del pin vigente con la paridad 1:1.
- **13:16:17Z** · Commit **`a54819137d1fd9612dbf630eb77f66d4f4d0307a`** + push con URL de un solo
  uso: `local == remoto` (**PUSH VERIFICADO**), sin cambios de modo.
- **13:16:20Z→13:18:48Z** · CI corrida **43718120579** (`pruebas`, push, head `a5481913`): job `unitarias`
  **success**, 12 pasos success/1 skipped (el de artefactos, sólo si falla). Logs descargados y
  auditados: `> Task :app:testDebugUnitTest`, `BUILD SUCCESSFUL in 53s`, resumen
  **`628 pruebas · 0 fallos · 0 errores · 15 saltadas`** (627→628 y 14→15: la prueba nueva de
  red real cuenta y queda saltada por ser opt-in. Coherente.)
- **13:22Z** · Diagnóstico dependabot sobre el fichero real: `serialize-javascript@^6.0.2` →
  **6.0.2** en `comun/kotlin-js-store/yarn.lock:390-393`, pedido por **`mocha@10.7.0`**
  (líneas 299/317), versión clavada por el plugin de Kotlin/JS ⇒ utillaje de pruebas JS, no
  código del APK. Sin `dependabot.yml` en el repo (las alertas son de la rama por defecto).
  **No se edita el lockfile a mano**: rompería `resolved`/`integrity` y sería un arreglo falso.
- **13:21Z** · `docs/auditoria/DEPENDABOT-SERIALIZE-JAVASCRIPT.md` (nuevo) con alcance, motivo
  de no ejecución y las dos rutas reales (resolución Yarn + `kotlinUpgradeYarnLock`, o subir el
  plugin de Kotlin). Commit **`27af15793ae57a01484f50aa5d594f3e38ded661`** (13:21:34Z) + push:
  `local == remoto` (**PUSH VERIFICADO**).
- **13:25Z** · PR #3 re-verificado por API: `state=open merged=False comentarios=0+0
  head=6711284aa4 actualizado=2026-11-15T12:09:43Z`. Vigilante `vigilante-pr-3-269f757d`
  `status=running` (sondea ~cada hora; última línea 12:14Z).
- **13:28Z** · Verificado porqué `27af157` no abrió corrida: `.github/workflows/pruebas.yml`
  lleva filtro de rutas (`android/**`, `.github/workflows/pruebas.yml`), y ese commit tocó sólo
  `docs/**`. **No es un fallo de CI: es el filtro funcionando.** Corridas reales del día:
  43718120579 (`a5481913`, success, creada 13:16:20Z) y 43712847510 (`a7fdbc71`, success,
  12:14:49Z). Horas corregidas en esta bitácora contra `git log --date=format-local` y la API
  (dos entradas traían el minuto estimado, no el real).
- **13:30Z** · Cierre de la ronda: pendientes (a) pines de docs, (b) recuentos de la prueba de
  red real, (c) divergencia MIXED y (d) diagnóstico dependabot → **los cuatro hechos y
  verificados**. Estado final cero-X: HEAD `27af15793ae57a01484f50aa5d594f3e38ded661`
  == remoto (comprobado con `git ls-remote`), árbol limpio, última corrida de CI sobre código
  (`a5481913`) = success con 628/0/0/15 auditado en los logs.

## Minuto 29 → 33 (13:30Z - 13:34Z)

- **13:30Z** · Comprobado en el código real que la aserción nueva no planta un rojo: el lector
  pb hace `codigo = versionCodePb % 1000` (`RepositoriosAuditados.kt:300`) y el JSON usa
  `code`, que es el mismo resto. Medido además el nombre de APK entre formatos:
  **iguales 1.702/1.702 (manga) y 272/272 (anime)** → sólo entonces se asertó.
- **13:31Z** · Commit **`7d108e17e6a2a7e8f37e3fae8219eb37896b18d6`** + push: `local == remoto`
  (**PUSH VERIFICADO**), sin cambios de modo.
- **13:33:38Z** · CI corrida **43719391526** (`pruebas`, push, head `7d108e17`): **completed
  success**, job `unitarias` sin pasos fallidos; logs auditados → `> Task
  :app:testDebugUnitTest`, `BUILD SUCCESSFUL in 53s`, resumen **`628 pruebas · 0 fallos · 0
  errores · 15 saltadas`** (sin variación: las aserciones nuevas viven dentro de la prueba
  opt-in, que sigue saltada sin `CEROX_NETWORK_TESTS=1`).
- **13:34Z** · Estado final de la ronda: cero-X HEAD `7d108e17` == remoto, árbol limpio, tres
  commits nuevos en la ronda (`a5481913`, `27af1579`, `7d108e17`) y las dos corridas de CI que
  tocaban código en success con logs auditados. PR #3 open, 0 comentarios, head `6711284aa4`,
  vigilante vivo. Pendientes (a)-(d) cerrados; el único cabo abierto es la ejecución de la
  corrección de `serialize-javascript`, que necesita un entorno con Gradle/Kotlin-JS y orden
  del dueño, y queda diagnosticada por escrito en el repo.
