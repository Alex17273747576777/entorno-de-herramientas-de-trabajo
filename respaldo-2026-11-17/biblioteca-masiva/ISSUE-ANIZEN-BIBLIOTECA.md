## Summary

AniZen can already merge entries — through `animes.parent_id` and a manual editor — but the user has
to know a duplicate exists, find it and merge it by hand. As a library grows that cost grows with it,
and the merge itself is season/parent-shaped rather than "same series from two sources" shaped.

[Reikai](https://github.com/unseensnick/Reikai) — same Mihon lineage, Apache-2.0, read at `main` =
`00206fe6ae0c6cf87e2f6114b59164ea295a6fd1` — makes grouping a **stored fact** (`merge_group` +
membership tables with `UNIQUE(manga_id)` and FK cascades), **offers the group in one tap** when a
same-titled series is added (default on, never silent), routes every title count through **one dedupe
helper**, and ships the performance side of a big library (`baseline-profile` module, memoised bucket
assembly, stable Compose keys, 10 SQL views, partial indexes).

AniZen is well placed to adopt this: you already write `activity_log` (`TYPE_OPEN/PLAY/COMPLETE`),
which is exactly the signal needed to rank which duplicate matters, and you already have
`SourceHealthCache` to avoid stitching a group around a dead source.

Mirror proposal on ShinKu: https://github.com/Harrys-HQ/ShinKu/issues/33. Separate from #94 (feed tabs) on purpose: different subsystem, independently reviewable. All claims
below cite real files; sample code matches your stack and is **not compiled** (no Android SDK/Gradle
in our environment).

## Correction (verified after posting — read this first)

The first version of this issue described AniZen's merge as parent/season-shaped and said there was no
automatic duplicate detection. **Both were incomplete**, and the real picture makes the proposal
smaller:

- AniZen already has the SY-lineage **`merged` table** (`data/src/main/sqldelight/tachiyomi/data/merged.sq`)
  with `info_anime`, `get_episode_updates`, `episode_sort_mode`, `download_episodes` and
  **`episode_priority` — "episode priority the deduplication uses"** (`MergedAnimeReference.kt`, with
  `EPISODE_SORT_NONE / NO_DEDUPE / PRIORITY`), both FKs, both indexes, a manual editor
  (`ui/anime/merged/EditMergedAnime*`) and `MergeAnimeSettingsUpdate`. `parent_id` is the *season*
  axis, not the merge axis.
- AniZen already **detects duplicates on add**: `GetDuplicateLibraryAnime` →
  `getDuplicateLibraryAnime(anime.id, anime.title.lowercase())` (`animes.sq:128`), shown through
  `DuplicateAnimeDialog` at `BrowseSourceScreen.kt:585`. The dialog is a bare confirm: it does not
  list the candidates and offers no grouping.

So what is actually missing is: (1) **list the candidates and offer "group with «X»"** in the dialog
that already opens, (2) group membership as a `UNIQUE`-constrained table resolved by id lookup,
(3) a **refusal memory** per pair, (4) **one dedupe helper** so every surface counts a merged series
once, (5) ranking the candidates with the `activity_log` and `SourceHealthCache` you already write,
(6) carry-over of out-of-DB state, and (7) the **performance package**. Items 1 and 3 are small;
`episode_priority` can be kept as `source_priority`. The proposal below is re-scoped to that.

A second correction, found while generating the accompanying patch: AniZen **already indexes both hot
library predicates** — `library_favorite_index ON animes(favorite) WHERE favorite = 1` (`animes.sq:43`)
and `episodes_unseen_by_anime_index ON episodes(anime_id, seen) WHERE seen = 0` (`episodes.sq:31`).
The first version of this issue claimed the unseen side was missing and proposed a new index that
would have been a redundant duplicate. That item is withdrawn; the performance side of this proposal
is only the `baseline-profile` module, memoised buckets, stable keys and the `libraryView` join.

## What AniZen has today (verified at `95160a724d1147777dd1f7997fff4885a4cd9deb`)

| Area | File | State |
|---|---|---|
| Seasons | `animes.sq:34` (`parent_id INTEGER`), index `:45`, queries `:236`/`:241`; `Anime.parentId`, `GetSeasonsByAnimeId`, `GetAnimeWithEpisodesAndSeasons` | Parent/child grouping **for seasons** — a different axis from cross-source merging, and it should stay |
| Merge UI | `ui/anime/merged/EditMergedAnimeAdapter.kt`, `EditMergedAnimeHolder.kt`, `EditMergedAnimeItem.kt`, `EditMergedAnimeSettingsDialog.kt`, `EditMergedAnimeSettingsHeaderAdapter.kt`; driven from `ui/anime/AnimeScreen.kt` / `AnimeScreenModel.kt` | **Manual**: a RecyclerView editor with drag/release, delete, per-entry toggles for episode updates and downloads |
| Duplicate detection | `domain/.../anime/interactor/GetDuplicateLibraryAnime.kt:6-11` → `AnimeRepository.getDuplicateLibraryAnime(id, title)` (`:29`) → `data/.../anime/AnimeRepositoryImpl.kt:70-72` → query `animes.sq:128`; dialog `eu/kanade/presentation/anime/DuplicateAnimeDialog.kt:34` used at `ui/browse/source/browse/BrowseSourceScreen.kt:585` | **Already exists**: same-title lookup on add, but the dialog is a bare confirm (`MR.strings.are_you_sure` / `confirm_add_duplicate_manga`) — it neither lists the candidates nor offers to group them |
| Cross-source merge | `data/src/main/sqldelight/tachiyomi/data/merged.sq` (`info_anime`, `get_episode_updates`, `episode_sort_mode`, `episode_priority`, `download_episodes`, `merge_id`, `merge_url`, `anime_id`, `anime_url`, `anime_source`; FK `ON DELETE SET NULL` / `ON DELETE CASCADE`; indexes `merged_merge_id_index`, `merged_anime_id_index`), model `domain/.../anime/model/MergedAnimeReference.kt` (`EPISODE_SORT_NONE=0`, `NO_DEDUPE=1`, `PRIORITY=2`), `MergeAnimeSettingsUpdate.kt`, editor `ui/anime/merged/EditMergedAnime*` | **Already exists** and already dedupes episodes by `episode_priority` — the trunk-source idea is here, shaped as a virtual merge entry rather than as a group |
| Library query | `data/src/main/sqldelight/tachiyomi/view/libraryView.sq` (+ `updatesView`, `historyView`, `episodestatsView`, `animeseasonsView`, `animeseasonstatsView`, `historystatsView`, `libraryUpdateErrorView`) | 8 views already: the shape Reikai uses, so the habit is there |
| Indexes | `library_favorite_index ON animes(favorite) WHERE favorite = 1` (`animes.sq:43`), `episodes_unseen_by_anime_index ON episodes(anime_id, seen) WHERE seen = 0` (`episodes.sq:31`), `episodes_anime_id_index` (`:29`), `animes_url_index`, `animes_parent_id_index`, `excluded_scanlators_anime_id_index`, `animes_categories_anime_id_index`, `history_history_episode_id_index`, `ai_messages_session_id_index`, `activity_log_*` (4) | **Both hot library predicates are already covered by partial indexes** — favourite entries and unseen episodes. Nothing to add here |
| Usage signal | `activity_log.sq` + `ActivityLog.TYPE_*`, written in `ui/home/FeedScreenModel.kt:97` and `:203`, consumed by `ui/stats/StatsScreenModel.kt` | Already collected — usable to rank duplicates |
| Source health | `domain/.../source/service/SourceHealthCache.kt` (`object`, `getStatus(id): NodeStatus`) | Already collected — usable to avoid a dead trunk source |
| Profiling | `macrobenchmark/` exists; **no `baseline-profile/` module** | Startup and library scroll are not covered by a shipped profile |

## What Reikai does (verified)

- **Stored membership.** `merge_group.sq` documents why: *"Replaces the pref-derived grouping:
  membership is a stored fact resolved by id lookup, not re-derived per call from prefs plus a
  same-title scan. The FK cascade from the member tables removes a member automatically when its
  entry row is deleted."* Tables: `merge_group(_id, content_type, title_override, cover_override,
  override_source_ranking)`, `merge_group_manga` / `merge_group_novel` with `UNIQUE(manga_id)`,
  `source_priority`, FK `ON DELETE CASCADE` both ways, plus
  `idx_merge_group_manga_group_id`.
- **Default-on, one tap, never silent.** `ReikaiLibraryPreferences.kt:161`
  `autoMergeSameTitle = getBoolean("auto_merge_same_title", true)` — *"Whether adding a same-titled
  series **offers** to group it with the match. Repurposed from silent auto-merge."* Consumed by
  `presentation/browse/DuplicatePrompt.kt:32` (`suggestGroup = mergeManager.suggestGroupingOnAdd`)
  and exposed at `SettingsLibraryScreen.kt:148`.
- **Refusals are remembered.** `mangaManualUnmerges`: normalised `"min,max"` id pairs that must never
  be grouped — the escape hatch that makes an on-by-default suggestion safe.
- **Counts cannot disagree.** `domain/merge/MergeGroupDedup.kt`: `dedupeByMergeGroup`,
  `onePerSeries`, `bucketByMergeGroup` — *"One definition of 'count a merged series once', so the
  surfaces counting titles cannot disagree."*
- **Stitched episode/chapter list.** `preferredMangaSources` (ranked trunk sources) +
  `MergedGroupStitcher`, `ReconcileMergedChapters`, `ChapterGap`, `StoredStitch`,
  `merged_chapter_unit.sq`; trackers mirror to every member (`syncTrackerLinksGrouped`, default true)
  and `handOutTrackersBeforeRemoval` moves them before an entry leaves a group.
- **Out-of-DB state follows the survivor.** `dedupe_merged_ids.sq` + `MergedDuplicateCarryMigration`
  carry custom covers and download folders keyed by a discarded id/title.
- **Performance.** `baseline-profile/` module (`BaselineProfileGenerator`, `StartupProfileGenerator`,
  `StartupBenchmarks`); memoised buckets (`presentation/library/LibraryAssembly.kt:100`,
  `itemsByKey.getOrPut(bucket.key)`); stable keys
  (`ReikaiLibraryContent.kt:238`, `key = { "reikai_cell_${bucket.key}_${it.entryId.contentType}_${it.entryId.rawId}" }`);
  `libraryView.sq` avoids the expensive history join unless the entry actually has excluded
  scanlators (`CASE WHEN EXISTS (…)`); partial indexes such as
  `chapter_unread_state_date_fetch_index … WHERE user_read = 0` and
  `manga_user_favorite_at_index … WHERE user_favorite_at IS NOT NULL`.
- **Tests**: `EntryMergeManagerTest`, `RestoreMergeGroupsTest`, `MergeGroupReconstructionTest`,
  `RenderMergedReadingOrderTest`, `MergedDuplicateCarryMigrationTest`,
  `MigrateMergePrefsToGroupsMigrationTest`, `MergedResumeDownloadedConformanceTest`.

## Proposal for AniZen

1. **Merge groups as a table**, next to `parent_id` (which keeps serving seasons): `merge_group` +
   `merge_group_anime` with `UNIQUE(anime_id)` and FK cascades, `source_priority` for the trunk
   source. Manual `EditMergedAnime*` keeps working and writes into the same table.
2. **Upgrade the dialog you already show**: `DuplicateAnimeDialog` stops being a bare confirm and lists the
   candidates with a *Group with «X»* action plus *don't ask again for this pair*. Default on, never silent.
   Rank candidates with data you already have: normalised title match first, then `activity_log` weight (a
   duplicate of something the user actually plays matters more), then `SourceHealthCache.getStatus` so the
   healthiest source becomes the trunk.
3. **One dedupe helper** (`dedupeByMergeGroup` / `onePerSeries`) used by the library grid, badges,
   the updates screen, the airing schedule and the feed rows of #94 — one total everywhere.
4. **Stitched episode list** from a ranked trunk source with gap handling, reusing `last_top_url`-style
   persistence habits you already have; mirror trackers to every member.
5. **Performance package**: `baseline-profile` module beside `macrobenchmark`; memoised bucket assembly;
   stable Compose keys; keep `libraryView` from paying the history join when no scanlator is excluded.
   (No new indexes: your favourite and unseen-episode partial indexes already exist — see the table.)
6. **Carry-over migration** so covers, download folders and `activity_log` rows keyed by a discarded
   id follow the survivor.
7. **Tests** pinning: group reconstruction, restore, stitched render order, carry-over, count
   agreement, and "refused pair is never suggested again".

## Sample code

<details>
<summary><b>1. <code>data/src/main/sqldelight/tachiyomi/data/merge_group.sq</code> (new)</b></summary>

```sql
-- Membership is a stored fact resolved by id lookup, not re-derived per call from preferences plus
-- a same-title scan. The FK cascades remove a member automatically when its anime row is deleted.
-- parent_id on animes keeps serving seasons; this table serves "same series, different source".
CREATE TABLE merge_group (
    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title_override TEXT,
    cover_override TEXT,
    override_source_ranking INTEGER AS Boolean NOT NULL DEFAULT 0
);

CREATE TABLE merge_group_anime (
    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    group_id INTEGER NOT NULL,
    anime_id INTEGER NOT NULL,
    source_priority INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY(group_id) REFERENCES merge_group (_id) ON DELETE CASCADE,
    FOREIGN KEY(anime_id) REFERENCES animes (_id) ON DELETE CASCADE,
    UNIQUE(anime_id)
);

CREATE INDEX merge_group_anime_group_id_index ON merge_group_anime(group_id);

getGroupId:
SELECT group_id FROM merge_group_anime WHERE anime_id = :animeId;

getMembers:
SELECT anime_id FROM merge_group_anime WHERE group_id = :groupId ORDER BY source_priority, anime_id;

getLibraryMemberships:
SELECT anime_id, group_id FROM merge_group_anime;

insertGroup:
INSERT INTO merge_group DEFAULT VALUES;

insertMember:
INSERT INTO merge_group_anime (group_id, anime_id, source_priority)
VALUES (:groupId, :animeId, :sourcePriority);

removeMember:
DELETE FROM merge_group_anime WHERE anime_id = :animeId;

deleteGroup:
DELETE FROM merge_group WHERE _id = :groupId;

selectLastInsertedRowId:
SELECT last_insert_rowid();
```
</details>

<details>
<summary><b>2. <code>domain/.../anime/interactor/SuggestDuplicateGroup.kt</code> (new) — ranked with data AniZen already writes</b></summary>

```kotlin
package tachiyomi.domain.anime.interactor

import eu.kanade.tachiyomi.network.model.NodeStatus
import tachiyomi.domain.anime.model.Anime
import tachiyomi.domain.history.model.ActivityLog
import tachiyomi.domain.history.repository.ActivityLogRepository
import tachiyomi.domain.library.interactor.GetLibraryAnime
import tachiyomi.domain.source.service.SourceHealthCache   // object singleton
import tachiyomi.domain.source.service.SourceManager
import java.util.Calendar

/**
 * The favourite a newly added anime most likely duplicates, best candidate first.
 *
 * Title match is normalised (case, punctuation, the "[Group] / (Dub) / Season 2" decorations sources
 * add). Ranking uses only data AniZen already stores — activity_log and SourceHealthCache — so
 * suggesting a group costs no network and no new collection. A pair the user already refused is
 * never suggested again.
 */
class SuggestDuplicateGroup(
    private val getLibraryAnime: GetLibraryAnime,
    private val activityLogRepository: ActivityLogRepository,
    private val sourceManager: SourceManager,
    private val uiPreferences: tachiyomi.domain.ui.UiPreferences,   // autoMergeSameTitle / manualUnmerges
) {

    suspend fun await(added: Anime, limit: Int = 3): List<Anime> {
        if (!uiPreferences.autoMergeSameTitle().get()) return emptyList()
        val refused = uiPreferences.mergeManualUnmerges().get()
        val key = normalise(added.title)

        val since = Calendar.getInstance().apply { add(Calendar.DAY_OF_YEAR, -30) }.time
        val counts: Map<Pair<Long, Int>, Long> = activityLogRepository.getCountsByPeriod(since)
        val usageBySource: Map<Long, Double> = counts.entries
            .groupBy({ it.key.first }, { it.key.second to it.value })
            .mapValues { (_, pairs) ->
                pairs.sumOf { (type, total) ->
                    when (type) {
                        ActivityLog.TYPE_PLAY -> 4.0 * total
                        ActivityLog.TYPE_COMPLETE -> 6.0 * total
                        ActivityLog.TYPE_OPEN -> 2.0 * total
                        else -> 0.0
                    }
                }
            }

        return getLibraryAnime.await()
            .map { it.anime }
            .filter { it.id != added.id && normalise(it.title) == key }
            .filter { !refused.contains(pairKey(added.id, it.id)) }
            .sortedByDescending { candidate ->
                usageBySource[candidate.source] ?: 0.0 +
                    when (SourceHealthCache.getStatus(candidate.source)) {
                        NodeStatus.OPERATIONAL -> 3.0
                        NodeStatus.DEGRADED -> 0.0
                        NodeStatus.CRITICAL -> -4.0
                        NodeStatus.OFFLINE -> -6.0
                    }
            }
            .take(limit)
    }

    private fun pairKey(a: Long, b: Long): String = "${minOf(a, b)},${maxOf(b, a)}"

    private fun normalise(title: String): String = title
        .lowercase()
        .replace(Regex("""[\[\(][^\]\)]*[\]\)]"""), " ")   // [SubsPlease] / (Dub) / (Uncensored)
        .replace(Regex("""\b(season|part)\s+\d+\b"""), " ")
        .replace(Regex("""[^a-z0-9]+"""), " ")
        .trim()
}
```

The UI side is a dialog on the "added to library" path — Reikai's `DuplicatePrompt.kt` is ~40 lines
and worth copying: *Group with «X»?* → create group / *Keep separate* → remember `pairKey`.
</details>

<details>
<summary><b>3. <code>domain/.../anime/model/MergeGroupDedup.kt</code> (new) — one definition of "count once"</b></summary>

```kotlin
package tachiyomi.domain.anime.model

/**
 * One item per merge group: the first item whose entry belongs to a group keeps it, later members of
 * that group drop out, and an ungrouped entry always stays.
 *
 * One definition of "count a merged series once", so the library grid, badges, updates, the airing
 * schedule and the feed rows cannot disagree about the total. Order decides the survivor: hand in a
 * deterministically ordered list.
 */
fun <T, K> List<T>.dedupeByMergeGroup(membership: Map<K, Long>, id: (T) -> K): List<T> {
    if (membership.isEmpty()) return this
    val seenGroups = HashSet<Long>()
    return filter { item -> membership[id(item)]?.let(seenGroups::add) ?: true }
}
```
</details>

<details>
<summary><b>4. Preferences — default on, with the escape hatch</b></summary>

```kotlin
/** Whether adding a same-titled series offers to group it with the match. Never silent. */
fun autoMergeSameTitle() = preferenceStore.getBoolean("auto_merge_same_title", true)

/** Normalised "min,max" id pairs the user refused: never suggested again. */
fun mergeManualUnmerges() = preferenceStore.getStringSet("merge_manual_unmerges", emptySet())

/** Source ids ranked highest-priority-first: the trunk source when stitching a merged episode list. */
fun preferredMergeSources() = preferenceStore.getLongArray("merge_preferred_sources", emptyList())
```
</details>

<details>
<summary><b>5. Partial indexes — nothing to add (verified)</b></summary>

AniZen already ships both hot-path partial indexes:

```sql
-- data/src/main/sqldelight/tachiyomi/data/animes.sq:43
CREATE INDEX library_favorite_index ON animes(favorite) WHERE favorite = 1;

-- data/src/main/sqldelight/tachiyomi/data/episodes.sq:31
CREATE INDEX episodes_unseen_by_anime_index ON episodes(anime_id, seen) WHERE seen = 0;
```

An earlier version of this issue proposed adding them. They exist, so the migration in the
accompanying patch only creates the merge-group tables.
</details>

<details>
<summary><b>6. <code>baseline-profile/</code> module (new) — beside your <code>macrobenchmark</code></b></summary>

```kotlin
// baseline-profile/build.gradle.kts
plugins {
    id("mihon.android.library")
    id("androidx.baselineprofile")
}

android {
    namespace = "mihon.baselineprofile"
    defaultConfig { minSdk = 28 }
    targetProjectPath = ":app"
}

baselineProfile {
    automaticGenerationDuringBuild = false
    saveInSrc = true
}

dependencies {
    implementation(libs.androidx.benchmark.macro.junit4)
}
```

```kotlin
// baseline-profile/src/main/kotlin/mihon/baselineprofile/LibraryScrollProfile.kt
@RunWith(AndroidJUnit4::class)
class LibraryScrollProfile {
    @get:Rule val rule = BaselineProfileRule()

    @Test
    fun libraryScroll() = rule.collect(
        packageName = "eu.kanade.tachiyomi.debug",   // your benchmark applicationId
        includeInStartupProfile = true,
    ) {
        startActivityAndWait()
        device.findObject(By.text("Library"))?.click()
        device.wait(Until.hasObject(By.res(packageName, "library_grid")), 5_000)
        val grid = device.findObject(By.res(packageName, "library_grid"))
        repeat(6) { grid?.fling(Direction.DOWN); device.waitForIdle() }
    }
}
```
</details>

<details>
<summary><b>7. Library path: memoised buckets + stable keys</b></summary>

```kotlin
// Build each bucket once per key and reuse it across recompositions
// (Reikai: presentation/library/LibraryAssembly.kt:100)
private val itemsByKey = mutableMapOf<Long, ImmutableList<LibraryItem>>()
fun itemsFor(categoryId: Long): ImmutableList<LibraryItem> =
    itemsByKey.getOrPut(categoryId) { buildItems(categoryId) }

// Stable keys so a reorder or a merge does not invalidate every cell
LazyVerticalGrid(state = gridState) {
    items(
        items = bucketItems,
        key = { "cell_${categoryId}_${it.anime.id}" },
        contentType = { it.contentType },
    ) { item -> LibraryItemCell(item) }
}
```
</details>

## Acceptance criteria

- [ ] Adding an anime that duplicates a favourite offers to group it in one tap; default on; nothing merged silently.
- [ ] Candidates are ranked with local data only (`activity_log`, `SourceHealthCache`), never a new network call.
- [ ] "Don't ask again for this pair" persists across restart and backup restore.
- [ ] Membership is a table lookup (`UNIQUE(anime_id)`), never a per-call same-title scan; deleting an anime cascades out of its group.
- [ ] `parent_id` keeps working for seasons; the manual `EditMergedAnime*` editor writes into the same group table.
- [ ] Library count, badges, updates, airing schedule and feed rows all report the same total for a merged series.
- [ ] A merged entry's episode list is stitched from a ranked trunk source with gaps handled and seen state preserved.
- [ ] `baseline-profile` covers cold start + library scroll (no new indexes needed: both hot predicates are already indexed).
- [ ] Tests pin: reconstruction, restore, stitched render order, carry-over of covers/downloads, count agreement, refused-pair memory.

## Phase 1 patch — published as a branch, not a pull request

Your `AGENTS.md` is explicit about this (**Git → Non-negotiables**: *"Never | Open a pull request.
Integrate into `preview` by pushing or merging"*, because `preview.yml` publishes a release on a
`pull_request` run and that desyncs the `r<commitCount>` tag scheme). So there is **no PR** for this:
the commit lives on a public fork branch instead, and you can fetch or cherry-pick it directly.

```bash
git fetch https://github.com/Alex17273747576777/AniZen merge-groups-phase1
git cherry-pick FETCH_HEAD          # commit e1c6b51, 3 files, +93
```

Three files, no deletions, and **no behaviour change** — nothing is wired into Injekt, the repository
or the UI yet, it only makes membership storable. `merged` (with `episode_priority`, *"the
deduplication uses"*) and `animes.parent_id` (seasons) are untouched.

| File | What |
|---|---|
| `data/.../tachiyomi/data/merge_group.sq` | `merge_group` + `merge_group_anime` (`UNIQUE(anime_id)`, both FKs `ON DELETE CASCADE`), their two indexes, 8 queries |
| `data/.../tachiyomi/data/migrations/147.sqm` | The same DDL for upgrading installs (147 is next after your `146.sqm`) |
| `domain/.../anime/model/MergeGroupDedup.kt` | `List<T>.dedupeByMergeGroup(membership, id)`, wrapped in `// ANZ -->` / `// ANZ <--` per your provenance convention, with a trailing `// ANZ` on a code line so `scripts/check-provenance.sh` R3 sees it |

The table is declared in **both** the `.sq` and the `.sqm` because that is your convention (checked
against every table in the repo — `feed_categories.sq` + `133.sqm`, `activity_log.sq` + `134.sqm`,
`custom_buttons.sq` + `129.sqm`): a fresh install takes its schema from the `.sq` DDL, an upgrade
replays the `.sqm`. Declaring it only in the migration would have left new installs without the table.

<details>
<summary><b>The patch (click to expand)</b></summary>

```diff
diff --git a/data/src/main/sqldelight/tachiyomi/data/merge_group.sq b/data/src/main/sqldelight/tachiyomi/data/merge_group.sq
new file mode 100644
index 0000000..2807dba
--- /dev/null
+++ b/data/src/main/sqldelight/tachiyomi/data/merge_group.sq
@@ -0,0 +1,55 @@
+import kotlin.Boolean;
+
+-- Cross-source grouping as a stored fact.
+--
+-- `merged` (the SY-lineage table, with episode_priority that "the deduplication uses") keeps serving
+-- the virtual merged entry, and `animes.parent_id` keeps serving seasons: neither changes. This table
+-- answers a different question — "which group is this anime in" — by id lookup instead of re-deriving
+-- it per call from preferences plus a same-title scan. UNIQUE(anime_id) keeps an anime in at most one
+-- group, and both foreign keys cascade so membership cannot outlive either side.
+CREATE TABLE merge_group(
+    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
+    title_override TEXT,
+    cover_override TEXT,
+    override_source_ranking INTEGER AS Boolean NOT NULL DEFAULT 0
+);
+
+CREATE TABLE merge_group_anime(
+    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
+    group_id INTEGER NOT NULL,
+    anime_id INTEGER NOT NULL,
+    source_priority INTEGER NOT NULL DEFAULT 0,
+    FOREIGN KEY(group_id) REFERENCES merge_group (_id)
+    ON DELETE CASCADE,
+    FOREIGN KEY(anime_id) REFERENCES animes (_id)
+    ON DELETE CASCADE,
+    UNIQUE(anime_id)
+);
+
+CREATE INDEX merge_group_anime_group_id_index ON merge_group_anime(group_id);
+CREATE INDEX merge_group_anime_anime_id_index ON merge_group_anime(anime_id);
+
+getGroupId:
+SELECT group_id FROM merge_group_anime WHERE anime_id = :animeId;
+
+getMembers:
+SELECT anime_id FROM merge_group_anime WHERE group_id = :groupId ORDER BY source_priority, anime_id;
+
+getMemberships:
+SELECT anime_id, group_id FROM merge_group_anime;
+
+insertGroup:
+INSERT INTO merge_group (override_source_ranking) VALUES (:overrideSourceRanking);
+
+insertMember:
+INSERT INTO merge_group_anime (group_id, anime_id, source_priority)
+VALUES (:groupId, :animeId, :sourcePriority);
+
+removeMember:
+DELETE FROM merge_group_anime WHERE anime_id = :animeId;
+
+deleteGroup:
+DELETE FROM merge_group WHERE _id = :groupId;
+
+selectLastInsertedRowId:
+SELECT last_insert_rowid();
diff --git a/data/src/main/sqldelight/tachiyomi/data/migrations/147.sqm b/data/src/main/sqldelight/tachiyomi/data/migrations/147.sqm
new file mode 100644
index 0000000..c72f571
--- /dev/null
+++ b/data/src/main/sqldelight/tachiyomi/data/migrations/147.sqm
@@ -0,0 +1,21 @@
+CREATE TABLE merge_group(
+    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
+    title_override TEXT,
+    cover_override TEXT,
+    override_source_ranking INTEGER AS Boolean NOT NULL DEFAULT 0
+);
+
+CREATE TABLE merge_group_anime(
+    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
+    group_id INTEGER NOT NULL,
+    anime_id INTEGER NOT NULL,
+    source_priority INTEGER NOT NULL DEFAULT 0,
+    FOREIGN KEY(group_id) REFERENCES merge_group (_id)
+    ON DELETE CASCADE,
+    FOREIGN KEY(anime_id) REFERENCES animes (_id)
+    ON DELETE CASCADE,
+    UNIQUE(anime_id)
+);
+
+CREATE INDEX merge_group_anime_group_id_index ON merge_group_anime(group_id);
+CREATE INDEX merge_group_anime_anime_id_index ON merge_group_anime(anime_id);
diff --git a/domain/src/main/java/tachiyomi/domain/anime/model/MergeGroupDedup.kt b/domain/src/main/java/tachiyomi/domain/anime/model/MergeGroupDedup.kt
new file mode 100644
index 0000000..96d537a
--- /dev/null
+++ b/domain/src/main/java/tachiyomi/domain/anime/model/MergeGroupDedup.kt
@@ -0,0 +1,17 @@
+package tachiyomi.domain.anime.model
+
+// ANZ -->
+/**
+ * One item per merge group: the first item whose anime belongs to a group keeps it, later members of
+ * that group drop out, and an ungrouped anime always stays.
+ *
+ * A single definition of "count a merged series once", so the library grid, the badges, the updates
+ * screen, the airing schedule and the feed rows cannot disagree about the total. Order decides the
+ * survivor, so hand in a deterministically ordered list (the group's `source_priority`, then id).
+ */
+fun <T, K> List<T>.dedupeByMergeGroup(membership: Map<K, Long>, id: (T) -> K): List<T> { // ANZ
+    if (membership.isEmpty()) return this
+    val seenGroups = HashSet<Long>()
+    return filter { item -> membership[id(item)]?.let(seenGroups::add) ?: true }
+}
+// ANZ <--
```

</details>

**Verified:** the DDL of both paths was executed against SQLite 3.46.1 together with the queries and
constraints — 13 assertions, 0 failures: `UNIQUE(anime_id)` rejects a second membership,
`FK(group_id)` and `FK(anime_id)` reject missing rows, deleting an anime cascades its membership away,
deleting a group empties it, `getMembers` orders by `source_priority, anime_id`. `git apply --check`
clean on `95160a72` (`master`). No line exceeds your `.editorconfig` `max_line_length = 120`, and no
locale or frozen i18n module is touched (R1/R2).

**Update — the Kotlin half is now compiled and its test executed.** The branch carries a second commit
(`b435e3fa3b5c`) adding `domain/src/test/java/tachiyomi/domain/anime/model/MergeGroupDedupTest.kt`: 7 cases
in your house style (`shouldBe`, `@Execution(ExecutionMode.CONCURRENT)`, backticked names, no mocks — the
helper is pure). Built and run with your own versions: `kotest-assertions-core 5.9.1` and `junit-jupiter
6.1.3` from `gradle/libs.versions.toml`, on JDK 17, through `junit-platform-console-standalone`:

```
[ 7 tests successful ]
[ 0 tests failed     ]
```

The cases: empty membership is identity; ungrouped items always survive; only the first member of a group
survives; input order (not id) decides the survivor; interleaved groups keep the first of each; grouped and
ungrouped mix correctly; a 1000-item list over 10 groups collapses to exactly 10 without mutating the input.
Your provenance guard was re-run over both commits: `0 violation(s), 0 warning(s)` → `✓ ok`.

**Not verified:** nothing was compiled *by Gradle* — there is no Android SDK or Gradle here, so SQLDelight
codegen, `spotlessCheck` and `detekt` have not run.

## Measurements (added later — these are real numbers, with their limits)

This issue originally said the performance argument was structural and carried no numbers. It now does.
Everything below was **executed**, on a desktop JVM and desktop SQLite — **not on an Android device** —
so read the ratios, not the absolute milliseconds.

The two paths being compared, on a simulated library of **50,000 favourite entries in 5,000 groups**:

```text
SQLite 3.46.1 · biblioteca simulada: 50000 entradas favoritas, 5000 grupos, 50000 pertenencias
  A) cargar TODA la pertenencia (getMemberships, 1 pasada): 22.38 ms  -> 50000 filas
  B) colapsar a uno por grupo en memoria (dedupeByMergeGroup): 5.12 ms -> 5000 supervivientes
  TOTAL ruta con pertenencia guardada (A+B): 27.50 ms para 50000 entradas
  C) detección por escaneo de título (el patrón real de animes.sq:128): 14.30 ms POR entrada (150 muestras)
     extrapolado a las 50000 entradas de la biblioteca: 714.8 s  (11.9 min)
  D) cociente: el escaneo por título cuesta 330× más que la pertenencia guardada en esta máquina
  E) una consulta getGroupId con el índice: 0.1184 ms
```

And the same comparison inside the JVM, using the `dedupeByMergeGroup` that this proposal ships versus a
faithful in-memory replica of the title-scan predicate (`lower(title) LIKE '%'||lower(:title)||'%'`):

```text
dedupeByMergeGroup (pertenencia guardada, el código del parche):
  n=5000    dedupeByMergeGroup                 ->    500 supervivientes en      5.67 ms
  n=20000   dedupeByMergeGroup                 ->   2000 supervivientes en     12.61 ms
  n=50000   dedupeByMergeGroup                 ->   5000 supervivientes en     25.00 ms
  n=200000  dedupeByMergeGroup                 ->  20000 supervivientes en     50.78 ms
escaneo por título (lo que hace hoy la detección de duplicados):
  n=1000    escaneoPorTitulo                   ->   1000 supervivientes en     42.91 ms
  n=2000    escaneoPorTitulo                   ->   2000 supervivientes en     37.45 ms
  n=4000    escaneoPorTitulo                   ->   4000 supervivientes en     75.29 ms
  n=8000    escaneoPorTitulo                   ->   8000 supervivientes en    300.62 ms
  n=16000   escaneoPorTitulo                   ->  16000 supervivientes en   1509.45 ms
```

What the two blocks say together:

- **Stored membership is linear.** Loading all 50,000 memberships plus collapsing to one item per group
  costs 27.5 ms; at 200,000 items the in-memory dedupe still costs 50.8 ms. Double the data, roughly
  double the time.
- **Title scanning is quadratic where it matters.** The in-memory replica goes 75 ms → 300 ms → 1,509 ms
  for 4k → 8k → 16k items: each doubling costs about 4-5×.
- **The per-add cost is the one users actually feel.** One duplicate check against a 50,000-entry library
  costs 14.3 ms of title scanning today, and that number grows with library size; a single indexed
  `getGroupId` lookup costs 0.12 ms and does not grow at all. Scanning every entry of that library the
  same way extrapolates to ~12 minutes, which is why a "find my duplicates" tool cannot be built on the
  scan.

Limits, stated plainly: x86 desktop JVM (Temurin 17.0.13) and SQLite 3.46.1, single run per size, no
device, no cold-start, no Compose, no real user data distribution; the extrapolation multiplies a
per-entry measurement, and the in-memory replica is my re-implementation of the SQL predicate, not your
code. The `animes`/`mangas` rows are synthetic titles with no substring overlap — with overlapping titles
the scan short-circuits earlier and looks faster than it is (that artefact fooled the first run of this
measurement).
## What we did NOT verify

- Sample code is **not compiled** and not run: no Android SDK/Gradle/`kotlinc` here. Signatures were matched by reading your sources (`GetLibraryAnime.await(): List<LibraryAnime>`, `ActivityLogRepository.getCountsByPeriod(Date): Map<Pair<Long, Int>, Long>`, `SourceHealthCache.getStatus(): NodeStatus`, `Anime.parentId`, the `animes`/`episodes` schema) and Reikai's.
- Partial-index columns were checked against the real schemas: `animes.favorite` / `animes.date_added` (`animes.sq:18,25`) and `episodes.seen` (`episodes.sq:9`). AniZen already indexes the favourite predicate (`animes.sq:43`), so only the unseen-episode index is proposed.
- We read Reikai at `00206fe6` only, and skipped its novel side (`content_type = 1`), which AniZen has no counterpart for.
- No library size was measured **on a device**: the desktop JVM/SQLite numbers above are ratios, not device timings.
- The benchmark `packageName` in the profile sketch is a guess; use your real benchmark application id.

Happy to send this as a PR split in four commits: schema + carry-over migration, dedupe helper +
count agreement, duplicate prompt ranked by `activity_log`, baseline-profile module + indexes.
