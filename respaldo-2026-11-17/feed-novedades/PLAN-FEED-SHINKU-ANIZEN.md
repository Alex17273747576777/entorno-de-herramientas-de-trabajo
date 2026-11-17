# Feed / Novedades — ShinKu ⇄ AniZen: investigación, plan y código de ejemplo

Ronda de 40 min del 2026-11-15 (T0 = 15:07:42Z). Encargo: investigar a fondo las pestañas de
novedades de **Harrys-HQ/ShinKu** y **salmanbappi/AniZen**, clonarlas, plasmar su código,
refinar la idea, hacer un plan completo y abrir un issue en cada repo pidiendo que cada uno
adopte las funciones del otro.

## 1. Entregables de esta ronda

| Qué | Dónde | Estado |
|---|---|---|
| Issue en ShinKu | https://github.com/Harrys-HQ/ShinKu/issues/32 | **abierto y verificado por API** (201 → GET: `state=open`, 23.214 chars) |
| Issue en AniZen | https://github.com/salmanbappi/AniZen/issues/94 | **abierto y verificado por API** (201 → GET: `state=open`, 22.048 chars, etiqueta `enhancement`) |
| Enlace cruzado entre los dos issues | PATCH sobre #32 → 200 | verificado |
| Cuerpo del issue de ShinKu | `ISSUE-SHINKU.md` | espejado aquí |
| Cuerpo del issue de AniZen | `ISSUE-ANIZEN.md` | espejado aquí |
| Código real de ambos subsistemas de novedades | `codigo/shinku/` (24 ficheros) · `codigo/anizen/` (29 ficheros) · 448 KB | copiado desde los clones, con su LICENSE (Apache-2.0 ambos) |
| Clones completos | `/var/tmp/feed/shinku` (110 MB) · `/var/tmp/feed/anizen` (33 MB) | **volátiles**: reaplicables con `git clone --depth 1` |

Procedencia exacta de lo copiado:
- ShinKu `main` = `043ab7d8e68e8a77752805c34969a2477195826a` (153.837 KB de repo, Kotlin, Apache-2.0, ★49, último push 2026-11-15T09:00:34Z).
- AniZen `master` = `95160a724d1147777dd1f7997fff4885a4cd9deb` (308.066 KB de repo, Kotlin + GLSL, Apache-2.0, ★202, último push 2026-11-15T05:31:25Z).
- Mis permisos en ambos: sólo lectura+issue en ShinKu (`push: false`); en AniZen la API informa `push: true` para esta cuenta, y **aun así no se empujó nada**: la regla de la casa en repos ajenos es cero push directo.

## 2. Lo que cada app tiene hoy (verificado en el código, con fichero y línea)

### ShinKu — manga, paquete `com.shinku.reader`
- **Tope duro de 10 fuentes**: `ui/browse/feed/FeedScreenModel.kt:650-652` → `hasTooManyFeeds() = countFeedSavedSearchGlobal.await() > 10`; mismo tope por fuente en `ui/browse/source/feed/SourceFeedScreenModel.kt:108`; aviso `Event.TooManyFeeds` → snackbar en `FeedTab.kt:174` con `SYMR.strings.too_many_in_feed`, cuyo texto lleva **el «10» escrito dentro de ~30 traducciones** (`i18n-sy/.../{ta,hr,zh-rTW,fil,ar,fr,…}/strings.xml`).
- **Una sola lista, sin pestañas**: `data/src/main/sqldelight/com/shinku/reader/data/feed_saved_search.sq` sólo tiene `_id, source, saved_search, global`. Sin `category`, sin `feed_order`, sin `search_type`.
- **Feed centrado en inglés por defecto**: `domain/.../exh/source/ShinKuPreferences.kt:65` → `feedLanguageFilter() = getString("pref_feed_language_filter", "en")`, y `FeedScreenModel.kt:230-246` filtra `it.lang.equals(languageFilterMode) || it.lang == "all"`. Contraste: `util/system/LocaleHelper.kt:89-91` → `getDefaultEnabledLanguages() = setOf("all", "en", Locale.getDefault().language)`, o sea que **el resto de la app sí habilita el idioma del dispositivo; el feed no**.
- **Piezas valiosas que AniZen no tiene**: `GenreFilterHelper.kt` (mapa de alias de géneros + variantes), `SuggestedTitlesScreen(.Model).kt` (modos `genre`/`for_you`, dedupe por id, `SourceHealthRepository` inyectado), `SourcePageCursor.kt` («a failed request never advances this cursor»), filas por género y «para ti» (`FeedScreenModel.kt:383` `take(10)` si biblioteca > 5; `:391` mapa de géneros offline; `:462` filas por género; `:505` búsqueda por filtro de género).
- **Sin telemetría de uso**: `activity_log`/`ActivityLog` no existen en el repo (grep = 0).
- Migraciones: `Migration { version: Float; invoke(MigrationContext) }`, registro en `core/migration/migrations/Migrations.kt`, **versión más alta hoy 75f**.

### AniZen — anime, paquete `eu.kanade.tachiyomi`
- **Multi-pestañas ya existe**: `data/.../feed_categories.sq` (`_id, name, sort`, fila de sistema `INSERT OR IGNORE … (1,'Global',0)`, `delete` rechaza `_id=1`) + `feed_saved_search.sq` con `feed_order`, `search_type`, `category` (FK con `ON DELETE CASCADE`) y `last_top_url`; consultas `selectGlobalByCategory`, `countGlobalByCategory`, `selectAllFeedWithSavedSearch`, `update`.
- **UI de pestañas**: `ui/home/FeedScreen.kt:69-115` (`visibleCategories` oculta un `Global` vacío, `rememberPagerState`, `ScrollableTabRow`, guarda contra página fuera de rango); gestión en `FeedManageScreen.kt` (491 l.) + `FeedManageScreenModel.kt` (227 l.); 14 interactores de feed en `domain/.../source/interactor/` (incluidos `ReorderFeed`, `InsertFeedSavedSearchCategory`, `UpdateFeedSavedSearch`).
- **Estadísticas ya recopiladas**: `data/.../activity_log.sq` (`source_id, feed_id, anime_id, event_type, count, timestamp`, `getCountsByPeriod`, `removeOldActivity`), `domain/.../history/model/ActivityLog.kt` (`TYPE_FETCH=1, OPEN=2, PLAY=3, COMPLETE=4, FEED_UPDATE=5`), `ActivityLogRepository` (`getCountsByPeriod(after): Map<Pair<Long,Int>, Long>`). **Ya conectadas al feed**: `ui/home/FeedScreenModel.kt:97` (`TYPE_OPEN` al pulsar) y `:203` (`TYPE_FEED_UPDATE` con `newItemsCount`); además `ui/stats/StatsScreenModel.kt` y `data/library/LibraryUpdateJob.kt`.
- **Salud de fuentes**: `domain/.../source/service/SourceHealthCache.kt`, usada por `ui/stats/InfrastructureScreenModel.kt` y `ui/browse/source/SourcesScreenModel.kt`.
- **Navegación adaptativa**: `NavLearningBrain.kt` / `NavAdaptiveEngine.kt` / `NavActionExecutor.kt`.
- **Dos huecos**: (1) **no hay tope de fuentes por pestaña** — `InsertFeedSavedSearch.await()` inserta sin contar y nada en `ui/home/*` comprueba el total; (2) **el feed no tiene dimensión de idioma** — grep de `lang`/`enabledLanguages`/`language` en `ui/home/*` sólo devuelve imports de `tachiyomi.core.common.util.lang.launchIO`.
- Migraciones: todas las de `mihon/core/migration/migrations/*` son `Migration.ALWAYS`; los cambios de esquema van por SQLDelight.

## 3. La idea refinada (qué se pide en cada issue)

Matriz de trasvase — cada app recibe lo que le falta del otro, y **las dos convergen en la misma regla de 25**:

| Función | ShinKu recibe de AniZen | AniZen recibe de ShinKu |
|---|---|---|
| Pestañas múltiples de novedades | `feed_categories` + `category`/`feed_order`/`search_type` + `ScrollableTabRow`/`HorizontalPager` + pantalla de gestión | ya lo tiene (no se toca) |
| Tope por pestaña | 10 → **25 por pestaña**, pestañas ilimitadas (constante única `FeedLimits`) | **25 por pestaña** con `countGlobalByCategory` (ya existe) antes de insertar |
| Filas del feed | ya las tiene (géneros, «para ti», sugeridos, cursor) | filas por género con alias, «para ti» desde la biblioteca, pantalla de títulos sugeridos, `SourcePageCursor` que no avanza si falla la petición, dedupe con `last_top_url` |
| Idiomas |默认 del dispositivo en vez de `"en"`; idioma por pestaña; pestaña **opcional** «explorar otros idiomas»; interruptor «quedarme en mi idioma» | dimensión de idioma en las pestañas + pestaña opcional de exploración (columnas aditivas `lang`/`explore` en `feed_categories`) |
| Sugerencias por escaneo + estadísticas | tabla nueva `feed_activity` con la **misma numeración de eventos** que AniZen, e interactor `SuggestFeedTabs` (biblioteca ×3, uso ×2, pinneado +5, idioma del dispositivo +4, salud de fuentes) | `SuggestFeedTabs` sobre `activity_log` ya existente (OPEN ×2, PLAY ×4, COMPLETE ×6, FEED_UPDATE ×0.5, FETCH ×0.25) + `SourceHealthCache` (sano +3 / roto −4) + idiomas de la biblioteca ×3 + locale ×8 |

Decisiones de diseño que se explican en los issues:
1. **Mismos nombres de tabla y columna en las dos apps** (`feed_categories`, `category`, `feed_order`, `search_type`, y la numeración `Popular=0/Latest=1/SavedSearch=2` que AniZen ya usa) → los backups de feed son intercambiables y el coste mental de mantenerlas es uno, no dos.
2. **25 por pestaña y no 25 en total**: la unidad útil es la pestaña; un lector en 4 idiomas quiere 4×25, no 25 repartidos. Se acompaña de `MAX_CONCURRENT_FETCHES_PER_TAB = 6` para que el refresco siga acotado.
3. **El número va como placeholder `%1$d`** en la cadena: si no, ~30 traducciones de ShinKu seguirían diciendo «10» después del cambio.
4. **«Explorar otros idiomas» es opt-in y apagado por defecto**: el usuario decide entre quedarse en su idioma o asomarse; no se le cuelan fuentes que no entiende.
5. **Sugerencias 100 % locales**: biblioteca, registro de actividad, pinneados/última fuente, idiomas habilitados, salud de fuentes, locale. Ninguna llamada de red nueva para construirlas.

## 4. Plan completo (fases, en el orden en que se ofrece el PR)

**Fase 0 — Acuerdo (0,5 día).** Los mantenedores confirman: 25 por pestaña, categorías en ShinKu con `_id=1` = `Global`, columnas aditivas en AniZen, y si quieren el registro de actividad nuevo en ShinKu (o prefieren derivar las sugerencias sólo de biblioteca + salud de fuentes).

**Fase 1 — Esquema y migración.**
- ShinKu: `feed_categories.sq` nuevo; `ALTER TABLE feed_saved_search ADD COLUMN category/feed_order/search_type`; consultas por categoría; `SetupFeedCategoriesMigration` en versión **76f** registrada en `Migrations.kt`; subir la versión de esquema SQLDelight. Migración idempotente y con la categoría de sistema preinsertada.
- AniZen: `ALTER TABLE feed_categories ADD COLUMN lang TEXT DEFAULT 'all'` y `explore INTEGER DEFAULT 0` (aditivas ⇒ installs y backups actuales siguen igual).
- **Backup/restore** en las dos: serializar las columnas nuevas; los backups viejos restauran a categoría 1.

**Fase 2 — Tope y cadenas.** `FeedLimits.MAX_SOURCES_PER_TAB = 25` en `domain` de cada app; en ShinKu sustituir `hasTooManyFeeds()` (`FeedScreenModel:650`) y el de `SourceFeedScreenModel:108` por un conteo **por categoría**; en AniZen añadir `isTabFull(categoryId)` con `countGlobalByCategory` **antes** de `insertFeedSavedSearch.await()`; cadenas con `%1$d` + las 4 nuevas (`feed_tab_explore_languages`, `feed_tab_suggested_for_language`, `feed_action_stay_in_my_language`, `feed_tab_full`).

**Fase 3 — Idioma.** ShinKu: `feedLanguageFilter()` por defecto = locale del dispositivo (o `"all"`), idioma por pestaña desde `feed_categories.lang`, y `getFilteredCatalogueSources()` recibiendo el idioma de la pestaña activa. AniZen: misma columna `lang` por categoría + filtro al construir las filas.

**Fase 4 — Estadísticas y sugerencias.** ShinKu: `feed_activity.sq` (misma forma y numeración que `activity_log.sq` de AniZen) + `LogFeedActivity` en los puntos donde ya se navega (apertura de manga, refresco de fila) + purga `removeOldActivity` enganchada a un job existente. Las dos: `SuggestFeedTabs` (código de ejemplo en los issues) que devuelve ≤ 6 pestañas de ≤ 25 fuentes, con la pestaña `explore` sólo si el interruptor está activo.

**Fase 5 — Filas de ShinKu en AniZen.** `FeedGenreHelper` (alias de anime: mecha, isekai, shounen/shoujo/seinen/josei, idol/music…), `SourcePageCursor` por entrada de feed + `last_top_url` para dedupe, `buildRows(category, entries, library)` con `Featured` / `ForYou` (sólo si biblioteca > 5) / `Genre` (mínimo 3 títulos distintos), y pantalla de títulos sugeridos reutilizando `GetRemoteAnime.QUERY_LATEST`/`QUERY_POPULAR` como ya hace `FeedTab.onSeeAllClick`.

**Fase 6 — Pruebas.** Unitarias: conteo por categoría (24 acepta, 25 rechaza), migración idempotente dos veces, backup viejo → categoría 1, cursor que no avanza con excepción, `SuggestFeedTabs` con fixture de `activity_log`/`feed_activity` (empate de puntuación ⇒ orden estable), pestaña `explore` ausente con el interruptor apagado. De instrumento/UI: pager con 1 y con 6 pestañas, `Global` vacío oculto en AniZen.

**Fase 7 — Traducciones.** Rellenar el placeholder en las ~30 locales de `i18n-sy` (ShinKu) y en `i18n-sy`/`i18n-ank`/`i18n-kmk` (AniZen); hasta que estén, se usa la cadena base en lugar de un número falso.

## 5. Lo NO verificado (declarado también en los issues)

- **El código de ejemplo no está compilado ni ejecutado**: este entorno no tiene Android SDK/Gradle ni `kotlinc` (comprobado: `which kotlinc` → ausente). Las firmas se ajustaron leyendo las fuentes reales, no construyéndolas.
- `SourceHealthCache.isHealthy(sourceId)` es la forma inferida de sus dos usos; el nombre real puede diferir.
- No se ejecutó ninguna migración SQLDelight real ni un ciclo de backup/restore.
- El vocabulario de géneros de anime del mapa de alias es ilustrativo: hay que cotejarlo con los géneros que emiten las fuentes instaladas.
- La etiqueta `enhancement` **no se aplicó en ShinKu** (ese repo no la tiene definida; la API la descartó en silencio: `labels=[]`). En AniZen sí (`labels=['enhancement']`).
- No se comprobó si alguno de los dos proyectos ya tiene planeada esta función; los issues lo dicen explícitamente.

## 6. Cabos abiertos

1. Respuesta de los mantenedores en #32 y #94 (vigilada en background por `vigilar-frentes.sh`).
2. Si aceptan, PR en tres commits por repo (esquema+migración / tope+cadenas / sugerencias+UI).
3. Frente Nox sin cambios en esta ronda: PR #3 `open`, 0 comentarios, head `6711284aa4`; cero-X HEAD `7d108e17` == remoto.
4. Pendiente del dueño: ejecución de la corrección de `serialize-javascript` (necesita entorno con Gradle/Kotlin-JS).

## 7. Addendum (15:27:36Z): la Fase 2 ya existe como parche verificado

| Parche | Base | `git apply --check` | Contenido |
|---|---|---|---|
| `parches/shinku-fase2-tope25-e-idioma.patch` (83 l.) | `043ab7d8` | **aplica limpio** | `FeedLimits` nuevo + los dos `> 10` → `>= 25` + `feedLanguageFilter()` al idioma del dispositivo |
| `parches/anizen-fase2-tope25-por-pestana.patch` (66 l.) | `95160a72` | **aplica limpio** | `FeedLimits` nuevo + guarda de pestaña llena en los dos sitios que insertan (`duplicate` y el movimiento entre categorías, con la guarda **antes** del `delete`) |

Los dos están publicados dentro de los issues (#32 y #94) en bloques `diff`, junto con la
declaración de lo que **no** hacen (esquema de categorías, cadenas con `%1`, snackbar en
AniZen) y de que **no están compilados**. Detalle en `COMO-APLICAR.md`.

Corrección adicional detectada al construir el parche de AniZen: `CountFeedSavedSearchGlobal.await(categoryId = 1)`
**ya admite categoría** sobre `FeedSavedSearchRepository.countGlobal(categoryId)`, y las dos
funciones que insertan ya tienen la lista de la pestaña en memoria ⇒ la guarda no necesita ningún
interactor nuevo ni ninguna consulta extra. Corregido públicamente en el issue («Correction #2»).
