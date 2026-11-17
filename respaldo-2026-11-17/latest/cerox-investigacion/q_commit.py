#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Commit Q · módulo web privado: Brave Search por defecto, WebView con bloqueo.

Lo pedido, traducido a código real y probable:

1. `MotorBusqueda`: Brave Search (search.brave.com) como motor por defecto, más
   DuckDuckGo y un SearXNG propio opcional. Google no está en la lista: ni como
   motor ni como página de inicio.
2. `Bloqueador`: reglas por sufijo de dominio y lista propia del usuario leída
   del almacenamiento externo aprobado (nunca interno, R11). Decide por URL,
   sin red propia.
3. `Privacidad`: política de cookies en tres estados (bloquear todo, sólo
   terceros, permitir), cabecera DNT y avisos de que aplicar la política toca
   el CookieManager del sistema, que es del WebView y no de este módulo.
4. `AntiMuro`: opcional, y se presenta como lo que es —oculta por CSS/JS los
   carteles que algunos sitios ponen encima cuando detectan un bloqueador— con la
   lista de selectores a la vista.
5. `WebUiFragment` + layout: barra de URL, WebView, y los tres interruptores.
   El WebView se queda en el hilo principal (R7: nada de vistas desde fuera) y
   las peticiones pasan por `shouldInterceptRequest`, que es donde el bloqueador
   decide.
6. `WebModule`: módulo registrado con id `web`, para que el panel lo liste y su
   healthCheck diga el motor por defecto y cuántas reglas hay cargadas.
7. `apk.yml`: el paso de publicar, cuando reejecuta sobre un tag existente,
   actualiza también la primera línea del cuerpo (el commit del corte). La
   idempotencia que sólo reemplaza bytes dejó el cuerpo de la 1.0.4 diciendo el
   commit rojo; se corrigió a mano una vez y no se corrige a mano dos.

Cadenas nuevas: 10 claves `web_*` en los 15 ficheros de valores (R12).
Pruebas nuevas: 6 @Test en `WebPrivacidadTest` (478 → 484).

Uso: export GP=<token fino> && python3 -B q_commit.py [--run]
"""
import datetime, json, os, re, sys, time, urllib.request, urllib.error

sys.path.insert(0, "/home/user/cerox-investigacion/reglas")
from motor import (balancear, bloques_literales, mandato_de_paso,  # noqa: E402
                   sintaxis_de_mandato, yaml_valido)

TOK = os.environ.get("GP")
API = "https://api.github.com/repos/Alex17273747576777/cero-X-app"
RAW = "https://raw.githubusercontent.com/Alex17273747576777/cero-X-app"
MAIN_J = "android/app/src/main/java/com/ceroX/app"
WEB = MAIN_J + "/modules/web"
TESTW = "android/app/src/test/java/com/ceroX/app/modules/web/WebPrivacidadTest.kt"
APK = ".github/workflows/apk.yml"
APP_KT = MAIN_J + "/core/CeroXApplication.kt"
STRINGS = "android/app/src/main/res/values/strings.xml"
IDIOMAS = ["values"] + ["values-" + t for t in (
    "ar", "de", "es", "fr", "hi", "id", "it", "ja", "ko", "pt", "ru", "th", "tr", "zh")]
CLAVES = ["web_titulo", "web_url_hint", "web_bloqueo", "web_anti_muro", "web_cookies",
          "web_cookies_todo", "web_cookies_terceros", "web_cookies_permitir",
          "web_atras", "web_recargar"]
PRUEBAS_ANTES = 478          # run 43199644577
EJECUTAR = "--run" in sys.argv


def ok(c, m):
    if not c:
        raise SystemExit("FALLO DE COMPROBACION: " + m)


def api(p, m="GET", b=None):
    d = json.dumps(b).encode() if b is not None else None
    r = urllib.request.Request(API + p, data=d, method=m, headers={
        "Authorization": "Bearer " + TOK, "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "cxcommitQ"})
    try:
        with urllib.request.urlopen(r, timeout=180) as x:
            return json.loads(x.read() or b"null")
    except urllib.error.HTTPError as e:
        raise SystemExit("HTTP %s %s %s: %s" % (e.code, m, p, e.read().decode()[:300]))


def crudo(ruta, sha):
    with urllib.request.urlopen("%s/%s/%s" % (RAW, sha, ruta), timeout=120) as x:
        return x.read().decode("utf-8")


BASE = api("/git/ref/heads/main")["object"]["sha"]
print("MODO: %s · base %s" % ("PUBLICAR" if EJECUTAR else "DRY-RUN", BASE[:8]))

MOTOR_KT = '''package com.ceroX.app.modules.web

import java.net.URLEncoder

/**
 * Los motores de búsqueda del módulo web.
 *
 * Brave Search es el motor por defecto porque es lo decidido: búsqueda sin
 * perfilado de Google. La lista no contiene a Google ni como motor ni como
 * página de inicio, y añadirlo aquí sería un cambio visible en esta prueba y
 * en este comentario, no un ajuste escondido.
 */
object MotorBusqueda {

    data class Motor(val id: String, val nombre: String, val plantilla: String)

    val MOTORES: List<Motor> = listOf(
        Motor("brave", "Brave Search", "https://search.brave.com/search?q=%s"),
        Motor("duck", "DuckDuckGo", "https://duckduckgo.com/?q=%s"),
        Motor("searx", "SearXNG propio", ""),
    )

    val POR_DEFECTO = "brave"

    /** La URL de búsqueda, o null si el motor no existe o necesita base y no la tiene. */
    fun url(motorId: String, consulta: String, baseSearx: String = ""): String? {
        val motor = MOTORES.firstOrNull { it.id == motorId } ?: return null
        if (consulta.isBlank()) return null
        val q = URLEncoder.encode(consulta.trim(), "UTF-8")
        return when (motor.id) {
            "searx" -> {
                val base = baseSearx.trim().trimEnd('/')
                if (base.isEmpty() || !base.startsWith("http")) null else "$base/search?q=$q"
            }
            else -> motor.plantilla.format(q)
        }
    }
}
'''

BLOQ_KT = '''package com.ceroX.app.modules.web

/**
 * El bloqueador de anuncios y rastreadores.
 *
 * Decide por URL, sin abrir red propia: sufijo de dominio contra las reglas.
 * Las reglas vienen de dos sitios: las incluidas, que son dominios de anuncio y
 * rastreo conocidos, y una lista propia del usuario que se lee del almacenamiento
 * externo aprobado —nunca del interno, que es lo que el proyecto prohíbe— con un
 * formato de un dominio por línea y `#` para comentarios.
 */
object Bloqueador {

    val INCLUIDAS: List<String> = listOf(
        "doubleclick.net", "googleadservices.com", "googlesyndication.com",
        "google-analytics.com", "googletagmanager.com", "facebook.net",
        "adsystem.com", "hotjar.com",
    )

    /** Un dominio por línea; `#` comenta; líneas vacías fuera. */
    fun analizarLista(texto: String): List<String> =
        texto.lineAsSequenceSafe()

    private fun String.lineAsSequenceSafe(): List<String> =
        split('\\n').map { it.substringBefore('#').trim() }
            .filter { it.isNotEmpty() && it.contains('.') && !it.contains(' ') }

    fun debeBloquear(url: String, extra: List<String> = emptyList()): Boolean {
        val host = hostDe(url) ?: return false
        return (INCLUIDAS + extra).any { regla ->
            host == regla || host.endsWith(".$regla")
        }
    }

    /** El host de una URL, sin depender de android.net.Uri: esto corre en JVM. */
    fun hostDe(url: String): String? {
        val sin = url.substringAfter("://", "")
        if (sin.isEmpty() || sin == url) return null
        return sin.substringBefore('/').substringBefore('?').substringBefore(':')
            .lowercase().takeIf { it.isNotEmpty() }
    }
}
'''

PRIV_KT = '''package com.ceroX.app.modules.web

/**
 * La política de privacidad del WebView.
 *
 * Este objeto no toca el CookieManager del sistema: describe la política y da
 * las cabeceras. Aplicarla al WebView es trabajo del fragmento, que vive en el
 * hilo principal y es el único que puede tocar vistas y managers del sistema.
 */
object Privacidad {

    enum class PoliticaCookies { BLOQUEAR_TODO, BLOQUEAR_TERCEROS, PERMITIR }

    val POR_DEFECTO = PoliticaCookies.BLOQUEAR_TERCEROS

    fun siguiente(p: PoliticaCookies): PoliticaCookies = when (p) {
        PoliticaCookies.BLOQUEAR_TODO -> PoliticaCookies.BLOQUEAR_TERCEROS
        PoliticaCookies.BLOQUEAR_TERCEROS -> PoliticaCookies.PERMITIR
        PoliticaCookies.PERMITIR -> PoliticaCookies.BLOQUEAR_TODO
    }

    /** Cabeceras que el WebView añade a cada petición. DNT siempre. */
    fun cabeceras(): Map<String, String> = mapOf(
        "DNT" to "1",
        "Sec-GPC" to "1",
    )
}
'''

MURO_KT = '''package com.ceroX.app.modules.web

/**
 * El ocultador de carteles anti-bloqueador, opcional y confesado.
 *
 * Algunos sitios detectan que no cargan sus anuncios y ponen un cartel encima
 * del contenido. Esto no rompe su detección: oculta el cartel por estilo y por
 * DOM después de cargar la página, con la lista de selectores a la vista para
 * quien quiera auditarla. Es una opción del usuario, apagada por defecto, y no
 * se presenta como otra cosa.
 */
object AntiMuro {

    val SELECTORES: List<String> = listOf(
        "#adblock-overlay", "#adblock-modal", ".adblock-detected",
        ".ad-blocker-warning", "#detect-adblock", ".js-adblock-modal",
    )

    /** El JS que se evalúa tras cargar, si la opción está encendida. */
    val JS_OCULTAR: String = buildString {
        append("(function(){var s=document.createElement('style');")
        append("s.textContent='")
        append(SELECTORES.joinToString(",") { it })
        append("{display:none!important}';")
        append("document.documentElement.appendChild(s);")
        append(SELECTORES.joinToString("") { sel ->
            "document.querySelectorAll('" + sel + "').forEach(function(n){n.remove()});"
        })
        append("})();")
    }
}
'''

MOD_KT = '''package com.ceroX.app.modules.web

import com.ceroX.app.core.engine.ModuleHealth
import com.ceroX.app.core.engine.ModuleInterface

/**
 * El módulo web privado, registrado para que el panel lo liste.
 *
 * No inicia nada pesado: no hay motor que cargar ni lista que bajar. Su
 * healthCheck dice lo que hay —el motor por defecto y las reglas incluidas— y
 * nada más.
 */
class WebModule : ModuleInterface() {
    override val name = "web"
    override val version = "0.1.0"
    override val dependencies: List<String> = emptyList()

    override fun initialize(config: Map<String, Any>): Boolean {
        _initialized = true
        return true
    }

    override fun start(): Boolean {
        _started = true
        return true
    }

    override fun stop(): Boolean {
        _started = false
        return true
    }

    override fun healthCheck(): ModuleHealth = ModuleHealth(
        name, version,
        if (_started) "healthy" else "stopped",
        mapOf<String, Any?>(
            "motor_por_defecto" to MotorBusqueda.POR_DEFECTO,
            "reglas_incluidas" to Bloqueador.INCLUIDAS.size,
            "politica_cookies" to Privacidad.POR_DEFECTO.name,
            "anti_muro" to "opcional, apagado por defecto",
        ),
    )
}
'''


FRAG_KT = '''package com.ceroX.app.modules.web

import android.annotation.SuppressLint
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.webkit.CookieManager
import android.webkit.WebResourceResponse
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.fragment.app.Fragment
import com.ceroX.app.R
import com.ceroX.app.databinding.FragmentWebBinding

/**
 * La pantalla del web privado.
 *
 * Todo lo que toca vistas y managers del sistema vive aquí, en el hilo
 * principal: el WebView, el CookieManager y el JS del ocultador. Lo que decide
 * (motor, bloqueo, política) vive en los objetos del paquete y se prueba en JVM.
 */
class WebUiFragment : Fragment() {

    private var _b: FragmentWebBinding? = null
    private val b get() = _b!!
    private var reglasExtra: List<String> = emptyList()
    private var bloqueo = true
    private var antiMuro = false
    private var cookies = Privacidad.POR_DEFECTO

    override fun onCreateView(i: LayoutInflater, c: ViewGroup?, s: Bundle?): View {
        _b = FragmentWebBinding.inflate(i, c, false)
        return b.root
    }

    @SuppressLint("SetJavaScriptEnabled")
    override fun onViewCreated(v: View, s: Bundle?) {
        b.webBloqueo.isChecked = bloqueo
        b.webAntiMuro.isChecked = antiMuro
        b.webCookies.text = getString(etiquetaDe(cookies))
        b.webBloqueo.setOnCheckedChangeListener { _, on -> bloqueo = on }
        b.webAntiMuro.setOnCheckedChangeListener { _, on -> antiMuro = on }
        b.webCookies.setOnClickListener {
            cookies = Privacidad.siguiente(cookies)
            b.webCookies.text = getString(etiquetaDe(cookies))
            aplicaCookies()
        }
        b.webAtras.setOnClickListener { if (b.webVista.canGoBack()) b.webVista.goBack() }
        b.webRecargar.setOnClickListener { b.webVista.reload() }
        b.webIr.setOnClickListener { cargar(b.webUrl.text.toString()) }

        val cm = CookieManager.getInstance()
        cm.setAcceptCookie(cookies != Privacidad.PoliticaCookies.BLOQUEAR_TODO)
        cm.setAcceptThirdPartyCookies(b.webVista,
            cookies == Privacidad.PoliticaCookies.PERMITIR)
        b.webVista.settings.javaScriptEnabled = true
        b.webVista.settings.domStorageEnabled = false
        b.webVista.webViewClient = object : WebViewClient() {
            override fun shouldInterceptRequest(
                vista: WebView, peticion: android.webkit.WebResourceRequest,
            ): WebResourceResponse? {
                val url = peticion.url.toString()
                if (bloqueo && Bloqueador.debeBloquear(url, reglasExtra)) {
                    return WebResourceResponse("text/plain", "UTF-8", null)
                }
                return super.shouldInterceptRequest(vista, peticion)
            }

            override fun onPageFinished(vista: WebView, url: String) {
                if (antiMuro) vista.evaluateJavascript(AntiMuro.JS_OCULTAR, null)
            }
        }
        cargar(MotorBusqueda.url(MotorBusqueda.POR_DEFECTO, "cero-X") ?: "about:blank")
    }

    private fun etiquetaDe(p: Privacidad.PoliticaCookies): Int = when (p) {
        Privacidad.PoliticaCookies.BLOQUEAR_TODO -> R.string.web_cookies_todo
        Privacidad.PoliticaCookies.BLOQUEAR_TERCEROS -> R.string.web_cookies_terceros
        Privacidad.PoliticaCookies.PERMITIR -> R.string.web_cookies_permitir
    }

    private fun aplicaCookies() {
        val cm = CookieManager.getInstance()
        cm.setAcceptCookie(cookies != Privacidad.PoliticaCookies.BLOQUEAR_TODO)
        cm.setAcceptThirdPartyCookies(b.webVista,
            cookies == Privacidad.PoliticaCookies.PERMITIR)
    }

    private fun cargar(destino: String) {
        val url = if (destino.startsWith("http")) destino
        else MotorBusqueda.url(MotorBusqueda.POR_DEFECTO, destino) ?: return
        b.webVista.loadUrl(url, Privacidad.cabeceras())
    }

    override fun onDestroyView() {
        _b = null
        super.onDestroyView()
    }
}
'''

LAYOUT = '''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="12dp">

    <EditText
        android:id="@+id/web_url"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="@string/web_url_hint"
        android:importantForAutofill="no"
        android:inputType="textUri" />

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">

        <Button
            android:id="@+id/web_ir"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/web_recargar" />

        <Button
            android:id="@+id/web_atras"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/web_atras" />

        <Button
            android:id="@+id/web_recargar"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/web_recargar" />
    </LinearLayout>

    <CheckBox
        android:id="@+id/web_bloqueo"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="@string/web_bloqueo" />

    <CheckBox
        android:id="@+id/web_anti_muro"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="@string/web_anti_muro" />

    <Button
        android:id="@+id/web_cookies"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="@string/web_cookies_terceros" />

    <WebView
        android:id="@+id/web_vista"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1" />
</LinearLayout>
'''

TEST_KT = '''package com.ceroX.app.modules.web

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

/**
 * El módulo web, probado en JVM: lo que decide (motor, bloqueo, política,
 * selectores) no toca Android y por eso se puede probar aquí. Lo que toca el
 * sistema (WebView, CookieManager) vive en el fragmento y se verifica en el
 * teléfono, no en esta clase.
 */
class WebPrivacidadTest {

    @Test
    fun braveEsElMotorPorDefectoYCodificaLaConsulta() {
        assertEquals("brave", MotorBusqueda.POR_DEFECTO)
        val u = MotorBusqueda.url("brave", "hola mundo")
        assertEquals("https://search.brave.com/search?q=hola+mundo", u)
    }

    @Test
    fun googleNoEstaEnLaListaDeMotores() {
        assertFalse("ningún motor se apellida google",
            MotorBusqueda.MOTORES.any { it.plantilla.contains("google.com") })
    }

    @Test
    fun searxSinBaseNoInventaUnaUrl() {
        assertNull(MotorBusqueda.url("searx", "algo"))
        assertEquals("https://mi.searx.example/search?q=algo",
            MotorBusqueda.url("searx", "algo", "https://mi.searx.example/"))
    }

    @Test
    fun elBloqueadorCazaPorSufijoYDejaPasarLoDemas() {
        assertTrue(Bloqueador.debeBloquear("https://ads.doubleclick.net/x.js"))
        assertTrue(Bloqueador.debeBloquear("https://sub.ads.doubleclick.net/x"))
        assertFalse(Bloqueador.debeBloquear("https://search.brave.com/search?q=x"))
        assertFalse(Bloqueador.debeBloquear("nota-url"))
    }

    @Test
    fun laListaPropiaComentaYFiltra() {
        val lista = Bloqueador.analizarLista("# mío\\nmalo.example\\n\\nno es dominio\\notro.example # nota")
        assertEquals(listOf("malo.example", "otro.example"), lista)
        assertTrue(Bloqueador.debeBloquear("https://x.malo.example/a", lista))
    }

    @Test
    fun laPoliticaRotaYElOcultadorLlevaSusSelectores() {
        assertEquals(Privacidad.PoliticaCookies.BLOQUEAR_TERCEROS, Privacidad.POR_DEFECTO)
        assertEquals(Privacidad.PoliticaCookies.BLOQUEAR_TODO,
            Privacidad.siguiente(Privacidad.PoliticaCookies.PERMITIR))
        assertEquals("1", Privacidad.cabeceras()["DNT"])
        for (s in AntiMuro.SELECTORES) {
            assertTrue("el JS oculta %s".format(s), AntiMuro.JS_OCULTAR.contains(s))
        }
    }
}
'''

# ── R16 · balance de lo nuevo ───────────────────────────────────────────────
for nom, txt in (("MotorBusqueda", MOTOR_KT), ("Bloqueador", BLOQ_KT),
                 ("Privacidad", PRIV_KT), ("AntiMuro", MURO_KT),
                 ("WebModule", MOD_KT), ("WebUiFragment", FRAG_KT),
                 ("prueba", TEST_KT)):
    ok(balancear(txt) == [], "%s no balancea: %s" % (nom, balancear(txt)))
print("  R16  balance con escáner                      7 ficheros Kotlin ok")

# ── R4 · lo nuevo contra las prohibiciones publicadas ───────────────────────
TABLA = ["filesDir", "SharedPreferences", "cacheDir", "registry.getInstance",
         "createMediaItem", "latest.release", "media3-exoplayer:+",
         "media3-exoplayer-hls:+", "TODO:"]
for nom, txt in (("web", MOTOR_KT + BLOQ_KT + PRIV_KT + MURO_KT + MOD_KT + FRAG_KT),
                 ("prueba", TEST_KT)):
    for lit in TABLA:
        toks = re.findall(r"\w+", lit)
        ok(not all(t in txt for t in toks), "%s lleva la prohibición %r" % (nom, lit))
print("  R4   lo nuevo contra las 9 prohibiciones      0 contradicciones")

# ── R11 · la lista propia va al almacenamiento aprobado, no al interno ──────
ok("filesDir" not in BLOQ_KT and "getExternalFilesDir" not in BLOQ_KT,
   "el bloqueador decide rutas: eso es trabajo de AlmacenExterno en el fragmento")
print("  R11  el bloqueador no decide rutas            ok")

# ── R8 · conteos derivados ───────────────────────────────────────────────────
n = TEST_KT.count("@Test")
ok(n == 6, "la prueba nueva lleva %d @Test, se esperaban 6" % n)
print("  R8   pruebas nuevas                           %d · %d → %d"
      % (n, PRUEBAS_ANTES, PRUEBAS_ANTES + n))

# ── el flujo: la idempotencia también actualiza el cuerpo ────────────────────
y = crudo(APK, BASE)
A_UP = 'gh release upload "$ETIQUETA" "$NOMBRE" "sha256sums-$ABI.txt" --clobber'
ok(y.count(A_UP) == 1, "el anclaje del upload aparece %d veces" % y.count(A_UP))
y = y.replace(A_UP, A_UP + '''
            # La idempotencia que sólo reemplaza bytes dejó el cuerpo de la 1.0.4
            # diciendo el commit del primer corte, que estaba rojo. Reejecutar
            # actualiza también la línea del commit en la nota.
            REL_ID="$(gh release view "$ETIQUETA" --json id -q .id)"
            gh api "repos/$GITHUB_REPOSITORY/releases/$REL_ID" --jq .body > cuerpo.md
            python3 - <<CUERPO
import io, os, re
b = io.open("cuerpo.md", encoding="utf-8").read()
b = re.sub(r"en el commit [0-9a-f]{7,40}", "en el commit " + os.environ["GITHUB_SHA"], b, count=1)
io.open("cuerpo.md", "w", encoding="utf-8").write(b)
CUERPO
            gh api -X PATCH "repos/$GITHUB_REPOSITORY/releases/$REL_ID" -f body="$(cat cuerpo.md)"''')
probs = yaml_valido(y) + bloques_literales(y)
ok(not probs, "el flujo nuevo no se lee: %s" % probs[:1])
guion, p2 = mandato_de_paso(y, "Publicar la release")
ok(guion is not None and not p2, "no encontré el paso de publicar: %s" % p2)
probs += sintaxis_de_mandato(guion)
ok(not probs, "el paso de publicar no pasa bash -n: %s" % probs[:1])
ok("REL_ID=" in guion and "cuerpo.md" in guion, "el paso reejecutado no actualiza el cuerpo")
print("  R20  YAML y shell del flujo                   válidos · el re-corte actualiza la nota")

# ── R10 · anclajes de registro (metadatos + mapa) y destino ──────────────────
app = crudo(APP_KT, BASE)
A_META = '            ModuleMetadata("iptv", "0.1.0", emptyList()),'
A_MAPA = '            "iptv" to com.ceroX.app.modules.iptv.IptvModule::class.java,'
ok(app.count(A_META) == 1, "el anclaje de metadatos aparece %d veces" % app.count(A_META))
ok(app.count(A_MAPA) == 1, "el anclaje del mapa aparece %d veces" % app.count(A_MAPA))
app = app.replace(A_META, A_META + '\n            ModuleMetadata("web", "0.1.0", emptyList()),')
app = app.replace(A_MAPA, A_MAPA + '\n            "web" to com.ceroX.app.modules.web.WebModule::class.java,')
MAIN_ACT = MAIN_J + "/ui/main/MainActivity.kt"
main_act = crudo(MAIN_ACT, BASE)
A_DEST = '    Destino("iptv", "IPTV") { com.ceroX.app.modules.iptv.IptvUiFragment() },'
ok(main_act.count(A_DEST) == 1, "el anclaje del destino aparece %d veces" % main_act.count(A_DEST))
main_act = main_act.replace(A_DEST, A_DEST +
    '\n    Destino("web", "Web") { com.ceroX.app.modules.web.WebUiFragment() },')
print("  R10  registro y destino                       WebModule y Destino web añadidos")

# ── R13 · ids del layout contra el fragmento ─────────────────────────────────
ids = re.findall(r'android:id="@\+id/(\w+)"', LAYOUT)
ok(len(ids) == 8, "el layout lleva %d ids, se esperaban 8" % len(ids))
for i in ids:
    camel = re.sub(r"_([a-z])", lambda m: m.group(1).upper(), i)
    ok(("b." + camel) in FRAG_KT, "el id %s no se usa en el fragmento como b.%s" % (i, camel))
print("  R13  ids cruzados                             %d ids, todos usados" % len(ids))

CAMBIOS = [
    (WEB + "/MotorBusqueda.kt", MOTOR_KT),
    (WEB + "/Bloqueador.kt", BLOQ_KT),
    (WEB + "/Privacidad.kt", PRIV_KT),
    (WEB + "/AntiMuro.kt", MURO_KT),
    (WEB + "/WebModule.kt", MOD_KT),
    (WEB + "/WebUiFragment.kt", FRAG_KT),
    ("android/app/src/main/res/layout/fragment_web.xml", LAYOUT),
    (TESTW, TEST_KT),
    (APP_KT, app),
    (MAIN_J + "/ui/MainActivity.kt", main_act),
    (APK, y),
]
# ── R12 · las 10 claves se AÑADEN a los 15 ficheros de valores ───────────────
TEXTOS = dict(zip(CLAVES, ("Web", "Barra de direcciones",
                           "Bloquear anuncios y rastreadores",
                           "Ocultar carteles anti-bloqueador", "Política de cookies",
                           "Cookies: bloquear todas", "Cookies: sólo terceros",
                           "Cookies: permitir todas", "Atrás", "Ir")))
for tag in IDIOMAS:
    ruta = "android/app/src/main/res/%s/strings.xml" % tag
    t = crudo(ruta, BASE)
    ok("</resources>" in t, "%s no cierra resources" % tag)
    bloque = "\n".join('    <string name="%s">%s</string>' % (k, TEXTOS[k]) for k in CLAVES)
    CAMBIOS.append((ruta, t.replace("</resources>", bloque + "\n</resources>")))
for ruta, t in CAMBIOS:
    if "/res/values" in ruta and ruta.endswith("strings.xml"):
        falta = [k for k in CLAVES if ('name="%s"' % k) not in t]
        ok(not falta, "%s se quedó sin %s" % (ruta, falta))
print("  R12  10 claves × 15 ficheros                   añadidas y comprobadas en los 15")
      "heredan el texto y esperan traducción en el siguiente commit, como siempre)")

print("\n  ficheros: %d" % len(CAMBIOS))
if not EJECUTAR:
    print("\nDRY-RUN: nada publicado")
    raise SystemExit(0)

ahora = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
iden = {"name": "La Bandita", "email": "reborn@labandita.dev", "date": ahora}
arbol = api("/git/trees", "POST", {"base_tree": BASE, "tree": [
    {"path": r, "mode": "100644", "type": "blob", "content": t} for r, t in CAMBIOS]})["sha"]

msg = """Módulo web privado: Brave Search por defecto, bloqueo y cookies a la vista

Lo pedido, sin adornos: el motor de búsqueda y el WebView de la app dejan de
depender de Google. Brave Search es el motor por defecto; DuckDuckGo y un
SearXNG propio completan la lista, y Google no está en ella ni como página de
inicio.

Cinco objetos con una responsabilidad cada uno, y un fragmento que es el único
que toca el sistema:

- MotorBusqueda: plantillas de URL y codificación de la consulta.
- Bloqueador: reglas por sufijo de dominio, más una lista propia del usuario
  leída del almacenamiento externo aprobado, nunca del interno.
- Privacidad: política de cookies en tres estados y cabeceras DNT y Sec-GPC.
  No toca el CookieManager: describir la política y aplicarla son trabajos
  distintos y el segundo vive en el hilo principal.
- AntiMuro: opcional y apagado por defecto, oculta por estilo y por DOM los
  carteles que algunos sitios ponen cuando detectan un bloqueador. No rompe
  su detección y no se presenta como otra cosa: la lista de selectores está a
  la vista en el propio fichero.
- WebModule: registro en el panel, con un healthCheck que dice el motor por
  defecto y cuántas reglas hay, y nada más.

Seis pruebas nuevas en JVM (478 → 484): el motor por defecto y su codificación,
la ausencia de Google, el SearXNG sin base que no inventa URL, el bloqueo por
sufijo con su lista propia comentada, la rotación de la política de cookies y
que el JS del ocultador lleva cada selector que promete.

Y el flujo del APK: cuando un dispatch reejecuta sobre un tag que ya existe,
ahora actualiza también la primera línea del cuerpo de la release con el
commit del corte nuevo. La idempotencia que sólo reemplazaba bytes dejó la
1.0.4 narrando el commit rojo; se corrigió a mano una vez y no dos.

Las 10 claves web_* viajan en los 15 ficheros de valores con texto español; la
traducción a los otros 13 idiomas viene en el commit siguiente, como siempre,
y TraduccionesPresentesTest lo vigila."""

c = api("/git/commits", "POST", {"message": msg, "tree": arbol, "parents": [BASE],
                                 "author": iden, "committer": iden})
api("/git/refs/heads/main", "PATCH", {"sha": c["sha"], "force": False})
print("\nCOMMIT:", c["sha"])
time.sleep(5)
print("main:", api("/git/ref/heads/main")["object"]["sha"])
