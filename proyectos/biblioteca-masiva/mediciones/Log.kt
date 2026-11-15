package android.util

// Doble local de la plataforma: android.util.Log sólo existe en un dispositivo. Se registra todo lo
// que el código real intenta escribir para poder afirmar qué se logueó al rechazar una inserción.
object Log {
    val capturados = mutableListOf<String>()

    @JvmStatic
    fun println(priority: Int, tag: String?, msg: String?): Int {
        capturados += "p$priority [$tag] $msg"
        return (msg?.length ?: 0) + 1
    }

    @JvmStatic
    fun isLoggable(tag: String?, level: Int): Boolean = true

    @JvmStatic fun d(tag: String?, msg: String?): Int = println(3, tag, msg)
    @JvmStatic fun i(tag: String?, msg: String?): Int = println(4, tag, msg)
    @JvmStatic fun w(tag: String?, msg: String?): Int = println(5, tag, msg)
    @JvmStatic fun e(tag: String?, msg: String?): Int = println(6, tag, msg)
    @JvmStatic fun v(tag: String?, msg: String?): Int = println(2, tag, msg)
    @JvmStatic fun getStackTraceString(tr: Throwable?): String = tr?.stackTraceToString() ?: ""
}
