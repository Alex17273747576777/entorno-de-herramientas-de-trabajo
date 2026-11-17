import android.util.Log
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flowOf
import kotlinx.coroutines.runBlocking
import tachiyomi.domain.source.interactor.InsertFeedSavedSearch
import tachiyomi.domain.source.model.FeedSavedSearch
import tachiyomi.domain.source.model.FeedSavedSearchUpdate
import tachiyomi.domain.source.model.SavedSearch
import tachiyomi.domain.source.repository.FeedSavedSearchRepository
import tachiyomi.domain.source.service.FeedLimits

// Doble del repositorio: guarda en memoria y cuenta cuántas inserciones reales hizo.
class FakeRepo : FeedSavedSearchRepository {
    val filas = mutableListOf<FeedSavedSearch>()
    var inserciones = 0
    var insercionesMasivas = 0
    private var siguiente = 1000L
    private fun entrada(id: Long, fuente: Long, cat: Long) = FeedSavedSearch(
        id = id, source = fuente, savedSearch = null, global = true,
        feedOrder = id, type = 1, category = cat,
    )
    override suspend fun getGlobal(categoryId: Long): List<FeedSavedSearch> =
        filas.filter { it.global && it.category == categoryId }
    override fun getGlobalAsFlow(categoryId: Long): Flow<List<FeedSavedSearch>> =
        flowOf(filas.filter { it.global && it.category == categoryId })
    override suspend fun getGlobalFeedSavedSearch(categoryId: Long): List<SavedSearch> = emptyList()
    override suspend fun countGlobal(categoryId: Long): Long = getGlobal(categoryId).size.toLong()
    override suspend fun getBySourceId(sourceId: Long): List<FeedSavedSearch> = filas.filter { it.source == sourceId }
    override fun getBySourceIdAsFlow(sourceId: Long): Flow<List<FeedSavedSearch>> =
        flowOf(filas.filter { it.source == sourceId })
    override suspend fun getBySourceIdFeedSavedSearch(sourceId: Long): List<SavedSearch> = emptyList()
    override suspend fun countBySourceId(sourceId: Long): Long = getBySourceId(sourceId).size.toLong()
    override suspend fun delete(feedSavedSearchId: Long) { filas.removeAll { it.id == feedSavedSearchId } }
    override suspend fun insert(feedSavedSearch: FeedSavedSearch): Long? {
        inserciones++; filas += feedSavedSearch.copy(id = siguiente++); return filas.last().id
    }
    override suspend fun insertAll(feedSavedSearch: List<FeedSavedSearch>) {
        insercionesMasivas += feedSavedSearch.size; filas += feedSavedSearch
    }
    override suspend fun updatePartial(update: FeedSavedSearchUpdate) {}
    override suspend fun updatePartial(updates: List<FeedSavedSearchUpdate>) {}
    fun rellena(cat: Long, n: Int) { repeat(n) { filas += entrada(siguiente++, it.toLong() + 1, cat) } }
}

var fallos = 0
fun chk(cond: Boolean, msg: String) { println((if (cond) "  ✓ " else "  ✗ ") + msg); if (!cond) fallos++ }

fun nueva(fuente: Long, cat: Long, global: Boolean = true) = FeedSavedSearch(
    id = -1, source = fuente, savedSearch = null, global = global, feedOrder = 0, type = 1, category = cat,
)

fun main() = runBlocking {
    val limite = FeedLimits.MAX_SOURCES_PER_TAB
    println("FeedLimits.MAX_SOURCES_PER_TAB = $limite")

    println("caso 1: pestaña con ${limite - 1} entradas -> acepta la siguiente")
    var repo = FakeRepo(); repo.rellena(1, limite - 1)
    var r = InsertFeedSavedSearch(repo).await(nueva(99, 1))
    chk(r != null, "devuelve id ($r) e inserta de verdad (inserciones=${repo.inserciones})")
    chk(repo.inserciones == 1, "una sola inserción en el repositorio")

    println("caso 2: pestaña llena ($limite) -> rechaza")
    repo = FakeRepo(); repo.rellena(1, limite)
    Log.capturados.clear()
    r = InsertFeedSavedSearch(repo).await(nueva(99, 1))
    chk(r == null, "devuelve null (la señal de fallo que ya existía)")
    chk(repo.inserciones == 0, "NO llega a tocar el repositorio (inserciones=0)")
    // La librería logcat real no escribe fuera de un runtime Android, así que el efecto de log NO es
    // observable aquí. Se informa, no se cuenta como fallo: lo que importa es que el rechazo ocurrió.
    println("  · log capturado por el doble de android.util.Log: ${Log.capturados.size} línea(s) " +
        "(la librería logcat no escribe fuera de un dispositivo; efecto de log NO verificado)")

    println("caso 3: el tope es por pestaña, no global")
    repo = FakeRepo(); repo.rellena(1, limite)
    r = InsertFeedSavedSearch(repo).await(nueva(99, 2))
    chk(r != null, "la pestaña 2 acepta aunque la 1 esté llena")

    println("caso 4: las entradas de fuente (global=false) no se topán")
    repo = FakeRepo(); repo.rellena(1, limite)
    r = InsertFeedSavedSearch(repo).await(nueva(99, 1, global = false))
    chk(r != null, "un feed específico de fuente se inserta aunque la pestaña 1 esté llena")

    println("caso 5: awaitAll (restauración) NO se topa")
    repo = FakeRepo(); repo.rellena(1, limite)
    val lote = (1..50).map { nueva(it.toLong(), 1) }
    InsertFeedSavedSearch(repo).awaitAll(lote)
    chk(repo.insercionesMasivas == 50, "las 50 entradas del lote pasan (restaurar un backup no pierde nada)")

    println("caso 6: frontera exacta")
    for (n in limite - 1..limite + 1) {
        repo = FakeRepo(); repo.rellena(1, n)
        val res = InsertFeedSavedSearch(repo).await(nueva(99, 1))
        println("    con $n entradas en la pestaña -> ${if (res != null) "acepta" else "rechaza"}")
    }
    repo = FakeRepo(); repo.rellena(1, limite - 1)
    chk(InsertFeedSavedSearch(repo).await(nueva(99, 1)) != null, "en ${limite - 1} acepta")
    repo = FakeRepo(); repo.rellena(1, limite)
    chk(InsertFeedSavedSearch(repo).await(nueva(99, 1)) == null, "en $limite rechaza")

    println(if (fallos == 0) "RESULTADO: SIN FALLOS" else "RESULTADO: $fallos FALLOS")
}
