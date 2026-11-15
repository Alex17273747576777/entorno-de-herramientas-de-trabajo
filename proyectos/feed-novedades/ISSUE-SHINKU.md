## TL;DR

Proposal for the Feed tab: multi-tab feed categories (as AniZen already ships), raise the per-tab source cap from 10 to 25 with unlimited tabs, stop defaulting the feed to English and suggest tabs in the user's own language plus an optional "explore other languages" tab, and derive those suggestions from source scanning plus usage statistics. Sample code below is written against your actual stack (SQLDelight + Voyager + Compose + Injekt + moko-resources) at the commit named below. It is **not compiled** — treat it as a starting point; happy to send a PR.

---

## What was actually read

Full source cloned and read at `main` = `043ab7d8e68e8a77752805c34969a2477195826a` (Apache-2.0). Everything below cites a real file and line from that commit.

| Area | File | What it does today |
|---|---|---|
| Tab entry point | `app/src/main/java/com/shinku/reader/ui/browse/feed/FeedTab.kt` | `Screen.feedTab(): TabContent`, actions *add* / *filter*, dialogs `FeedFilter` / `AddFeed` / `AddFeedSearch` / `DeleteFeed`, snackbar on `Event.TooManyFeeds` (line 174) |
| Global feed model | `app/src/main/java/com/shinku/reader/ui/browse/feed/FeedScreenModel.kt` (837 lines) | rows: `featured`, `forYou` (line 383, `take(10)` when library > 5), offline genre map (line 391), per-genre rows (line 462, `take(10)`), genre search (line 505) |
| Per-source feed | `app/src/main/java/com/shinku/reader/ui/browse/source/feed/SourceFeedScreenModel.kt` | line 108: same cap, per source |
| Persistence | `data/src/main/sqldelight/com/shinku/reader/data/feed_saved_search.sq` | columns: `_id, source, saved_search, global` — **no category, no order, no search type** |
| Domain/data | `domain/.../source/model/FeedSavedSearch.kt`, `domain/.../source/repository/FeedSavedSearchRepository.kt`, `data/.../source/FeedSavedSearchRepositoryImpl.kt` + `FeedSavedSearchMapper.kt` | one flat global list |
| Language | `domain/src/main/java/com/shinku/reader/exh/source/ShinKuPreferences.kt:65` | `feedLanguageFilter() = preferenceStore.getString("pref_feed_language_filter", "en")` |
| Language filter use | `FeedScreenModel.kt:230-246` (`getFilteredCatalogueSources`) | `if (languageFilterMode == "all") … else allSources.filter { it.lang.equals(languageFilterMode) \|\| it.lang == "all" }` |
| Device languages | `app/src/main/java/com/shinku/reader/util/system/LocaleHelper.kt:89-91` | `getDefaultEnabledLanguages() = setOf("all", "en", Locale.getDefault().language)` |
| Existing helpers worth reusing | `ui/browse/feed/GenreFilterHelper.kt`, `SuggestedTitlesScreen.kt`, `SuggestedTitlesScreenModel.kt` (uses `SourceHealthRepository`, modes `genre` / `for_you`), `SourcePageCursor.kt` | genre aliases, dedupe/pagination with a cursor that never advances on a failed request |
| Migrations | `app/src/main/java/com/shinku/reader/core/migration/migrations/*` + `Migrations.kt` | `Migration { version: Float; invoke(MigrationContext) }`; highest version today **75f** |
| Strings | `i18n-sy/src/commonMain/moko-resources/*/strings.xml` → `too_many_in_feed` | the number **10 is hardcoded inside ~30 translations** |

## The three concrete problems

1. **Hard cap of 10 sources.** `FeedScreenModel.kt:650-652`:
   ```kotlin
   private suspend fun hasTooManyFeeds(): Boolean {
       return countFeedSavedSearchGlobal.await() > 10
   }
   ```
   and `SourceFeedScreenModel.kt:108` (`countFeedSavedSearchBySourceId.await(source.id) > 10`). Users hit `Event.TooManyFeeds` → `SYMR.strings.too_many_in_feed`.

2. **One single feed, no tabs.** `feed_saved_search.sq` has no `category` and no `feed_order`, so there is nowhere to hang a second tab. AniZen solved this with a `feed_categories` table plus `category` / `feed_order` / `search_type` columns on the same table, a `ScrollableTabRow` + `HorizontalPager` and a management screen — that schema is a direct fit here (both projects descend from the same lineage, and the table/column names can be kept identical so backups and mental models stay compatible).

3. **The feed is English-first even when the app is not.** `feedLanguageFilter()` defaults to `"en"`, so `getFilteredCatalogueSources()` keeps only `lang == "en" || lang == "all"` until the user finds the filter dialog — while `LocaleHelper.getDefaultEnabledLanguages()` already enables `{"all", "en", <device language>}` for the rest of the app. Result: a Spanish/Portuguese/Arabic/Bengali user gets an English feed out of the box, and there is no way to say "keep my language" *and* "let me peek at others".

There is also no usage telemetry of any kind in this repo (`activity_log` / `ActivityLog` do not exist here), so today nothing can rank suggestions by what the user actually opens.

## Proposal

**A. Multi-tab feed (categories).** Add `feed_categories` and hang each feed entry on a category, with ordering and a per-category count. Show the tab row only when there is more than one category (AniZen hides an empty `Global` too). Keep `Global` as the system category with `_id = 1` so existing installs keep working untouched.

**B. Cap = 25 sources per tab, tabs unlimited.** Replace both `> 10` checks with one shared constant, counted **per category** instead of globally, and make the message carry the number instead of hardcoding it (otherwise the ~30 translations keep saying "10" after the change).

**C. Language policy for the feed.** Default the feed language to the device locale ∪ `enabledLanguages()` instead of `"en"`; let each tab declare its language (`"all"` allowed); add an explicit **"Explore other languages"** tab that is opt-in and clearly labelled, so the user can either stay in their language or browse beyond it. This is a preference change plus a per-tab column — no source changes.

**D. Suggestions from source scanning + statistics.** Rank candidate sources per language using signals the app already has: library overlap (`forYou` already reads the library), `SourceHealthRepository` (already injected in `SuggestedTitlesScreenModel`), `pinnedSources()` / `lastUsedSource()`, enabled languages, and — new — a tiny local event log (source id, feed id, event type, count, timestamp) so the ranking learns. Suggest one tab per top language of the user, then optionally the explore tab.

## Sample code

Written against the commit above and your module layout. **Not compiled, not run on a device.**

<details>
<summary><b>1. SQLDelight — <code>data/src/main/sqldelight/com/shinku/reader/data/feed_categories.sq</code> (new)</b></summary>

```sql
CREATE TABLE feed_categories (
    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sort INTEGER NOT NULL,
    lang TEXT NOT NULL DEFAULT 'all',   -- 'all' = mixed-language tab
    explore INTEGER AS Boolean NOT NULL DEFAULT 0  -- the opt-in "other languages" tab
);

-- System category. Existing installs keep their current feed here.
INSERT OR IGNORE INTO feed_categories(_id, name, sort) VALUES (1, 'Global', 0);

selectAll:
SELECT * FROM feed_categories ORDER BY sort;

selectById:
SELECT * FROM feed_categories WHERE _id = :id;

insert:
INSERT INTO feed_categories(name, sort, lang, explore)
VALUES (:name, (SELECT COALESCE(MAX(sort), 0) + 1 FROM feed_categories), :lang, :explore);

update:
UPDATE feed_categories SET name = :name, lang = :lang WHERE _id = :id;

updateSort:
UPDATE feed_categories SET sort = :sort WHERE _id = :id;

-- never delete the system category
delete:
DELETE FROM feed_categories WHERE _id = :id AND _id != 1;

selectLastInsertedRowId:
SELECT last_insert_rowid();
```
</details>

<details>
<summary><b>2. SQLDelight — additions to <code>feed_saved_search.sq</code></b></summary>

```sql
ALTER TABLE feed_saved_search ADD COLUMN category INTEGER NOT NULL DEFAULT 1;
ALTER TABLE feed_saved_search ADD COLUMN feed_order INTEGER NOT NULL DEFAULT 0;
ALTER TABLE feed_saved_search ADD COLUMN search_type INTEGER NOT NULL DEFAULT 1;

-- 1 = Latest (unchanged default), 0 = Popular, 2 = SavedSearch: same encoding AniZen uses,
-- so the two apps can exchange feed backups without a translation table.

countGlobalByCategory:
SELECT count(*) FROM feed_saved_search WHERE global = 1 AND category = :categoryId;

selectGlobalByCategory:
SELECT * FROM feed_saved_search WHERE global = 1 AND category = :categoryId ORDER BY feed_order;

selectGlobalFeedSavedSearchByCategory:
SELECT saved_search.*
FROM (
    SELECT saved_search FROM feed_saved_search
    WHERE global = 1 AND category = :categoryId ORDER BY feed_order
) AS M
JOIN saved_search ON saved_search._id = M.saved_search;

insertWithCategory:
INSERT INTO feed_saved_search (source, saved_search, global, category, feed_order, search_type)
VALUES (:sourceId, :savedSearch, :global, :category,
        (SELECT COALESCE(MAX(feed_order), 0) + 1 FROM feed_saved_search WHERE category = :category),
        :searchType);

reorderInCategory:
UPDATE feed_saved_search SET feed_order = :feedOrder WHERE _id = :id AND category = :categoryId;
```
</details>

<details>
<summary><b>3. One shared cap — <code>domain/.../source/service/FeedLimits.kt</code> (new)</b></summary>

```kotlin
package com.shinku.reader.domain.source.service

/**
 * Feed composition limits.
 *
 * The old rule was a flat 10 sources for the whole feed
 * (FeedScreenModel.hasTooManyFeeds, SourceFeedScreenModel). Now the limit is per tab,
 * and the number of tabs is not limited: a user who reads four languages gets four tabs
 * of 25 sources instead of one tab of 10.
 */
object FeedLimits {
    const val MAX_SOURCES_PER_TAB: Int = 25

    /** Keep a small headroom for parallel fetches inside one tab. */
    const val MAX_CONCURRENT_FETCHES_PER_TAB: Int = 6
}
```

`FeedScreenModel.kt` (line 650) becomes per-category, and the same change applies to
`SourceFeedScreenModel.kt` (line 108):

```kotlin
private suspend fun hasTooManyFeeds(categoryId: Long = state.value.activeCategory): Boolean =
    countFeedSavedSearchGlobalByCategory.await(categoryId) >= FeedLimits.MAX_SOURCES_PER_TAB
```
</details>

<details>
<summary><b>4. Message that carries the number (instead of "10" in 30 translations)</b></summary>

```xml
<!-- i18n-sy/src/commonMain/moko-resources/base/strings.xml -->
<string name="too_many_in_feed">Too many sources in this feed tab, you can\'t add more than %1$d</string>
<string name="feed_tab_explore_languages">Explore other languages</string>
<string name="feed_tab_language_suggested">Suggested for %1$s</string>
<string name="feed_action_stay_in_my_language">Stay in my language</string>
```

```kotlin
// FeedTab.kt — the snackbar at line 174 stops hardcoding the limit
val tooManyFeedsString = stringResource(
    SYMR.strings.too_many_in_feed,
    FeedLimits.MAX_SOURCES_PER_TAB,
)
```

Existing translations keep working as soon as the placeholder is filled in; until they are
re-translated, the base string is used rather than a wrong number.
</details>

<details>
<summary><b>5. Language policy — <code>ShinKuPreferences.kt</code></b></summary>

```kotlin
// was: getString("pref_feed_language_filter", "en")
// The feed now starts where the rest of the app already starts: the device locale.
fun feedLanguageFilter() = preferenceStore.getString(
    "pref_feed_language_filter",
    LocaleHelper.getDeviceFeedLanguage(),   // "all" | <device language>
)

/** Opt-in tab that shows sources outside the user's languages. */
fun feedShowExploreLanguagesTab() = preferenceStore.getBoolean("pref_feed_explore_tab", false)

/** Per-tab language is stored on the category (feed_categories.lang), not here. */
```

```kotlin
// LocaleHelper.kt
fun getDeviceFeedLanguage(): String = Locale.getDefault().language.takeIf { it.isNotBlank() } ?: "all"
```

`getFilteredCatalogueSources()` (line 230) then keeps working unchanged for `"all"`, and a
category with `lang = "es"` filters exactly like today's `languageFilterMode`, but per tab:

```kotlin
val wanted = category.lang          // from feed_categories
var filtered = if (wanted == "all") {
    allSources.filter { it.lang in enabledLanguages || it.lang == "all" }
} else {
    allSources.filter { it.lang.equals(wanted, ignoreCase = true) || it.lang == "all" }
}
```
</details>

<details>
<summary><b>6. Local event log for statistics — <code>feed_activity.sq</code> (new)</b></summary>

```sql
import java.util.Date;

CREATE TABLE feed_activity (
    _id INTEGER NOT NULL PRIMARY KEY,
    source_id INTEGER NOT NULL,
    category_id INTEGER,
    manga_id INTEGER,
    event_type INTEGER NOT NULL,   -- 1 FETCH, 2 OPEN, 3 READ, 4 COMPLETE, 5 FEED_UPDATE
    count INTEGER,
    timestamp INTEGER AS Date NOT NULL
);

CREATE INDEX feed_activity_source_index ON feed_activity(source_id);
CREATE INDEX feed_activity_time_index ON feed_activity(timestamp);

insert:
INSERT INTO feed_activity (source_id, category_id, manga_id, event_type, count, timestamp)
VALUES (:sourceId, :categoryId, :mangaId, :eventType, :count, :timestamp);

-- what the user actually opens, per source, in the last N days
getCountsByPeriod:
SELECT source_id, event_type, SUM(count) AS total_count, COUNT(*) AS event_count
FROM feed_activity
WHERE timestamp >= :after
GROUP BY source_id, event_type;

removeOldActivity:
DELETE FROM feed_activity WHERE timestamp < :before;
```

Same shape and same event numbering AniZen uses in `activity_log.sq`, so the two apps can
share the ranking logic and even backup entries.
</details>

<details>
<summary><b>7. Suggestion interactor — <code>domain/.../source/interactor/SuggestFeedTabs.kt</code> (new)</b></summary>

```kotlin
package com.shinku.reader.domain.source.interactor

import com.shinku.reader.domain.manga.interactor.GetLibraryManga
import com.shinku.reader.domain.source.service.FeedLimits
import com.shinku.reader.domain.source.service.SourcePreferences
import com.shinku.reader.exh.source.ShinKuPreferences
import com.shinku.reader.util.system.LocaleHelper
import eu.kanade.tachiyomi.source.CatalogueSource
import tachiyomi.domain.source.service.SourceManager

data class SuggestedFeedTab(
    val lang: String,
    val label: String,
    val sources: List<Long>,      // <= FeedLimits.MAX_SOURCES_PER_TAB
    val explore: Boolean = false,
)

/**
 * Builds the tabs the feed offers on first run and after the user installs new extensions.
 *
 * Signals, in order of weight (all local, no network):
 *  1. library overlap      — languages/sources the user already reads
 *  2. feed_activity        — OPEN/READ/COMPLETE counts in the last 30 days
 *  3. source health        — SourceHealthRepository, already used by SuggestedTitlesScreenModel
 *  4. pinned + last used   — SourcePreferences
 *  5. device language      — LocaleHelper.getDefaultEnabledLanguages()
 */
class SuggestFeedTabs(
    private val sourceManager: SourceManager,
    private val sourcePreferences: SourcePreferences,
    private val shinkuPreferences: ShinKuPreferences,
    private val getLibraryManga: GetLibraryManga,
    private val getActivityCounts: GetFeedActivityCounts,   // wraps getCountsByPeriod
) {

    suspend fun await(maxTabs: Int = 6): List<SuggestedFeedTab> {
        val enabled = sourcePreferences.enabledLanguages().get()
        val device = LocaleHelper.getDeviceFeedLanguage()
        val pinned = sourcePreferences.pinnedSources().get()
        val disabled = sourcePreferences.disabledSources().get()
            .mapNotNull { it.toLongOrNull() }.toSet()
        val sources: List<CatalogueSource> = sourceManager.getVisibleCatalogueSources()
            .filterNot { it.id in disabled }

        // 1. library overlap per language
        // GetLibraryManga.await() returns List<LibraryManga>; the source id is
        // LibraryManga.manga.source (LibraryManga.id is the manga id).
        val libraryLang = getLibraryManga.await()
            .mapNotNull { entry -> sources.firstOrNull { it.id == entry.manga.source }?.lang }
            .groupingBy { it }.eachCount()

        // 2. usage in the last 30 days per source
        val used = getActivityCounts.await(days = 30)

        val scored = sources.map { source ->
            val opens = used[source.id].orEmpty()
            source to (
                (libraryLang[source.lang] ?: 0) * 3.0 +
                    opens * 2.0 +
                    (if (source.id.toString() in pinned) 5.0 else 0.0) +
                    (if (source.lang == device) 4.0 else 0.0)
                )
        }

        val myLanguages = (enabled + device).distinct()
        val mine = scored
            .filter { (lang, _) -> lang in myLanguages }
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
            .sortedByDescending { it.sources.size }
            .take(maxTabs)

        if (!shinkuPreferences.feedShowExploreLanguagesTab().get()) return mine

        val others = scored
            .filter { (lang, _) -> lang !in myLanguages && lang != "all" }
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

`SourceHealthRepository` can be added as a sixth signal where it is already injected
(`SuggestedTitlesScreenModel`). Its real API is
`getBySourceId(sourceId): SourceHealth?` / `subscribeAll(): Flow<List<SourceHealth>>`
(`domain/.../source/repository/SourceHealthRepository.kt:6-11`), and `SourceHealth` already
carries `failureCount`, `successCount`, `avgLatency` and a computed `isFailingNow`
(`domain/.../source/model/SourceHealth.kt:5-15`), so the weight above becomes:

```kotlin
val health = migrationSafe { sourceHealth.getBySourceId(source.id) }   // nullable by design
val healthScore = when {
    health == null -> 0.0                 // never probed: neutral, not penalised
    health.isFailingNow -> -4.0
    health.successCount > health.failureCount -> 2.0
    else -> -1.0
}
```
</details>

<details>
<summary><b>8. UI — tab row + pager in the existing <code>presentation/browse/FeedScreen.kt</code> style</b></summary>

```kotlin
val categories by screenModel.categories.collectAsState()   // List<FeedSavedSearchCategory>
val activeCategory by screenModel.activeCategory.collectAsState()
val pagerState = rememberPagerState(pageCount = { categories.size })

LaunchedEffect(pagerState.currentPage) {
    screenModel.setActiveCategory(categories[pagerState.currentPage].id)
}

Column(Modifier.fillMaxSize().padding(contentPadding)) {
    if (categories.size > 1) {
        ScrollableTabRow(
            selectedTabIndex = pagerState.currentPage.coerceIn(0, categories.lastIndex),
            edgePadding = 0.dp,
            divider = {},
        ) {
            categories.forEachIndexed { index, category ->
                Tab(
                    selected = pagerState.currentPage == index,
                    onClick = { scope.launch { pagerState.animateScrollToPage(index) } },
                    text = {
                        Text(
                            if (category.explore) stringResource(SYMR.strings.feed_tab_explore_languages)
                            else category.name,
                        )
                    },
                )
            }
        }
    }

    HorizontalPager(state = pagerState, modifier = Modifier.fillMaxSize()) { page ->
        // exactly today's FeedScreen content, scoped to categories[page].id
        FeedPageContent(
            state = state.forCategory(categories[page].id),
            onClickManga = onClickManga,
            onClickGenre = onClickGenre,
            onSeeAllTitles = onSeeAllTitles,
            onAddFeed = onAddFeed,
            onRefresh = onRefresh,
        )
    }
}
```
</details>

<details>
<summary><b>9. Migration — <code>core/migration/migrations/SetupFeedCategoriesMigration.kt</code> (new, version 76f)</b></summary>

```kotlin
package com.shinku.reader.core.migration.migrations

import com.shinku.reader.core.common.util.lang.withIOContext
import com.shinku.reader.core.migration.Migration
import com.shinku.reader.core.migration.MigrationContext
import com.shinku.reader.domain.source.repository.FeedSavedSearchCategoryRepository  // new: part of this proposal

/**
 * Creates the system category (id 1, "Global") and moves every existing feed entry into it.
 * Idempotent: safe to run twice, safe on a fresh install.
 */
class SetupFeedCategoriesMigration : Migration {
    override val version: Float = 76f

    override suspend fun invoke(migrationContext: MigrationContext): Boolean = withIOContext {
        val categories = migrationContext.get<FeedSavedSearchCategoryRepository>()
            ?: return@withIOContext false
        if (categories.getAll().isEmpty()) categories.insertSystemGlobal()
        return@withIOContext true
    }
}
```

register it in `core/migration/migrations/Migrations.kt` next to the current highest version
(75f today), and bump the SQLDelight schema version so the `ALTER TABLE` statements above run.

Two extra points that need care:
- **Backups**: the backup serializer/restorer must learn `category`, `feed_order`,
  `search_type` and the new table, otherwise restoring a backup silently drops tabs.
- **Older backups** (no category column) must restore into category 1.
</details>

## Acceptance criteria

- [ ] A user can create N feed tabs; each tab holds up to 25 sources; the 26th is refused with a message that states 25 (not 10).
- [ ] Existing installs keep their current feed inside a `Global` tab, with no data loss and no re-adding of sources.
- [ ] Feed tab order can be changed and survives a restart and a backup restore.
- [ ] On a device set to a non-English locale, the first-run feed is not English-only.
- [ ] "Explore other languages" is opt-in, off by default, and clearly labelled.
- [ ] Suggestions are computed from local data only (library, activity log, pinned/last used, enabled languages, source health); no new network call is made to build them.
- [ ] `too_many_in_feed` and the new strings go through moko-resources, with the number as a placeholder.

## What we did NOT verify (so nobody inherits a false positive)

- The sample code was **not compiled and not run**: our environment has no Android SDK/Gradle and no `kotlinc`. Signatures were matched by reading your sources, not by building them.
- We did not test the SQLDelight `ALTER TABLE` path on an upgrade from an older schema version, nor the backup round-trip.
- `SourceHealthRepository`'s exact API was read only where `SuggestedTitlesScreenModel` uses it.
- We did not check whether a category feature is already planned; if it is, this is meant as input, not as a competing design.

Cross-posted to AniZen (the mirror proposal: adopt ShinKu's feed row format there, with the same 25-per-tab rule): _link added below once opened_.

If this is welcome, I can send it as a PR split in three commits: schema + migration, cap + strings, suggestions + UI.


---

## Symbol check (added after posting)

Every symbol in the sample code was checked against `main` = `043ab7d8e68e8a77752805c34969a2477195826a`. Corrections now applied to the snippets above:

1. `GetLibraryManga.await()` returns `List<LibraryManga>`, and the source id is `LibraryManga.manga.source` (`domain/.../library/model/LibraryManga.kt:5-15`).
2. `MigrationContext` is a **class** `MigrationContext(val dryrun: Boolean)` with `inline fun <reified T> get(): T?` backed by Injekt (`app/.../core/migration/MigrationContext.kt:5-9`), not an interface — the migration sketch uses it as such.
3. `FeedSavedSearchCategoryRepository` / `insertSystemGlobal()` are **new** files introduced by this proposal, not existing ones; they are now marked that way.
4. `SourceHealthRepository`'s real API (`getBySourceId`, `subscribeAll`, `updateStats`, `resetStats`) and `SourceHealth.isFailingNow` are now used explicitly as a scoring signal.

Confirmed as written: `CountFeedSavedSearchGlobal`, `CountFeedSavedSearchBySourceId`, `getVisibleCatalogueSources()`, `getCatalogueSources()`, `GetSavedSearchBySourceId`, `withIOContext` (`core/common/.../CoroutinesExtensions.kt:60`), the `Migration { version: Float; invoke(MigrationContext): Boolean }` shape (highest existing version **75f**, hence 76f for the new one), `preferenceStore.getString/getBoolean`, and `LocaleHelper.getDefaultEnabledLanguages() = {"all","en",device}`.

Still not compiled, still no device run — our environment has no Android SDK/Gradle and no `kotlinc`.



---

## Phase 2 patch withdrawn — please do not apply the diff below

The diff at the bottom of this issue was generated and `git apply --check`-clean, but re-reading your
tree before publishing it as a pull request turned up three problems that make it wrong to land. It is
kept below, collapsed and marked, only so the reasoning is checkable. **No branch and no PR were pushed
for ShinKu's feed.**

1. **"Per tab" is not a unit ShinKu has.** `feed_saved_search.sq` has exactly four columns
   (`_id, source, saved_search, global`) and there is no `feed_categories.sq` anywhere in the repo: the
   feed is one global list plus per-source lists. The patch named its constant `MAX_SOURCES_PER_TAB`
   while applying it to `countFeedSavedSearchGlobal.await()` — a global count. That is not a 25-per-tab
   cap, it is the old global cap raised from 10 to 25 under a name that promises something else.
2. **It would make the app lie to the user.** `too_many_in_feed` is a literal in the base string
   (`i18n-sy/src/commonMain/moko-resources/base/strings.xml:469`, *"…cannot add more than 10"*) and in 15
   other locales. Raising the cap without touching it leaves the snackbar at `FeedTab.kt:174` and the
   toast at `SourceFeedScreenModel.kt:270` saying 10 after the app has accepted 25.
3. **Telling the truth there is not a one-line change.** Both call sites pass a bare `StringResource`
   (`onToast(SYMR.strings.too_many_in_feed)`, `stringResource(SYMR.strings.too_many_in_feed)`), so a
   `%1$d` in the base string also means changing the `onToast` signature and every screen that supplies
   it — plus 16 locale files that Weblate owns (your `pr_label.yml` labels its PRs). That is your call,
   not something to slip into a patch.

Also withdrawn from that diff: the `feedLanguageFilter()` default change (`"en"` → device language). It
silently changes the feed of every install that never touched the setting, so it belongs in the
discussion rather than in a patch.

### Corrected sequence

- **Phase 1 — schema (prerequisite for any per-tab wording):** `feed_categories.sq`, plus
  `category` / `feed_order` / `search_type` on `feed_saved_search`, migration `76f`, and the backup model
  with the legacy `@SerialName` annotations preserved (`AGENTS.md` §2).
- **Phase 2 — the cap:** `FeedLimits.MAX_SOURCES_PER_TAB` applied to a **per-category** count, base
  string taking `%1$d`, translations left to Weblate.
- **Phase 3 — language:** device-language default, scan-based suggestions, optional explore-languages tab.

For reference, the cross-repo work that *is* published: AniZen has real tabs (`feed_categories.sq`,
`category` column), so its 25-per-tab cap is coherent today and is up as a branch on #94. ShinKu's
library work is separate and is up as #34.

<details>
<summary><b>Withdrawn diff — do not apply (kept only so the three points above are checkable)</b></summary>

```diff
diff --git a/app/src/main/java/com/shinku/reader/ui/browse/feed/FeedScreenModel.kt b/app/src/main/java/com/shinku/reader/ui/browse/feed/FeedScreenModel.kt
index f42bb71..d94b2e5 100644
--- a/app/src/main/java/com/shinku/reader/ui/browse/feed/FeedScreenModel.kt
+++ b/app/src/main/java/com/shinku/reader/ui/browse/feed/FeedScreenModel.kt
@@ -25,6 +25,7 @@ import com.shinku.reader.domain.source.interactor.InsertFeedSavedSearch
 import com.shinku.reader.domain.source.model.FeedSavedSearch
 import com.shinku.reader.domain.source.model.SavedSearch
 import com.shinku.reader.domain.source.repository.SourceHealthRepository
+import com.shinku.reader.domain.source.service.FeedLimits
 import com.shinku.reader.domain.source.service.SourceManager
 import com.shinku.reader.domain.source.service.SourcePreferences
 import com.shinku.reader.presentation.browse.FeedItemUI
@@ -648,7 +649,7 @@ open class FeedScreenModel(
     }
 
     private suspend fun hasTooManyFeeds(): Boolean {
-        return countFeedSavedSearchGlobal.await() > 10
+        return countFeedSavedSearchGlobal.await() >= FeedLimits.MAX_SOURCES_PER_TAB
     }
 
     fun getEnabledSources(): ImmutableList<CatalogueSource> {
diff --git a/app/src/main/java/com/shinku/reader/ui/browse/source/feed/SourceFeedScreenModel.kt b/app/src/main/java/com/shinku/reader/ui/browse/source/feed/SourceFeedScreenModel.kt
index b934338..fde8161 100644
--- a/app/src/main/java/com/shinku/reader/ui/browse/source/feed/SourceFeedScreenModel.kt
+++ b/app/src/main/java/com/shinku/reader/ui/browse/source/feed/SourceFeedScreenModel.kt
@@ -11,6 +11,7 @@ import dev.icerock.moko.resources.StringResource
 import com.shinku.reader.core.preference.asState
 import com.shinku.reader.domain.manga.interactor.UpdateManga
 import com.shinku.reader.domain.source.interactor.GetExhSavedSearch
+import com.shinku.reader.domain.source.service.FeedLimits
 import com.shinku.reader.domain.ui.UiPreferences
 import com.shinku.reader.presentation.browse.SourceFeedUI
 import eu.kanade.tachiyomi.source.CatalogueSource
@@ -105,7 +106,7 @@ open class SourceFeedScreenModel(
     }
 
     private suspend fun hasTooManyFeeds(): Boolean {
-        return countFeedSavedSearchBySourceId.await(source.id) > 10
+        return countFeedSavedSearchBySourceId.await(source.id) >= FeedLimits.MAX_SOURCES_PER_TAB
     }
 
     fun createFeed(savedSearchId: Long) {
diff --git a/domain/src/main/java/com/shinku/reader/domain/source/service/FeedLimits.kt b/domain/src/main/java/com/shinku/reader/domain/source/service/FeedLimits.kt
new file mode 100644
index 0000000..a1779a2
--- /dev/null
+++ b/domain/src/main/java/com/shinku/reader/domain/source/service/FeedLimits.kt
@@ -0,0 +1,16 @@
+package com.shinku.reader.domain.source.service
+
+/**
+ * Feed composition limits.
+ *
+ * The old rule was a flat 10 sources for the whole feed (FeedScreenModel.hasTooManyFeeds and
+ * SourceFeedScreenModel.hasTooManyFeeds). The limit now lives in one place and is expressed as
+ * "sources per tab", which is the unit a reader actually experiences: someone following four
+ * languages wants four tabs of 25 sources, not one tab of 10.
+ *
+ * MAX_CONCURRENT_FETCHES_PER_TAB keeps a tab refresh bounded no matter how full the tab is.
+ */
+object FeedLimits {
+    const val MAX_SOURCES_PER_TAB: Int = 25
+    const val MAX_CONCURRENT_FETCHES_PER_TAB: Int = 6
+}
diff --git a/domain/src/main/java/com/shinku/reader/exh/source/ShinKuPreferences.kt b/domain/src/main/java/com/shinku/reader/exh/source/ShinKuPreferences.kt
index f09216e..3fa5f5f 100644
--- a/domain/src/main/java/com/shinku/reader/exh/source/ShinKuPreferences.kt
+++ b/domain/src/main/java/com/shinku/reader/exh/source/ShinKuPreferences.kt
@@ -62,7 +62,13 @@ class ShinKuPreferences(
 
     fun feedSourceFilter() = preferenceStore.getString("pref_feed_source_filter", "all")
 
-    fun feedLanguageFilter() = preferenceStore.getString("pref_feed_language_filter", "en")
+    // The feed used to default to English while the rest of the app already enables the device
+    // language (LocaleHelper.getDefaultEnabledLanguages). Default to the device language so a
+    // non-English install does not start with an English-only feed; "all" stays available.
+    fun feedLanguageFilter() = preferenceStore.getString(
+        "pref_feed_language_filter",
+        java.util.Locale.getDefault().language.ifBlank { "all" },
+    )
 
     fun feedShowSourceFeeds() = preferenceStore.getBoolean("pref_feed_show_source_feeds", true)
 

```

</details>
