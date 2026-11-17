#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Registro de reglas de cero-X: incidente → contra → evolución.

Cada regla nace de un fallo concreto, con su commit. Ninguna es genérica: dicen
qué fichero, qué literal, qué API. Y cada una lleva dos fixtures —la que
reproduce el incidente y la que ya está arreglada—, así que `pruebas_reglas.py`
puede demostrar que la regla caza lo que dice cazar.

CÓMO SE AÑADE UNA REGLA NUEVA (y es la única forma)
---------------------------------------------------
1. El fallo ocurre y se arregla.
2. Se escribe aquí con su commit, su contra y sus dos fixtures.
3. `pruebas_reglas.py` tiene que pasar: la fixture mala debe dar problemas y la
   buena ninguno. Una regla que no caza su propio incidente no es una regla, es
   una opinión.
4. Cuando la regla vuelve a fallar por un caso nuevo, no se sustituye: se añade
   una línea a `evolucion` y se extiende el contra. Así se sabe por qué es como es.
"""
import os
import re

from motor import (PROHIBIDOS, aporta_dato, api_verificada, aplicar_puerta,
                   bloques_literales, idempotente,
                   auditar_almacenamiento, balancear, censar_acciones,
                   auditar_escapes_kotlin, auditar_hilos, auditar_matriz_idiomas,
                   auditar_prosa, censar_pruebas, coincide_literal, comparar_conjuntos,
                   contradicciones, cruzar_ids, exigir_api_verificada, literal_de,
                   mencionar, merece_respuesta, prohibir, separar_prosa, solo_codigo,
                   yaml_valido, mandato_de_paso, sintaxis_de_mandato,
                   correr_mandato, sondeo_sano, lectores_de_literal)

# ── Lo que no se puede escribir, ni siquiera para explicar que no se puede ──

prohibir("gradle", "version_dinamica", "latest.release",
         "el resolvedor de Gradle que elige la última versión disponible",
         "commit H: el comentario que explicaba por qué la versión de media3 es fija "
         "la escribía, y la puerta que la prohíbe mira el fichero entero")
prohibir("gradle", "rango_dinamico", "media3-exoplayer:+",
         "el rango dinámico de la pieza principal del reproductor",
         "misma puerta, mismo commit: cambiaría lo que se compila sin decidirlo")
prohibir("media3", "metodo_inventado", "createMediaItem",
         "el método de la fábrica de fuentes de media3 que no existe",
         "commit 917c3f06: salió rojo en CI con Unresolved reference; el bueno es "
         "createMediaSource y lo dice la documentación, no la memoria")
prohibir("almacenamiento", "interno", "filesDir",
         "el directorio interno de la app",
         "917c3f06 → 708a9904: ReglaDeAlmacenamientoTest prohíbe escribir datos ahí "
         "salvo tokens, y el módulo IPTV guardaba ahí las fuentes del usuario")
prohibir("almacenamiento", "preferencias", "getSharedPreferences",
         "las preferencias de Android, que viven en el interno",
         "regla del proyecto: los ajustes van a core/Prefs, JSON en AlmacenExterno")
prohibir("pantallas", "registro_viejo", "registry.getInstance",
         "la búsqueda de módulos por el registro, que nunca registró nada",
         "3f0fe9d0 / 83c1ef78: seis pantallas se cerraban al abrirlas por pedir su "
         "módulo a un motor que no registraba; el camino bueno es core/Pantallas.modulo")
prohibir("relleno", "pendiente", "TODO:",
         "la marca de trabajo pendiente",
         "barrido de fabricación 8d56dff7…c7c657d4: 45 sitios devolvían éxito "
         "inventado; la marca se prohibió en src/main")


REGLAS = []


def regla(rid, tema, titulo, incidente, contra, comprobar, mala, buena, evolucion):
    REGLAS.append({
        "id": rid, "tema": tema, "titulo": titulo, "incidente": incidente,
        "contra": contra, "comprobar": comprobar, "mala": mala, "buena": buena,
        "evolucion": evolucion,
    })


# ══════════════════════════════════════════════════════════════════════════
#  R1 · La prosa describe, no cita
# ══════════════════════════════════════════════════════════════════════════

def _r1(texto="", mensaje="", **_):
    p = auditar_prosa(texto, donde="fichero")
    p += auditar_prosa(mensaje, donde="mensaje del commit") if mensaje else []
    return ["%s:%d cita %s (%s) — %s" % (d, i, t, n, mencionar(t, n))
            for (i, t, n, _lit, d) in p]


regla("R1", "prosa", "Un comentario que explica una prohibición no puede escribirla",
      "Seis veces. Las dos últimas: el comentario de la versión fija de media3 y el "
      "comentario del arreglo del método inexistente. Las puertas buscan la cadena en "
      "el fichero entero, así que la explicación se convertía en la infracción.",
      "Los literales prohibidos se registran una vez en motor.PROHIBIDOS con su "
      "descripción; la prosa llama a mencionar() y recibe la descripción. Antes de "
      "publicar se audita cada fichero generado Y el mensaje del commit.",
      _r1,
      # Sin triples comillas a propósito: el divisor de prosa de Python las lee
      # como una docstring, y esto es un dato, no documentación.
      {"texto": ("    // Versión fija a propósito. Nada de '1.+' ni '%s': cambiaría\n"
                 "    // lo que se compila sin que nadie lo decida.\n"
                 "    implementation 'androidx.media3:media3-exoplayer:1.11.1'\n"
                 % literal_de("gradle", "version_dinamica"))},
      {"texto": '''    // Versión fija a propósito, y las dos piezas en la misma. Nada de rangos
    // dinámicos ni de resolvedores que elijan la última disponible: cambiarían lo
    // que se compila sin que nadie lo decida. La prueba que vigila esto busca las
    // dos cadenas por su nombre, así que este comentario las describe y no las
    // escribe — citarlas aquí sería exactamente el fallo que la prueba caza.
    implementation 'androidx.media3:media3-exoplayer:1.11.1'
'''},
      ["2026-11-11 · nace como comprobación suelta en h_commit.py",
       "2026-11-11 · se extiende al mensaje del commit, que también se publica",
       "2026-11-11 · se separa prosa de código: las puertas que quitan comentarios "
       "(ReglaDeAlmacenamientoTest) admiten prosa libre; las que no, no"])


# ══════════════════════════════════════════════════════════════════════════
#  R2 · Una puerta nueva mira lo que se añade, salvo que imite a una publicada
# ══════════════════════════════════════════════════════════════════════════

def _puerta_commentario(texto):
    fuera = []
    for i, linea in enumerate(texto.split("\n"), 1):
        t = linea.strip()
        if "*/" in linea and t != "*/" and not t.endswith("*/"):
            fuera.append("%d: un */ a mitad de línea → %s" % (i, t[:60]))
    return fuera


def _r2(antes="", despues="", espejo=False, **_):
    return aplicar_puerta(antes, despues, _puerta_commentario, espejo=espejo)


regla("R2", "puertas", "El ámbito de una puerta nueva se decide, no se supone",
      "La puerta contra */ a mitad de línea disparó contra "
      "`excludes += '/META-INF/*/versions/*'`, que llevaba en build.gradle desde "
      "hacía meses. No era mi código: era un glob dentro de una cadena.",
      "applyer_puerta(antes, despues, puerta, espejo): por defecto sólo lo añadido. "
      "espejo=True sólo cuando la puerta imita a una prueba publicada, porque ésas "
      "mirarán el fichero entero al ejecutarse.",
      _r2,
      {"antes": "    packagingOptions {\n        excludes += '/META-INF/*/versions/*'\n    }\n",
       "despues": "    packagingOptions {\n        excludes += '/META-INF/*/versions/*'\n    }\n"
                  "    // línea nueva con un */ suelto\n",
       "espejo": True},
      {"antes": "    packagingOptions {\n        excludes += '/META-INF/*/versions/*'\n    }\n",
       "despues": "    packagingOptions {\n        excludes += '/META-INF/*/versions/*'\n    }\n"
                  "    implementation 'androidx.media3:media3-exoplayer:1.11.1'\n",
       "espejo": False},
      ["2026-11-11 · nace tras el falso positivo en build.gradle",
       "2026-11-11 · se añade el modo espejo: las puertas que imitan a una prueba "
       "publicada no pueden mirar menos que ella",
       "2026-11-11 · el balance de símbolos deja de hacerse recortando con regex y "
       "pasa al escáner de R16: tres falsos positivos en un día"])


# ══════════════════════════════════════════════════════════════════════════
#  R16 · El balance de símbolos se cuenta con un escáner, no recortando
# ══════════════════════════════════════════════════════════════════════════

def _r16(texto="", **_):
    return balancear(texto)


regla("R16", "balance", "Los símbolos se cuentan con un escáner que sabe dónde está",
      "Tres veces en un día: una regex escrita dentro de una cadena de Kotlin, un "
      "apóstrofo en la prosa y un KDoc largo hicieron creer que faltaba una llave o "
      "un paréntesis donde no faltaba. Cada vez se perdió un ciclo entero persiguiendo "
      "un fallo que no existía.",
      "balancear() recorre el texto carácter a carácter sabiendo si está dentro de un "
      "comentario de línea, de bloque, de una cadena normal, de una cadena cruda o de "
      "un literal de carácter, y dice la línea donde se abrió lo que no se cerró.",
      _r16,
      {"texto": "class A {\n    fun f() {\n        val r = Regex(\"([a-z]\")\n    }\n"},
      {"texto": "class A {\n    fun f() {\n        // una llave suelta } en un comentario\n"
                "        val r = Regex(\"(?<![A-Za-z0-9_])\")\n"
                "        val c = '{\'\n        return r\n    }\n}\n"},
      ["2026-11-11 · nace al preparar la prueba de coherencia, sustituye al recorte "
       "por regex que venía usándose desde la limpieza"])

# ══════════════════════════════════════════════════════════════════════════
#  R17 · En un hilo ajeno, o se aporta un dato o no se comenta
# ══════════════════════════════════════════════════════════════════════════

def _r17(hilo=None, borrador="", **_):
    """El problema es el comentario que se iba a publicar y no aporta nada."""
    veredicto, motivo = merece_respuesta(hilo or {}, borrador)
    return ["comentario de ruido en un hilo ajeno: " + motivo] \
        if veredicto == "callar" else []


_HILO_MUERTO = {"state": "closed", "locked": False,
                "respondio_mantenedor": True, "pendiente": False}
# Cerrado también, pero con una acusación dirigida a la cuenta sin responder: ahí una
# retirada sí corrige algo, y borrarla habría dejado la publicación original en pie.
_HILO_CON_DEUDA = {"state": "closed", "locked": False,
                   "respondio_mantenedor": True, "pendiente": True}

regla("R17", "hilos ajenos", "O el comentario aporta un dato, o no se publica",
      "komikku-app/komikku#892, cerrada en 2025 con respuesta de dos colaboradores. La "
      "cuenta publicó un cierre de cortesía dieciocho meses después y un colaborador "
      "contestó: «Stop spamming shit in old ass not planned issues». Al auditar los 48 "
      "comentarios de esa tanda salió que 31 iban a hilos cerrados y 25 de ésos ya "
      "tenían respuesta del mantenedor. Sólo uno protestó; el patrón era de 25.",
      "Antes de publicar, merece_respuesta() mira el hilo y el borrador: si no aporta "
      "enlace, código, versión, fichero, fallo concreto, desenlace o pregunta, no se "
      "publica, por muy educado que sea. Y si la respuesta que llega es hostil, no se "
      "contesta: contestar a «deja de comentar» con otro comentario es hacer justo lo "
      "que piden que se deje de hacer. Se cumple en el mismo medio —silencio en el "
      "hilo— y se cambia la conducta, que es lo único que el otro puede comprobar.",
      _r17,
      {"hilo": _HILO_MUERTO,
       "borrador": "A separate app for text reading is a reasonable answer, and with a "
                   "light-novel reader already planned there is nothing left here. "
                   "Withdrawn - thanks to both."},
      {"hilo": _HILO_CON_DEUDA,
       "borrador": "That was machine-generated text rather than a request anybody "
                   "wrote, and it is withdrawn."},
      ["2026-11-12 · nace del comentario de un colaborador en una issue cerrada hacía "
       "dieciocho meses",
       "2026-11-12 · la comprobación salió al revés el primer día (marcaba problema "
       "cuando el comentario sí aportaba algo): misma inversión que R4, y la muestra "
       "mala es lo que la delata",
       "2026-11-12 · la auditoría de los 48 comentarios publicados el día anterior "
       "convirtió un enfado puntual en regla: 31 hilos cerrados, 25 ya respondidos",
       "2026-11-12 · al leer los 30 textos marcados como ruido resultó que la mayoría "
       "eran retiradas y enmiendas de issues generadas por máquina; borrarlos habría "
       "dejado esas publicaciones sin corregir. Una retirada cambia lo que el hilo "
       "debe creer, así que cuenta como dato",
       "2026-11-12 · y eso rompió la muestra mala, porque el comentario del incidente "
       "también era una retirada. La diferencia no está en la palabra sino en si queda "
       "algo en pie que retirar: se añade `pendiente` al hilo y la muestra buena pasa "
       "a ser una retirada donde sí había deuda",
       "2026-11-12 · `pendiente` vale False cuando no se sabe: callar es el fallo "
       "seguro de esta regla, publicar de más fue el fallo real"])


# ══════════════════════════════════════════════════════════════════════════
#  R18 · Un mandato «todos» se censura antes de ejecutarse
# ══════════════════════════════════════════════════════════════════════════

def _r18(acciones=None, clasificar=None, **_):
    acc = acciones or []
    _lineas, alarma = censar_acciones(acc, clasificar or (lambda x: x))
    return ["habría que haber parado a preguntar"] if alarma else []


regla("R18", "mandatos", "«Cada uno» se cuenta antes de hacerlo, no después",
      "La instrucción era responder a cada comentario sin contestar de las issues de la "
      "cuenta. Se ejecutó entera y se informó del total —42 publicadas, 0 fallos— sin "
      "decir de qué estaba hecha: 31 iban a hilos cerrados. El número que se dio "
      "sonaba a trabajo hecho y ocultaba que la mayor parte no era trabajo que nadie "
      "hubiera pedido.",
      "censar_acciones() agrupa la lista por su clasificador y devuelve la composición "
      "con porcentajes más una alarma cuando la categoría muerta pasa de la mitad. Con "
      "alarma no se ejecuta: se enseña la composición y se pregunta. Informar sólo del "
      "total es informar de lo que no molesta.",
      _r18,
      {"acciones": ["muerta"] * 31 + ["viva"] * 12, "clasificar": lambda x: x},
      {"acciones": ["viva"] * 9 + ["muerta"] * 2, "clasificar": lambda x: x},
      ["2026-11-12 · nace de la misma tanda que R17: el fallo no fue comentar, fue "
       "ejecutar un «todos» sin mirar qué contenía",
       "2026-11-12 · el propio censo de los 48 comentarios dijo «sin alarma» contando "
       "cero en una categoría que no existía: el clasificador decía una cosa y la "
       "función buscaba otra. Ahora levanta ValueError, porque un censo que no puede "
       "fallar no vigila nada"])



# ══════════════════════════════════════════════════════════════════════════
#  R3 · Ningún nombre de API ajena sin verificar
# ══════════════════════════════════════════════════════════════════════════

def _r3(codigo="", nombres=(), **_):
    sin = exigir_api_verificada(codigo, list(nombres))
    return ["%s no está verificado: se escribe de memoria y lo caza el compilador" % n
            for n in sin]


api_verificada("createMediaSource",
               "androidx.media3 DefaultMediaSourceFactory (MediaSourceFactory)",
               "única función de creación de la interfaz; devuelve MediaSource")
api_verificada("media3-exoplayer-hls",
               "https://dl.google.com/dl/android/maven2/androidx/media3/group-index.xml",
               "el índice de grupo lista las piezas; el de cada pieza sale vacío")

regla("R3", "api ajena", "Los nombres de API que no son del proyecto se verifican",
      "917c3f06 salió rojo con «Unresolved reference 'createMediaItem'»: el nombre "
      "lo puso la memoria. Antes habían pasado cosas parecidas con el tipo de "
      "devolución de un getter de audio (float, no int) y con el nombre corto de la "
      "pieza HLS del reproductor.",
      "api_verificada(nombre, fuente, comprobado) registra el nombre con dónde se "
      "miró; exigir_api_verificada() falla si el código usa uno sin registrar. Una "
      "prueba de JVM no puede cazar esto: sólo el compilador.",
      _r3,
      {"codigo": "fabrica.%s(elemento)" % literal_de("media3", "metodo_inventado"),
       "nombres": [literal_de("media3", "metodo_inventado")]},
      {"codigo": "fabrica.createMediaSource(elemento)", "nombres": ["createMediaSource"]},
      ["2026-11-11 · nace del rojo en CI",
       "2026-11-11 · se aplica también a nombres de artefactos de Gradle, no sólo a "
       "métodos: el índice por pieza sale vacío y hay que mirar el de grupo",
       "2026-11-12 · y a los **valores** de los parámetros, no sólo a los nombres: el "
       "motivo de cierre acepta la forma con guion bajo, no la cadena que se muestra en "
       "la web. Un 422 que dice «specify a valid state reason» ya señala el parámetro, "
       "así que se prueba la variante antes de irse a leer veintiuna páginas de manual"])


# ══════════════════════════════════════════════════════════════════════════
#  R4 · Ninguna prueba propia puede defender un fallo
# ══════════════════════════════════════════════════════════════════════════

def _r4(codigo_de_prueba="", prohibidos_por_ruta=None, **_):
    """Busca aserciones de presencia sobre literales prohibidos."""
    prohibidos_por_ruta = prohibidos_por_ruta or {}
    todos = sorted({l for v in prohibidos_por_ruta.values() for l in v})
    fuera = []
    lineas = codigo_de_prueba.split("\n")
    for i, linea in enumerate(lineas):
        for lit in todos:
            # La prueba mala del incidente no escribía el nombre pelado: lo llevaba
            # dentro de una construcción de ruta. Y un nombre legítimo que contenga
            # el prohibido no cuenta: se compara por token.
            if "contains(" not in linea or not coincide_literal(linea, lit):
                continue
            for j in range(i, max(-1, i - 8) - 1, -1):
                if "assertTrue" in lineas[j]:
                    fuera.append("%d: una prueba exige %r, que el proyecto prohíbe" % (i + 1, lit))
                    break
                if "assertFalse" in lineas[j]:
                    break
    return fuera


regla("R4", "pruebas propias", "Una prueba no puede exigir lo que el proyecto prohíbe",
      "708a9904: IptvReproductorTest tenía assertTrue(t.contains(«el directorio "
      "interno»)) con un mensaje que decía «se guardan en el almacenamiento "
      "privado», o sea justo lo contrario de la regla del proyecto. La prueba "
      "convertía el fallo en requisito.",
      "Antes de publicar una prueba nueva se pasa _r4 sobre ella con la tabla de "
      "prohibiciones. En el repo lo vigila CoherenciaDePruebasTest, que además "
      "comprueba que ninguna prueba publicada contradice a otra.",
      _r4,
      {"codigo_de_prueba": '''        assertTrue(
            "las fuentes se guardan en el almacenamiento privado, no en el APK",
            t.contains("File(c.%s"),
        )''' % literal_de("almacenamiento", "interno"),
       "prohibidos_por_ruta": {"modules/iptv": [literal_de("almacenamiento", "interno")]}},
      {"codigo_de_prueba": '''        assertFalse(
            "los datos no se escriben en el almacenamiento interno: ahí sólo viven " +
                "los tokens cifrados",
            t.contains("%s"),
        )''' % literal_de("almacenamiento", "interno"),
       "prohibidos_por_ruta": {"modules/iptv": [literal_de("almacenamiento", "interno")]}},
      ["2026-11-11 · nace al arreglar el módulo: se cambió el código primero y la "
       "prueba después, nunca al revés",
       "2026-11-11 · se publica como prueba del repo para que no dependa de que yo "
       "me acuerde",
       "2026-11-11 · la comparación por subcadena denunciaba dos mecanismos "
       "aprobados cuyo nombre contiene lo prohibido (el almacén cifrado de tokens y "
       "la migración de las preferencias viejas); se cambia a token con frontera de "
       "identificador",
       "2026-11-12 · y le faltaba la dirección contraria: dos pruebas publicadas llegaron a "
       "exigir contrarios del mismo literal (una, que viviera en los módulos; la otra, que no "
       "viviera fuera de la puerta). R4 vigila prohibición contra prueba; prueba contra prueba "
       "es el trabajo de R23"])


# ══════════════════════════════════════════════════════════════════════════
#  R5 · Censo de pruebas publicadas antes de escribir una línea
# ══════════════════════════════════════════════════════════════════════════

def _r5(raiz_tests="", prohibidos_por_ruta=None, **_):
    if not raiz_tests or not os.path.isdir(raiz_tests):
        return ["no hay censo: sin él se escribe a ciegas"]
    return contradicciones(censar_pruebas(raiz_tests), prohibidos_por_ruta or {})


regla("R5", "pruebas ajenas", "Leer las pruebas publicadas antes de escribir código",
      "El módulo IPTV escribió en el interno sin saber que "
      "ReglaDeAlmacenamientoTest lo prohibía desde hacía semanas. Y al diseñar la "
      "pantalla hubo que leer cuatro pruebas más (manifiesto, traducciones, "
      "pantallas, marcadores) antes de escribir el primer layout.",
      "censar_pruebas(raiz) extrae de cada prueba qué ficheros lee y qué literales "
      "exige o prohíbe; contradicciones() cruza ese censo con lo que se va a "
      "escribir. Se hace al empezar, no al fallar.",
      _r5,
      {"raiz_tests": "/no/existe"},
      {"raiz_tests": os.path.join(os.path.dirname(os.path.abspath(__file__)), "muestras_ok")},
      ["2026-11-11 · nace del rojo de ReglaDeAlmacenamientoTest",
       "2026-11-11 · el censo distingue exige/prohíbe por la aserción más cercana, "
       "que en Kotlin con mensajes largos está varias líneas más arriba",
       "2026-11-11 · las prohibiciones se parten en globales y por ruta: las "
       "globales sirven para buscar contradicciones entre pruebas, las otras sólo "
       "para auditar el fichero concreto",
       "2026-11-12 · el commit O marcó el límite del censo: se censó la prueba que lee el flujo "
       "(FirmaNuevaTest) y no las que leen los módulos que el commit reescribía por contenido. "
       "Ese censo tiene ahora regla propia (R23) y habilidad propia (lectores_de_literal), y "
       "muerde en las dos direcciones: acoplados que hay que adaptar y consumidores que no"])


# ══════════════════════════════════════════════════════════════════════════
#  R6 · Escapes entre capas: se comprueba el valor evaluado
# ══════════════════════════════════════════════════════════════════════════

def _r6(texto_generado="", **_):
    return auditar_escapes_kotlin(texto_generado)


regla("R6", "escapes", "Un raw string de Kotlin no procesa escapes",
      "Dos veces se preparó una prueba con las barras duplicadas al pasar el texto "
      "por dos capas de Python. Y una comprobación propia leyó el texto fuente del "
      "generador en vez del valor evaluado, y denunció un fallo que no existía.",
      "auditar_escapes_kotlin() sobre el valor ya evaluado, obtenido con "
      "valor_evaluado() (ast), nunca con una regex sobre el fuente del generador.",
      _r6,
      {"texto_generado": 'val ids = Regex("""android:id="@\\\\+id/([a-z0-9_]+)""").findAll(x)'},
      {"texto_generado": 'val ids = Regex("""android:id="@\\+id/([a-z0-9_]+)""").findAll(x)\n'
                         'val t = s.substringBefore("\\n    }\\n")'},
      ["2026-11-11 · nace en la preparación de la pantalla IPTV",
       "2026-11-11 · se añade valor_evaluado(): comprobar el texto fuente del "
       "generador enseña los escapes sin resolver y miente"])


# ══════════════════════════════════════════════════════════════════════════
#  R7 · Hilos: el fondo no toca la pantalla, y hay APIs con hilo propio
# ══════════════════════════════════════════════════════════════════════════

def _r7(codigo="", regiones=("Thread({", "enSegundoPlano {"), estado=(), api_principal=(), **_):
    return auditar_hilos(codigo, list(regiones), list(estado), list(api_principal))


regla("R7", "hilos", "El hilo de fondo no toca vistas ni APIs con Looper propio",
      "En la pantalla IPTV: el reproductor exige el hilo en que se creó y lanza si "
      "se le llama desde otro, mientras que descargar una lista en el principal "
      "congela la interfaz (el ANR original de la app). Y dentro del lambda de "
      "fondo se colaron dos escrituras de estado de la pantalla.",
      "auditar_hilos() sobre las regiones de fondo declaradas, con la lista de "
      "variables de estado y la de APIs que exigen hilo principal. Las dos listas "
      "las pone quien genera, porque dependen del tema.",
      _r7,
      {"codigo": '''    private fun anadir() {
        enSegundoPlano {
            fuenteElegida = hecho.fuente?.nombre
            binding.estado.text = aviso
        }
    }

    private fun reproducir(canal: Canal) {
        enSegundoPlano { m.reproducir(canal, null) }
    }
''',
       "estado": ["fuenteElegida", "enMarcha"], "api_principal": ["m.reproducir("]},
      {"codigo": '''    private fun anadir() {
        enSegundoPlano {
            val hecho = m.anadirFuente(nombre, url, tipo, null)
            r.getString(R.string.iptv_fuente_anadida, hecho.fuente?.nombre ?: nombre)
        }
    }

    private fun reproducir(canal: Canal) {
        val fallo = m.reproducir(canal, binding.superficieVideo)
    }
''',
       "estado": ["fuenteElegida", "enMarcha"], "api_principal": ["m.reproducir("]},
      ["2026-11-11 · nace con la pantalla IPTV",
       "2026-11-11 · se añade la lista de APIs con hilo propio, que no es genérica: "
       "la pone cada tema",
       "2026-11-11 · liberar sin crear: pedirle al módulo su reproductor sólo para "
       "soltarlo reserva un decodificador para nada"])


# ══════════════════════════════════════════════════════════════════════════
#  R8 · Conteos con nombres, no con números a mano
# ══════════════════════════════════════════════════════════════════════════

def _r8(nombre="", obtenido=(), esperado=(), **_):
    return comparar_conjuntos(nombre, list(obtenido), list(esperado))


regla("R8", "conteos", "Un conteo esperado se deriva, o se compara por nombres",
      "«el layout declara 16 ids, se esperaban 15» y «IptvTest debería tener 10 "
      "pruebas, tiene 12»: los dos números los conté a mano y los dos estaban mal. "
      "Un número no dice cuál falta.",
      "comparar_conjuntos(nombre, obtenido, esperado) devuelve qué sobra y qué "
      "falta. Cuando el esperado no se puede derivar, se escribe la lista nominal, "
      "nunca el total.",
      _r8,
      {"nombre": "ids del layout", "obtenido": ["a", "b", "c"], "esperado": ["a", "b"]},
      {"nombre": "ids del layout", "obtenido": ["a", "b"], "esperado": ["a", "b"]},
      ["2026-11-11 · nace con los layouts de la pantalla IPTV",
       "2026-11-12 · y muerde también en la comprobación: verifiqué 43 ediciones con "
       "una longitud esperada escrita a mano («línea + 5 + original») cuando el "
       "separador tiene 7 caracteres, y las 43 dieron fallo siendo correctas. La "
       "constante se deriva en el código que escribe y en el que comprueba",
       "2026-11-12 · y en l_fix.py, tres veces seguidas del mismo lado: la "
       "comprobación de los escapes esperaba seis `\\$` cuando el texto llevaba "
       "cinco, `(\\s|$)` cuando lleva `(?:\\s|$)`, y `\"\\$X\"` cuando en Kotlin "
       "va `\\\"\\$X\\\"`. Los tres fallos decían que el contenido estaba mal "
       "estando bien, que es la firma de una comprobación equivocada. La forma "
       "esperada se deriva ahora del valor evaluado del bloque que se va a "
       "publicar (ast.literal_eval del literal de Python), no de un literal "
       "escrito a su lado",
       "2026-11-12 · commit P: escribí «llevaba 3 @Test» de memoria, tras leer 75 líneas de un "
       "fichero de 101; eran 6. El conteo ahora se deriva del fichero publicado antes de editar "
       "y se compara con el de después: este commit no añade pruebas, así que ambos valen lo mismo"])


# ══════════════════════════════════════════════════════════════════════════
#  R9 · La fixture se reproduce antes de publicar
# ══════════════════════════════════════════════════════════════════════════

def _r9(reproducir=None, afirmados=(), **_):
    """`reproducir` es la lógica reimplantada en Python; `afirmados`, lo que la
    prueba va a afirmar. Se ejecuta aquí y se compara antes de publicar."""
    if reproducir is None:
        return ["no hay reproducción de la lógica: se publicaría a ciegas"]
    fuera = []
    for valor, esperado in afirmados:
        obtenido = reproducir(valor)
        if obtenido != esperado:
            fuera.append("la prueba va a afirmar %r y la lógica da %r" % (esperado, obtenido))
    return fuera


regla("R9", "fixtures", "Sospechar de la fixture antes que de la implementación",
      "ecaae4f4 salió rojo con dos fallos y los dos eran de mis fixtures: una "
      "escribía un atributo sin comillas y sin valor, y la otra afirmaba la "
      "ausencia de un título que sí estaba escrito. La implementación tenía razón.",
      "El generador reimplanta la lógica en Python y la ejecuta sobre cada valor "
      "que la prueba va a afirmar. Si no coinciden, se publica la corrección de la "
      "fixture o del código, pero nunca se relaja la aserción para que pase.",
      _r9,
      {"reproducir": lambda x: x.upper(), "afirmados": [("hola", "HOLA!")]},
      {"reproducir": lambda x: x.upper(), "afirmados": [("hola", "HOLA")]},
      ["2026-11-11 · nace con las dos fixtures mal escritas del IPTV",
       "2026-11-11 · se añade la prohibición expresa de relajar una aserción para "
       "que pase: es la forma elegante de borrar la regla"])


# ══════════════════════════════════════════════════════════════════════════
#  R10 · Anclajes únicos y del ámbito correcto
# ══════════════════════════════════════════════════════════════════════════

def _r10(texto="", anclas=(), **_):
    fuera = []
    for a, veces in anclas:
        n = texto.count(a)
        if n != veces:
            fuera.append("el anclaje %r aparece %d veces, se esperaban %d" % (a[:50], n, veces))
    return fuera


regla("R10", "anclajes", "Todo anclaje se cuenta antes de sustituir",
      "Un anclaje que paraba demasiado pronto empalmó código en el ámbito "
      "equivocado; otro que aparecía dos veces sustituyó donde no era. Y en este "
      "mismo turno una comprobación comparó el texto ya editado consigo mismo, "
      "porque no se guardó el original.",
      "Contar el anclaje y exigir el número exacto; guardar el original antes de "
      "editar cuando la comprobación necesite comparar antes y después.",
      _r10,
      {"texto": "a\nb\na\n", "anclas": [("a", 1)]},
      {"texto": "a\nb\na\n", "anclas": [("a", 2), ("b", 1)]},
      ["2026-11-11 · se añade guardar el original: comparar el texto editado "
       "consigo mismo da un fallo inventado"])


# ══════════════════════════════════════════════════════════════════════════
#  R11 · Almacenamiento: los mecanismos aprobados del proyecto
# ══════════════════════════════════════════════════════════════════════════

def _r11(codigo="", excepciones=(), **_):
    return ["%d: %s → %s" % (i, p, l) for (i, p, l) in
            auditar_almacenamiento(codigo, tuple(excepciones))]


regla("R11", "almacenamiento", "Los datos van a los mecanismos aprobados del proyecto",
      "917c3f06 guardó las fuentes del usuario en el interno. La regla del proyecto "
      "no es una opinión: sólo los tokens cifrados pueden vivir ahí.",
      "auditar_almacenamiento() con la lista de patrones prohibidos; y si un sitio "
      "necesita escribir, se declara en core/InventoryStorage con su veredicto, que "
      "es para lo que existe ese inventario.",
      _r11,
      {"codigo": "        almacen = AlmacenFuentes(File(c.%s, NOMBRE))\n"
                 % literal_de("almacenamiento", "interno")},
      {"codigo": '        val destino = AlmacenExterno.archivo(c, NOMBRE) ?: return false\n'
                 '        almacen = AlmacenFuentes(destino)\n'},
      ["2026-11-11 · nace del rojo de ReglaDeAlmacenamientoTest",
       "2026-11-11 · se añade declarar el sitio en InventoryStorage: sin eso la "
       "regla siguiente vuelve a fallar aunque el código esté bien"])


# ══════════════════════════════════════════════════════════════════════════
#  R12 · Traducciones: una cadena nueva son quince entradas
# ══════════════════════════════════════════════════════════════════════════

IDIOMAS = ["en", "ca", "pt", "fr", "id", "ja", "ko", "ru", "th", "tr", "uk", "vi", "zh", "ar"]


def _r12(cadenas=(), **_):
    return auditar_matriz_idiomas(list(cadenas), IDIOMAS)


regla("R12", "recursos", "Una cadena nueva son quince entradas, con los mismos marcadores",
      "Al diseñar la pantalla IPTV: TraduccionesPresentesTest exige que toda cadena "
      "de values/ esté en las catorce carpetas y no vacía. Una cadena suelta en un "
      "layout sería texto que catorce idiomas no ven.",
      "auditar_matriz_idiomas() comprueba huecos, vacías y marcadores distintos. Los "
      "apóstrofos se escapan al escribirlas, que sin la barra no compilan.",
      _r12,
      {"cadenas": [("iptv_cargar", {"es": "Cargar", "en": "Load", "fr": ""})]},
      {"cadenas": [("iptv_canales", dict([("es", "%1$d canales")] +
                                        [(i, "%1$d channels") for i in IDIOMAS]))]},
      ["2026-11-11 · nace con las 22 cadenas de la pantalla IPTV",
       "2026-11-11 · se comprueban también los marcadores: una traducción sin %1$d "
       "no falla al compilar y se come el dato"])


# ══════════════════════════════════════════════════════════════════════════
#  R13 · Layouts: nada de texto a mano, ni vistas muertas
# ══════════════════════════════════════════════════════════════════════════

def _r13(codigo="", xml_fragmento="", xml_items=(), **_):
    fuera = cruzar_ids(codigo, xml_fragmento, "\n".join(xml_items))
    for xml in [xml_fragmento] + list(xml_items):
        for _attr, valor in re.findall(r'android:(text|hint)="([^"]*)"', xml):
            if not valor.startswith("@string/"):
                fuera.append("texto sin traducir en el layout: %r" % valor)
    return fuera


regla("R13", "layouts", "Los IDs se cruzan en las dos direcciones y el texto va a recursos",
      "Al preparar la pantalla IPTV sobraba el id de una de las dos opciones de "
      "tipo: el código leía la otra. Una vista declarada que nadie usa es un adorno, "
      "y esta app se pasó una limpieza entera quitando adornos.",
      "cruzar_ids() en las dos direcciones + ningún android:text o android:hint que "
      "no empiece por @string/.",
      _r13,
      {"codigo": "binding.estado.text = x\nb.canalTitulo.text = y\n",
       "xml_fragmento": '<LinearLayout><TextView android:id="@+id/estado" '
                        'android:text="Estado" /><TextView android:id="@+id/sobra" /></LinearLayout>',
       "xml_items": ['<LinearLayout><TextView android:id="@+id/canal_titulo" /></LinearLayout>']},
      {"codigo": "binding.estado.text = x\nb.canalTitulo.text = y\n",
       "xml_fragmento": '<LinearLayout><TextView android:id="@+id/estado" '
                        'android:text="@string/iptv_estado" /></LinearLayout>',
       "xml_items": ['<LinearLayout><TextView android:id="@+id/canal_titulo" /></LinearLayout>']},
      ["2026-11-11 · nace con la pantalla IPTV",
       "2026-11-11 · se añade el cruce inverso (layout → código): el directo solo "
       "caza lo que no compila, no lo que sobra"])


# ══════════════════════════════════════════════════════════════════════════
#  R14 · Honestidad: nada de «funciona» sin lectura tras escritura
# ══════════════════════════════════════════════════════════════════════════

VERBOS_PROHIBIDOS_SIN_PRUEBA = ["funciona", "ya está aplicado", "queda arreglado",
                                "se ve bien", "reproduce correctamente"]


def _r14(informe="", evidencias=(), **_):
    """Un informe que afirma un resultado tiene que citar la evidencia."""
    fuera = []
    bajo = informe.lower()
    for verbo in VERBOS_PROHIBIDOS_SIN_PRUEBA:
        if verbo in bajo and not evidencias:
            fuera.append("«%s» sin ninguna evidencia citada" % verbo)
    for e in ("run", "sha256", "bytes", "pruebas ·"):
        pass
    return fuera


regla("R14", "informe", "Ningún «funciona» sin la evidencia al lado",
      "Corrección de pie del usuario desde el principio: nada de decir que algo "
      "funciona o está aplicado sin lectura tras escritura. Y en este proyecto hay "
      "una frontera fija: 468 pruebas de JVM verdes no demuestran que la app "
      "funcione en un teléfono.",
      "El informe cita run, bytes, sha256 y conteo de pruebas; y separa siempre lo "
      "verificado de lo que no se pudo verificar. auditar_huellas() no existe: esto "
      "es un procedimiento, no una puerta, y se marca como tal.",
      _r14,
      {"informe": "La app ya funciona y el ecualizador queda arreglado.", "evidencias": []},
      {"informe": "468 pruebas · 0 fallos (run 43124399468). No probado en dispositivo.",
       "evidencias": ["run 43124399468"]},
      ["2026-11-11 · se separa siempre lo verificado de lo pendiente: el V60 ThinQ "
       "5G es el banco y aquí no hay /dev/kvm"])


# ══════════════════════════════════════════════════════════════════════════
#  R15 · Workspace: nada re-descargable, y las claves fuera del snapshot
# ══════════════════════════════════════════════════════════════════════════

RE_DESCARGABLE = [".tgz", ".apk", "log2", "indice.json", "sitemap"]


def _r15(raiz="/home/user", **_):
    fuera = []
    for d, dirs, ficheros in os.walk(raiz):
        dirs[:] = [x for x in dirs if x not in ("__pycache__", ".git", "node_modules")]
        for f in ficheros:
            tam = os.path.getsize(os.path.join(d, f))
            if any(k in f for k in RE_DESCARGABLE) or tam > 8 * 1024 * 1024:
                fuera.append("%s (%d KB) es re-descargable" % (os.path.relpath(os.path.join(d, f), raiz), tam // 1024))
    return fuera


regla("R15", "workspace", "Lo que se puede volver a descargar no se guarda",
      "El workspace llegó a 58 MB con tarballs, clones, sitemaps y logs de CI, todo "
      "regenerable. Se bajó a 12 KB. En este turno volvió a pasar: 33 MB de APK "
      "descargado para comprobarlo y seis logs de CI.",
      "Los artefactos de verificación se descargan a /tmp, se comprueban y se "
      "borran. Lo que deba vivir entre turnos va a /home/user, y las claves a "
      ".cerox-keys (que no está en el snapshot y aún debe su copia fuera de GitHub).",
      _r15,
      {},
      {"raiz": os.path.join(os.path.dirname(os.path.abspath(__file__)), "muestras_ok")},
      ["2026-11-11 · se añade el APK: verificarlo no es guardarlo"])


# ── Tabla de prohibiciones por ruta, compartida por R4 y R5 ────────────────

# Lo que no puede aparecer en ningún sitio de src/main. Estas son las que sirven
# para buscar contradicciones entre pruebas publicadas, porque no dependen de la
# ruta a la que apunte cada aserción.
PROHIBIDOS_GLOBALES = [
    literal_de("media3", "metodo_inventado"),
    literal_de("pantallas", "registro_viejo"),
    literal_de("gradle", "version_dinamica"),
    literal_de("gradle", "rango_dinamico"),
]

# Lo que está prohibido sólo en una ruta: en otro sitio del proyecto puede ser
# legítimo (el cargador de extensiones usa el directorio de caché del sistema
# porque el cargador de clases lo exige, y eso está declarado en el inventario).
PROHIBIDOS_POR_RUTA = {
    "modules/iptv": [literal_de("almacenamiento", "interno"),
                     literal_de("almacenamiento", "preferencias"), "cacheDir"],
    "src/main/java/com/ceroX/app": PROHIBIDOS_GLOBALES,
    "build.gradle": [literal_de("gradle", "version_dinamica"),
                     literal_de("gradle", "rango_dinamico")],
}


# ══════════════════════════════════════════════════════════════════════════
#  R19 · Un guion que escribe fuera se puede volver a ejecutar
# ══════════════════════════════════════════════════════════════════════════

def _r19(aplicar=None, estado_inicial="", ya_esta=None, veces=2, **_):
    """El problema es que ejecutarlo dos veces duplique la marca."""
    final = idempotente(aplicar, estado_inicial, ya_esta or (lambda e: False), veces)
    marcas = final.count(LINEA) if LINEA in final else 0
    return ["al ejecutarse dos veces la marca quedó %d veces" % marcas] if marcas > 1 else []


LINEA = "**Withdrawn.**"


def _doblar(estado):
    return LINEA + "\n\n" + estado


regla("R19", "escrituras fuera", "Un guion que escribe fuera se puede volver a ejecutar",
      "Retirando los cuerpos de 43 issues, el guion leyó un campo de un censo guardado "
      "antes de empezar, el campo no existía y reventó con KeyError — **después** de "
      "haber publicado la primera edición. Una issue quedó escrita y sin registrar, y "
      "al volver a ejecutarlo la habría editado dos veces, dejando la misma línea "
      "duplicada arriba del cuerpo.",
      "El estado se lee **vivo** antes de cada escritura, no del censo guardado; y el "
      "guion se comprueba idempotente: si ya lleva la marca, no la vuelve a poner. "
      "idempotente() aplica la acción dos veces sobre el mismo estado y cuenta las "
      "marcas. Un lote que escribe en repos ajenos tiene que poder reejecutarse sin "
      "que nadie lo piense, porque se va a interrumpir.",
      _r19,
      {"aplicar": _doblar, "estado_inicial": "cuerpo original",
       "ya_esta": lambda e: False},
      {"aplicar": _doblar, "estado_inicial": "cuerpo original",
       "ya_esta": lambda e: e.startswith(LINEA)},
      ["2026-11-12 · nace del KeyError que reventó el lote de retiradas después de la "
       "primera edición publicada",
       "2026-11-12 · la idempotencia del paso de publicar cubría los bytes pero no lo que "
       "los describe: el segundo corte de la 1.0.4 subió los APKs verdes y dejó el cuerpo de "
       "la release diciendo el commit rojo. Reejecutar tiene que actualizar también la "
       "nota; se corrigió a mano con PATCH y quedó narrado en el propio cuerpo"])


# ══════════════════════════════════════════════════════════════════════════
#  R20 · Un flujo se valida como YAML antes de publicarlo
# ══════════════════════════════════════════════════════════════════════════

def _r20(texto="", **_):
    return yaml_valido(texto) + bloques_literales(texto)


# El incidente real: dentro de un bloque de varias líneas de un flujo, la continuación
# de una sustitución de mandato se escribió en la columna 0 del fichero. El bloque
# pedía diez espacios de sangría y esa línea no llevaba ninguno.
_ROTO = ("jobs:\n"
         "  apk:\n"
         "    steps:\n"
         "      - name: Publicar\n"
         "        run: |\n"
         "          if [ -n \"$X\" ]; then\n"
         "            CAMBIOS=\"Cambios desde $X:\n"
         "$(git log --oneline \"$X\"..HEAD)\"\n"
         "          fi\n")
_BIEN = _ROTO.replace("\n$(git log", "\n            $(git log")

regla("R20", "flujos", "Un flujo se valida como YAML antes de publicarlo",
      "El commit L publicó apk.yml con la continuación de una sustitución de mandato en "
      "la columna 0, dentro de un bloque que pedía diez espacios de sangría. GitHub lo "
      "reportó como un run fallido **sin ningún job** y con el nombre en forma de ruta, "
      "que es como dice «no he podido ni leer el fichero». Las 472 pruebas salieron en "
      "verde al lado: ninguna prueba de JVM lee un flujo y el compilador no lo ve.",
      "Todo guion que toque .github/workflows/ valida el resultado con yaml_valido() y "
      "con bloques_literales() antes de publicar. El segundo no depende de ninguna "
      "biblioteca y dice la línea exacta donde algo cuelga fuera de la sangría del "
      "bloque. Y si falta la biblioteca de YAML, la puerta levanta ImportError en vez de "
      "callarse: una comprobación que no se ejecutó no puede decir que pasó.",
      _r20,
      {"texto": _ROTO},
      {"texto": _BIEN},
      ["2026-11-12 · nace del commit L, publicado roto y arreglado en el siguiente",
       "2026-11-12 · el pre-vuelo de ese commit tenía balance de símbolos para los "
       "ficheros Kotlin y no tenía nada para los flujos: se comprobaba lo que se sabía "
       "comprobar, no lo que el commit tocaba",
       "2026-11-12 · y la puerta local no basta: yaml_valido vive en mi guion, que no "
       "viaja con el repo. El arreglo (commit M) se publicó acompañado de "
       "core/FlujosValidosTest.kt, tres @Test que recorren .github/workflows/*.yml "
       "sin ninguna biblioteca de YAML en el classpath, para que la próxima vez acuse "
       "el propio CI y no yo. Verificado en el run 43134156604: 475 pruebas · 0 "
       "fallos · 0 errores · 6 saltadas"])


# ══════════════════════════════════════════════════════════════════════════
#  R21 · Un paso que la prueba no ejecuta se ejecuta en un repo de juguete
# ══════════════════════════════════════════════════════════════════════════

def _r21(texto="", paso="", montar=None, entorno=None, esperado="", **_):
    guion, fallos = mandato_de_paso(texto, paso)
    if guion is None:
        return fallos
    fallos = fallos + sintaxis_de_mandato(guion)
    if fallos:
        return fallos
    if montar is None:
        return fallos + ["el paso no corre en la comprobación por omisión y no se "
                         "montó escenario: no hay prueba de que funcione"]
    salida, f2 = correr_mandato(guion, montar=montar, entorno=entorno)
    fallos = fallos + f2
    if esperado and esperado not in salida:
        fallos = fallos + ["la salida no lleva %r; salió: %s"
                           % (esperado, salida.strip().replace("\n", " / ")[:200])]
    return fallos


def _repo_con_dos_tags(d):
    """El escenario mínimo del paso de publicar: un repo con dos etiquetas, que
    es lo que necesita `git describe … HEAD^` para tener un «anterior»."""
    import subprocess
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="a@b.c",
               GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="a@b.c")

    def g(*a):
        subprocess.run(["git"] + list(a), cwd=d, check=True,
                       capture_output=True, env=env)

    g("init", "-q", ".")
    open(os.path.join(d, "a.txt"), "w", encoding="utf-8").write("uno\n")
    g("add", "-A"); g("commit", "-qm", "uno"); g("tag", "v1.0.1-beta-x")
    open(os.path.join(d, "b.txt"), "w", encoding="utf-8").write("dos\n")
    g("add", "-A"); g("commit", "-qm", "dos"); g("tag", "v1.0.2-beta-y")


# El incidente real: el arreglo del commit M vive en el paso «Publicar la release»,
# que sólo corre con publicar=true. El despacho de comprobación fue con
# publicar=false, así que el flujo arrancó sin tocar nunca las líneas corregidas.
# Las dos fixtures son YAML válido —lo que las separa es el shell de dentro—, que
# es justo lo que R20 no mira.
_Q = chr(39)   # la comilla sencilla del sed, escrita así para que no se la coma
               # ninguna capa de escape al generar este fichero
_LINEAS_PASO = [
    "name: apk",
    "on: workflow_dispatch",
    "jobs:",
    "  apk:",
    "    runs-on: ubuntu-26.04",
    "    steps:",
    "      - name: Publicar la release",
    "        run: |",
    "          ANTERIOR=\"$(git describe --tags --abbrev=0 HEAD^)\"",
    "          CAMBIOS=\"Cambios desde $ANTERIOR:",
    "          $(git log --oneline --no-decorate \"$ANTERIOR\"..HEAD | sed "
    + _Q + "s/^/  · /" + _Q + ")__C__",
    "          printf " + _Q + "%s\\n" + _Q + " \"$CAMBIOS\"",
]
_FLUJO_BIEN = "\n".join(l.replace("__C__", "\"") for l in _LINEAS_PASO) + "\n"
_FLUJO_ROTO = "\n".join(l.replace("__C__", "") for l in _LINEAS_PASO) + "\n"

regla("R21", "pasos", "Un paso que la prueba no ejecuta se ejecuta en un repo de juguete",
      "El arreglo de apk.yml cayó en el paso «Publicar la release», que sólo corre con "
      "publicar=true; el despacho de comprobación fue con publicar=false. El YAML ya se "
      "leía y el flujo arrancaba en verde, y las líneas corregidas no se habían "
      "ejecutado ni una vez. Un YAML válido no dice nada del shell que lleva dentro: "
      "una comilla sin cerrar pasa el YAML y revienta en el corredor, en un paso que "
      "nadie corre hasta el día de la release.",
      "Se saca el guion del YAML ya evaluado con mandato_de_paso(texto, nombre) —por "
      "nombre de paso, no por índice—, se le pasa sintaxis_de_mandato() (bash -n) y se "
      "ejecuta con correr_mandato(montar=…) en un directorio preparado que reproduzca "
      "lo que el paso necesita. Si no se puede montar el escenario, la puerta lo dice "
      "en vez de callarse: «no hay prueba de que funcione».",
      _r21,
      {"texto": _FLUJO_ROTO, "paso": "Publicar la release",
       "montar": _repo_con_dos_tags, "esperado": "Cambios desde v1.0.1-beta-x:"},
      {"texto": _FLUJO_BIEN, "paso": "Publicar la release",
       "montar": _repo_con_dos_tags, "esperado": "Cambios desde v1.0.1-beta-x:"},
      ["2026-11-12 · nace del commit M: se extrajo el guion del paso, se le pasó "
       "bash -n y se ejecutó en un repo de juguete con dos tags, donde la lista de "
       "cambios se construyó de verdad antes de despachar el flujo",
       "2026-11-12 · y completa a R20 por el otro lado: R20 mira que el fichero se "
       "lea, R21 mira que lo que hay dentro funcione. Las dos fixtures de aquí son "
       "YAML válido, así que R20 no las caza"])


# ══════════════════════════════════════════════════════════════════════════
#  R22 · Un bucle de espera distingue «todavía no» de «la llamada falló»
# ══════════════════════════════════════════════════════════════════════════

def _r22(status=200, cuerpo="", claves=(), **_):
    return sondeo_sano(status, cuerpo, claves)


regla("R22", "sondeos", "Un bucle de espera distingue «todavía no» de «la llamada falló»",
      "El despacho con publicar=true devolvió 401 porque el token fino tuvo una "
      "ventana mala de unos veinticinco minutos. El bucle de vigilancia pedía los "
      "runs del commit y leía `workflow_runs` sin mirar el estado: con el 401 el "
      "cuerpo no traía la clave, el python del bucle moría en cada vuelta y el "
      "bucle imprimía «dispatch: » vacío cincuenta veces seguidas —media hora— "
      "sin decir nunca que lo que fallaba era la credencial y no la espera. La "
      "misma forma tenía el primer listado de artefactos del turno, que reventó "
      "con KeyError en vez de decir «401».",
      "Toda respuesta que alimenta un bucle pasa antes por sondeo_sano(status, "
      "cuerpo, claves): estado distinto de 200 es un fallo y se dice; cuerpo sin "
      "las claves esperadas es un fallo y se dice con el `message` que traiga. "
      "Un bucle que no puede distinguir ambas cosas convierte una credencial "
      "caída en silencio.",
      _r22,
      {"status": 401, "cuerpo": '{"message": "Bad credentials", '
                                '"documentation_url": "https://docs.github.com/rest"}',
       "claves": ("workflow_runs",)},
      {"status": 200, "cuerpo": '{"total_count": 0, "workflow_runs": []}',
       "claves": ("workflow_runs",)},
      ["2026-11-12 · nace de la ventana de 401 del token fino entre el commit N y "
       "su despacho: cincuenta iteraciones mudas, y el run de pruebas del commit "
       "terminó sin que nadie lo viera porque el bucle miraba otra cosa"])


# ══════════════════════════════════════════════════════════════════════════
#  R23 · Quien mueve un literal de sitio busca quién más lo lee
# ══════════════════════════════════════════════════════════════════════════

def _r23(textos=None, literal="", tocados=(), **_):
    lectores = lectores_de_literal(textos or {}, literal)
    return ["%s escanea %r por contenido y el commit no lo adapta"
            % (n, literal[:32]) for n in lectores if n not in tocados]


# El incidente real, en dos actos. Acto uno: el commit O movió la creación del
# entorno ONNX detrás de MotorOnnx.entorno() y dejó roto ArranqueHonestoTest,
# que escanea los siete módulos buscando el literal y exigiendo `by lazy` en la
# misma línea: main quedó en 478 · 1 y la release v1.0.4 se cortó de un commit
# con el suite en rojo. Acto dos: el censo nuevo, al estrenarse en el commit P,
# señaló también a ModelosEjecutadosTest, que no escanea nada: crea su propio
# entorno para ejercitar modelos. De ahí la división en dos clases.
_T_ESCAN = 'fun f() { val l = src.readText().lines().filter { it.contains("OrtEnvironment.getEnvironment()") } }'
_T_CONS = 'fun g() { val env = OrtEnvironment.getEnvironment() }'

regla("R23", "acoples", "Quien mueve un literal de sitio busca quién más lo lee",
      "Una prueba que escanea fuentes por contenido es un contrato publicado: "
      "ArranqueHonestoTest exigía que la línea que crea el entorno ONNX viviera "
      "en cada módulo y llevara `by lazy`. El commit O movió esa línea detrás de "
      "una puerta y no censó a quién la leía: la prueba falló en main y la "
      "release v1.0.4-beta-dos-apks se cortó de un commit con 478 · 1. El "
      "pre-vuelo de O censó FirmaNuevaTest, que lee el flujo, pero no las "
      "pruebas que leen los ficheros que el commit reescribía: el censo miraba "
      "lo famoso y no lo tocado.",
      "Antes de publicar, lectores_de_literal(pruebas_publicadas, literal) con "
      "como_cadena=True devuelve las pruebas que tienen el literal entre "
      "comillas, o sea como blanco de búsqueda: el commit tiene que adaptarlas o "
      "confirmarlas una por una. Con como_cadena=False salen también los "
      "consumidores que usan el literal como código propio, que no se rompen al "
      "moverse y no se tocan: confundir las dos clases fue el primer mordisco de "
      "la regla, que estrenándose señaló a un consumidor que no necesitaba nada.",
      _r23,
      {"textos": {"ArranqueHonestoTest.kt": _T_ESCAN, "Otro.kt": "sin nada"},
       "literal": "OrtEnvironment.getEnvironment()", "tocados": ()},
      {"textos": {"ArranqueHonestoTest.kt": _T_ESCAN,
                  "ModelosEjecutadosTest.kt": _T_CONS},
       "literal": "OrtEnvironment.getEnvironment()",
       "tocados": ("ArranqueHonestoTest.kt",)},
      ["2026-11-12 · nace del commit O roto y del commit P que lo cerró: el "
       "censo de lectores, estrenado en el pre-vuelo de P, encontró al lector "
       "que O no vio",
       "2026-11-12 · y mordió al estrenarse: señaló a ModelosEjecutadosTest, un "
       "consumidor que crea su entorno para ejercitar modelos y no lee fuentes. "
       "La división entre escaneadores (literal entre comillas) y consumidores "
       "(literal como código) viene de ese mordisco"])
