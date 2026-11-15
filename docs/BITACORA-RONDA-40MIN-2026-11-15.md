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

# RONDA NUEVA (T0 = 1794755262 = 15:07:42Z, fin 15:47:42Z) — encargo feed ShinKu ⇄ AniZen

- **15:07:42Z** · T0 fijado. Metadata por API de los dos repos: ShinKu `main`, Kotlin, 153.837 KB,
  Apache-2.0, ★49, 1 issue abierto, permisos míos `push:false`; AniZen `master`, Kotlin+GLSL,
  308.066 KB, Apache-2.0, ★202, 19 issues, `push:true` (**no se usó: cero push en repos ajenos**).
- **15:07:45-47Z** (mtime de `.git/HEAD` de cada clon) · Clon **en paralelo** de los dos (`git clone --depth 1`): `shinku` 110 MB
  @ `043ab7d8e68e8a77752805c34969a2477195826a`, `anizen` 33 MB
  @ `95160a724d1147777dd1f7997fff4885a4cd9deb`, en `/var/tmp/feed/`.
- **15:09-15:14Z** · Lectura del subsistema de novedades de los dos **en paralelo** (dos llamadas
  simultáneas): 1.450 .kt en ShinKu, 1.298 en AniZen; localizados `FeedTab/FeedScreen/
  FeedScreenModel` en cada uno, los `.sq` de persistencia y las migraciones.
- **15:10-15:13Z** · **Evidencia clave verificada con fichero y línea**: tope de 10 en
  `shinku/.../FeedScreenModel.kt:650-652` (`countFeedSavedSearchGlobal.await() > 10`) y
  `SourceFeedScreenModel.kt:108`; «10» escrito dentro de ~30 traducciones de
  `too_many_in_feed`; `ShinKuPreferences.kt:65` `feedLanguageFilter()` por defecto **`"en"`**
  mientras `LocaleHelper.kt:89-91` sí habilita el idioma del dispositivo para el resto de la app;
  `feed_saved_search.sq` de ShinKu sin `category`/`feed_order`/`search_type`.
- **15:10-15:13Z** · AniZen: `feed_categories.sq` (categoría de sistema `_id=1 'Global'`),
  `feed_saved_search.sq` con `feed_order`/`search_type`/`category`/`last_top_url` y
  `countGlobalByCategory`; `activity_log.sq` + `ActivityLog` (TYPE_FETCH/OPEN/PLAY/COMPLETE/
  FEED_UPDATE) **ya conectado al feed** en `FeedScreenModel.kt:97` y `:203`; `SourceHealthCache`;
  `FeedScreen.kt:69-115` con `ScrollableTabRow`+`HorizontalPager`. Huecos: **sin tope por
  pestaña** (`InsertFeedSavedSearch.await` inserta sin contar) y **sin dimensión de idioma**
  (grep de `lang` en `ui/home/*` sólo da imports de `launchIO`).
- **15:14Z** · Migraciones: ShinKu usa `Migration{version:Float}` con máximo **75f**; AniZen las
  tiene todas en `Migration.ALWAYS` (el esquema va por SQLDelight). `which kotlinc` → **ausente**:
  nada de lo propuesto puede compilarse aquí, y así se declara en los issues.
- **15:14:24Z y 15:15:32Z** (mtime real) · `write_file` ×2: `ISSUE-SHINKU.md` (9 bloques de código de ejemplo: `feed_categories.sq`,
  ALTERs, `FeedLimits`, cadenas con `%1$d`, política de idioma, `feed_activity.sq`, `SuggestFeedTabs`,
  UI con pager, migración 76f) y `ISSUE-ANIZEN.md` (8 bloques: `FeedLimits`, guarda con
  `countGlobalByCategory`, cadenas, `FeedGenreHelper` de anime, `SourcePageCursor`, `buildRows`,
  `SuggestFeedTabs` sobre `activity_log`, columnas aditivas `lang`/`explore`).
- **15:16:38Z** (created_at real de la API) · **Issues abiertos y verificados por lectura real**: ShinKu
  **201 → https://github.com/Harrys-HQ/ShinKu/issues/32** y AniZen
  **201 → https://github.com/salmanbappi/AniZen/issues/94**; enlace cruzado **PATCH 200** sobre #32.
  GET de comprobación: #32 `state=open` 23.214 chars `labels=[]` (ShinKu no tiene `enhancement`
  definida y la API la descartó en silencio — registrado, no maquillado); #94 `state=open`
  22.048 chars `labels=['enhancement']`.
- **15:17:37Z** (mtime real) · Código real de los dos subsistemas **plasmado en el workspace** (los clones viven en
  `/var/tmp`, volátil): `work/feed-novedades/codigo/shinku/` 24 ficheros + `codigo/anizen/` 29
  ficheros + los dos LICENSE = 448 KB.
- **15:18:40Z** (mtime real) · `work/feed-novedades/PLAN-FEED-SHINKU-ANIZEN.md`: investigación con evidencia
  fichero:línea, matriz de trasvase, plan en 8 fases (acuerdo → esquema/migración → tope/cadenas →
  idioma → estadísticas/sugerencias → filas ShinKu en AniZen → pruebas → traducciones), bloque
  «Lo NO verificado» y cabos abiertos.

### Corrección de horas de esta ronda (FALLA-009)

Las siete horas de las entradas anteriores se habían escrito **de memoria**, estimadas, y estaban
desviadas hasta 17 minutos (la ronda iba por 15:19Z cuando la bitácora decía 15:36Z). Se
sustituyeron por horas **leídas de evidencia real**: `mtime` de cada fichero escrito en el
workspace (`date -u -r`) y `created_at` de la API para los dos issues. Los hechos no cambian;
sólo las horas. Contraparche registrado como FALLA-009.

- **15:20:15Z** · Arrancado el vigilante de los tres frentes externos
  (`vigilar-frentes.sh` → `work/feed-novedades/vigilancia.log`, sondeo cada 10 min: PR #3 de
  anime-extensoes + issue #32 de ShinKu + issue #94 de AniZen). `process_id`
  `vigilante-pr-3-issues-32-94-08e70660`, `status=running`. Vive lo que viva la sesión.
- **15:21-15:22Z** · **Verificación de símbolos** de todo el código de ejemplo contra las fuentes
  clonadas (tabla en `work/feed-novedades/VERIFICACION-SIMBOLOS.md`). Cazados **dos errores míos
  reales**: en AniZen `SourceHealthCache` es un `object` con `getStatus(Long): NodeStatus`
  (`OPERATIONAL|DEGRADED|CRITICAL|OFFLINE`, `SourceHealthCache.kt:12-28` +
  `InfrastructureModels.kt:19-24`), no un `isHealthy()` inyectable; y `GetLibraryAnime.await()`
  devuelve `List<LibraryAnime>` cuyo `source` está en `.anime.source`. En ShinKu:
  `LibraryManga.manga.source` (no `.source`), `MigrationContext` es clase con
  `inline fun <reified T> get()` (`MigrationContext.kt:5-9`), y `SourceHealth.isFailingNow` /
  `getBySourceId()` existen (`SourceHealth.kt:5-15`, `SourceHealthRepository.kt:6-11`).
  Confirmados tal cual: `CountFeedSavedSearchGlobal`, `InsertFeedSavedSearch.await/awaitAll`,
  `ReorderFeed`, campos exactos de `FeedSavedSearch`/`FeedSavedSearchCategory`,
  `ActivityLogRepository.getCountsByPeriod(Date): Map<Pair<Long,Int>,Long>`, numeración
  `ActivityLog.TYPE_*`, `withIOContext` (`CoroutinesExtensions.kt:60`), forma de `Migration`
  (máxima 75f ⇒ 76f para la nueva).
- **15:23:01Z / 15:23:02Z** · **Corrección publicada en los dos issues** (no en silencio):
  snippets arreglados + sección «Symbol check (added after posting)» con lo corregido, lo
  confirmado y lo que sigue sin compilar. `PATCH` **200** en ambos; verificado por `GET`:
  #32 body 25.484 chars `updated_at=15:23:01Z`, #94 body 24.299 chars `updated_at=15:23:02Z`,
  los dos `state=open`.
- **15:24:14Z** · Cierre: ronda de 40 min (15:07:42Z → 15:47:42Z) con el encargo del feed completo y el
  frente Nox intacto (PR #3 `open`, 0 comentarios, head `6711284aa4`; cero-X HEAD `7d108e17`
  == remoto). FALLA-009 registrada por las horas estimadas de la bitácora.

- **15:25:34Z** · Parche ShinKu de Fase 2 generado sobre el clon prístino y **verificado con
  `git apply --check` → APLICA_LIMPIO** (83 líneas, 31 añadidas): `FeedLimits.kt` nuevo en
  `domain`, los dos `> 10` (`FeedScreenModel.kt` y `SourceFeedScreenModel.kt`) sobre la
  constante 25, y `feedLanguageFilter()` pasando de `"en"` al idioma del dispositivo. Árbol
  devuelto a prístino tras generar el parche (`git status --porcelain` = 0).
- **15:26:15Z** · Parche AniZen de Fase 2 generado y **verificado `git apply --check` →
  APLICA_LIMPIO** (66 líneas): `FeedLimits.kt` nuevo + guarda en los **dos** sitios que insertan
  en `FeedManageScreenModel` (`duplicate` y el movimiento entre categorías), con la guarda
  **antes** del `deleteFeedSavedSearchById` para que un destino lleno no borre la entrada. Usa la
  lista que esas funciones ya consultan ⇒ cero dependencias y cero consultas nuevas. Árbol a
  prístino (0 cambios).
- **15:26:53Z / 15:26:54Z** · **Parches publicados dentro de los issues** y corrección añadida:
  `PATCH` **200** en #32 (body 31.013 chars) y #94 (body 29.187 chars); verificado por `GET`
  (ambos `state=open`, contienen el `diff` y las marcas nuevas). En AniZen se publicó además
  «Correction #2»: `CountFeedSavedSearchGlobal.await(categoryId = 1)` **ya** admite categoría
  (`FeedSavedSearchRepository.countGlobal(categoryId)`), así que el interactor nuevo que proponía
  el snippet 2 no hace falta.
- **15:27:36Z** · `COMO-APLICAR.md` (cómo aplicar, qué toca cada parche, y lo que **no** hacen:
  esquema de categorías = Fase 1, cadenas con `%1$d`, snackbar en AniZen; y que no están
  compilados) + addendum §7 al plan. Divergencia declarada: con el parche de ShinKu el límite real
  es 25 mientras `too_many_in_feed` sigue diciendo «10» hasta la Fase 2 completa.

- **15:29-15:30Z** · **Subida de vara: lint**. Comprobado que los dos repos pasan **spotless +
  ktlint** en CI (`shinku.code.lint.gradle.kts` + `build_check.yml`; `mihon.code.lint.gradle.kts`
  + `spotless.yml` + `config/detekt`) con imports en orden alfabético estricto. Mi primera
  versión de los parches insertaba los imports fuera de orden ⇒ **habrían reventado el lint de los
  dos proyectos**. Regenerados colocando cada import en su posición ordenada (bisect sobre el
  bloque real: ShinKu posiciones 25/61 y 11/53; AniZen 13/30, 15/31 y 29/32), y re-verificados:
  `git apply --check` **OK** en los dos, árboles prístinos (0 cambios). Idiom `logcat(LogPriority.WARN) { }`
  cotejado contra usos reales (`PlayerActivity.kt:659`). Issues re-publicados (`PATCH` **200**:
  #32 → 31.291 chars `updated_at=15:30:11Z`; #94 → 29.954 chars `updated_at=15:30:12Z`) con la
  nota de lint explícita.
- **15:31:16Z** · Verificación final por `GET` de las marcas de cada issue (#32: `spotless + ktlint`,
  `git apply --check`, `MAX_SOURCES_PER_TAB`, `Symbol check`, `feedLanguageFilter`; #94:
  `spotless + ktlint`, `git apply --check`, `Correction #2`, `logcat(LogPriority.WARN)`,
  `NodeStatus`) → resultado en el chat. Un chequeo mío anterior daba `nota_lint=False` para #32
  porque probaba una marca exclusiva de AniZen (`logcat.LogPriority`): error del chequeo, no del
  issue; rehecho con las marcas correctas.

# RONDA NUEVA (T0 = 1794758872 = 16:07:52Z, fin 16:47:52Z) — biblioteca masiva + fusión (Reikai) y issues en inglés

- **16:07:52Z** · T0 fijado con `date -u +%s`. Estado de variables verificado y escrito en
  `work/edt/docs/ESTADO-VARIABLES-2026-11-15.md` (tokens vivos como `Alex17273747576777` por
  `GET /user`; cero-X HEAD `7d108e17`; edt `16c351d`; clones feed prístinos; clon Reikai nuevo
  `00206fe6`; y **detectado que el vigilante anterior murió**: última línea 15:30:16Z, sin sondeos
  a las 15:40/15:50/16:00 ⇒ los procesos de fondo no sobreviven al cambio de turno).
- **16:08Z** · Clon de Reikai (`--depth 1`, 3,8 s, 100 MB, HEAD `00206fe6ae0c6cf87e2f6114b59164ea295a6fd1`,
  Apache-2.0, ★48, «multi-source grouping and merge»).
- **16:09-16:15Z** · Investigación **en paralelo** (Reikai por un lado, ShinKu+AniZen por otro):
  grupos persistidos `merge_group.sq` con `UNIQUE(manga_id)` y FK en cascada; `auto_merge_same_title`
  por defecto **true** pero «offers to group» (nunca silencioso) vía `DuplicatePrompt.kt:32`;
  memoria de parejas rechazadas; `MergeGroupDedup.kt` como única definición de «contar una serie
  fusionada una vez»; costura de capítulos con fuente troncal (`preferredMangaSources`,
  `MergedGroupStitcher`, `ChapterGap`, `StoredStitch`); arrastre de estado fuera de la BD
  (`dedupe_merged_ids.sq` + `MergedDuplicateCarryMigration`); paquete de rendimiento
  (`baseline-profile/`, `LibraryAssembly.kt:100` memoizado, `ReikaiLibraryContent.kt:238` claves
  estables, 10 vistas, índices parciales, `libraryView.sq` con `CASE WHEN EXISTS`); 7 tests del merge.
- **16:15Z** · `write_file` ×3: `ESTADO-VARIABLES-2026-11-15.md`, `ISSUE-SHINKU-BIBLIOTECA.md`
  (7 bloques de código: `merge_group.sq` para `mangas`, `SuggestDuplicateGroup`, `MergeGroupDedup`,
  preferencias, migración 77f, módulo `baseline-profile` con perfil de scroll de biblioteca,
  memoización+claves) y `ISSUE-ANIZEN-BIBLIOTECA.md` (7 bloques: `merge_group.sq` para `animes`,
  `SuggestDuplicateGroup` rankeado con `activity_log`+`SourceHealthCache`, `MergeGroupDedup`,
  preferencias, índices parciales, `baseline-profile`, memoización+claves).
- **16:13:30Z / 16:13:31Z** · **Issues de feed traducidos a inglés puro**: fuera el TL;DR en español
  de #32 (31.291 → 30.582 chars) y #94 (29.954 → 29.149 chars); `PATCH` **200** en ambos y
  verificado por `GET` que `**ES:**` ya no aparece.
- **16:13:33Z / 16:13:32Z** · **Issues nuevos abiertos**: ShinKu **#33**
  https://github.com/Harrys-HQ/ShinKu/issues/33 y AniZen **#95**
  https://github.com/salmanbappi/AniZen/issues/95 (`POST` **201**, enlace cruzado `PATCH` **200**).
  Etiquetas: `enhancement` **sí** en AniZen, **descartada en silencio** en ShinKu (no la tiene
  definida) — registrado, no maquillado.
- **16:14-16:16Z** · **Re-verificación de mis propias afirmaciones → dos errores míos graves cazados**:
  ShinKu **sí** detecta duplicados (`mangas.sq:122-149` con CTE que excluye scanlators,
  `GetDuplicateLibraryManga`, diálogo en `BrowseSourceScreen.kt:269-278` con añadir igualmente /
  abrir / migrar) y su tabla `merged` es más rica de lo que escribí (`chapter_priority`,
  `chapter_sort_mode`, editor `EditMergedManga*`, backup); AniZen **también** tiene la tabla
  `merged` del linaje SY (`episode_priority` «the deduplication uses», `MergedAnimeReference` con
  `EPISODE_SORT_NONE/NO_DEDUPE/PRIORITY`) **y** `GetDuplicateLibraryAnime` + `DuplicateAnimeDialog`
  en `BrowseSourceScreen.kt:585` (`parent_id` es el eje de temporadas, no el de fusión).
- **16:16:03Z / 16:16:04Z** · **Corrección publicada, no silenciosa**: sección «Correction (verified
  after posting — read this first)» al principio de #33 y #95, filas de la tabla reescritas con la
  evidencia real, y propuesta **re-alcanceada** a lo que de verdad falta (agrupar en un toque desde el
  diálogo que ya existe, grupos persistidos con `UNIQUE`, memoria de parejas rechazadas, un único
  helper de recuento, arrastre de estado, paquete de rendimiento). `PATCH` **200**: #33 → 22.464
  chars, #95 → 22.559 chars; comprobado por `GET` que la sección está publicada (posición 1260 y 1431
  del body).
- **16:17Z** (acotado entre 16:16:05Z y 16:17:30Z, ambos verificados) · **Error de mi propio chequeo, cazado**: la verificación dio `Correction…=False` porque
  la cadena de prueba llevaba un paréntesis de cierre que el texto real no tiene (`… posting — read
  this first)`). Re-comprobado con `find("Correction")` + contexto: publicado correctamente en los
  dos. El fallo era del chequeo, no de la publicación.
- **16:17:19Z** · Vigilante re-arrancado cubriendo **los cinco frentes** (PR #3 + #32 + #33 + #94 + #95) cada
  10 min → `work/feed-novedades/vigilancia.log`; `LEEME.md` nuevo en `work/biblioteca-masiva/` con
  procedencia, reaplicación de clones y el índice de todas las citas verificadas.

- **16:18:54Z** · Parches de Fase 1 construidos **localmente y no publicados** (para no añadir ruido a
  los issues, que es lo que pidió el dueño): `shinku-fase1-grupos-y-dedupe.patch` (`42.sqm` con
  `merge_group`+`merge_group_manga` y sus 2 índices, `merge_group.sq` con 8 consultas,
  `MergeGroupDedup.kt`) y el de AniZen (`147.sqm`, `merge_group.sq`, `MergeGroupDedup.kt`).
  Numeración de migraciones tomada de la real: ShinKu tiene hasta `41.sqm` ⇒ 42; AniZen hasta
  `146.sqm` ⇒ 147. Ambos `git apply --check` **OK**, árboles devueltos a prístino (0 cambios).
- **16:19:20Z / 16:19:21Z** · **Segundo error mío cazado al verificar columnas reales**: AniZen **ya
  tiene** `library_favorite_index ON animes(favorite) WHERE favorite = 1` (`animes.sq:43`) **y**
  `episodes_unseen_by_anime_index ON episodes(anime_id, seen) WHERE seen = 0` (`episodes.sq:31`),
  además de `episodes_anime_id_index` (`:29`). Mi issue afirmaba que faltaba el lado de episodios no
  vistos y mi parche añadía un índice **redundante**. ShinKu igual: `migrations/13.sqm:226,228` ya
  cubren no-leídos y favoritos, así que la frase «no aplicado a todo el camino caliente» también era
  falsa.
- **16:20:19Z / 16:20:20Z** · **Corrección publicada en los dos issues** (`PATCH` **200**): #95 →
  23.433 chars (fila de índices reescrita con las tres citas reales, propuesta 5 sin índices, bloque de
  código 5 sustituido por «nothing to add (verified)», criterio de aceptación corregido, y segunda
  corrección añadida a la sección «Correction» explicando que se retira el índice redundante); #33 →
  22.582 chars (fila de índices corregida, propuesta 5 sin índices, resumen sin «partial indexes»).
  Verificado por `GET` que las afirmaciones falsas **ya no están** en ninguno de los dos bodies.
- **16:20:21Z** · **Tercer error mío, cazado**: editar a mano el cuerpo de un `git diff` para quitar el
  índice **corrompió el parche** (`error: corrupt patch at line 64`, `git apply --check` → NO) porque
  los contadores de líneas del hunk dejaron de cuadrar. Regenerado desde el clon (ficheros + `git diff
  --cached`) en vez de parchear el parche.
- **16:20:45Z** · Re-verificación: **ANIZEN APLICA_LIMPIO: sí · SHINKU APLICA_LIMPIO: sí**, árboles
  prístinos (0/0), y `grep -c '^+CREATE INDEX'` en el parche de AniZen = **2** (sólo los de
  `merge_group_anime`; el redundante fuera). 88 y 84 líneas.
- **16:21:14Z** · Cierre de la ronda: los cuatro issues publicados, en inglés, corregidos en público y
  verificados por lectura; dos parches locales verificados y **sin publicar** a propósito; vigilante de
  los cinco frentes vivo (sondeo 16:17:30Z).
