## Summary

ShinKu can hold a big library, but two things get in the way as it grows: **the same series from
two sources stays as two entries** unless the user notices and merges them by hand through the
legacy `merged` table, and **the library path has no compiled-profile or memoisation work** behind
it (`macrobenchmark` exists, `baseline-profile` does not).

[Reikai](https://github.com/unseensnick/Reikai) — same Mihon lineage, Apache-2.0, read at `main` =
`00206fe6ae0c6cf87e2f6114b59164ea295a6fd1` — solved both: membership in a merge group is a
**stored fact resolved by id lookup**, adding a same-titled series **offers to group it in one tap**
(default on), and every surface that counts titles goes through **one dedupe helper** so the counts
cannot disagree. On the performance side it ships a `baseline-profile` module, memoised bucket
assembly and stable Compose keys.

Mirror proposal on AniZen: https://github.com/salmanbappi/AniZen/issues/95. This issue is deliberately separate from #32 (feed tabs): different subsystem, independently
reviewable. Everything below cites real files in both repos; sample code matches your stack
(SQLDelight + Voyager + Compose + Injekt) and is **not compiled** — our environment has no Android
SDK/Gradle.

## Correction (verified after posting — read this first)

The first version of this issue said ShinKu had no duplicate detection. **That was wrong**, and the
real picture makes the proposal smaller and cheaper, not bigger:

- `getDuplicateLibraryManga` (`mangas.sq:122-149`) already finds same-title favourites, and its
  `chapter_counts` CTE already **excludes scanlators the user filtered out** — a nicer query than
  Reikai's.
- It is already wired into the browse UI: long-press an entry → if it is a favourite, remove it; else
  if duplicates exist, `Dialog.AddDuplicateManga(manga, duplicates)` (`BrowseSourceScreen.kt:269-278`,
  `BrowseSourceScreenModel.kt:448`), rendered by `DuplicateMangaDialog` (`presentation/manga/DuplicateMangaDialog.kt:81`,
  title `MR.strings.possible_duplicates_title`) with *add anyway* / *open* / *migrate*.
- The legacy `merged` table is richer than described: it already stores `chapter_priority` (the
  deduplication priority), `chapter_sort_mode`, `info_manga`, `get_chapter_updates`,
  `download_chapters`, has both FKs and both indexes, a manual editor (`ui/manga/merged/EditMergedManga*`)
  and backup support (`BackupMergedMangaReference`).

So ShinKu already has **detection** and **manual merge with priority-based chapter dedupe**. What is
actually missing is only: (1) a **"group these two" action in the dialog that already opens**, (2)
group membership as a `UNIQUE`-constrained table resolved by id lookup instead of a virtual source,
(3) a **refusal memory** so it stops asking about a pair, (4) **one dedupe helper** so every surface
counts a merged series once, (5) carry-over of out-of-DB state when a duplicate is folded away, and
(6) the **performance package** (baseline profiles, memoised buckets, stable keys).
The proposal below is re-scoped to exactly that; items 1 and 3 are small, and the existing
`chapter_priority` semantics can be kept as `source_priority`.

**Phase 1 of this proposal is up as a pull request:** #34 (`merge_group` + `merge_group_manga` in both
the `.sq` schema and `42.sqm`, plus `MergeGroupDedup.kt`; 3 files, +92, no behaviour change). The rest
of the phases below are design only.

## What ShinKu has today (verified)

| Area | File | State |
|---|---|---|
| Library query | `data/src/main/sqldelight/com/shinku/reader/view/libraryView.sq` | One view joining `mangas` + chapter aggregates + categories |
| Indexes | `migrations/13.sqm:225-228` (`chapters_manga_id_index`, `chapters_unread_by_manga_index … WHERE read = 0`, `library_favorite_index ON mangas(favorite) WHERE favorite = 1`), `migrations/14.sqm:52`, `migrations/29.sqm:8` | Both hot library predicates are **already covered**: favourite entries (`library_favorite_index … WHERE favorite = 1`) and unread chapters (`chapters_unread_by_manga_index … WHERE read = 0`) |
| Duplicate detection | `data/src/main/sqldelight/com/shinku/reader/data/mangas.sq:122-149` (`getDuplicateLibraryManga`), `domain/.../manga/interactor/GetDuplicateLibraryManga.kt`, wired at `ui/browse/source/browse/BrowseSourceScreen.kt:271` and `BrowseSourceScreenModel.kt:96,397,448`, dialog `presentation/manga/DuplicateMangaDialog.kt:81` | **Already exists and is smarter than a plain title match**: a `duplicates` CTE over favourites with `lower(title) LIKE '%' \|\| lower(:title) \|\| '%'`, plus a `chapter_counts` CTE that **excludes scanlators in `excluded_scanlators`**. The dialog offers *add anyway* / *open the existing one* / *migrate* — what it does **not** offer is grouping them |
| Group persistence | `merged.sq` columns `info_manga`, `get_chapter_updates`, `chapter_sort_mode`, `chapter_priority`, `download_chapters`, `merge_id`, `merge_url`, `manga_id`, `manga_url`, `manga_source`; FK `ON DELETE SET NULL` (member) / `ON DELETE CASCADE` (merge); indexes `merged_merge_id_index`, `merged_manga_id_index`; editor `ui/manga/merged/EditMergedManga*`; backup `data/backup/models/BackupMergedMangaReference.kt` | Per-merge settings including a **chapter priority used for deduplication** and sort modes — the trunk-source idea is already here, in a table shaped as a virtual source rather than as a group |
| Profiling | `macrobenchmark/` exists; **no `baseline-profile/` module** | Startup and library scroll are not covered by a shipped profile |
| Library UI | `app/src/main/java/com/shinku/reader/ui/library/LibraryScreenModel.kt` | Compose + ScreenModel |

## What Reikai does (verified, with the design reasoning it documents itself)

**Persisted groups instead of re-derived ones.** `data/src/main/sqldelight/tachiyomi/data/merge_group.sq`
opens with its own rationale: *"Replaces the pref-derived grouping: membership is a stored fact
resolved by id lookup, not re-derived per call from prefs plus a same-title scan. The FK cascade from
the member tables removes a member automatically when its entry row is deleted, which closes the
stale-pref id-reuse capture the pref system had."*

- `merge_group(_id, content_type, title_override, cover_override, override_source_ranking)` — one
  table shared by manga and novels through a `content_type` discriminator (0 = manga, 1 = novel).
- `merge_group_manga(_id, group_id, manga_id, source_priority)` with `UNIQUE(manga_id)` (an entry
  belongs to **at most one** group, and that unique index also serves the reverse lookup) plus FK
  `ON DELETE CASCADE` to both `merge_group` and `manga`; twin table `merge_group_novel`.
- `CREATE INDEX idx_merge_group_manga_group_id ON merge_group_manga(group_id)`.

**One-tap grouping on add, on by default — and honest about what it is.**
`app/src/main/java/reikai/domain/library/ReikaiLibraryPreferences.kt:161`:
```kotlin
/** Whether adding a same-titled series offers to group it with the match. Repurposed from silent
 *  auto-merge; the one-time pref-to-group migration also reads it. */
val autoMergeSameTitle: Preference<Boolean> = preferenceStore.getBoolean("auto_merge_same_title", true)
```
surfaced in `presentation/browse/DuplicatePrompt.kt:32` (`suggestGroup = mergeManager.suggestGroupingOnAdd`)
and in settings at `SettingsLibraryScreen.kt:148`. So the user gets **a prompt with the match already
found**, not a silent rewrite — and the pref doubles as the flag the one-time migration reads to
rebuild the groups a silent auto-merge would have formed (`MergeGroupReconstruction.kt:31`).

**Explicit "never group these two".** `mangaManualUnmerges` = normalised `"min,max"` id pairs that
must never be grouped (`ReikaiLibraryPreferences.kt:154-158`) — the escape hatch that makes an
on-by-default suggestion safe.

**One definition of "count a merged series once".** `app/src/main/java/reikai/domain/merge/MergeGroupDedup.kt`:
`dedupeByMergeGroup(membership, id)`, `EntryMergeManager.onePerSeries(items, id)` and
`bucketByMergeGroup(membership, mergingEnabled, id)` — documented as *"One definition of 'count a
merged series once', so the surfaces counting titles cannot disagree."*

**Stitched chapter list with a trunk source.** `preferredMangaSources` (ranked source ids) picks the
trunk; `MergedGroupStitcher`, `ReconcileMergedChapters`, `ChapterGap`, `StoredStitch`,
`GroupChapterSettings`/`GroupChapterFlags` do the merge of chapter lists, and `merged_chapter_unit.sq`
persists the result. Trackers mirror to every member (`syncTrackerLinksGrouped`, default true), and
`handOutTrackersBeforeRemoval` moves them off an entry before it leaves a group.

**State outside the DB follows the survivor.** `dedupe_merged_ids.sq` (`dedupe_merged_ids`,
`dedupe_merged_chapter_ids`) records what the dedupe migrations merged away so a custom cover or a
download folder keyed by the discarded id/title can be carried over; `MergedDuplicateCarryMigration`
consumes and empties it.

**Performance package.** `baseline-profile/` module (`BaselineProfileGenerator`,
`StartupProfileGenerator`, `StartupBenchmarks`, `constants.kt`) on top of `macrobenchmark`; 10 SQL
views (`libraryView`, `recentsUnread`, `recentlyAddedView`, `updatesView`, `historyView` + novel
twins); `libraryView.sq` carries a comment about the slowest part of the query (joining history to
every chapter) and only pays it for entries that actually have excluded scanlators, via
`CASE WHEN EXISTS (…)`. Memoised assembly in `presentation/library/LibraryAssembly.kt:100`
(`itemsByKey.getOrPut(bucket.key) { items(bucket) }`) and stable keys in
`presentation/library/ReikaiLibraryContent.kt:238`
(`key = { "reikai_cell_${bucket.key}_${it.entryId.contentType}_${it.entryId.rawId}" }`).

**Tests that pin the semantics**: `EntryMergeManagerTest`, `RestoreMergeGroupsTest`,
`MergeGroupReconstructionTest`, `RenderMergedReadingOrderTest`, `MergedDuplicateCarryMigrationTest`,
`MigrateMergePrefsToGroupsMigrationTest`, `MergedResumeDownloadedConformanceTest`.

## Proposal for ShinKu

1. **Persisted merge groups** (`merge_group` + `merge_group_manga`) alongside — not on top of — the
   legacy `merged` table, with a migration that moves every existing `merged` row into a group and
   carries its cover/downloads. Keep `UNIQUE(manga_id)` and the FK cascades: they are what makes a
   big library cheap and self-cleaning.
2. **One more action in the dialog you already show**: `DuplicateMangaDialog` gains *Group with «X»* next to
   *add anyway* / *open* / *migrate*, plus *don't ask again for this pair* (the `manualUnmerges` memory).
   Default on, never silent — Reikai calls the same thing `suggestGroupingOnAdd`.
3. **One dedupe helper** (`dedupeByMergeGroup` / `onePerSeries`) used by the library grid, badges,
   the updates screen, global search results and the feed rows from #32, so no two surfaces report
   different totals.
4. **Trunk-source stitching** for the chapter list of a group, with a ranked preferred-source
   preference and gap handling, replacing the virtual `MergedSource` path for new merges (keep the
   old one working for existing users until they migrate).
5. **Performance package**: add a `baseline-profile` module next to `macrobenchmark`; memoise library
   bucket assembly per key; stable Compose keys for cells; keep `libraryView` from paying the history
   join when nothing excludes scanlators. (No new indexes: `migrations/13.sqm:226,228` already cover
   the unread-chapter and favourite predicates.)
6. **Tests** mirroring Reikai's: group reconstruction from prefs, restore, render order of a stitched
   list, carry-over of covers/downloads, and the "counts agree everywhere" property.

## Sample code

<details>
<summary><b>1. <code>data/src/main/sqldelight/com/shinku/reader/data/merge_group.sq</code> (new)</b></summary>

```sql
-- Membership is a stored fact resolved by id lookup, not re-derived per call from preferences plus
-- a same-title scan. The FK cascades remove a member automatically when its manga row is deleted,
-- which closes the stale-pref id-reuse capture a pref-derived grouping has.
CREATE TABLE merge_group (
    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title_override TEXT,
    cover_override TEXT,
    override_source_ranking INTEGER AS Boolean NOT NULL DEFAULT 0
);

-- UNIQUE(manga_id): a manga belongs to at most one group, and the same index serves the reverse
-- lookup "which group is this manga in". Moving an entry is an explicit delete + insert.
CREATE TABLE merge_group_manga (
    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    group_id INTEGER NOT NULL,
    manga_id INTEGER NOT NULL,
    source_priority INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY(group_id) REFERENCES merge_group (_id) ON DELETE CASCADE,
    FOREIGN KEY(manga_id) REFERENCES mangas (_id) ON DELETE CASCADE,
    UNIQUE(manga_id)
);

CREATE INDEX merge_group_manga_group_id_index ON merge_group_manga(group_id);

getGroupId:
SELECT group_id FROM merge_group_manga WHERE manga_id = :mangaId;

getMembers:
SELECT manga_id FROM merge_group_manga WHERE group_id = :groupId ORDER BY source_priority, manga_id;

-- one row per grouped manga: what the dedupe helper consumes in a single query
getLibraryMemberships:
SELECT manga_id, group_id FROM merge_group_manga;

insertGroup:
INSERT INTO merge_group DEFAULT VALUES;

insertMember:
INSERT INTO merge_group_manga (group_id, manga_id, source_priority)
VALUES (:groupId, :mangaId, :sourcePriority);

removeMember:
DELETE FROM merge_group_manga WHERE manga_id = :mangaId;

deleteGroup:
DELETE FROM merge_group WHERE _id = :groupId;

selectLastInsertedRowId:
SELECT last_insert_rowid();
```
</details>

<details>
<summary><b>2. <code>domain/.../manga/interactor/SuggestDuplicateGroup.kt</code> (new) — the prompt on add</b></summary>

```kotlin
package com.shinku.reader.domain.manga.interactor

import com.shinku.reader.domain.library.model.LibraryManga
import com.shinku.reader.domain.manga.model.Manga

/**
 * Finds the favourite that a newly added series most likely duplicates.
 *
 * Title match is normalised (case, punctuation, the "(Digital)" / "[Scanlator]" decorations sources
 * add) and a pair the user already refused is never suggested again. No network, no new state: it
 * reads the library the caller already has.
 */
class SuggestDuplicateGroup(
    private val getLibraryManga: GetLibraryManga,
    private val libraryPreferences: LibraryPreferences,   // holds the refused pairs
) {

    suspend fun await(added: Manga): LibraryManga? {
        if (!libraryPreferences.autoMergeSameTitle().get()) return null
        val key = normalise(added.title)
        val refused = libraryPreferences.manualUnmerges().get()
        return getLibraryManga.await()
            .filter { it.manga.id != added.id }
            .firstOrNull { candidate ->
                normalise(candidate.manga.title) == key &&
                    !refused.contains(pairKey(added.id, candidate.manga.id))
            }
    }

    private fun pairKey(a: Long, b: Long): String = "${minOf(a, b)},${maxOf(a, b)}"

    private fun normalise(title: String): String = title
        .lowercase()
        .replace(Regex("""[\[\(][^\]\)]*[\]\)]"""), " ")   // [Scanlator] / (Digital)
        .replace(Regex("""[^a-z0-9]+"""), " ")
        .trim()
}
```

The UI side is a dialog on the "added to library" path (`presentation/browse/DuplicatePrompt.kt` in
Reikai is a ~40-line composable worth copying): *Group with «X»?* → `mergeManager.merge(ids)` /
*Keep separate* → remember `pairKey` in `manualUnmerges`.
</details>

<details>
<summary><b>3. <code>domain/.../manga/model/MergeGroupDedup.kt</code> (new) — one definition of "count once"</b></summary>

```kotlin
package com.shinku.reader.domain.manga.model

/**
 * One item per merge group: the first item whose entry belongs to a group keeps it, later members of
 * that group drop out, and an ungrouped entry always stays.
 *
 * One definition of "count a merged series once", so the library grid, the badges, the updates
 * screen and the feed rows cannot disagree about the total. Order decides the survivor: hand in a
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
<summary><b>4. Preferences (<code>LibraryPreferences</code>) — default on, with the escape hatch</b></summary>

```kotlin
/** Whether adding a same-titled series offers to group it with the match. Never silent. */
fun autoMergeSameTitle() = preferenceStore.getBoolean("auto_merge_same_title", true)

/** Normalised "min,max" id pairs the user refused: never suggested again. */
fun manualUnmerges() = preferenceStore.getStringSet("merge_manual_unmerges", emptySet())

/** Source ids ranked highest-priority-first: the trunk source when stitching a merged chapter list. */
fun preferredMergeSources() = preferenceStore.getObject(
    "merge_preferred_sources",
    { it.decodeLongArray() },
    { o, v -> o.encodeLongArray(v) },
    emptyList(),
)
```
</details>

<details>
<summary><b>5. Migration — carry the legacy <code>merged</code> rows into groups</b></summary>

```kotlin
package com.shinku.reader.core.migration.migrations

import com.shinku.reader.core.common.util.lang.withIOContext
import com.shinku.reader.core.migration.Migration
import com.shinku.reader.core.migration.MigrationContext
import com.shinku.reader.domain.manga.repository.MergeGroupRepository   // new

/**
 * Every legacy merged manga becomes one merge_group, and whatever state lived outside the database
 * under the discarded id or title (custom cover, download folder) is recorded so it can follow the
 * survivor. Idempotent: running it twice creates no second group.
 */
class MigrateLegacyMergedToGroupsMigration : Migration {
    override val version: Float = 77f   // 76f is the feed-categories one proposed in #32

    override suspend fun invoke(migrationContext: MigrationContext): Boolean = withIOContext {
        val groups = migrationContext.get<MergeGroupRepository>() ?: return@withIOContext false
        val legacy = groups.getLegacyMergedRows()          // merge_id -> member manga_ids
        if (legacy.isEmpty()) return@withIOContext true
        legacy.forEach { (mergeId, members) ->
            if (groups.groupIdOf(members.first()) == null) groups.createGroup(members)
        }
        return@withIOContext true
    }
}
```
</details>

<details>
<summary><b>6. <code>baseline-profile/</code> module (new) — you already have <code>macrobenchmark</code></b></summary>

```kotlin
// baseline-profile/build.gradle.kts — same shape Reikai ships
plugins {
    id("shinku.android.library")
    id("androidx.baselineprofile")
}

android {
    namespace = "com.shinku.reader.baselineprofile"
    defaultConfig { minSdk = 28 }
    targetProjectPath = ":app"
}

baselineProfile {
    // Profile the two paths that dominate a big library: cold start and library scroll.
    automaticGenerationDuringBuild = false
    saveInSrc = true
}

dependencies {
    implementation(libs.androidx.benchmark.macro.junit4)
}
```

```kotlin
// baseline-profile/src/main/kotlin/com/shinku/reader/baselineprofile/LibraryScrollProfile.kt
@RunWith(AndroidJUnit4::class)
class LibraryScrollProfile {
    @get:Rule val rule = BaselineProfileRule()

    @Test
    fun libraryScroll() = rule.collect(
        packageName = "com.shinku.reader",
        includeInStartupProfile = true,
    ) {
        startActivityAndWait()
        // Navigate to the library and scroll it: with a seeded large library this is the path
        // that pays for itself on a mid-range device.
        device.findObject(By.text("Library"))?.click()
        device.wait(Until.hasObject(By.res("com.shinku.reader", "library_grid")), 5_000)
        val grid = device.findObject(By.res("com.shinku.reader", "library_grid"))
        repeat(6) { grid?.fling(Direction.DOWN); device.waitForIdle() }
    }
}
```
</details>

<details>
<summary><b>7. Library path: memoised buckets + stable keys</b></summary>

```kotlin
// LibraryAssembly-style memoisation: build each bucket once per key, reuse across recompositions
private val itemsByKey = mutableMapOf<String, ImmutableList<LibraryItem>>()
fun itemsFor(bucket: LibraryBucket): ImmutableList<LibraryItem> =
    itemsByKey.getOrPut(bucket.key) { items(bucket) }

// Stable keys so a reorder or a merge does not invalidate every cell
LazyVerticalGrid(state = gridState) {
    items(
        items = bucketItems,
        key = { "cell_${bucket.key}_${it.manga.id}" },
        contentType = { it.contentType },
    ) { item -> LibraryItemCell(item) }
}
```
</details>

## Acceptance criteria

- [ ] Adding a series that duplicates a favourite offers to group it in one tap; the default is on; nothing is merged silently.
- [ ] "Don't ask again for this pair" persists and survives a restart and a backup restore.
- [ ] Group membership is a table lookup (`UNIQUE(manga_id)`), never a per-call same-title scan; deleting a member row cascades.
- [ ] Legacy `merged` rows migrate into groups exactly once, carrying covers/downloads.
- [ ] Library count, badges, updates and feed rows all report the same total for a merged series (one dedupe helper).
- [ ] A merged entry's chapter list is stitched from a ranked trunk source, with gaps handled and read state preserved.
- [ ] `baseline-profile` module exists and produces a profile covering cold start + library scroll.
- [ ] Tests pin: reconstruction from prefs, restore, stitched render order, carry-over, and count agreement.

## What we did NOT verify

- Sample code is **not compiled** and not run: no Android SDK/Gradle/`kotlinc` in our environment. Signatures were matched by reading your sources (`GetLibraryManga`, `MigrationContext.get<T>()`, `preferenceStore`, the `merged`/`mangas` schema) and Reikai's.
- We read Reikai at `00206fe6ae0c6cf87e2f6114b59164ea295a6fd1` only; its novel side (`content_type = 1`) has no ShinKu counterpart and was left out of the proposal.
- We did not measure any library size on a device: the performance claims are structural (stored membership, memoised buckets, stable keys, shipped profile), not benchmark numbers.
- The exact current semantics of `MergedSource` were read only where `MangaScreen` and `mangas.sq:189` touch it; if a rewrite migration is already planned, treat this as input.
- `preferenceStore.getObject` encoding for the ranked-source list is illustrative; use whatever your `PreferenceStore` already offers for ordered lists.

Happy to send this as a PR split in four commits: schema + migration, dedupe helper + count
agreement, duplicate prompt + preferences, baseline-profile module.
