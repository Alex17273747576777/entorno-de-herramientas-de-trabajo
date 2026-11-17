import io.github.labandita.glreborn.componerParte
import io.github.labandita.glreborn.primerFotogramaDeLaApp

val PILA_MIXTA = """io.github.labandita.glreborn.FalloRaro: algo
	at android.os.Handler.dispatchMessage(Handler.java:106)
	at io.github.labandita.glreborn.ui.Pantalla.dibujar(Pantalla.kt:157)
	at io.github.labandita.glreborn.MainActivity.onCreate(MainActivity.kt:88)"""

val PILA_SOLO_ANDROID = """java.lang.IllegalStateException: sin app
	at android.os.Handler.dispatchMessage(Handler.java:106)
	at android.app.ActivityThread.main(ActivityThread.java:8000)"""

val PILA_CLASE_NUESTRA = """io.github.labandita.glreborn.FalloRaro: la cabecera también menciona el paquete
	at android.os.Handler.dispatchMessage(Handler.java:106)
	at io.github.labandita.glreborn.core.Director.leer(Director.kt:42)"""

val PILA_CAUSA = """java.lang.RuntimeException: envoltorio
	at android.os.Handler.dispatchMessage(Handler.java:106)
Caused by: java.io.FileNotFoundException: /sdcard/x
	at io.github.labandita.glreborn.core.Escritor.guardar(Escritor.kt:31)
	... 4 more"""

var fallos = 0
fun caso(nombre: String, cond: Boolean, detalle: String = "") {
    println("${if (cond) "  [ok]   " else "  [FALLO]"} $nombre${if (cond) "" else "   → $detalle"}")
    if (!cond) fallos++
}

fun parte(pila: String, memoria: Boolean = false) = componerParte(
    fecha = "2026-11-17 11:00:00", contexto = "hilo main", version = "1.16.1",
    api = 33, modelo = "TECNO BG7", clase = "java.lang.IllegalStateException",
    mensaje = "boom", pila = pila, sinMemoria = memoria,
)

fun main() {
    println("=== primerFotogramaDeLaApp ===")
    caso("stack mixto → el fotograma de la app, con archivo y línea",
        primerFotogramaDeLaApp(PILA_MIXTA) == "at io.github.labandita.glreborn.ui.Pantalla.dibujar(Pantalla.kt:157)",
        primerFotogramaDeLaApp(PILA_MIXTA).toString())
    caso("excepción de clase nuestra → no devuelve la cabecera (el bug de extracto())",
        primerFotogramaDeLaApp(PILA_CLASE_NUESTRA) == "at io.github.labandita.glreborn.core.Director.leer(Director.kt:42)",
        primerFotogramaDeLaApp(PILA_CLASE_NUESTRA).toString())
    caso("stack sólo de Android → null, no una línea inventada",
        primerFotogramaDeLaApp(PILA_SOLO_ANDROID) == null, primerFotogramaDeLaApp(PILA_SOLO_ANDROID).toString())
    caso("pila vacía → null", primerFotogramaDeLaApp("") == null, "no null")
    caso("«Caused by» también cuenta: encuentra el fotograma tras la causa",
        primerFotogramaDeLaApp(PILA_CAUSA) == "at io.github.labandita.glreborn.core.Escritor.guardar(Escritor.kt:31)",
        primerFotogramaDeLaApp(PILA_CAUSA).toString())

    println("\n=== componerParte ===")
    val p = parte(PILA_MIXTA)
    println(p.lines().take(7).joinToString("\n") { "  | $it" })
    caso("el parte nombra el fotograma de la app antes del stack",
        p.indexOf("APP      at io.github.labandita.glreborn.ui.Pantalla.dibujar(Pantalla.kt:157)") in 1..p.indexOf("at android.os.Handler"),
        "la línea APP no está antes del stack")
    caso("sigue llevando el stack completo", p.contains("at io.github.labandita.glreborn.MainActivity.onCreate(MainActivity.kt:88)"), "falta")
    caso("lleva la versión, la API y el modelo", p.contains("VERSIÓN  1.16.1") && p.contains("ANDROID  API 33 · TECNO BG7"), "faltan cabeceras")
    caso("un fallo normal NO habla de memoria", !p.contains("MEMORIA") && !p.contains("CONSEJO"), "sobra MEMORIA")

    val sin = parte(PILA_SOLO_ANDROID)
    caso("sin fotograma de la app → no hay línea APP", !sin.contains("APP      "), "inventa un fotograma")
    caso("  …y el stack de Android sí está", sin.contains("at android.app.ActivityThread.main"), "falta el stack")

    val mem = parte(PILA_SOLO_ANDROID, memoria = true)
    println(mem.lines().take(9).joinToString("\n") { "  | $it" })
    caso("OutOfMemoryError → MEMORIA y CONSEJO", mem.contains("MEMORIA  sí") && mem.contains("CONSEJO"), "no lo dice")
    caso("  …y el consejo es el otro, no leer código", mem.contains("cerrad otras apps"), "consejo genérico")

    val larga = parte("x".repeat(9000))
    caso("un stack enorme se corta a 6000 (no revienta el fichero)",
        larga.length < 7000 && !larga.contains("x".repeat(6001)), "no se cortó")

    println("\nRESULTADO: ${if (fallos == 0) "TODOS LOS CASOS PASAN" else "$fallos FALLOS"}")
    kotlin.system.exitProcess(if (fallos == 0) 0 else 1)
}
