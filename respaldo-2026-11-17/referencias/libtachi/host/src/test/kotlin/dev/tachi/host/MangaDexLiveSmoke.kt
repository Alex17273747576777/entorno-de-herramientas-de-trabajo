package dev.tachi.host

import eu.kanade.tachiyomi.source.online.HttpSource
import kotlinx.coroutines.runBlocking
import java.io.File

/** Arnés local opt-in; no forma parte de cero-X ni de los tests automáticos. */
object MangaDexLiveSmoke {
    @JvmStatic
    fun main(args: Array<String>) {
        val apk = File(args.single()).absoluteFile
        val data = File.createTempFile("cerox-libtachi-", "-data").apply {
            delete()
            mkdirs()
        }
        TachiRuntime.init(RuntimeConfig(dataDir = data.absolutePath, userAgent = "cero-X-host16-verification"))
        val info = ExtensionLoader.install(apk)
        val loaded = ExtensionLoader.extension(info.pkg) ?: error("Extensión no registrada")
        val source = loaded.sources.filterIsInstance<HttpSource>().first { it.lang == "en" }
        println("JVM_NOX_LOAD_OK paquete=${info.pkg} fuentes=${loaded.sources.size}")
        val result = runBlocking { source.getSearchManga(1, "Solo Leveling", source.getFilterList()) }
        check(result.mangas.isNotEmpty()) { "Búsqueda vacía" }
        println("JVM_NOX_SEARCH_OK resultados=${result.mangas.size}")
        val update = runBlocking {
            source.getMangaUpdate(result.mangas.first(), emptyList(), fetchDetails = true, fetchChapters = true)
        }
        check(update.chapters.isNotEmpty()) { "Sin capítulos" }
        println("JVM_NOX_DETAIL_OK capitulos=${update.chapters.size}")
        val pages = runBlocking { source.getPageList(update.chapters.first()) }
        check(pages.isNotEmpty()) { "Sin páginas" }
        println("JVM_NOX_PAGES_OK paginas=${pages.size}")
        val bytes = runBlocking {
            val page = pages.first()
            if (page.imageUrl == null) page.imageUrl = source.getImageUrl(page)
            source.getImage(page).use { it.body.bytes() }
        }
        check(bytes.size > 1000) { "Imagen vacía" }
        check(
            bytes.take(4) == listOf(0x89.toByte(), 0x50, 0x4e, 0x47) ||
                bytes.take(2) == listOf(0xff.toByte(), 0xd8.toByte()) ||
                bytes.take(4) == "RIFF".toByteArray().toList(),
        ) { "Cabecera de imagen desconocida" }
        println("JVM_NOX_IMAGE_OK bytes=${bytes.size}")
    }
}
