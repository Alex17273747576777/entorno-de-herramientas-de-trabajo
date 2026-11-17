#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Commit I: la pantalla de IPTV — fuentes, canales y reproducción.

22 ficheros: el Fragment con sus dos adapters, tres layouts, 22 cadenas en los 15
idiomas del proyecto, el destino en la barra inferior, `liberarReproductor()` en el
módulo y una prueba que cruza los IDs del layout con lo que toca el código.

Antes de publicar se comprueba lo que rompería la compilación o una prueba publicada:
que cada `binding.x` exista como `@+id/x`, que el XML parse, que ninguna cadena nueva
se quede sin traducir, que no haya texto escrito a mano en los layouts, y que los
anclajes sean únicos.
"""
import base64, datetime, json, os, re, sys, time, urllib.request, urllib.error
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from i_textos import CADENAS, IDIOMAS, escapar  # noqa: E402

TOK = os.environ.get("GP")
API = "https://api.github.com/repos/Alex17273747576777/cero-X-app"
APP = "android/app/src/"
MAIN = APP + "main/java/com/ceroX/app/"
TEST = APP + "test/java/com/ceroX/app/"
RES = APP + "main/res/"
P_MOD = MAIN + "modules/iptv/IptvModule.kt"
P_MAIN = MAIN + "ui/main/MainActivity.kt"
P_FRAG = MAIN + "modules/iptv/IptvUiFragment.kt"
P_TEST = TEST + "modules/iptv/IptvPantallaTest.kt"
L_FRAG = RES + "layout/fragment_iptv.xml"
L_FUENTE = RES + "layout/item_fuente_iptv.xml"
L_CANAL = RES + "layout/item_canal_iptv.xml"
BASE_ESPERADO = "708a9904818b581a2d990c567bce91abf31d2bad"
EJECUTAR = "--run" in sys.argv

MARCAS = ["Placeholder", "placeholder", "Simular", "simulado", "TODO:", "FIXME", "dummy",
          "hardcodeado", "sin implementar", "not implemented", "CoreEngine"]
SOSPECHOSAS = ["compatible", "mejorado", "improved", "stabilized", "estable",
               "verificado", "verified", "funciona", "works", "listo"]
PRUEBAS_ANTES = 461


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


BASE = api("/git/ref/heads/main")["object"]["sha"]
ok(BASE == BASE_ESPERADO, "main se movio: " + BASE)
print("MODO: %s · base %s" % ("PUBLICACION" if EJECUTAR else "DRY-RUN", BASE[:8]))


def leer(p):
    return base64.b64decode(api("/contents/%s?ref=%s" % (p, BASE))["content"]).decode()


def solo_codigo(t):
    t = re.sub(r'"""[\s\S]*?"""', " ", t)
    t = t.replace('\\"', " ")
    t = re.sub(r'"[^"\n]*"', " ", t)
    t = re.sub(r"'[^'\n]*'", " ", t)
    t = re.sub(r"/\*[\s\S]*?\*/", " ", t)
    return "\n".join(l for l in t.split("\n") if not l.strip().startswith("//"))


def a_snake(nombre):
    """`fuenteNombre` -> `fuente_nombre`, como ViewBinding lee los `@+id/`."""
    return "_".join(re.findall(r"[A-Z]?[a-z0-9]+", nombre)).lower()


# ══════════════════════════════════════════════════════════════════════════
#  LAYOUTS
# ══════════════════════════════════════════════════════════════════════════

LAYOUT_FRAG = '''<?xml version="1.0" encoding="utf-8"?>
<!--
  La pantalla de IPTV, en tres bloques: las fuentes que instala el usuario, los
  canales que trae la fuente elegida, y el reproductor.

  Los textos vienen de @string/ y no escritos aquí a mano. El proyecto traduce a
  catorce idiomas y TraduccionesPresentesTest vigila que no falte ninguno, así que
  una cadena suelta en el layout sería texto que catorce idiomas no ven. Las otras
  pantallas del proyecto sí las tienen sueltas; esta no las añade nuevas.
-->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="8dp">

    <TextView
        android:id="@+id/estado"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:paddingBottom="8dp"
        android:textSize="14sp" />

    <EditText
        android:id="@+id/fuente_nombre"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="@string/iptv_nombre_fuente"
        android:inputType="text" />

    <EditText
        android:id="@+id/fuente_url"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="@string/iptv_url_lista"
        android:inputType="textUri" />

    <EditText
        android:id="@+id/fuente_huella"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="@string/iptv_huella_opcional"
        android:inputType="text" />

    <RadioGroup
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">

        <RadioButton
            android:id="@+id/tipo_lista"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:checked="true"
            android:text="@string/iptv_tipo_lista" />

        <!-- Sin id a propósito: el código lee la opción marcada por defecto y de
             ahí deduce el tipo. Un id que nadie consulta es una vista muerta. -->
        <RadioButton
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/iptv_tipo_guia" />
    </RadioGroup>

    <Button
        android:id="@+id/boton_anadir_fuente"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="@string/iptv_anadir_fuente" />

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/lista_fuentes"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"
        app:layoutManager="androidx.recyclerview.widget.LinearLayoutManager" />

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">

        <EditText
            android:id="@+id/busqueda_canales"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:hint="@string/iptv_buscar_canal"
            android:inputType="text" />

        <Button
            android:id="@+id/boton_cargar"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/iptv_cargar" />
    </LinearLayout>

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/lista_canales"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"
        app:layoutManager="androidx.recyclerview.widget.LinearLayoutManager" />

    <SurfaceView
        android:id="@+id/superficie_video"
        android:layout_width="match_parent"
        android:layout_height="200dp" />

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">

        <Button
            android:id="@+id/boton_reproducir"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="@string/iptv_reproducir" />

        <Button
            android:id="@+id/boton_pausa"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="@string/iptv_pausa" />

        <Button
            android:id="@+id/boton_parar"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="@string/iptv_parar" />
    </LinearLayout>

    <TextView
        android:id="@+id/reproduccion"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:paddingTop="4dp"
        android:textSize="14sp" />

</LinearLayout>
'''

LAYOUT_FUENTE = '''<?xml version="1.0" encoding="utf-8"?>
<!-- Una fuente instalada: su nombre, qué es y de dónde viene, y cómo quitarla. -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal"
    android:padding="8dp">

    <LinearLayout
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:orientation="vertical">

        <TextView
            android:id="@+id/fuente_titulo"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:textSize="16sp"
            android:textStyle="bold" />

        <TextView
            android:id="@+id/fuente_detalle"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:textSize="13sp" />
    </LinearLayout>

    <Button
        android:id="@+id/boton_quitar_fuente"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/iptv_quitar" />

</LinearLayout>
'''

LAYOUT_CANAL = '''<?xml version="1.0" encoding="utf-8"?>
<!--
  Un canal. No lleva el logo: cargarlo sería una petición de red más por canal de
  una lista que puede tener miles, y esta pantalla no va a hacer eso sin que nadie
  lo pida.
-->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical"
    android:padding="8dp">

    <TextView
        android:id="@+id/canal_titulo"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:textSize="16sp" />

    <TextView
        android:id="@+id/canal_detalle"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:textSize="12sp" />

</LinearLayout>
'''

# ══════════════════════════════════════════════════════════════════════════
#  EL FRAGMENT
# ══════════════════════════════════════════════════════════════════════════

FRAGMENT = '''package com.ceroX.app.modules.iptv

import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.widget.doAfterTextChanged
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.ceroX.app.R
import com.ceroX.app.core.CeroXApplication
import com.ceroX.app.core.Pantallas
import com.ceroX.app.databinding.FragmentIptvBinding
import com.ceroX.app.databinding.ItemCanalIptvBinding
import com.ceroX.app.databinding.ItemFuenteIptvBinding

/**
 * La pantalla de IPTV: las fuentes que instala el usuario, los canales que traen y
 * la reproducción.
 *
 * CÓMO CONSIGUE EL MÓDULO
 * -----------------------
 * Por [Pantallas.modulo], que es el único camino que queda: devuelve null en vez de
 * reventar y, si el módulo todavía no se inicializó —el arranque va en su propio hilo
 * desde la 1.0.1—, lo inicializa en segundo plano y llama a [pintar] al terminar. Una
 * pantalla vacía que dice por qué está vacía es un fallo visible; una excepción es un
 * cierre, que es lo que pasaba antes con seis pantallas.
 *
 * LO QUE AQUÍ NO HAY
 * ------------------
 * Ninguna lista de canales ni ningún «catálogo» de fuentes sugeridas. cero-X no lleva
 * fuentes dentro del APK: las pone el usuario, una por una, y se descargan al
 * cargarlas. Un buscador de listas recomendadas sería exactamente lo mismo con otro
 * nombre, y la licencia del contenido no la decide esta app.
 *
 * HILOS
 * -----
 * Descargar una lista y escribir el almacén van en su propio hilo ([enSegundoPlano]):
 * en el principal congelarían la interfaz, que es el fallo que tenía la app al
 * arrancar. La reproducción **no** va fuera: ExoPlayer comprueba desde qué hilo se le
 * llama y lanza si no es el suyo, y puede quedarse en el principal porque preparar y
 * empezar no bloquean —la red la atiende el propio reproductor—.
 */
class IptvUiFragment : Fragment() {

    private lateinit var binding: FragmentIptvBinding
    private val principal = Handler(Looper.getMainLooper())
    private val adaptadorFuentes = FuentesAdapter()
    private val adaptadorCanales = CanalesAdapter()

    private var modulo: IptvModule? = null
    private var reproductor: ReproductorIptv? = null
    private var fuentesActuales: List<Fuente> = emptyList()
    private var fuenteElegida: String? = null
    private var enMarcha: Canal? = null
    private var falloReproduccion: String? = null
    private var ultimoAviso: String? = null
    private var filtro = ""

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?,
    ): View {
        binding = FragmentIptvBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val app = requireActivity().application as CeroXApplication
        modulo = Pantallas.modulo(app, "iptv", IptvModule::class.java) {
            if (isAdded) pintar()
        }

        binding.listaFuentes.layoutManager = LinearLayoutManager(requireContext())
        binding.listaFuentes.adapter = adaptadorFuentes
        adaptadorFuentes.alTocar = { fuente ->
            fuenteElegida = fuente.nombre
            adaptadorFuentes.submit(fuentesActuales, fuenteElegida)
        }
        adaptadorFuentes.alQuitar = { fuente -> quitar(fuente) }

        binding.listaCanales.layoutManager = LinearLayoutManager(requireContext())
        binding.listaCanales.adapter = adaptadorCanales
        adaptadorCanales.alTocar = { canal -> reproducir(canal) }

        binding.botonAnadirFuente.setOnClickListener { anadir() }
        binding.botonCargar.setOnClickListener { cargar() }
        binding.botonReproducir.setOnClickListener { seguir() }
        binding.botonPausa.setOnClickListener { pausar() }
        binding.botonParar.setOnClickListener { pararTodo() }
        binding.busquedaCanales.doAfterTextChanged { texto ->
            filtro = texto?.toString()?.trim().orEmpty()
            pintarCanales()
        }

        pintar()
    }

    override fun onDestroyView() {
        // La superficie se va con la vista. Un reproductor vivo enganchado a una
        // superficie muerta se queda el decodificador de hardware, y el siguiente que
        // se cree no lo va a tener. Se libera sin crearlo: pedirle el reproductor al
        // módulo aquí lo construiría sólo para soltarlo.
        modulo?.liberarReproductor()
        reproductor = null
        enMarcha = null
        falloReproduccion = null
        super.onDestroyView()
    }

    // ── acciones ───────────────────────────────────────────────────────────

    private fun anadir() {
        val m = modulo ?: return
        val r = resources
        val nombre = binding.fuenteNombre.text.toString().trim()
        val url = binding.fuenteUrl.text.toString().trim()
        val huella = binding.fuenteHuella.text.toString().trim()
        // Se lee la opción marcada por defecto y no la otra: si se leen las dos,
        // una de las dos vistas queda sin usar, que es un adorno.
        val tipo = if (binding.tipoLista.isChecked) "m3u" else "xmltv"
        // Nada de estado de la pantalla dentro de este lambda: corre en otro hilo y
        // quien repinta es el principal. La fuente añadida se elige tocándola, que es
        // lo que dice el texto de estado.
        enSegundoPlano {
            val hecho = m.anadirFuente(nombre, url, tipo, huella.ifEmpty { null })
            if (hecho.motivo != null) {
                hecho.motivo
            } else {
                r.getString(R.string.iptv_fuente_anadida, hecho.fuente?.nombre ?: nombre)
            }
        }
    }

    private fun quitar(fuente: Fuente) {
        val m = modulo ?: return
        val r = resources
        val nombre = fuente.nombre
        enSegundoPlano {
            // Si la fuente quitada era la elegida, pintar() la descarta: ya no está en
            // la lista. Tocarlo aquí sería escribir estado desde otro hilo.
            val fallo = m.quitarFuente(nombre)
            fallo ?: r.getString(R.string.iptv_fuente_quitada, nombre)
        }
    }

    private fun cargar() {
        val m = modulo ?: return
        val r = resources
        val nombre = fuenteElegida
        if (nombre == null) {
            ultimoAviso = r.getString(R.string.iptv_elige_fuente)
            pintar()
            return
        }
        enSegundoPlano {
            val carga = m.cargar(nombre)
            if (carga.correcta) {
                r.getString(R.string.iptv_canales_cargados, carga.cuantos, nombre)
            } else {
                carga.motivo
            }
        }
    }

    private fun reproducir(canal: Canal) {
        val m = modulo ?: return
        falloReproduccion = null
        // En el hilo principal a propósito: ver el comentario de la clase.
        val fallo = m.reproducir(canal, binding.superficieVideo)
        if (fallo != null) {
            falloReproduccion = fallo
            enMarcha = null
        } else {
            enMarcha = canal
            // Ya existe: reproducir lo acaba de crear, así que esto no construye nada.
            reproductor = m.reproductor()
        }
        pintarReproduccion()
    }

    private fun seguir() {
        val r = reproductor
        if (r == null) {
            falloReproduccion = resources.getString(R.string.iptv_elige_canal)
            pintarReproduccion()
            return
        }
        falloReproduccion = r.empezar()
        pintarReproduccion()
    }

    private fun pausar() {
        reproductor?.pausar()
    }

    private fun pararTodo() {
        modulo?.liberarReproductor()
        reproductor = null
        enMarcha = null
        falloReproduccion = null
        pintarReproduccion()
    }

    /**
     * Trabajo que toca red o disco fuera del hilo principal, y repintado en él.
     *
     * [trabajo] devuelve el aviso que hay que enseñar. Si lanza, el aviso es la
     * excepción con su mensaje: un fallo que no se enseña es un botón que parece no
     * hacer nada, y esta app ya tuvo bastantes de ésos.
     */
    private fun enSegundoPlano(trabajo: () -> String?) {
        Thread({
            val aviso = try {
                trabajo()
            } catch (e: Exception) {
                val detalle = e.message
                if (detalle == null) e.javaClass.simpleName else e.javaClass.simpleName + ": " + detalle
            }
            principal.post {
                if (!isAdded) return@post
                ultimoAviso = aviso
                pintar()
            }
        }, "cerox-iptv-pantalla").start()
    }

    // ── pintado ────────────────────────────────────────────────────────────

    private fun pintar() {
        val m = modulo
        if (m == null) {
            binding.estado.text = getString(R.string.iptv_modulo_no_disponible)
            pintarReproduccion()
            return
        }
        val listado = m.fuentes()
        fuentesActuales = listado.fuentes
        if (listado.fuentes.none { it.nombre == fuenteElegida }) fuenteElegida = null
        adaptadorFuentes.submit(listado.fuentes, fuenteElegida)
        binding.estado.text = textoDeEstado(listado, m.canales().size)
        pintarCanales()
        pintarReproduccion()
    }

    private fun pintarCanales() {
        val m = modulo ?: return
        val visibles = if (filtro.isEmpty()) m.canales() else m.buscar(filtro)
        adaptadorCanales.submit(visibles)
    }

    private fun pintarReproduccion() {
        val fallo = falloReproduccion
        val canal = enMarcha
        binding.reproduccion.text = when {
            fallo != null -> fallo
            canal != null -> getString(R.string.iptv_reproduciendo, canal.titulo)
            else -> getString(R.string.iptv_sin_reproduccion)
        }
    }

    /**
     * Lo que se lee arriba. Primero el aviso de la última acción, porque es lo que el
     * usuario acaba de preguntar; después lo que diga el almacén; después cuántos
     * canales hay. Nunca un «listo» genérico: si algo falló, se enseña el motivo que
     * devolvió el módulo, que para eso lo devuelve.
     */
    private fun textoDeEstado(listado: Listado, cuantosCanales: Int): String {
        ultimoAviso?.let { return it }
        listado.motivo?.let { return it }
        if (listado.fuentes.isEmpty()) return getString(R.string.iptv_sin_fuentes)
        if (cuantosCanales > 0) {
            val de = fuenteElegida ?: listado.fuentes[0].nombre
            return getString(R.string.iptv_canales_cargados, cuantosCanales, de)
        }
        return getString(R.string.iptv_estado_inicial)
    }
}

/** Las fuentes instaladas. La elegida se marca con una flecha delante. */
private class FuentesAdapter : RecyclerView.Adapter<FuentesAdapter.Vista>() {

    var alTocar: (Fuente) -> Unit = {}
    var alQuitar: (Fuente) -> Unit = {}

    private var elementos: List<Fuente> = emptyList()
    private var elegida: String? = null

    fun submit(nuevos: List<Fuente>, elegida: String?) {
        elementos = nuevos
        this.elegida = elegida
        notifyDataSetChanged()
    }

    class Vista(val b: ItemFuenteIptvBinding) : RecyclerView.ViewHolder(b.root)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): Vista =
        Vista(ItemFuenteIptvBinding.inflate(LayoutInflater.from(parent.context), parent, false))

    override fun getItemCount(): Int = elementos.size

    override fun onBindViewHolder(holder: Vista, position: Int) {
        val f = elementos[position]
        val detalle = f.tipo + " · " + f.url
        holder.b.fuenteTitulo.text = f.nombre
        holder.b.fuenteDetalle.text = if (f.nombre == elegida) "▸ $detalle" else detalle
        holder.b.botonQuitarFuente.setOnClickListener { alQuitar(f) }
        holder.itemView.setOnClickListener { alTocar(f) }
    }
}

/** Los canales de la fuente cargada. */
private class CanalesAdapter : RecyclerView.Adapter<CanalesAdapter.Vista>() {

    var alTocar: (Canal) -> Unit = {}

    private var elementos: List<Canal> = emptyList()

    fun submit(nuevos: List<Canal>) {
        elementos = nuevos
        notifyDataSetChanged()
    }

    class Vista(val b: ItemCanalIptvBinding) : RecyclerView.ViewHolder(b.root)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): Vista =
        Vista(ItemCanalIptvBinding.inflate(LayoutInflater.from(parent.context), parent, false))

    override fun getItemCount(): Int = elementos.size

    override fun onBindViewHolder(holder: Vista, position: Int) {
        val c = elementos[position]
        val grupo = c.grupo
        holder.b.canalTitulo.text = c.titulo
        holder.b.canalDetalle.text = if (grupo == null) c.url else grupo + " · " + c.url
        holder.itemView.setOnClickListener { alTocar(c) }
    }
}
'''

# ══════════════════════════════════════════════════════════════════════════
#  LA PRUEBA
# ══════════════════════════════════════════════════════════════════════════

PRUEBA = '''package com.ceroX.app.modules.iptv

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test
import java.io.File

/**
 * El cableado de la pantalla de IPTV.
 *
 * Nada de esto abre un teléfono: crear el Fragment necesita una actividad y una
 * superficie de vídeo necesita un decodificador. Lo que se comprueba aquí es lo que
 * se rompe **en silencio** y no falla hasta que alguien toca la pantalla:
 *
 *   · una vista que el código pide y el layout no tiene (no compila, pero se escribe
 *     fácil cuando el layout y el Kotlin se hacen a la vez),
 *   · un texto suelto en el layout, que catorce idiomas no verían nunca,
 *   · una cadena nueva sin traducir,
 *   · un destino de la barra inferior que no lleva a ningún sitio, que es exactamente
 *     el fallo que tenía esta app y por el que se veía en blanco,
 *   · un reproductor que no se libera al morir la vista y se queda el decodificador.
 */
class IptvPantallaTest {

    private val fuentes = File("src/main/java/com/ceroX/app")
    private val recursos = File("src/main/res")

    private fun leer(f: File): String {
        assertTrue("falta " + f.path, f.isFile)
        return f.readText()
    }

    private val pantalla: String get() = leer(File(fuentes, "modules/iptv/IptvUiFragment.kt"))
    private val moduloKt: String get() = leer(File(fuentes, "modules/iptv/IptvModule.kt"))
    private val layoutFragmento: String get() = leer(File(recursos, "layout/fragment_iptv.xml"))
    private val layoutsDeItem: String
        get() = leer(File(recursos, "layout/item_fuente_iptv.xml")) +
            leer(File(recursos, "layout/item_canal_iptv.xml"))

    private fun ids(xml: String): Set<String> =
        Regex("""android:id="@\\+id/([a-z0-9_]+)"""").findAll(xml)
            .map { it.groupValues[1] }.toSet()

    /** `fuenteNombre` → `fuente_nombre`, que es como ViewBinding nombra las vistas. */
    private fun aSnake(nombre: String): String = buildString {
        for (c in nombre) {
            if (c.isUpperCase()) append('_').append(c.lowercaseChar()) else append(c)
        }
    }

    @Test
    fun `la pantalla pide su modulo al gestor y no a un registro`() {
        val t = pantalla
        assertTrue("no pide el módulo por Pantallas", t.contains("Pantallas.modulo"))
        assertTrue("y no pide el módulo iptv", t.contains("\\"iptv\\""))
        assertFalse("sigue buscando en un registro", t.contains("registry.getInstance"))
        assertTrue(
            "si el módulo no está, la pantalla tiene que decirlo en vez de quedarse muda",
            t.contains("iptv_modulo_no_disponible"),
        )
    }

    @Test
    fun `cada vista que toca el codigo existe en su layout`() {
        val delFragmento = ids(layoutFragmento)
        assertTrue("el layout del fragmento no declara ninguna vista", delFragmento.isNotEmpty())
        val pedidos = Regex("""binding\\.([a-z][A-Za-z0-9]*)""").findAll(pantalla)
            .map { it.groupValues[1] }.filter { it != "root" }.toSet()
        assertTrue("el código no toca ninguna vista", pedidos.isNotEmpty())
        assertEquals(
            "el código pide vistas que el layout no tiene: no compilaría",
            emptySet<String>(),
            pedidos.filter { aSnake(it) !in delFragmento }.toSet(),
        )

        val deItems = ids(layoutsDeItem)
        val pedidosItems = Regex("""\\bb\\.([a-z][A-Za-z0-9]*)""").findAll(pantalla)
            .map { it.groupValues[1] }.filter { it != "root" }.toSet()
        assertTrue("los adapters no tocan ninguna vista", pedidosItems.isNotEmpty())
        assertEquals(
            "un adapter pide vistas que su layout no tiene",
            emptySet<String>(),
            pedidosItems.filter { aSnake(it) !in deItems }.toSet(),
        )

        // Y al revés: una vista declarada y no usada es un adorno, que es lo que esta
        // app tenía por todas partes antes de la limpieza.
        val usados = pedidos.map { aSnake(it) } + pedidosItems.map { aSnake(it) }
        assertEquals(
            "vistas declaradas que nadie usa",
            emptySet<String>(),
            (delFragmento + deItems).filter { it !in usados }.toSet(),
        )
    }

    @Test
    fun `ningun layout escribe texto a mano`() {
        for (xml in listOf(layoutFragmento, layoutsDeItem)) {
            val sueltos = Regex("""android:(?:text|hint)="([^"]*)"""").findAll(xml)
                .map { it.groupValues[1] }
                .filter { !it.startsWith("@string/") }
                .toList()
            assertEquals(
                "texto que no pasa por strings.xml y por tanto no se traduce",
                emptyList<String>(),
                sueltos,
            )
        }
    }

    @Test
    fun `las cadenas de la pantalla estan en los quince idiomas`() {
        val usadas = (
            Regex("""R\\.string\\.(iptv_[a-z_]+)""").findAll(pantalla).map { it.groupValues[1] } +
                Regex("""@string/(iptv_[a-z_]+)""").findAll(layoutFragmento + layoutsDeItem)
                    .map { it.groupValues[1] }
            ).toSet()
        assertTrue("la pantalla no usa ninguna cadena propia: " + usadas, usadas.size >= 20)

        val carpetas = listOf("values") + listOf(
            "en", "ca", "pt", "fr", "id", "ja", "ko", "ru", "th", "tr", "uk", "vi", "zh", "ar",
        ).map { "values-$it" }
        for (carpeta in carpetas) {
            val xml = leer(File(recursos, "$carpeta/strings.xml"))
            for (clave in usadas) {
                val m = Regex("""<string name="$clave">([^<]*)</string>""").find(xml)
                assertTrue("falta $clave en $carpeta", m != null)
                assertTrue(
                    "$clave está vacía en $carpeta: una cadena vacía se ve como un hueco",
                    (m?.groupValues?.get(1) ?: "").trim().isNotEmpty(),
                )
            }
        }
    }

    @Test
    fun `el destino de la barra inferior lleva a la pantalla`() {
        val main = leer(File(fuentes, "ui/main/MainActivity.kt"))
        assertTrue(
            "IPTV no está en la barra inferior: la pantalla existiría y no se podría llegar",
            main.contains("Destino(\\"iptv\\""),
        )
        assertTrue("el destino no crea el fragmento", main.contains("IptvUiFragment()"))
    }

    @Test
    fun `el reproductor se libera al morir la vista`() {
        val t = pantalla
        assertTrue("no hay onDestroyView", t.contains("override fun onDestroyView()"))
        assertTrue("y no libera el reproductor", t.contains("liberarReproductor()"))

        val delModulo = moduloKt
        assertTrue(
            "el módulo no sabe liberar el reproductor sin crearlo",
            delModulo.contains("fun liberarReproductor(): Boolean"),
        )
        val cuerpo = delModulo.substringAfter("fun liberarReproductor(): Boolean")
            .substringBefore("\\n    }\\n")
        assertFalse(
            "liberarReproductor no puede llamar a reproductor(): lo crearía sólo para soltarlo",
            cuerpo.contains("reproductor()"),
        )
        assertTrue("y no libera nada", cuerpo.contains("liberar()"))
    }

    @Test
    fun `la red va fuera del hilo principal y el reproductor dentro`() {
        val cargar = pantalla.substringAfter("private fun cargar()")
            .substringBefore("\\n    private fun")
        assertTrue(
            "cargar descarga una lista: en el hilo principal congelaría la interfaz",
            cargar.contains("enSegundoPlano"),
        )
        val rep = pantalla.substringAfter("private fun reproducir(canal: Canal)")
            .substringBefore("\\n    private fun")
        assertFalse(
            "ExoPlayer lanza si se le llama desde un hilo que no es el suyo",
            rep.contains("enSegundoPlano"),
        )
        assertTrue("y no reproduce nada", rep.contains("m.reproducir(canal, binding.superficieVideo)"))
        assertTrue(
            "el repintado tiene que volver al hilo principal",
            pantalla.contains("Handler(Looper.getMainLooper())"),
        )
    }
}
'''

# ══════════════════════════════════════════════════════════════════════════
#  STRINGS: las 22 cadenas en los 15 ficheros
# ══════════════════════════════════════════════════════════════════════════


def bloque(orden):
    """Las 22 cadenas en el orden del idioma, listas para meter antes de </resources>."""
    lineas = []
    for clave, textos in CADENAS:
        lineas.append('    <string name="%s">%s</string>' % (clave, escapar(textos[orden])))
    return ("\n" if orden == "es" else "\n") + "\n".join(lineas) + "\n"


def meter(texto, orden, ruta):
    ok(texto.count("</resources>") == 1, ruta + ": no hay un solo cierre de resources")
    for clave, _ in CADENAS:
        ok('name="%s"' % clave not in texto, ruta + ": la clave " + clave + " ya existe")
    return texto.replace("</resources>", bloque(orden).lstrip("\n") + "</resources>")


cambios = {
    L_FRAG: LAYOUT_FRAG,
    L_FUENTE: LAYOUT_FUENTE,
    L_CANAL: LAYOUT_CANAL,
    P_FRAG: FRAGMENT,
    P_TEST: PRUEBA,
}
nuevos = set(cambios)

# strings.xml de los 15 idiomas
for orden in ["es"] + IDIOMAS:
    ruta = RES + ("values/strings.xml" if orden == "es" else "values-%s/strings.xml" % orden)
    cambios[ruta] = meter(leer(ruta), orden, ruta)

# ── IptvModule: liberar sin crear, y un comentario que ya no era verdad ────

mod = leer(P_MOD)
mod_original = mod
ancla = """    fun parar() {
        reproductor?.pausar()
    }
"""
ok(mod.count(ancla) == 1, "ancla de parar(): %d" % mod.count(ancla))
mod = mod.replace(ancla, ancla + '''
    /**
     * Libera el reproductor si existe, **sin crearlo**, y dice si había algo que
     * liberar.
     *
     * Existe porque la pantalla necesita soltar el decodificador al destruir su
     * vista, y [reproductor] lo construiría sólo para eso: reservar hardware que
     * nadie va a usar. Devolver el dato tampoco es adorno —quien llama puede saber
     * si de verdad se liberó algo o si no había nada—.
     */
    fun liberarReproductor(): Boolean {
        val r = reproductor ?: return false
        r.liberar()
        reproductor = null
        return true
    }
''')

viejo_com = '''        /** En el directorio privado de la app: no es contenido del usuario que haya
         *  que exponer, y no viaja en el APK. */'''
nuevo_com = '''        /** En la carpeta propia de la app dentro del almacenamiento externo, que es
         *  donde la regla de almacenamiento del proyecto manda poner los datos. No
         *  viaja en el APK y no está en el almacenamiento interno. */'''
ok(mod.count(viejo_com) == 1, "ancla del comentario del companion: %d" % mod.count(viejo_com))
mod = mod.replace(viejo_com, nuevo_com)
cambios[P_MOD] = mod

# ── MainActivity: el destino ──────────────────────────────────────────────

main = leer(P_MAIN)
main_original = main
ancla_main = '''    Destino("catalogo", "Catálogo") { com.ceroX.app.modules.catalog.CatalogUIFragment() },
)'''
ok(main.count(ancla_main) == 1, "ancla de DESTINOS: %d" % main.count(ancla_main))
main = main.replace(ancla_main, '''    Destino("catalogo", "Catálogo") { com.ceroX.app.modules.catalog.CatalogUIFragment() },
    // Un destino es un Fragment que existe: esta entrada se añade con la pantalla
    // hecha, no antes. Una barra con un botón que no lleva a ningún sitio es justo
    // lo que hacía que esta app se viera en blanco.
    Destino("iptv", "IPTV") { com.ceroX.app.modules.iptv.IptvUiFragment() },
)''')
cambios[P_MAIN] = main

# ══════════════════════════════════════════════════════════════════════════
#  COMPROBACIONES
# ══════════════════════════════════════════════════════════════════════════

print("\nCOMPROBACIONES")

# 1 · XML parseable y cadenas completas
for orden in ["es"] + IDIOMAS:
    ruta = RES + ("values/strings.xml" if orden == "es" else "values-%s/strings.xml" % orden)
    t = cambios[ruta]
    try:
        ET.fromstring(t)
    except ET.ParseError as e:
        raise SystemExit("%s no es XML valido: %s" % (ruta, e))
    for clave, textos in CADENAS:
        m = re.search(r'<string name="%s">([^<]*)</string>' % clave, t)
        ok(m, "%s: falta %s" % (ruta, clave))
        ok(m.group(1).strip(), "%s: %s vacia" % (ruta, clave))
        ok("%1" not in textos[orden] or "%1$" in textos[orden],
           "%s: marcador mal escrito en %s" % (ruta, clave))
    # Los marcadores tienen que ser los mismos en los 15 idiomas.
    for clave, textos in CADENAS:
        base = re.findall(r"%\d\$[ds]", textos["es"])
        for idioma in IDIOMAS:
            ok(sorted(base) == sorted(re.findall(r"%\d\$[ds]", textos[idioma])),
               "%s: los marcadores de %s no coinciden con la base en %s" % (ruta, clave, idioma))
for p in [L_FRAG, L_FUENTE, L_CANAL]:
    try:
        ET.fromstring(cambios[p])
    except ET.ParseError as e:
        raise SystemExit("%s no es XML valido: %s" % (p, e))
print("  XML valido                %d strings.xml + 3 layouts" % (len(IDIOMAS) + 1))
print("  cadenas                   %d claves x %d idiomas, marcadores iguales" % (len(CADENAS), len(IDIOMAS) + 1))

# 2 · IDs cruzados en las dos direcciones
ids_frag = set(re.findall(r'android:id="@\+id/([a-z0-9_]+)"', LAYOUT_FRAG))
ids_items = set(re.findall(r'android:id="@\+id/([a-z0-9_]+)"', LAYOUT_FUENTE + LAYOUT_CANAL))
ok(len(ids_frag) == 15, "el layout del fragmento declara %d ids, se esperaban 15" % len(ids_frag))
ok(len(ids_items) == 5, "los items declaran %d ids, se esperaban 5" % len(ids_items))
usa_frag = set(re.findall(r"binding\.([a-z][A-Za-z0-9]*)", FRAGMENT)) - {"root"}
usa_items = set(re.findall(r"\bb\.([a-z][A-Za-z0-9]*)", FRAGMENT)) - {"root"}
huerfanos = {u for u in usa_frag if a_snake(u) not in ids_frag}
ok(not huerfanos, "el codigo pide vistas que el layout no tiene: %s" % sorted(huerfanos))
huerfanos2 = {u for u in usa_items if a_snake(u) not in ids_items}
ok(not huerfanos2, "un adapter pide vistas que su item no tiene: %s" % sorted(huerfanos2))
usados = {a_snake(u) for u in usa_frag | usa_items}
muertos = (ids_frag | ids_items) - usados
ok(not muertos, "vistas declaradas que nadie usa: %s" % sorted(muertos))
print("  IDs cruzados              %d del fragmento + %d de items, sin huerfanos ni muertos"
      % (len(ids_frag), len(ids_items)))

# 3 · Las cadenas que se usan existen
usadas = set(re.findall(r"R\.string\.(iptv_[a-z_]+)", FRAGMENT))
usadas |= set(re.findall(r"@string/(iptv_[a-z_]+)", LAYOUT_FRAG + LAYOUT_FUENTE + LAYOUT_CANAL))
usadas |= set(re.findall(r"R\.string\.(iptv_[a-z_]+)", PRUEBA))
definidas = {c for c, _ in CADENAS}
ok(usadas <= definidas, "se usan cadenas que no estan definidas: %s" % sorted(usadas - definidas))
sin_usar = definidas - usadas
ok(not sin_usar, "cadenas definidas que nadie usa (habria que traducirlas igual): %s" % sorted(sin_usar))
print("  cadenas usadas            %d, todas definidas y todas usadas" % len(usadas))

# 4 · Ningun texto a mano en los layouts
for p in [L_FRAG, L_FUENTE, L_CANAL]:
    for attr, valor in re.findall(r'android:(text|hint)="([^"]*)"', cambios[p]):
        ok(valor.startswith("@string/"), "%s: texto sin traducir %r" % (p, valor))
print("  texto en layouts          todo por @string/")

# 5 · Kotlin: prohibidos y balance
for p in [P_FRAG, P_MOD, P_MAIN, P_TEST]:
    t = cambios[p]
    for m in MARCAS:
        ok(m not in t, "marca %r en %s" % (m, p))
    cod = solo_codigo(t)
    ok(cod.count("{") == cod.count("}"), "%s: llaves %d/%d" % (p, cod.count("{"), cod.count("}")))
    ok(cod.count("(") == cod.count(")"), "%s: parentesis %d/%d" % (p, cod.count("("), cod.count(")")))
for p in [P_FRAG, P_MOD]:
    t = cambios[p]
    ok("!!" not in t, p + ": doble ! prohibido")
    ok('?: ""' not in t, p + ': ?: con cadena vacia')
    ok("filesDir" not in t, p + ": almacenamiento interno prohibido")
    for linea in t.split("\n"):
        c = linea.strip()
        if c.startswith("//") or c.startswith("*"):
            continue
        if "*/" in c and c != "*/" and not c.endswith("*/"):
            raise SystemExit("%s: un */ a mitad de linea: %s" % (p, c[:70]))
print("  Kotlin                    sin !!, sin ?: vacio, sin interno, balanceado")

# 6 · IptvReproductorTest lee cuatro ficheros, así que no se puede exigir que todos
#    sus literales estén en el módulo. Lo exacto: cada literal que la prueba busca y
#    que ESTABA en IptvModule.kt tiene que seguir estando. El cambio es aditivo (un
#    método nuevo y un comentario corregido), así que nada puede desaparecer.
publicado = leer(TEST + "modules/iptv/IptvReproductorTest.kt")
vigilados = 0
for lit in re.findall(r't\.contains\("([^"]+)"\)', publicado):
    lit = lit.replace('\\"', '"').replace("\\n", "\n")
    if lit not in mod_original:
        continue
    vigilados += 1
    ok(lit in cambios[P_MOD], "IptvReproductorTest exige %r y el cambio lo ha quitado" % lit)
ok(vigilados >= 8, "solo %d literales vigilados: el filtro se ha pasado" % vigilados)
ok("directorio privado" not in cambios[P_MOD],
   "el comentario que ya no era verdad sigue ahi")
ok("almacenamiento externo" in cambios[P_MOD], "y no se ha dicho donde vive ahora")
print("  IptvReproductorTest        %d literales del modulo, todos presentes" % vigilados)

# 7 · El destino y el conteo
ok(cambios[P_MAIN].count("Destino(") == main_original.count("Destino(") + 1, "conteo de destinos raro")
ok('Destino("iptv", "IPTV")' in cambios[P_MAIN], "el destino no quedo como se esperaba")
ok(cambios[P_TEST].count("@Test") == 7, "la prueba nueva tiene %d @Test" % cambios[P_TEST].count("@Test"))
print("  destinos                  5 -> 6")
print("  pruebas                   %d -> %d (+7)" % (PRUEBAS_ANTES, PRUEBAS_ANTES + 7))

for p in sorted(cambios):
    print("  %7d B · %s%s" % (len(cambios[p].encode()), p.replace(APP, "…/"),
                              "" if p in nuevos else "   (editado)"))

if not EJECUTAR:
    print("\nDRY-RUN: nada publicado")
    raise SystemExit(0)

ahora = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
iden = {"name": "La Bandita", "email": "reborn@labandita.dev", "date": ahora}
arb = api("/git/trees", "POST", {"base_tree": BASE, "tree": [
    {"path": p, "mode": "100644", "type": "blob", "content": cambios[p]}
    for p in sorted(cambios)]})["sha"]
msg = """IPTV: la pantalla, con las 22 cadenas en los 15 idiomas del proyecto

El módulo ya tenía API para todo (fuentes, anadirFuente, quitarFuente, cargar,
canales, buscar, grupos, guia, reproducir, parar) y no había forma de llegar a ella.
Esta es la pantalla que la usa, y un destino «IPTV» en la barra inferior para poder
abririrla: un destino es un Fragment que existe, no un botón que no lleva a ningún
sitio, que es el fallo que dejaba esta app en blanco.

QUÉ HACE
--------
Arriba, el formulario para instalar una fuente: nombre, URL, SHA-256 esperado
(opcional) y si es una lista de canales (M3U) o una guía (XMLTV). Debajo, las fuentes
instaladas —se toca una para elegirla, se marca con una flecha, y cada una tiene su
botón para quitarla—. «Cargar» descarga la fuente elegida, comprueba su huella si la
declaró, la parsea y llena la lista de canales; el buscador filtra sobre lo cargado.
Tocar un canal lo reproduce en el SurfaceView, con reproducir, pausa y parar, y debajo
el motivo de lo que haya fallado.

LO QUE NO HAY, Y ES A PROPÓSITO
-------------------------------
Ninguna lista de canales dentro del APK y ningún catálogo de fuentes «recomendadas».
Las fuentes las pone el usuario, una por una. Tampoco se cargan los logos de los
canales: sería una petición de red más por canal en listas que pueden tener miles, y
esta pantalla no hace eso sin que nadie lo pida —está dicho en el layout—.

DETALLES QUE ROMPEN SI NO SE DICEN
----------------------------------
  · Hilos. Descargar y escribir el almacén van en su propio hilo; en el principal
    congelarían la interfaz, que es el fallo que tenía la app al arrancar. La
    reproducción NO va fuera: ExoPlayer comprueba desde qué hilo se le llama y lanza
    si no es el suyo, y puede quedarse dentro porque preparar y empezar no bloquean.
  · `IptvModule.liberarReproductor()` es nuevo y existe por esto: al destruir la vista
    hay que soltar el decodificador, y `reproductor()` lo crearía sólo para liberarlo,
    que es reservar hardware para nada. Libera sin crear y dice si había algo.
  · Si el módulo no está disponible, la pantalla lo dice con su propia cadena en vez
    de quedarse muda: pide el módulo por `Pantallas.modulo`, que devuelve null y lo
    inicializa en segundo plano repintando al terminar.
  · Cada fallo se enseña con el motivo que devolvió el módulo. Ningún «listo» genérico.

TRADUCCIONES
------------
22 cadenas nuevas, y cada una en los quince ficheros: values/ y las catorce carpetas
values-<tag>. `TraduccionesPresentesTest` exige que no falte ninguna y que ninguna
esté vacía, así que una cadena suelta en el layout habría sido texto que catorce
idiomas no ven. Los apóstrofos van escapados, que en un recurso de Android sin la
barra no compila.

LA PRUEBA NUEVA (7, y van 468)
------------------------------
`IptvPantallaTest` comprueba lo que se rompe en silencio: que cada vista que toca el
código exista en su layout **y al revés** (una vista declarada que nadie usa es un
adorno), que ningún layout escriba texto a mano, que las 22 cadenas estén en los 15
idiomas y no vacías, que el destino lleve a la pantalla, que el reproductor se libere
al morir la vista sin crearlo, y que la red vaya fuera del hilo principal mientras el
reproductor se queda dentro.

También corrige un comentario de `IptvModule` que el commit anterior dejó mintiendo:
decía que el almacén vive «en el directorio privado de la app» cuando desde entonces
vive en la carpeta propia del almacenamiento externo.

SIN COMPROBAR EN UN DISPOSITIVO. Que el vídeo se vea, que el SurfaceView se enganche
bien y que una lista real se reproduzca lo dice un teléfono, no estas pruebas: aquí no
hay ni emulador ni decodificador. El banco es el V60 ThinQ 5G."""
c = api("/git/commits", "POST", {"message": msg, "tree": arb, "parents": [BASE],
                                 "author": iden, "committer": iden})
api("/git/refs/heads/main", "PATCH", {"sha": c["sha"], "force": False})
print("\nCOMMIT:", c["sha"])
time.sleep(5)
print("main:", api("/git/ref/heads/main")["object"]["sha"])
