package tachiyomi.domain.source.interactor

import io.kotest.matchers.shouldBe
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flowOf
import kotlinx.coroutines.test.runTest
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.parallel.Execution
import org.junit.jupiter.api.parallel.ExecutionMode
import tachiyomi.domain.source.model.FeedSavedSearch
import tachiyomi.domain.source.model.FeedSavedSearchUpdate
import tachiyomi.domain.source.model.SavedSearch
import tachiyomi.domain.source.repository.FeedSavedSearchRepository
import tachiyomi.domain.source.service.FeedLimits

// ANZ -->
@Execution(ExecutionMode.CONCURRENT)
class InsertFeedSavedSearchTest { // ANZ

    private val limit = FeedLimits.MAX_SOURCES_PER_TAB

    /**
     * In-memory double rather than a mock: the cap depends on what the repository already holds for a
     * category, and a fake makes that state explicit instead of stubbing it per test.
     */
    private class InMemoryFeedSavedSearchRepository : FeedSavedSearchRepository {
        val rows = mutableListOf<FeedSavedSearch>()
        var inserts = 0
        var bulkInserts = 0
        var failOnInsert = false
        private var nextId = 1000L

        fun fill(category: Long, count: Int) {
            repeat(count) { rows += entry(nextId++, category) }
        }

        private fun entry(id: Long, category: Long) = FeedSavedSearch(
            id = id,
            source = id,
            savedSearch = null,
            global = true,
            feedOrder = id,
            type = FeedSavedSearch.Type.Latest.value,
            category = category,
        )

        override suspend fun getGlobal(categoryId: Long): List<FeedSavedSearch> =
            rows.filter { it.global && it.category == categoryId }

        override fun getGlobalAsFlow(categoryId: Long): Flow<List<FeedSavedSearch>> =
            flowOf(rows.filter { it.global && it.category == categoryId })

        override suspend fun getGlobalFeedSavedSearch(categoryId: Long): List<SavedSearch> = emptyList()

        override suspend fun countGlobal(categoryId: Long): Long = getGlobal(categoryId).size.toLong()

        override suspend fun getBySourceId(sourceId: Long): List<FeedSavedSearch> =
            rows.filter { it.source == sourceId }

        override fun getBySourceIdAsFlow(sourceId: Long): Flow<List<FeedSavedSearch>> =
            flowOf(rows.filter { it.source == sourceId })

        override suspend fun getBySourceIdFeedSavedSearch(sourceId: Long): List<SavedSearch> = emptyList()

        override suspend fun countBySourceId(sourceId: Long): Long = getBySourceId(sourceId).size.toLong()

        override suspend fun delete(feedSavedSearchId: Long) {
            rows.removeAll { it.id == feedSavedSearchId }
        }

        override suspend fun insert(feedSavedSearch: FeedSavedSearch): Long? {
            if (failOnInsert) throw IllegalStateException("insert failed")
            inserts++
            rows += feedSavedSearch.copy(id = nextId++)
            return rows.last().id
        }

        override suspend fun insertAll(feedSavedSearch: List<FeedSavedSearch>) {
            bulkInserts += feedSavedSearch.size
            rows += feedSavedSearch
        }

        override suspend fun updatePartial(update: FeedSavedSearchUpdate) = Unit

        override suspend fun updatePartial(updates: List<FeedSavedSearchUpdate>) = Unit
    }

    private fun newEntry(source: Long, category: Long, global: Boolean = true) = FeedSavedSearch(
        id = -1,
        source = source,
        savedSearch = null,
        global = global,
        feedOrder = 0,
        type = FeedSavedSearch.Type.Latest.value,
        category = category,
    )

    @Test
    fun `await inserts while the tab is below the cap`() = runTest {
        val repo = InMemoryFeedSavedSearchRepository().apply { fill(1, limit - 1) }
        InsertFeedSavedSearch(repo).await(newEntry(99, 1)) shouldBe 1000L + limit - 1
        repo.inserts shouldBe 1
    }

    @Test
    fun `await refuses at the cap and never touches the repository`() = runTest {
        val repo = InMemoryFeedSavedSearchRepository().apply { fill(1, limit) }
        InsertFeedSavedSearch(repo).await(newEntry(99, 1)) shouldBe null
        repo.inserts shouldBe 0
    }

    @Test
    fun `the cap is per tab, not global`() = runTest {
        val repo = InMemoryFeedSavedSearchRepository().apply { fill(1, limit) }
        InsertFeedSavedSearch(repo).await(newEntry(99, 2)) shouldBe repo.rows.last().id
        repo.inserts shouldBe 1
    }

    @Test
    fun `source specific feeds are not capped`() = runTest {
        val repo = InMemoryFeedSavedSearchRepository().apply { fill(1, limit) }
        InsertFeedSavedSearch(repo).await(newEntry(99, 1, global = false)) shouldBe repo.rows.last().id
        repo.inserts shouldBe 1
    }

    @Test
    fun `awaitAll is not capped so restoring a backup cannot lose entries`() = runTest {
        val repo = InMemoryFeedSavedSearchRepository().apply { fill(1, limit) }
        InsertFeedSavedSearch(repo).awaitAll((1..50).map { newEntry(it.toLong(), 1) })
        repo.bulkInserts shouldBe 50
    }

    @Test
    fun `await still returns null when the repository throws`() = runTest {
        val repo = InMemoryFeedSavedSearchRepository().apply { failOnInsert = true }
        InsertFeedSavedSearch(repo).await(newEntry(99, 1)) shouldBe null
    }
}
// ANZ <--
