# Verificación de símbolos del código de ejemplo (ShinKu ⇄ AniZen)

Cada símbolo usado en el código de ejemplo de los issues se comprobó contra las fuentes clonadas
(`shinku` @ `043ab7d8`, `anizen` @ `95160a72`). Lo que no existía o tenía otra firma se **corrigió
en los issues** y se dejó constancia pública de la corrección. Nada de esto está compilado: es
verificación de existencia y firma por lectura, no por build (`kotlinc` ausente en este entorno).

## ShinKu (`com.shinku.reader`)

| Símbolo usado | Veredicto | Evidencia |
|---|---|---|
| `CountFeedSavedSearchGlobal` | **existe** | `domain/.../source/interactor/CountFeedSavedSearchGlobal.kt` |
| `CountFeedSavedSearchBySourceId` | **existe** | `domain/.../source/interactor/CountFeedSavedSearchBySourceId.kt` |
| `sourceManager.getVisibleCatalogueSources()` | **existe** | `source/AndroidSourceManager.kt`, `domain/.../source/service/SourceManager.kt` |
| `sourceManager.getCatalogueSources()` | **existe** | idem |
| `GetSavedSearchBySourceId` | **existe** | `domain/.../source/interactor/GetSavedSearchBySourceId.kt` (y variante `…BySourceIdFeed.kt`) |
| `GetLibraryManga.await()` | **existe**, devuelve `List<LibraryManga>` | `domain/.../manga/interactor/GetLibraryManga.kt:17-19` |
| `LibraryManga.source` | **NO existe así**: es `LibraryManga.manga.source` (`val id = manga.id`) | `domain/.../library/model/LibraryManga.kt:5-15` → **corregido en el issue** |
| `withIOContext { }` | **existe** | `core/common/src/main/kotlin/com/shinku/reader/core/common/util/lang/CoroutinesExtensions.kt:60` |
| `MigrationContext.get<T>()` | **existe**, pero es `class MigrationContext(val dryrun: Boolean)` con `inline fun <reified T> get(): T?` (Injekt), no una interfaz | `app/.../core/migration/MigrationContext.kt:5-9` → aclarado en el issue |
| `Migration { version: Float; invoke(MigrationContext): Boolean }` | **existe** | `core/migration/Migration.kt`, ejemplo real `RemoveShortLibraryUpdatesMigration.kt` (versión 22f); máxima hoy **75f** |
| `SourceHealthRepository` | **existe**: `subscribeAll()`, `getBySourceId(Long): SourceHealth?`, `updateStats(...)`, `resetStats(...)` | `domain/.../source/repository/SourceHealthRepository.kt:6-11` |
| `SourceHealth` | **existe**: `sourceId, lastSuccess, lastFailure, failureCount, successCount, avgLatency, lastError` + `isFailingNow` | `domain/.../source/model/SourceHealth.kt:5-15` → añadido como señal real en el issue |
| `FeedSavedSearchCategoryRepository` / `insertSystemGlobal()` | **nuevos** (propuesta): no existen en el repo | marcado como fichero nuevo en el issue |
| `preferenceStore.getString/getBoolean` | **existe** | `domain/.../exh/source/ShinKuPreferences.kt:63-67` |
| `LocaleHelper.getDefaultEnabledLanguages()` | **existe** = `setOf("all","en",Locale.getDefault().language)` | `util/system/LocaleHelper.kt:89-91` |
| `SYMR.strings.too_many_in_feed` | **existe** en ~30 locales con el «10» literal dentro | `i18n-sy/src/commonMain/moko-resources/*/strings.xml` |

## AniZen (`eu.kanade.tachiyomi` / `tachiyomi.domain`)

| Símbolo usado | Veredicto | Evidencia |
|---|---|---|
| `CountFeedSavedSearchGlobal` | **existe** | `domain/.../source/interactor/CountFeedSavedSearchGlobal.kt` |
| `CountFeedSavedSearchGlobalByCategory` | **no existe** (propuesta): la consulta `countGlobalByCategory` sí existe en SQL | `data/.../feed_saved_search.sq`; ya se declaraba como envoltorio nuevo |
| `InsertFeedSavedSearch.await / awaitAll` | **existe** | `domain/.../source/interactor/InsertFeedSavedSearch.kt` |
| `InsertFeedSavedSearchCategory`, `UpdateFeedSavedSearchCategory`, `ReorderFeed` | **existen** | `domain/.../source/interactor/*.kt` |
| `FeedSavedSearch(id, source, savedSearch, global, feedOrder, type, category, lastTopUrl)` | **existe**, campos exactos | `domain/.../source/model/FeedSavedSearch.kt` |
| `FeedSavedSearchCategory(id, name, order)` | **existe** | `domain/.../source/model/FeedSavedSearchCategory.kt` |
| `ActivityLogRepository.getCountsByPeriod(after: Date): Map<Pair<Long,Int>, Long>` | **existe** | `domain/.../history/repository/ActivityLogRepository.kt` |
| `ActivityLog.TYPE_FETCH/OPEN/PLAY/COMPLETE/FEED_UPDATE = 1..5` | **existe** | `domain/.../history/model/ActivityLog.kt` |
| `GetLibraryAnime.await()` | **existe**, devuelve `List<LibraryAnime>` | `domain/.../anime/interactor/GetLibraryAnime.kt:14-16` |
| `LibraryAnime.source` | **NO existe así**: es `LibraryAnime.anime.source` | `domain/.../library/model/LibraryAnime.kt:5-7` → **corregido en el issue** |
| `SourceHealthCache.isHealthy(Long)` | **NO existe**: es un `object` con `getStatus(Long): NodeStatus` y `latencyMap`; `NodeStatus = OPERATIONAL \| DEGRADED \| CRITICAL \| OFFLINE` (por defecto `OPERATIONAL` si desconocido) | `domain/.../source/service/SourceHealthCache.kt:12-28`, `core/common/.../network/model/InfrastructureModels.kt:19-24` → **corregido en el issue** |
| `sourceManager.getCatalogueSources()` | **existe** | `domain/.../source/service/SourceManager.kt` |
| `logActivity.await(sourceId, eventType, feedId, animeId, count)` | **existe** y ya se usa en el feed | `ui/home/FeedScreenModel.kt:97` y `:203` |
| Migraciones de app | todas `Migration.ALWAYS`; los cambios de esquema van por SQLDelight | `mihon/core/migration/migrations/Migrations.kt` |

## Correcciones aplicadas a los issues (y declaradas en ellos)

1. **AniZen #94**: `SourceHealthCache` tratado como singleton (`object`) con
   `getStatus(sourceId)` comparado contra `NodeStatus`, en vez de un `isHealthy()` inventado e
   inyectado; `libraryLang` construido con `LibraryAnime.anime.source`; import de `NodeStatus`.
2. **ShinKu #32**: `libraryLang` construido con `LibraryManga.manga.source`; `MigrationContext`
   descrito como clase con `inline fun <reified T> get()`; `SourceHealth.isFailingNow` y
   `getBySourceId()` añadidos como señal real de salud; marcado `FeedSavedSearchCategoryRepository`
   como fichero nuevo de la propuesta.
