## TL;DR

Proposal for the Feed tab: adopt ShinKu's feed row format (genre rows, "for you" from the library, a suggested-titles screen, and a pagination cursor that never advances on a failed request) on top of the category pager you **already ship**; cap sources at **25 per tab** (we found no cap today) with unlimited tabs; and use the `activity_log` you already write to **suggest tabs in the user's own language**, plus an optional "explore other languages" tab. Sample code is written against your real stack at the commit below. It is **not compiled** — a starting point; happy to send a PR.

---

## What was actually read

Full source cloned and read at `master` = `95160a724d1147777dd1f7997fff4885a4cd9deb` (Apache-2.0). Every claim below cites a real file/line from that commit.

**What AniZen already has (and ShinKu does not):**

| Capability | File |
|---|---|
| Feed categories (multi-tab) | `data/src/main/sqldelight/tachiyomi/data/feed_categories.sq` — `_id, name, sort`, system row `INSERT OR IGNORE … (1, 'Global', 0)`, `delete` refuses `_id = 1` |
| Per-entry ordering, type and tab | `data/src/main/sqldelight/tachiyomi/data/feed_saved_search.sq` — `feed_order`, `search_type`, `category` (FK → `feed_categories`, `ON DELETE CASCADE`), `last_top_url`; queries `selectAllGlobal`, `selectGlobalByCategory`, `countGlobalByCategory`, `selectAllFeedWithSavedSearch`, `update` |
| Domain model | `domain/src/main/java/tachiyomi/domain/source/model/FeedSavedSearch.kt` (`Type.Popular=0 / Latest=1 / SavedSearch=2`), `FeedSavedSearchCategory.kt`, `FeedSavedSearchUpdate.kt` |
| Interactors | `domain/.../source/interactor/`: `GetFeedSavedSearchCategories`, `InsertFeedSavedSearchCategory`, `UpdateFeedSavedSearchCategory`, `DeleteFeedSavedSearchCategory`, `ReorderFeed`, `UpdateFeedSavedSearch`, `CountFeedSavedSearchGlobal`, `CountFeedSavedSearchBySourceId`, … |
| Tab UI | `app/src/main/java/eu/kanade/tachiyomi/ui/home/FeedScreen.kt:69-115` — `visibleCategories` (hides an empty `Global`), `rememberPagerState`, `ScrollableTabRow`, guard against out-of-range page |
| Tab management | `ui/home/FeedManageScreen.kt` (491 lines) + `FeedManageScreenModel.kt` (227 lines) |
| Usage statistics | `data/.../activity_log.sq` (`source_id, feed_id, anime_id, event_type, count, timestamp`, `getCountsByPeriod`, `removeOldActivity`), `domain/.../history/model/ActivityLog.kt` (`TYPE_FETCH=1, OPEN=2, PLAY=3, COMPLETE=4, FEED_UPDATE=5`), `ActivityLogRepository` |
| Statistics already wired into the feed | `ui/home/FeedScreenModel.kt:97` (`logActivity.await(source, TYPE_OPEN, feedId, animeId)`) and `:203` (`TYPE_FEED_UPDATE` with `newItemsCount`); also `ui/stats/StatsScreenModel.kt`, `data/library/LibraryUpdateJob.kt` |
| Source health | `domain/src/main/java/tachiyomi/domain/source/service/SourceHealthCache.kt`, used by `ui/stats/InfrastructureScreenModel.kt` and `ui/browse/source/SourcesScreenModel.kt` |
| Adaptive navigation | `ui/home/NavLearningBrain.kt`, `NavAdaptiveEngine.kt`, `NavActionExecutor.kt` |

**What ShinKu has and AniZen does not** (read at ShinKu `main` = `043ab7d8e68e8a77752805c34969a2477195826a`):

| Piece | File | Why it matters for the feed |
|---|---|---|
| Genre alias map + matching | `ui/browse/feed/GenreFilterHelper.kt` | normalises `sci-fi / science fiction / scifi`, `isekai / reincarnation / transmigration`, etc., so a genre row works across sources that spell genres differently |
| Genre rows, offline genre map | `ui/browse/feed/FeedScreenModel.kt:391, :462` | rows built per genre, `take(10)` each, with an offline fallback map |
| "For you" from the library | `FeedScreenModel.kt:383` | `if (libraryManga.size > 5) libraryManga.filter { it !in featured }.take(10)` |
| Suggested titles screen | `ui/browse/feed/SuggestedTitlesScreen.kt` + `SuggestedTitlesScreenModel.kt` | modes `genre` / `for_you`, dedupe by id, `hasMore` only for those modes, `SourceHealthRepository` injected |
| Pagination cursor that never lies | `ui/browse/feed/SourcePageCursor.kt` | "A failed request never advances this cursor. Seed titles are deduplicated against page one." |
| Genre search through source filters | `FeedScreenModel.kt:505` | `source.getSearchManga(1, "", filterList).mangas.take(10)` |

**Two gaps found in AniZen:**

1. **No per-tab source cap.** `InsertFeedSavedSearch.await(feedSavedSearch)` inserts unconditionally (`domain/.../source/interactor/InsertFeedSavedSearch.kt`), and nothing in `ui/home/*` counts before inserting. A tab can grow without bound, and the feed fetches every entry of every visible category (`FeedScreenModel.setupFeedSubscriptions`), so a huge tab is a real cost in network and memory. `countGlobalByCategory` already exists in SQL — the guard is one call away. ShinKu caps at 10 (`FeedScreenModel.kt:650-652`), which is too small; **25 per tab with unlimited tabs** is the balance this proposal suggests for both apps.

2. **The feed has no language dimension.** `grep` for `lang` / `enabledLanguages` / `language` across `ui/home/*` returns only unrelated `tachiyomi.core.common.util.lang.launchIO` imports. Tabs are language-agnostic, so a user who installs Japanese, Spanish and English sources gets one mixed firehose, and nothing suggests organising by the language they actually watch.

## Proposal

**A. ShinKu-style rows inside the existing category pager.** Keep `feed_categories` + `HorizontalPager` exactly as they are, and enrich each page with: genre rows (alias-normalised), a "for you" row derived from the library, a suggested-titles screen reachable from a row header, and a per-source page cursor that does not advance on failure. Use `last_top_url` (already a column) for the dedupe that ShinKu does in memory.

**B. 25 sources per tab, unlimited tabs.** One shared constant, checked per category with the existing `countGlobalByCategory` before insert, message carries the number as a placeholder.

**C. Language-aware tab suggestions from `activity_log`.** Score sources with the data you already write (`TYPE_OPEN`, `TYPE_PLAY`, `TYPE_COMPLETE`, `TYPE_FEED_UPDATE` via `getCountsByPeriod`), plus `SourceHealthCache` and library composition; group by source language; offer one tab per top language of the user and an **opt-in** "explore other languages" tab. Nothing new has to be collected — the log already exists.

**D. Do not disturb what works.** `PanoramaMode`, `NavLearningBrain` / `NavAdaptiveEngine`, the `Global` system category and the current backup format stay intact; category 1 keeps meaning "everything".

## Sample code

Written against the commit above and your module layout (`eu.kanade.tachiyomi` / `tachiyomi.domain` / `tachiyomi.data`, Injekt, Voyager, moko-resources `SYMR`/`MR`). **Not compiled, not run on a device.**

<details>
<summary><b>1. One shared cap — <code>domain/.../source/service/FeedLimits.kt</code> (new)</b></summary>

```kotlin
package tachiyomi.domain.source.service

/**
 * Feed composition limits.
 *
 * AniZen had no cap; ShinKu caps the whole feed at 10. Both extremes are wrong for a
 * multi-tab feed: the useful unit is the tab. 25 sources per tab keeps a refresh bounded
 * (see MAX_CONCURRENT_FETCHES_PER_TAB) while the number of tabs stays unlimited.
 */
object FeedLimits {
    const val MAX_SOURCES_PER_TAB: Int = 25
    const val MAX_CONCURRENT_FETCHES_PER_TAB: Int = 6
}
```
</details>

<details>
<summary><b>2. Guard before inserting — <code>ui/home/FeedManageScreenModel.kt</code></b></summary>

```kotlin
import tachiyomi.domain.source.interactor.CountFeedSavedSearchGlobalByCategory
import tachiyomi.domain.source.service.FeedLimits

class FeedManageScreenModel(
    // … existing dependencies …
    private val countFeedSavedSearchGlobalByCategory:
        CountFeedSavedSearchGlobalByCategory = Injekt.get(),
) : StateScreenModel<FeedManageScreenModel.State>(State()) {

    /** True when the tab is full; the UI shows the snackbar, the insert never happens. */
    suspend fun isTabFull(categoryId: Long): Boolean =
        countFeedSavedSearchGlobalByCategory.await(categoryId) >= FeedLimits.MAX_SOURCES_PER_TAB

    suspend fun addToFeed(sourceId: Long, savedSearchId: Long?, type: Int, categoryId: Long) {
        if (isTabFull(categoryId)) {
            mutableState.update { it.copy(event = Event.TabFull(FeedLimits.MAX_SOURCES_PER_TAB)) }
            return
        }
        insertFeedSavedSearch.await(
            FeedSavedSearch(
                id = 0,
                source = sourceId,
                savedSearch = savedSearchId,
                global = true,
                feedOrder = 0,               // the insert query assigns MAX(feed_order)+1
                type = type,
                category = categoryId,
            ),
        )
    }
}
```

The `CountFeedSavedSearchGlobalByCategory` interactor is a two-line wrapper over the
`countGlobalByCategory` query that already exists in `feed_saved_search.sq`, following the
shape of `CountFeedSavedSearchGlobal`.
</details>

<details>
<summary><b>3. Strings — <code>i18n-sy</code> (moko-resources), number as placeholder</b></summary>

```xml
<string name="feed_tab_full">This feed tab is full: up to %1$d sources per tab. Create another tab to add more.</string>
<string name="feed_tab_explore_languages">Explore other languages</string>
<string name="feed_tab_suggested_for_language">Suggested: %1$s</string>
<string name="feed_action_stay_in_my_language">Stay in my language</string>
<string name="feed_row_for_you">For you</string>
<string name="feed_row_see_all_titles">See all titles</string>
```
</details>

<details>
<summary><b>4. Genre alias helper ported to anime — <code>ui/home/FeedGenreHelper.kt</code> (new)</b></summary>

ShinKu's map (`GenreFilterHelper.GENRE_ALIASES`) is manga-flavoured; the anime rows need their
own aliases. Same interface, different vocabulary:

```kotlin
package eu.kanade.tachiyomi.ui.home

object FeedGenreHelper {

    private val GENRE_ALIASES = mapOf(
        "mecha" to listOf("mecha", "mech", "robot", "super robot"),
        "isekai" to listOf("isekai", "reincarnation", "another world", "transmigration"),
        "sci-fi" to listOf("sci-fi", "science fiction", "scifi", "sci fi"),
        "slice of life" to listOf("slice of life", "slice-of-life", "iyashikei", "daily life"),
        "shounen" to listOf("shounen", "shonen"),
        "shoujo" to listOf("shoujo", "shojo"),
        "seinen" to listOf("seinen"),
        "josei" to listOf("josei"),
        "sports" to listOf("sports", "sport", "tournament"),
        "music" to listOf("music", "musical", "idol"),
        "harem" to listOf("harem", "reverse harem"),
        "thriller" to listOf("thriller", "crime", "suspense"),
        "horror" to listOf("horror", "gore"),
        "drama" to listOf("drama", "melodrama"),
        "action" to listOf("action", "fighting", "action & adventure"),
        "adventure" to listOf("adventure", "quest"),
        "fantasy" to listOf("fantasy", "magic", "high fantasy", "dark fantasy"),
        "romance" to listOf("romance", "romantic"),
        "comedy" to listOf("comedy", "humor", "gag"),
        "mystery" to listOf("mystery", "detective"),
    )

    fun variants(genre: String): List<String> {
        val lower = genre.trim().lowercase()
        return (listOf(lower) + GENRE_ALIASES[lower].orEmpty()).distinct()
    }

    fun matches(genreOfAnime: String, target: String): Boolean {
        val lower = genreOfAnime.trim().lowercase()
        return variants(target).any { lower == it || lower.contains(it) }
    }
}
```
</details>

<details>
<summary><b>5. Page cursor that never advances on failure — <code>ui/home/SourcePageCursor.kt</code> (new)</b></summary>

Ported as-is from ShinKu (`ui/browse/feed/SourcePageCursor.kt`), where it is documented as
"A failed request never advances this cursor. Seed titles are deduplicated against page one."

```kotlin
package eu.kanade.tachiyomi.ui.home

internal class SourcePageCursor {
    var nextPage = 1
        private set
    var hasMore = true

    fun accept(hasNextPage: Boolean) {
        check(hasMore)
        nextPage++
        hasMore = hasNextPage
    }
}
```

In `FeedScreenModel`, keep one cursor per feed entry (`Map<Long, SourcePageCursor>` keyed by
`FeedSavedSearch.id`) and pair it with the `last_top_url` column you already persist, so a
refresh after a failure re-requests the same page instead of skipping it.
</details>

<details>
<summary><b>6. Rows: "for you" + genre rows inside a category page — <code>ui/home/FeedScreenModel.kt</code></b></summary>

```kotlin
private fun buildRows(
    category: FeedSavedSearchCategory,
    entries: List<FeedItem>,
    library: List<Anime>,
): ImmutableList<FeedRow> {
    val featured = entries.flatMap { it.items }.take(10).toImmutableList()

    // ShinKu's rule: only build a "for you" row when the library is big enough to mean something.
    val forYou = if (library.size > 5) {
        library.filter { anime -> featured.none { it.animeId == anime.id } }.take(10)
    } else {
        emptyList()
    }

    val genreRows = entries
        .flatMap { item -> item.items.map { anime -> item.source to anime } }
        .flatMap { (source, anime) -> anime.genre.orEmpty().map { Triple(source, anime, it) } }
        .groupBy({ it.third.lowercase() }, { it.second })
        .filter { (_, list) -> list.distinctBy { it.id }.size >= 3 }
        .map { (genre, list) ->
            FeedRow.Genre(
                genre = genre,
                items = list.distinctBy { it.id }.take(FeedLimits.MAX_CONCURRENT_FETCHES_PER_TAB * 2)
                    .toImmutableList(),
            )
        }
        .sortedByDescending { it.items.size }

    return (
        listOf(FeedRow.Featured(featured)) +
            (if (forYou.isNotEmpty()) listOf(FeedRow.ForYou(forYou.toImmutableList())) else emptyList()) +
            genreRows
        ).toImmutableList()
}
```

`FeedRow` is a small sealed interface (`Featured`, `ForYou`, `Genre`) rendered by the existing
`FeedScreen` pager page; the "see all" header of a genre row pushes a suggested-titles screen
(the equivalent of ShinKu's `SuggestedTitlesScreen`, using `GetRemoteAnime.QUERY_LATEST` /
`QUERY_POPULAR` as `FeedTab.onSeeAllClick` already does).
</details>

<details>
<summary><b>7. Language-aware tab suggestions from <code>activity_log</code> — <code>domain/.../source/interactor/SuggestFeedTabs.kt</code> (new)</b></summary>

```kotlin
package tachiyomi.domain.source.interactor

import tachiyomi.domain.anime.interactor.GetLibraryAnime
import tachiyomi.domain.history.model.ActivityLog
import tachiyomi.domain.history.repository.ActivityLogRepository
import tachiyomi.domain.source.service.FeedLimits
import eu.kanade.tachiyomi.network.model.NodeStatus
import tachiyomi.domain.source.service.SourceHealthCache   // object singleton
import tachiyomi.domain.source.service.SourceManager
import java.util.Calendar
import java.util.Date

data class SuggestedFeedTab(
    val lang: String,
    val label: String,
    val sources: List<Long>,          // <= FeedLimits.MAX_SOURCES_PER_TAB
    val explore: Boolean = false,
)

/**
 * Ranks the tabs the feed should offer, using only data AniZen already stores:
 * activity_log (OPEN/PLAY/COMPLETE/FEED_UPDATE), SourceHealthCache, the library and the
 * device locale. No new collection, no network.
 */
class SuggestFeedTabs(
    private val activityLogRepository: ActivityLogRepository,
    private val sourceManager: SourceManager,
    private val getLibraryAnime: GetLibraryAnime,
    // SourceHealthCache is an `object` in your codebase: no injection, just call it.
    private val deviceLanguage: () -> String = { java.util.Locale.getDefault().language },
) {

    suspend fun await(maxTabs: Int = 6, exploreOtherLanguages: Boolean = false): List<SuggestedFeedTab> {
        val since = Calendar.getInstance().apply { add(Calendar.DAY_OF_YEAR, -30) }.time

        // weighted usage per source, from the log you already write in FeedScreenModel
        val counts: Map<Pair<Long, Int>, Long> = activityLogRepository.getCountsByPeriod(since)
        val weight = mapOf(
            ActivityLog.TYPE_OPEN to 2.0,
            ActivityLog.TYPE_PLAY to 4.0,
            ActivityLog.TYPE_COMPLETE to 6.0,
            ActivityLog.TYPE_FEED_UPDATE to 0.5,
            ActivityLog.TYPE_FETCH to 0.25,
        )
        val usage: Map<Long, Double> = counts.entries
            .groupBy({ it.key.first }, { (it.key.second to it.value) })
            .mapValues { (_, pairs) -> pairs.sumOf { (type, total) -> (weight[type] ?: 0.0) * total } }

        // LibraryAnime wraps the anime: the source id lives on LibraryAnime.anime.source
        val libraryLang: Map<String, Int> = getLibraryAnime.await()
            .mapNotNull { libraryAnime -> sourceManager.get(libraryAnime.anime.source)?.lang }
            .groupingBy { it }.eachCount()

        val device = deviceLanguage()
        val scored = sourceManager.getCatalogueSources().map { source ->
            source to (
                (usage[source.id] ?: 0.0) +
                    (libraryLang[source.lang] ?: 0) * 3.0 +
                    (if (source.lang == device) 8.0 else 0.0) +
                    // SourceHealthCache.getStatus returns NodeStatus and defaults to OPERATIONAL
                    // when the source has never been probed, so only a real failure penalises.
                    when (SourceHealthCache.getStatus(source.id)) {
                        NodeStatus.OPERATIONAL -> 3.0
                        NodeStatus.DEGRADED -> 0.0
                        NodeStatus.CRITICAL -> -4.0
                        NodeStatus.OFFLINE -> -6.0
                    }
                )
        }

        val myLanguages = (libraryLang.keys + device).distinct()

        val mine = scored
            .filter { (source, _) -> source.lang in myLanguages }
            .groupBy({ it.first.lang }, { it })
            .map { (lang, list) ->
                SuggestedFeedTab(
                    lang = lang,
                    label = lang,
                    sources = list.sortedByDescending { it.second }
                        .take(FeedLimits.MAX_SOURCES_PER_TAB)
                        .map { it.first.id },
                )
            }
            .filter { it.sources.isNotEmpty() }
            .sortedByDescending { tab -> tab.sources.sumOf { usage[it] ?: 0.0 } }
            .take(maxTabs)

        if (!exploreOtherLanguages) return mine

        val others = scored
            .filter { (source, _) -> source.lang !in myLanguages && source.lang != "all" }
            .sortedByDescending { it.second }
            .take(FeedLimits.MAX_SOURCES_PER_TAB)
            .map { it.first.id }

        return if (others.isEmpty()) mine else mine + SuggestedFeedTab(
            lang = "all",
            label = "explore",
            sources = others,
            explore = true,
        )
    }
}
```

Applying a suggestion = `InsertFeedSavedSearchCategory.await(name)` once, then
`InsertFeedSavedSearch.awaitAll(...)` for its sources, both of which already exist. The
`explore` flag can live in the category name or in a new `explore INTEGER` column on
`feed_categories` (ShinKu's mirror proposal adds `lang` and `explore` there, so the two
schemas can converge).
</details>

<details>
<summary><b>8. Optional columns on <code>feed_categories.sq</code> (converging with ShinKu)</b></summary>

```sql
ALTER TABLE feed_categories ADD COLUMN lang TEXT NOT NULL DEFAULT 'all';
ALTER TABLE feed_categories ADD COLUMN explore INTEGER AS Boolean NOT NULL DEFAULT 0;
```

Both are additive with defaults, so existing installs and existing backups keep working: every
current category becomes `lang = 'all'`, `explore = 0`, i.e. exactly today's behaviour.
</details>

## Acceptance criteria

- [ ] A tab refuses the 26th source with a message that states 25; the number of tabs is not limited.
- [ ] The check uses the existing `countGlobalByCategory` query and happens **before** the insert.
- [ ] Genre rows, "for you" and the suggested-titles screen appear inside each category page, without changing `PanoramaMode` or the adaptive navigation.
- [ ] A failed fetch does not advance the page cursor, and `last_top_url` is used for dedupe.
- [ ] Suggestions come from `activity_log` + `SourceHealthCache` + library + device locale; no new network call, no new telemetry.
- [ ] "Explore other languages" is opt-in and off by default.
- [ ] Category `_id = 1` (`Global`) still cannot be deleted and still means "everything".
- [ ] Backup/restore round-trips the new columns.

## What we did NOT verify (so nobody inherits a false positive)

- The sample code was **not compiled and not run**: our environment has no Android SDK/Gradle and no `kotlinc`. Signatures were matched by reading your sources (`InsertFeedSavedSearch`, `ActivityLogRepository`, `SourceHealthCache`, `FeedSavedSearch`), not by building.
- `SourceHealthCache` was first sketched with an invented `isHealthy(sourceId)`; it has been corrected below to the real API (`object` + `getStatus(): NodeStatus`).
- We found **no** existing per-tab cap in `ui/home/*` or in the feed interactors. If a cap lives in another layer (a preference, a WorkManager limit), tell us and we will adjust the proposal.
- Anime genre vocabulary in the alias map is illustrative; it should be checked against the genres your installed sources actually emit.
- We did not run the SQLDelight `ALTER TABLE` path on an upgrade, nor a backup round-trip.

Cross-posted to ShinKu (the mirror proposal: give ShinKu the category schema AniZen already has, raise its hard 10-source cap to the same 25 per tab, and stop defaulting its feed language to `en`): _link added below once opened_.

If this is welcome, I can send it as a PR split in three commits: cap + strings, ShinKu-style rows + cursor, suggestions from `activity_log`.


---

## Symbol check (added after posting)

Every symbol in the sample code was checked against `master` = `95160a724d1147777dd1f7997fff4885a4cd9deb`. Two things were wrong in the first version and are now fixed in the snippets above:

1. `SourceHealthCache` is an **`object`**, not an injectable class, and its API is `getStatus(sourceId): NodeStatus` with `NodeStatus = OPERATIONAL | DEGRADED | CRITICAL | OFFLINE` (`domain/src/main/java/tachiyomi/domain/source/service/SourceHealthCache.kt:12-28`, `core/common/src/main/kotlin/eu/kanade/tachiyomi/network/model/InfrastructureModels.kt:19-24`). It defaults to `OPERATIONAL` for an unprobed source, so the score now only penalises a real `CRITICAL`/`OFFLINE`.
2. `GetLibraryAnime.await()` returns `List<LibraryAnime>`, and the source id is `LibraryAnime.anime.source` (`domain/.../library/model/LibraryAnime.kt:5-7`), not `LibraryAnime.source`.

Confirmed as written: `CountFeedSavedSearchGlobal`, `InsertFeedSavedSearch.await/awaitAll`, `InsertFeedSavedSearchCategory`, `UpdateFeedSavedSearchCategory`, `ReorderFeed`, the exact `FeedSavedSearch` and `FeedSavedSearchCategory` fields, `ActivityLogRepository.getCountsByPeriod(after: Date): Map<Pair<Long, Int>, Long>`, the `ActivityLog.TYPE_*` numbering, `sourceManager.getCatalogueSources()`, and the `logActivity.await(...)` calls already present in `FeedScreenModel.kt:97` and `:203`. `CountFeedSavedSearchGlobalByCategory` does **not** exist yet: it is the two-line wrapper over your existing `countGlobalByCategory` query described above.

Still not compiled, still no device run — our environment has no Android SDK/Gradle and no `kotlinc`.


---

## Correction #2: no new interactor is needed for the per-tab count

Snippet 2 above proposed a `CountFeedSavedSearchGlobalByCategory` wrapper. Reading the real
interfaces again: `CountFeedSavedSearchGlobal.await(categoryId: Long = 1)` **already takes the
category** (`domain/.../source/interactor/CountFeedSavedSearchGlobal.kt`) over
`FeedSavedSearchRepository.countGlobal(categoryId: Long = 1)`. And in `FeedManageScreenModel` both
insert sites already hold the tab's list (`getFeedSavedSearchGlobal.await(categoryId)`), so the
guard needs **no new dependency and no extra query**. The patch below supersedes snippet 2.
## Phase 2 patch — corrected, and published as a branch (no pull request)

Same rule as #95: your `AGENTS.md` (Non-negotiables → Git) says *"Never | Open a pull request"*, because a
PR run publishes a release built from unmerged code. So this is a public fork branch plus the diff.

```bash
git fetch https://github.com/Alex17273747576777/AniZen feed-cap-per-tab
git cherry-pick FETCH_HEAD          # commit f5f1bdd, 3 files, +55
```

### What changed since the first version of this diff was posted here

Re-reading your tree before publishing it turned up three defects. All three are fixed in the branch:

| First version | Now | Why |
|---|---|---|
| Guards only in `FeedManageScreenModel.updateFeedCategory` and `.duplicate` | The cap lives in `InsertFeedSavedSearch.await` | There are **three** insertion paths, not two: those plus `SourcesScreenModel.addToFeed` (`:206`), which stayed uncapped — a tab could still grow without bound through the main "add source to feed" action |
| — | `updateFeedCategory` keeps a check **before** its delete | That move is implemented as `deleteFeedSavedSearchById.await(feed.id)` and *then* an insert. A cap in the interactor alone would delete the entry and then refuse to re-insert it: the cap would eat data |
| `awaitAll` not considered | `awaitAll` deliberately **not** capped | It is the bulk/restore path. Refusing rows there would silently drop entries from a backup instead of refusing one user action |
| Guard inside `.duplicate` | removed | Redundant once the interactor caps it — smaller diff |

`await` returns `null` on refusal, which is what it already returns on failure, so no call site changes
signature and nothing else has to be touched.

### Verified by executing, not by claiming

- **Your own provenance guard, run against `origin/master`:** `provenance guard: 0 violation(s), 0 warning(s)` → `✓ ok`. R1/R2 clean (no locale file, no frozen i18n module touched). R3 satisfied: every added Kotlin block is wrapped in `// ANZ -->` / `// ANZ <--` **and** carries a trailing `// ANZ` on a code line, because `scripts/check-provenance.sh` strips comment-only lines before grepping for the marker.
- `git apply --check` clean on `95160a72` (`master`); no line over your `.editorconfig` `max_line_length = 120`.
- Import order follows the alphabetical layout spotless/ktlint enforce (`logcat.LogPriority` before `tachiyomi.*`; `service.FeedLimits` before `service.SourceManager`), and `tachiyomi.core.common.util.system.logcat` is the real path — the same one `FeedScreenModel.kt:25` uses.

### Not verified

- **Nothing was compiled**: no Android SDK, Gradle or `kotlinc` where this was written, so `detekt`, `spotlessCheck` and `assemblePreview` have not run.
- **The refusal is logged, not surfaced.** `FeedManageScreenModel.State` (`:215`) carries only `items` and `categories` — no event channel — so a user who hits the cap sees nothing happen. Surfacing it needs an event flow in that screen; `FeedScreenModel` already has one that could be mirrored. That is a design decision, so it is named here rather than taken.
- No unit test in this phase (`InsertFeedSavedSearch` refusing at 25 and accepting at 24, and `updateFeedCategory` leaving the entry in place when the destination is full, are the two cases worth writing).

