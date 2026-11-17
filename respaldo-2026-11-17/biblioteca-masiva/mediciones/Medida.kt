// Medida real: pertenencia guardada (O(n)) contra escaneo por título (O(n²)) con el código publicado.
import tachiyomi.domain.anime.model.dedupeByMergeGroup

data class Entrada(val id: Long, val titulo: String)

// Réplica fiel de la lógica de getDuplicateLibraryAnime/animes.sq: lower(title) LIKE '%'||lower(:title)||'%'
fun dedupePorEscaneoDeTitulo(items: List<Entrada>): List<Entrada> {
    val vistos = mutableListOf<String>()
    val salida = mutableListOf<Entrada>()
    for (e in items) {
        val t = e.titulo.lowercase()
        var duplicado = false
        for (v in vistos) {
            if (v.contains(t) || t.contains(v)) { duplicado = true; break }
        }
        if (!duplicado) { vistos += t; salida += e }
    }
    return salida
}

fun mide(etiqueta: String, n: Int, bloques: Int, f: (List<Entrada>) -> List<Entrada>) {
    val items = (1L..n).map { Entrada(it, "entrada ${it.toString().padStart(7, '0')}") }
    val pertenencia = items.associate { it.id to (it.id % bloques) }
    System.gc(); val t0 = System.nanoTime()
    val r = f(items)
    val ms = (System.nanoTime() - t0) / 1_000_000.0
    println(String.format("  n=%-7d %-34s -> %6d supervivientes en %9.2f ms", n, etiqueta, r.size, ms))
}

val idDe: (Entrada) -> Long = { e -> e.id }

fun main() {
    println("dedupeByMergeGroup (pertenencia guardada, el código del parche):")
    for (n in intArrayOf(5_000, 20_000, 50_000, 200_000)) {
        val grupos = (n / 10).toLong()
        mide("dedupeByMergeGroup", n, n / 10) { l ->
            val pertenencia: Map<Long, Long> = l.associate { it.id to (it.id % grupos) }
            l.dedupeByMergeGroup(pertenencia, idDe)
        }
    }
    println("escaneo por título (lo que hace hoy la detección de duplicados):")
    for (n in intArrayOf(1_000, 2_000, 4_000, 8_000, 16_000)) mide("escaneoPorTitulo", n, n / 10, ::dedupePorEscaneoDeTitulo)
}
