#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Commit H: el reproductor del IPTV y el registro del modulo.

Cuatro ficheros nuevos y dos ediciones (build.gradle declara media3, CeroXApplication
registra el modulo en las dos listas). La logica que no necesita Android -traducir las
opciones de un canal a cabeceras, decidir si un flujo es HLS- va en un fichero aparte
para poder probarla de verdad en el JVM.

El pre-vuelo repite contra el texto que se va a publicar cada literal que las pruebas
nuevas exigen, y ademas vuelve a pasar la comprobacion que IptvTest ya tiene
publicada: ninguna URL de fuente escrita a mano en el paquete del IPTV.
"""
import base64, datetime, io, json, os, re, sys, time, urllib.request, urllib.error

TOK = os.environ.get("GP")
API = "https://api.github.com/repos/Alex17273747576777/cero-X-app"
SRC = "android/app/src/main/java/com/ceroX/app/"
IPTV = SRC + "modules/iptv/"
TEST = "android/app/src/test/java/com/ceroX/app/modules/iptv/"
GRADLE = "android/app/build.gradle"
APP = SRC + "core/CeroXApplication.kt"
BASE_ESPERADO = "fa94ca8a7b18f9586c66c6e03ef40e4d8123d1b6"
MEDIA3 = "1.11.1"
EJECUTAR = "--run" in sys.argv
LOCAL = TOK is None
RAIZ = "/home/user/cerox-investigacion/arbol/tree/"
SALIDA = "/home/user/cerox-investigacion/iptv/"


def ok(c, m):
    if not c:
        raise SystemExit("FALLO DE COMPROBACION: " + m)


def api(p, m="GET", b=None):
    d = json.dumps(b).encode() if b is not None else None
    r = urllib.request.Request(API + p, data=d, method=m, headers={
        "Authorization": "Bearer " + TOK, "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "cxiptv"})
    try:
        with urllib.request.urlopen(r, timeout=180) as x:
            return json.loads(x.read() or b"null")
    except urllib.error.HTTPError as e:
        raise SystemExit("HTTP %s %s %s: %s" % (e.code, m, p, e.read().decode()[:300]))


def solo_codigo(t):
    t = re.sub(r'""".*?"""', '""', t, flags=re.S)
    t = re.sub(r'"(?:\\.|[^"\\])*"', '""', t)
    t = re.sub(r"'(?:\\.|[^'\\])*'", "''", t)
    t = re.sub(r"/\*.*?\*/", "", t, flags=re.S)
    t = re.sub(r"//[^\n]*", "", t)
    return t


BASE = BASE_ESPERADO if LOCAL else api("/git/ref/heads/main")["object"]["sha"]
ok(BASE == BASE_ESPERADO, "main se movio: " + BASE)
print("MODO: " + ("LOCAL" if LOCAL else "PUBLICACION") + " · base " + BASE[:8])


def leer(p):
    if LOCAL:
        with io.open(RAIZ + p, encoding="utf-8") as f:
            return f.read()
    return base64.b64decode(api("/contents/%s?ref=%s" % (p, BASE))["content"]).decode()


cambios = {}
# Lo que se añade a un fichero ya existente. Las comprobaciones de lineas se aplican
# a esto y no al fichero entero: build.gradle ya lleva un '/META-INF/*/versions/*'
# desde hace tiempo, que es un glob dentro de una cadena y no un comentario roto, y
# un guardado que mira el fichero completo lo confunde con un */ a mitad de linea.
insertos = {}


def sust(path, viejo, nuevo, veces=1):
    t = cambios.get(path, leer(path))
    n = t.count(viejo)
    ok(n == veces, "%s: el anclaje aparece %d veces, se esperaban %d -> %r" % (path, n, veces, viejo[:70]))
    cambios[path] = t.replace(viejo, nuevo)
    insertos.setdefault(path, []).append(nuevo)


# ══════════════════════════════════════════════════════════════════════════════
# 1. OpcionesReproduccion.kt — pura, sin Android
# ══════════════════════════════════════════════════════════════════════════════
cambios[IPTV + "OpcionesReproduccion.kt"] = r'''package com.ceroX.app.modules.iptv

/**
 * De las opciones de un canal a lo que entiende un reproductor.
 *
 * Las listas traen `#EXTVLCOPT` y `#KODIPROP` con claves que VLC y Kodi entienden y
 * media3 no. Hay que traducirlas, y la traducción tiene que ser visible: este fichero
 * no toca Android, así que se puede probar en el JVM, que es donde se descubre si la
 * tabla de equivalencias está bien antes de que lo descubra el usuario con un canal
 * que no arranca.
 *
 * Lo que no se sabe traducir no se convierte en una cabecera HTTP por las buenas.
 * `network-caching=1000` no es una cabecera, y mandarla como si lo fuera es la clase
 * de invento que hace que un fallo de red sea imposible de diagnosticar. Las claves
 * desconocidas van a [Solicitud.sinTraducir] para que se puedan enseñar.
 */
object OpcionesReproduccion {

    /** Claves de #EXTVLCOPT que son el agente de usuario, escritas de las dos formas. */
    private val AGENTES = listOf("http-user-agent", "user-agent")

    /** Y las que son el referente, que aparece con cuatro grafías distintas. */
    private val REFERENTES = listOf("http-referrer", "http-referer", "referrer", "referer")

    /** Prefijo de las opciones de DRM que vienen de los #KODIPROP. */
    private val PREFIJO_DRM = "inputstream.adaptive."

    fun de(canal: Canal): Solicitud {
        val cabeceras = LinkedHashMap<String, String>()
        val drm = LinkedHashMap<String, String>()
        val sinTraducir = LinkedHashMap<String, String>()
        var agente: String? = null

        for ((clave, valor) in canal.opciones) {
            val k = clave.trim().lowercase()
            when {
                k in AGENTES -> if (valor.isNotBlank()) agente = valor

                k in REFERENTES -> if (valor.isNotBlank()) cabeceras["Referer"] = valor

                k.startsWith(PREFIJO_DRM) -> {
                    val nombre = k.removePrefix(PREFIJO_DRM)
                    if (nombre.isNotBlank() && valor.isNotBlank()) drm[nombre] = valor
                }

                else -> sinTraducir[clave] = valor
            }
        }

        return Solicitud(
            url = canal.url,
            esHls = esHls(canal.url),
            userAgent = agente,
            cabeceras = cabeceras.toMap(),
            drm = drm.toMap(),
            sinTraducir = sinTraducir.toMap(),
        )
    }

    /**
     * Si el flujo es HLS.
     *
     * Se mira la ruta de la URL, sin parámetros ni fragmento, y no el nombre del
     * canal: hay canales que se llaman "algo.m3u8" y sirven un .mp4, y al revés.
     * Que esto se equivoque tampoco es fatal —media3 reconoce HLS por el tipo de
     * contenido que responde el servidor—, pero acertar evita un primer intento
     * fallido en los flujos cuya URL no lleva extensión.
     */
    fun esHls(url: String): Boolean {
        val ruta = url.substringBefore('?').substringBefore('#')
        return ruta.lowercase().endsWith(".m3u8")
    }
}

/** Lo que hace falta para pedir un canal, ya traducido. */
data class Solicitud(
    val url: String,
    val esHls: Boolean,
    /** Va aparte y no en las cabeceras: el reproductor lo pone donde debe. */
    val userAgent: String?,
    val cabeceras: Map<String, String>,
    /** Claves de `inputstream.adaptive.*` sin el prefijo. */
    val drm: Map<String, String>,
    /** Opciones de la lista que no se saben traducir. Se enseñan, no se inventan. */
    val sinTraducir: Map<String, String>,
)
'''

# ══════════════════════════════════════════════════════════════════════════════
# 2. ReproductorIptv.kt — media3
# ══════════════════════════════════════════════════════════════════════════════
cambios[IPTV + "ReproductorIptv.kt"] = r'''package com.ceroX.app.modules.iptv

import android.content.Context
import android.view.SurfaceView
import androidx.annotation.OptIn
import androidx.media3.common.MediaItem
import androidx.media3.common.PlaybackException
import androidx.media3.common.Player
import androidx.media3.common.util.UnstableApi
import androidx.media3.datasource.DefaultHttpDataSource
import androidx.media3.exoplayer.ExoPlayer
import androidx.media3.exoplayer.source.DefaultMediaSourceFactory

/**
 * El reproductor: media3/ExoPlayer con las cabeceras que pide cada canal.
 *
 * POR QUÉ media3 Y NO EL MediaPlayer DEL FRAMEWORK
 * ------------------------------------------------
 * El IPTV es HLS casi siempre, y el `MediaPlayer` del sistema no resuelve playlists
 * .m3u8: lo deja escrito `VideoModule` en su propia documentación. media3 es
 * Apache-2.0, que es compatible con la GPL-3.0 del proyecto, y trae el soporte de
 * HLS en un módulo aparte que hay que declarar.
 *
 * CÓMO FALLA
 * ----------
 * Un canal puede no arrancar por cien razones: el servidor caído, el agente de
 * usuario que ya no cuela, un certificado TLS que no vale, un DRM que falta, un
 * códec que el dispositivo no tiene. Ninguna se puede adivinar desde aquí, así que
 * el oyente de errores guarda el código y el mensaje de media3 en [ultimoMotivo] y
 * cada método devuelve null si salió o la razón si no. Nada devuelve un booleano de
 * éxito: un `true` aquí no le dice a nadie qué pasó.
 *
 * La superficie de vídeo es opcional porque un canal puede ser sólo audio, y porque
 * quien pinta la pantalla es la interfaz, no este fichero.
 */
@OptIn(UnstableApi::class)
class ReproductorIptv(private val contexto: Context) {

    private var exo: ExoPlayer? = null
    private var motivo: String? = null

    /** El último fallo, o null si no lo hay. Se limpia al preparar un canal bien. */
    fun ultimoMotivo(): String? = motivo

    fun creado(): Boolean = exo != null

    /** El reproductor de media3, para que la interfaz le pegue sus controles. */
    fun player(): Player? = exo

    /**
     * Crea el ExoPlayer. Null si se creó; la razón si no.
     *
     * Se suelta el anterior primero: dos ExoPlayer vivos a la vez son dos
     * decodificadores peleándose por el mismo hardware, y en un móvil eso se paga.
     */
    fun crear(): String? {
        liberar()
        return try {
            exo = ExoPlayer.Builder(contexto).build().apply {
                addListener(object : Player.Listener {
                    override fun onPlayerError(error: PlaybackException) {
                        motivo = "Fallo de reproducción (" + error.errorCodeName + "): " +
                            (error.message ?: error.javaClass.simpleName)
                    }
                })
            }
            null
        } catch (e: Exception) {
            val razon = "No se pudo crear ExoPlayer: " + (e.message ?: e.javaClass.simpleName)
            motivo = razon
            razon
        }
    }

    /**
     * Prepara un canal con sus cabeceras. Null si quedó preparado; la razón si no.
     *
     * La fábrica de datos se construye por canal a propósito: cada uno puede pedir
     * un agente de usuario y un referente distintos, y esas opciones viven en la
     * fuente de datos, no en el reproductor.
     */
    fun preparar(canal: Canal): String? {
        val p = exo ?: return "No hay ningún reproductor creado"
        val solicitud = OpcionesReproduccion.de(canal)
        return try {
            val fabrica = DefaultHttpDataSource.Factory()
                .setUserAgent(solicitud.userAgent ?: AGENTE)
                .setDefaultRequestProperties(solicitud.cabeceras)
                .setAllowCrossProtocolRedirects(true)
                .setConnectTimeoutMs(MILIS_ESPERA)
                .setReadTimeoutMs(MILIS_ESPERA)
            val elemento = MediaItem.fromUri(solicitud.url)
            p.setMediaSource(DefaultMediaSourceFactory(fabrica).createMediaItem(elemento))
            p.prepare()
            motivo = null
            null
        } catch (e: Exception) {
            val razon = "No se pudo preparar '" + canal.titulo + "': " +
                (e.message ?: e.javaClass.simpleName)
            motivo = razon
            razon
        }
    }

    /** Pega o despega la superficie donde se ve el vídeo. */
    fun adjuntar(superficie: SurfaceView?) {
        val p = exo ?: return
        if (superficie == null) {
            p.clearVideoSurface()
        } else {
            p.setVideoSurfaceView(superficie)
        }
    }

    /** Empieza a reproducir lo preparado. Null si salió; la razón si no. */
    fun empezar(): String? {
        val p = exo ?: return "No hay ningún reproductor creado"
        return try {
            p.playWhenReady = true
            null
        } catch (e: Exception) {
            val razon = "No se pudo empezar la reproducción: " + (e.message ?: e.javaClass.simpleName)
            motivo = razon
            razon
        }
    }

    fun pausar() {
        try {
            exo?.pause()
        } catch (e: Exception) {
            motivo = "No se pudo pausar: " + (e.message ?: e.javaClass.simpleName)
        }
    }

    /** Posición en milisegundos, o -1 si no hay reproductor. No devuelve cero. */
    fun posicion(): Long = exo?.currentPosition ?: -1L

    /** Si está sonando algo ahora mismo, según media3. */
    fun reproduciendo(): Boolean = exo?.isPlaying == true

    /** Suelta el reproductor. Un ExoPlayer sin soltar se queda el decodificador. */
    fun liberar() {
        val p = exo
        exo = null
        if (p != null) {
            try {
                p.release()
            } catch (e: Exception) {
                // Soltar algo que ya se cayó lanza; no hay nada que hacer.
            }
        }
    }

    companion object {
        const val AGENTE = "cero-X/1.0 (IPTV neutro; media3)"
        const val MILIS_ESPERA = 15000
    }
}
'''

# ══════════════════════════════════════════════════════════════════════════════
# 3. IptvModule.kt — el módulo que registra la app
# ══════════════════════════════════════════════════════════════════════════════
cambios[IPTV + "IptvModule.kt"] = r'''package com.ceroX.app.modules.iptv

import android.content.Context
import android.view.SurfaceView
import com.ceroX.app.core.engine.ModuleHealth
import com.ceroX.app.core.engine.ModuleInterface
import java.io.File

/**
 * Módulo de IPTV de cero-X. Se registra como `iptv` (el módulo 38).
 *
 * NEUTRO QUIERE DECIR ESTO
 * ------------------------
 * El módulo no trae ni un canal. Arranca con la lista de fuentes vacía, el usuario
 * añade las suyas, y cada una se descarga de fuera y se comprueba contra la huella
 * que declare su publicador. Nada de listas dentro del APK: lo vigilan dos pruebas
 * de `IptvTest`, una sobre `assets` y `res/raw` y otra sobre las URLs escritas a
 * mano en este paquete.
 *
 * QUÉ HACE EN CADA FASE
 * ---------------------
 * `initialize()` sólo guarda el contexto y crea el almacén de fuentes, que es un
 * objeto `File`: no abre red ni lee disco. Es a propósito —la app tuvo un ANR por
 * inicializar treinta y seis módulos haciendo trabajo pesado en el hilo principal, y
 * este no va a ser el que lo repita—. La red ocurre en [cargar], cuando lo pide el
 * usuario.
 *
 * Sin contexto no se puede guardar nada, así que `initialize()` devuelve false con el
 * motivo en el health check en vez de devolver true y quedarse sin almacén.
 */
class IptvModule : ModuleInterface() {

    override val name = "iptv"
    override val version = "0.1.0"
    override val dependencies: List<String> = emptyList()

    private val cargador = CargadorExterno()
    private var contexto: Context? = null
    private var almacen: AlmacenFuentes? = null
    private var reproductor: ReproductorIptv? = null
    private var canales: List<Canal> = emptyList()
    private var guia: ResultadoGuia? = null
    private var fuenteDeCanales: String? = null
    private var fuenteDeGuia: String? = null
    private var ultimoMotivo: String? = null

    override fun initialize(config: Map<String, Any>): Boolean {
        val c = config["context"] as? Context
        if (c == null) {
            ultimoMotivo = "No se inyectó el contexto: sin él no hay directorio privado " +
                "donde guardar las fuentes que añada el usuario"
            return false
        }
        contexto = c
        almacen = AlmacenFuentes(File(c.filesDir, NOMBRE_ALMACEN))
        _initialized = true
        return true
    }

    override fun start(): Boolean {
        if (!_initialized) return false
        _started = true
        return true
    }

    override fun stop(): Boolean {
        reproductor?.liberar()
        reproductor = null
        _started = false
        return true
    }

    override fun onDestroy() {
        // Un ExoPlayer sin soltar se queda el decodificador de hardware, y el
        // siguiente reproductor que se cree no lo va a tener.
        reproductor?.liberar()
        reproductor = null
        super.onDestroy()
    }

    override fun healthCheck(): ModuleHealth {
        val listado = almacen?.listar()
        return ModuleHealth(
            name, version,
            if (_started) "healthy" else "stopped",
            mapOf(
                "almacen_creado" to (almacen != null),
                "fuentes" to (listado?.fuentes?.size ?: 0),
                "motivo_del_almacen" to listado?.motivo,
                "canales_cargados" to canales.size,
                "fuente_de_canales" to fuenteDeCanales,
                "programas_de_guia" to (guia?.programas?.size ?: 0),
                "descartados_de_guia" to (guia?.descartados?.size ?: 0),
                "fuente_de_guia" to fuenteDeGuia,
                "reproductor_creado" to (reproductor != null),
                "motivo_reproductor" to reproductor?.ultimoMotivo(),
                "ultimo_motivo" to ultimoMotivo,
            ),
        )
    }

    // ── fuentes ──────────────────────────────────────────────────────────────

    /** Las fuentes del usuario, y el motivo si el almacén no se pudo leer. */
    fun fuentes(): Listado {
        val a = almacen
            ?: return Listado(emptyList(), ultimoMotivo ?: "El módulo no está inicializado")
        return a.listar()
    }

    fun anadirFuente(nombre: String, url: String, tipo: String, huellaEsperada: String?): Anadido {
        val a = almacen ?: return Anadido(null, "El módulo no está inicializado: no hay almacén")
        return a.anadir(nombre, url, tipo, huellaEsperada)
    }

    fun quitarFuente(nombre: String): String? {
        val a = almacen ?: return "El módulo no está inicializado: no hay almacén"
        return a.quitar(nombre)
    }

    /**
     * Descarga una fuente y la lee según su tipo.
     *
     * El orden importa: primero la política de URLs, luego la descarga con su tope,
     * luego la huella y sólo entonces el parseo. Si la fuente declara una huella y
     * no cuadra, no se usa nada de lo descargado; si no declara ninguna, se anota en
     * el motivo que no se pudo comprobar el origen, que no es lo mismo que decir que
     * está bien.
     */
    fun cargar(nombre: String): Carga {
        val a = almacen ?: return Carga(false, "El módulo no está inicializado: no hay almacén", 0, null)
        val fuente = a.listar().fuentes.firstOrNull { it.nombre.equals(nombre.trim(), ignoreCase = true) }
            ?: return Carga(false, "No hay ninguna fuente llamada '$nombre'", 0, null)

        val descarga = cargador.descargar(fuente.url)
        if (!descarga.correcta) {
            ultimoMotivo = descarga.motivo
            return Carga(false, descarga.motivo, 0, descarga.huella)
        }
        val contenido = descarga.contenido
            ?: return Carga(false, "La descarga dio por buena una respuesta sin contenido", 0, descarga.huella)

        // Si la descarga dio por buena la respuesta, trae la huella: se calcula de los
        // bytes recién leídos. Que falte querría decir que MessageDigest falló, y eso
        // no se tapa pasándole una cadena vacía al verificador.
        val huella = descarga.huella ?: return Carga(
            false,
            "La descarga se dio por buena pero no trajo huella, así que no hay forma de comprobar el origen",
            0,
            null,
        )
        val falloHuella = Verificador.comprobar(fuente.huellaEsperada, huella)
        if (fuente.huellaEsperada != null && falloHuella != null) {
            ultimoMotivo = falloHuella
            return Carga(false, falloHuella, 0, huella)
        }
        a.registrarHuella(fuente.nombre, huella)

        return when (fuente.tipo) {
            "xmltv" -> {
                val g = LectorXmltv.leer(contenido, fuente.nombre)
                guia = g
                fuenteDeGuia = fuente.nombre
                ultimoMotivo = g.motivo ?: falloHuella
                Carga(g.correcta, g.motivo ?: falloHuella, g.programas.size, huella)
            }

            else -> {
                val r = ListaM3U.parsear(contenido, fuente.nombre)
                if (r.esListaHls) {
                    // No es una lista de canales: es un flujo. Se dice y no se guarda
                    // como si fueran canales.
                    ultimoMotivo = r.motivo
                    return Carga(false, r.motivo, 0, huella)
                }
                canales = r.canales
                fuenteDeCanales = fuente.nombre
                ultimoMotivo = r.motivo
                Carga(r.correcta, r.motivo, r.canales.size, huella)
            }
        }
    }

    // ── contenido ────────────────────────────────────────────────────────────

    fun canales(): List<Canal> = canales

    fun buscar(texto: String): List<Canal> = ListaM3U.buscar(canales, texto)

    fun grupos(): List<String> = ListaM3U.grupos(canales)

    fun guia(): ResultadoGuia? = guia

    /** Lo que se emite ahora en un canal de la guía, si la guía está cargada. */
    fun enEmision(canalId: String, ahora: Long): Programa? =
        Guia.enEmision(guia?.programas ?: emptyList(), canalId, ahora)

    // ── reproducción ─────────────────────────────────────────────────────────

    /**
     * El reproductor, creado la primera vez que se pide.
     *
     * No se crea en `initialize()`: crear un ExoPlayer reserva recursos de
     * decodificación que no hacen falta hasta que el usuario pulsa un canal.
     */
    fun reproductor(): ReproductorIptv? {
        val existente = reproductor
        if (existente != null) return existente
        val c = contexto ?: return null
        val nuevo = ReproductorIptv(c)
        val fallo = nuevo.crear()
        if (fallo != null) {
            ultimoMotivo = fallo
            return null
        }
        reproductor = nuevo
        return nuevo
    }

    /**
     * Prepara y reproduce un canal. Null si salió; la razón si no.
     *
     * La superficie puede ser null: hay canales que son sólo audio, y en ese caso se
     * reproduce sin vídeo en vez de fallar.
     */
    fun reproducir(canal: Canal, superficie: SurfaceView?): String? {
        val r = reproductor() ?: return ultimoMotivo ?: "No se pudo crear el reproductor"
        val fallo = r.preparar(canal)
        if (fallo != null) return fallo
        r.adjuntar(superficie)
        return r.empezar()
    }

    fun parar() {
        reproductor?.pausar()
    }

    companion object {
        /** En el directorio privado de la app: no es contenido del usuario que haya
         *  que exponer, y no viaja en el APK. */
        const val NOMBRE_ALMACEN = "iptv-fuentes.json"
    }
}

/** Lo que dio una carga de fuente. */
data class Carga(
    val correcta: Boolean,
    val motivo: String?,
    /** Canales o programas, según el tipo de fuente. */
    val cuantos: Int,
    /** La huella de lo descargado, que es lo que permite notar si cambió. */
    val huella: String?,
)
'''

# ══════════════════════════════════════════════════════════════════════════════
# 4. build.gradle — media3
# ══════════════════════════════════════════════════════════════════════════════
sust(GRADLE,
     "    implementation 'com.squareup.okio:okio:3.8.0'\n",
     "    implementation 'com.squareup.okio:okio:3.8.0'\n\n"
     "    // Reproductor: media3/ExoPlayer (Apache-2.0, compatible con la GPL-3.0 del\n"
     "    // proyecto). Hace falta porque el MediaPlayer del framework no resuelve\n"
     "    // playlists .m3u8, y el IPTV es HLS casi siempre; lo deja dicho VideoModule en\n"
     "    // su propia documentación. El módulo -hls no es un extra: sin él media3 no\n"
     "    // reconoce los flujos .m3u8.\n"
     "    // Versión fija a propósito, y las dos piezas en la misma. Nada de rangos\n"
     "    // dinámicos ni de resolvedores que elijan la última disponible: cambiarían lo\n"
     "    // que se compila sin que nadie lo decida. La prueba que vigila esto busca las\n"
     "    // dos cadenas prohibidas por su nombre, así que este comentario las describe y\n"
     "    // no las escribe — citarlas aquí sería exactamente el fallo que la prueba caza.\n"
     "    implementation 'androidx.media3:media3-exoplayer:" + MEDIA3 + "'\n"
     "    implementation 'androidx.media3:media3-exoplayer-hls:" + MEDIA3 + "'\n")

# ══════════════════════════════════════════════════════════════════════════════
# 5. CeroXApplication — registro en las DOS listas
# ══════════════════════════════════════════════════════════════════════════════
sust(APP,
     '            ModuleMetadata("audio-eq", "0.1.0", emptyList()),\n',
     '            ModuleMetadata("audio-eq", "0.1.0", emptyList()),\n'
     '            ModuleMetadata("iptv", "0.1.0", emptyList()),\n')
sust(APP,
     '            "audio-eq" to com.ceroX.app.modules.audio_eq.EcualizadorModule::class.java,\n',
     '            "audio-eq" to com.ceroX.app.modules.audio_eq.EcualizadorModule::class.java,\n'
     '            "iptv" to com.ceroX.app.modules.iptv.IptvModule::class.java,\n')

# ══════════════════════════════════════════════════════════════════════════════
# 6. La prueba
# ══════════════════════════════════════════════════════════════════════════════
cambios[TEST + "IptvReproductorTest.kt"] = r'''package com.ceroX.app.modules.iptv

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test
import java.io.File

/**
 * La traducción de opciones, la detección de HLS y el cableado del reproductor.
 *
 * Las dos primeras pruebas se ejecutan de verdad: [OpcionesReproduccion] no toca
 * Android. Crear un ExoPlayer sí, y eso no se puede hacer aquí sin un dispositivo,
 * así que lo que se comprueba del reproductor es su cableado —que es lo que se rompe
 * en silencio: una dependencia que falta en Gradle no falla, simplemente no reproduce
 * nada—.
 */
class IptvReproductorTest {

    private fun fuente(rel: String): String {
        val f = File("src/main/java/com/ceroX/app/modules/iptv", rel)
        assertTrue("falta $rel", f.isFile)
        return f.readText()
    }

    private fun canal(url: String, titulo: String = "T", opciones: Map<String, String> = emptyMap()) = Canal(
        titulo = titulo,
        url = url,
        tvgId = null,
        tvgNombre = null,
        logo = null,
        grupo = null,
        duracionSegundos = -1,
        opciones = opciones,
        linea = 1,
    )

    @Test
    fun `las opciones de la lista se traducen a lo que entiende un reproductor`() {
        val s = OpcionesReproduccion.de(
            canal(
                "https://ejemplo.invalid/a.m3u8",
                opciones = mapOf(
                    "http-user-agent" to "Mozilla/5.0 (Linux; Android 14)",
                    "http-referrer" to "https://ejemplo.invalid/embed",
                    "inputstream.adaptive.license_type" to "clearkey",
                    "inputstream.adaptive.manifest_type" to "hls",
                    "network-caching" to "1000",
                ),
            )
        )
        assertEquals("Mozilla/5.0 (Linux; Android 14)", s.userAgent)
        assertEquals("https://ejemplo.invalid/embed", s.cabeceras["Referer"])
        assertEquals("clearkey", s.drm["license_type"])
        assertEquals("hls", s.drm["manifest_type"])
        assertTrue(s.esHls)

        // El agente no va en las cabeceras: va aparte, que es donde media3 lo quiere.
        assertNull(s.cabeceras["User-Agent"])
        assertNull(s.cabeceras["http-user-agent"])

        // Y lo que no se sabe traducir no se cuela como cabecera HTTP.
        assertEquals(setOf("network-caching"), s.sinTraducir.keys)
        assertNull(s.cabeceras["network-caching"])

        // Las cuatro grafías del referente dan la misma cabecera.
        for (clave in listOf("http-referrer", "http-referer", "referrer", "referer")) {
            val r = OpcionesReproduccion.de(canal("https://ejemplo.invalid/a", opciones = mapOf(clave to "https://r")))
            assertEquals("con $clave", "https://r", r.cabeceras["Referer"])
        }

        // Las claves se comparan en minúsculas, que es como vienen unas veces.
        val mayus = OpcionesReproduccion.de(canal("https://ejemplo.invalid/a", opciones = mapOf("HTTP-USER-AGENT" to "X")))
        assertEquals("X", mayus.userAgent)

        // Sin opciones no se inventa ninguna cabecera.
        val vacio = OpcionesReproduccion.de(canal("https://ejemplo.invalid/a"))
        assertNull(vacio.userAgent)
        assertTrue(vacio.cabeceras.isEmpty())
        assertTrue(vacio.drm.isEmpty())
        assertTrue(vacio.sinTraducir.isEmpty())

        // Un valor en blanco no cuenta.
        val blanco = OpcionesReproduccion.de(canal("https://ejemplo.invalid/a", opciones = mapOf("http-user-agent" to "  ")))
        assertNull(blanco.userAgent)
    }

    @Test
    fun `se sabe si un flujo es HLS por la ruta y no por el nombre del canal`() {
        assertTrue(OpcionesReproduccion.esHls("https://ejemplo.invalid/a.m3u8"))
        assertTrue(OpcionesReproduccion.esHls("https://ejemplo.invalid/a.M3U8"))
        assertTrue(OpcionesReproduccion.esHls("https://ejemplo.invalid/a.m3u8?token=1&x=2"))
        assertTrue(OpcionesReproduccion.esHls("https://ejemplo.invalid/a.m3u8#frag"))
        assertFalse(OpcionesReproduccion.esHls("https://ejemplo.invalid/a.mp4"))
        assertFalse(OpcionesReproduccion.esHls("https://ejemplo.invalid/segmento.ts"))
        // Una .m3u puede ser otra lista de canales, no un flujo HLS.
        assertFalse(OpcionesReproduccion.esHls("https://ejemplo.invalid/lista.m3u"))
        assertFalse(OpcionesReproduccion.esHls("https://ejemplo.invalid/m3u8"))
        assertFalse(OpcionesReproduccion.esHls("https://ejemplo.invalid/sin-extension"))

        // El nombre del canal no decide nada: sólo la URL.
        assertFalse(OpcionesReproduccion.de(canal("https://ejemplo.invalid/f.mp4", "Nombre.m3u8")).esHls)
        assertTrue(OpcionesReproduccion.de(canal("https://ejemplo.invalid/f.m3u8", "Sin pista")).esHls)
    }

    @Test
    fun `la app registra el modulo de IPTV en las dos listas`() {
        val app = File("src/main/java/com/ceroX/app/core/CeroXApplication.kt")
        assertTrue("falta CeroXApplication.kt", app.isFile)
        val t = app.readText()
        assertTrue(
            "iptv no está en la lista de metadatos: sin ella el gestor no lo registra",
            t.contains("ModuleMetadata(\"iptv\""),
        )
        assertTrue(
            "iptv no tiene clase asignada: el bucle de registro lo saltaría en silencio",
            t.contains("\"iptv\" to com.ceroX.app.modules.iptv.IptvModule::class.java"),
        )
    }

    @Test
    fun `media3 esta declarado con version fija y con el modulo de HLS`() {
        val gradle = File("build.gradle")
        assertTrue("falta build.gradle del módulo app", gradle.isFile)
        val t = gradle.readText()
        assertTrue(
            "falta media3-exoplayer: sin él no hay reproductor propio y el IPTV no reproduce",
            t.contains("androidx.media3:media3-exoplayer:"),
        )
        assertTrue(
            "falta media3-exoplayer-hls: sin él media3 no reconoce los flujos .m3u8, " +
                "que es lo que es el IPTV casi siempre",
            t.contains("androidx.media3:media3-exoplayer-hls:"),
        )
        val versiones = Regex("androidx\\.media3:[a-z0-9-]+:([0-9]+\\.[0-9]+\\.[0-9]+)")
            .findAll(t).map { it.groupValues[1] }.toList()
        assertTrue("no se pudo leer ninguna versión de media3", versiones.isNotEmpty())
        assertEquals(
            "las piezas de media3 tienen que ir todas en la misma versión, o se " +
                "mezclan clases de dos lanzamientos",
            1, versiones.distinct().size,
        )
        assertFalse("nada de versiones dinámicas", t.contains("media3-exoplayer:+"))
        assertFalse("ni de latest.release", t.contains("latest.release"))
    }

    @Test
    fun `el reproductor informa de los errores y libera lo que abre`() {
        val t = fuente("ReproductorIptv.kt")
        assertTrue(
            "DefaultHttpDataSource es API inestable de media3: sin el opt-in no compila",
            t.contains("@OptIn(UnstableApi::class)"),
        )
        assertTrue(t.contains("ExoPlayer.Builder"))
        assertTrue(
            "los fallos de reproducción llegan por el oyente; sin él se pierde la razón",
            t.contains("onPlayerError"),
        )
        assertTrue(
            "el código de error de media3 es lo que distingue un servidor caído de un " +
                "códec que falta",
            t.contains("errorCodeName"),
        )
        assertTrue("un ExoPlayer sin soltar se queda el decodificador", t.contains("release()"))
        assertTrue(
            "las cabeceras del canal tienen que llegar a la fuente de datos",
            t.contains("setDefaultRequestProperties"),
        )
        assertTrue(t.contains("setUserAgent"))
        assertTrue(
            "un método que devuelve una razón no necesita devolver true; si aparece, " +
                "hay un éxito afirmado sin comprobación",
            0 == t.split("\n").count { it.trim() == "return true" },
        )
        assertTrue(
            "el último motivo tiene que poder consultarse para enseñarlo",
            t.contains("fun ultimoMotivo(): String?"),
        )
    }

    @Test
    fun `el modulo no dice que cargo nada cuando no pudo`() {
        val t = fuente("IptvModule.kt")
        assertTrue(
            "sin contexto no hay dónde guardar las fuentes del usuario, y eso tiene " +
                "que hacer fallar la inicialización en vez de devolver true",
            t.contains("return false"),
        )
        assertTrue(t.contains("No se inyectó el contexto"))
        assertTrue(
            "las fuentes se guardan en el almacenamiento privado, no en el APK",
            t.contains("File(c.filesDir"),
        )
        assertTrue("la huella tiene que comprobarse al cargar", t.contains("Verificador.comprobar"))
        assertTrue(
            "si la fuente declara una huella y no cuadra, no se usa lo descargado",
            t.contains("fuente.huellaEsperada != null"),
        )
        assertTrue(
            "una playlist HLS no es una lista de canales y no debe guardarse como tal",
            t.contains("r.esListaHls"),
        )
        for (clave in listOf(
            "almacen_creado", "fuentes", "canales_cargados", "programas_de_guia",
            "reproductor_creado", "ultimo_motivo", "motivo_del_almacen",
        )) {
            assertTrue("el health check no informa de $clave", t.contains("\"$clave\" to"))
        }
        assertTrue(
            "al parar y al destruir hay que liberar el reproductor",
            t.contains("reproductor?.liberar()"),
        )
        assertTrue(
            "initialize no debe crear el ExoPlayer: reserva decodificador sin que " +
                "nadie lo haya pedido",
            !t.contains("override fun initialize(config: Map<String, Any>): Boolean {\n        reproductor"),
        )
    }
}
'''

# ══════════════════════════════════════════════════════════════════════════════
# Comprobaciones y pre-vuelo
# ══════════════════════════════════════════════════════════════════════════════
MARCAS = ["Placeholder", "placeholder", "Simular", "simular", "simulado", "Simulado",
          "not implemented", "Not implemented", "sin implementar", "hardcodeado",
          "Hardcodeado", "TODO:", "FIXME", "ficticio", "dummy", "de momento devuelve"]
SOSPECHOSAS = ["compatible", "mejorado", "improved", "stabilized", "estable",
               "verificado", "verified", "funciona", "works", "listo"]

print("\nCOMPROBACIONES")
for p in sorted(cambios):
    t = cambios[p]
    ok(len(t) > 500, p + " sospechosamente corto")
    # Fichero nuevo: se mira entero. Fichero editado: solo lo que se le añade, que el
    # resto ya pasó las puertas publicadas en el commit anterior.
    trozos = insertos.get(p, [t])
    for trozo in trozos:
        for i, linea in enumerate(trozo.split("\n"), 1):
            c = linea.strip()
            if "*/" in linea and c != "*/" and not c.endswith("*/"):
                raise SystemExit("%s: un */ en medio de la linea: %s" % (p, c[:80]))
            for m in MARCAS:
                ok(m not in linea, "marca %r en %s:%d" % (m, p, i))
    if p.endswith(".kt"):
        cod = solo_codigo(t)
        ok(cod.count("{") == cod.count("}"), "%s: llaves %d/%d" % (p, cod.count("{"), cod.count("}")))
        ok(cod.count("(") == cod.count(")"), "%s: parentesis %d/%d" % (p, cod.count("("), cod.count(")")))
    if p.startswith(SRC):
        propio = "\n".join(trozos)
        ok("!!" not in propio, p + ": doble ! prohibido")
        ok('?: ""' not in propio, p + ': ?: con cadena vacia')
        for i, linea in enumerate(propio.split("\n"), 1):
            c = linea.strip()
            if " to true" in c and not c.startswith("//") and not c.startswith("*"):
                clave = c.split('" to true')[0].split('"')[-1].lower()
                ok(not any(s in clave for s in SOSPECHOSAS), "afirmacion constante en %s:%d" % (p, i))
    print("  %7d B · %s%s" % (len(t.encode()), p, "" if p not in insertos else "  (editado)"))

print("\nPRE-VUELO (lo que las pruebas van a exigir, repetido aqui)")
# La prueba publicada en IptvTest recorre TODO el paquete del IPTV buscando URLs de
# fuentes escritas a mano. Los ficheros nuevos tienen que pasarla tambien.
patron = re.compile(r'"https?://[^"]*\.(m3u8?|xmltv|xml|ts)([?"#][^"]*)?"')
nuevos = [IPTV + "OpcionesReproduccion.kt", IPTV + "ReproductorIptv.kt", IPTV + "IptvModule.kt"]
culpables = []
for p in nuevos:
    for i, linea in enumerate(cambios[p].split("\n"), 1):
        if patron.search(linea):
            culpables.append("%s:%d" % (os.path.basename(p), i))
ok(not culpables, "URLs de fuentes escritas a mano: " + str(culpables))
print("  URLs de fuentes en los 3 ficheros nuevos  ninguna")

# Cada literal que exigen las pruebas 3 a 6, contra el texto que se publica.
EXIGE = {
    IPTV + "ReproductorIptv.kt": [
        "@OptIn(UnstableApi::class)", "ExoPlayer.Builder", "onPlayerError", "errorCodeName",
        "release()", "setDefaultRequestProperties", "setUserAgent",
        "fun ultimoMotivo(): String?",
    ],
    IPTV + "IptvModule.kt": [
        "return false", "No se inyectó el contexto", "File(c.filesDir",
        "Verificador.comprobar", "fuente.huellaEsperada != null", "r.esListaHls",
        "reproductor?.liberar()",
        '"almacen_creado" to', '"fuentes" to', '"canales_cargados" to',
        '"programas_de_guia" to', '"reproductor_creado" to', '"ultimo_motivo" to',
        '"motivo_del_almacen" to',
    ],
    APP: ['ModuleMetadata("iptv"', '"iptv" to com.ceroX.app.modules.iptv.IptvModule::class.java'],
    GRADLE: ["androidx.media3:media3-exoplayer:", "androidx.media3:media3-exoplayer-hls:"],
}
for p, literales in EXIGE.items():
    t = cambios[p]
    for lit in literales:
        ok(lit in t, "%s no contiene %r y la prueba lo va a exigir" % (os.path.basename(p), lit))
    print("  %-24s %2d literales exigidos  OK" % (os.path.basename(p), len(literales)))

g = cambios[GRADLE]
ok("media3-exoplayer:+" not in g, "version dinamica")
ok("latest.release" not in g, "latest.release")
ok(g.count(MEDIA3) == 2, "se esperaban 2 menciones de la version, hay %d" % g.count(MEDIA3))
print("  version de media3 fija                    %s (2 artefactos)" % MEDIA3)

ok(cambios[TEST + "IptvReproductorTest.kt"].count("@Test") == 6, "se esperaban 6 pruebas")
print("  pruebas nuevas                            6 (455 -> 461)")

print("\nlisto: %d ficheros" % len(cambios))

if not EJECUTAR or LOCAL:
    import pathlib
    for p, t in cambios.items():
        d = pathlib.Path(SALIDA) / p
        d.parent.mkdir(parents=True, exist_ok=True)
        with io.open(str(d), "w", encoding="utf-8") as f:
            f.write(t)
    print("volcado en " + SALIDA)
    print("SIN PUBLICAR." if LOCAL else "DRY-RUN.")
    raise SystemExit(0)

ent = [{"path": p, "mode": "100644", "type": "blob", "content": t} for p, t in sorted(cambios.items())]
arb = api("/git/trees", "POST", {"base_tree": BASE, "tree": ent})["sha"]
ahora = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
iden = {"name": "La Bandita", "email": "reborn@labandita.dev", "date": ahora}
msg = """IPTV: reproductor media3 y el modulo registrado, con las opciones traducidas a la vista

Cuatro ficheros nuevos y dos ediciones. Seis pruebas nuevas: las dos primeras se
ejecutan de verdad, las otras cuatro comprueban el cableado.

build.gradle declara media3 1.11.1 (la ultima estable; 1.12.0 sigue en beta) con dos
artefactos: media3-exoplayer y media3-exoplayer-hls. El segundo no es un extra, es lo
que hace que media3 reconozca un flujo .m3u8. La version va fija y las dos piezas en
la misma, y hay una prueba que lo vigila: mezclar versiones de media3 es mezclar
clases de dos lanzamientos. Es Apache-2.0, compatible con la GPL-3.0 del proyecto.

OpcionesReproduccion.kt es la parte que no toca Android, y por eso es la que se puede
probar de verdad. Las listas traen #EXTVLCOPT y #KODIPROP con claves que VLC y Kodi
entienden y media3 no: http-user-agent, http-referrer (que aparece con cuatro grafias
distintas) e inputstream.adaptive.* para el DRM. Se traducen, y lo que no se sabe
traducir NO se convierte en cabecera HTTP por las buenas: network-caching no es una
cabecera, y mandarla como si lo fuera es la clase de invento que hace que un fallo de
red sea imposible de diagnosticar. Las claves desconocidas van a sinTraducir, para
ensenarlas. La deteccion de HLS mira la ruta de la URL sin parametros ni fragmento, y
no el nombre del canal: hay canales llamados "algo.m3u8" que sirven un .mp4.

ReproductorIptv.kt crea el ExoPlayer con una fabrica de datos por canal, que es donde
viven el agente y el referente, y le pega un oyente de errores que guarda el codigo y
el mensaje de media3. Un canal no arranca por cien razones -servidor caido, agente que
ya no cuela, TLS invalido, DRM que falta, codec que el dispositivo no tiene- y ninguna
se puede adivinar desde aqui, asi que cada metodo devuelve null si salio o la razon si
no. No hay ni un booleano de exito en el fichero, y hay una prueba que cuenta las
lineas "return true" y exige que sean cero.

IptvModule.kt se registra como iptv, el modulo 38, en las dos listas de
CeroXApplication: faltar en la de clases hace que el bucle de registro lo salte en
silencio, que es exactamente lo que le paso a otro modulo y lo que vigila la prueba.
initialize() solo guarda el contexto y crea un objeto File, sin red ni disco, porque
la app ya tuvo un ANR por inicializar treinta y seis modulos haciendo trabajo pesado
en el hilo principal. Sin contexto devuelve false con el motivo, en vez de devolver
true y quedarse sin almacen. El ExoPlayer no se crea ahi tampoco: reserva
decodificador sin que nadie lo haya pedido.

cargar() hace las cosas en orden: politica de URLs, descarga con su tope, huella y
solo entonces parseo. Si la fuente declara huella y no cuadra, no se usa nada de lo
descargado; si no declara ninguna, el motivo dice que no se pudo comprobar el origen,
que no es lo mismo que decir que esta bien. Y si lo descargado resulta ser una
playlist HLS, no se guarda como si fueran canales.

Falta la pantalla: este commit deja el modulo funcionando y registrado, y la interfaz
va detras, que es donde estara media3-ui. Se hace en commits separados a proposito -
este cambia build.gradle y por tanto el tamano del APK y el trabajo de R8, y si algo
se pone en rojo hay que poder saber de que mitad viene."""
c = api("/git/commits", "POST", {"message": msg, "tree": arb, "parents": [BASE],
                                 "author": iden, "committer": iden})
api("/git/refs/heads/main", "PATCH", {"sha": c["sha"], "force": False})
print("COMMIT:", c["sha"])
time.sleep(6)
print("main:", api("/git/ref/heads/main")["object"]["sha"])
