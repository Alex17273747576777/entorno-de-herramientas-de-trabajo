#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Habilidades reutilizables para publicar en cero-X sin repetir fallos conocidos.

No es una librería genérica: cada función existe porque un commit salió rojo, o
porque una puerta propia cazó algo antes de publicar. El incidente que la originó
va en su docstring, y en `registro.py` está la regla que la usa.

Se importa desde los generadores de commits:

    sys.path.insert(0, "/home/user/cerox-investigacion/reglas")
    from motor import solo_codigo, censar_pruebas, auditar_prosa, mencionar
"""
import json
import os
import re
import xml.etree.ElementTree as ET

# ══════════════════════════════════════════════════════════════════════════
#  1 · PROSA QUE NO CITA. El patrón que se repitió seis veces.
# ══════════════════════════════════════════════════════════════════════════
#
# Un comentario que explica por qué algo está prohibido tiende a escribir lo
# prohibido, y las puertas buscan la cadena en el fichero entero: la explicación
# se convierte en la infracción. Pasó con el resolvedor de versiones dinámicas de
# Gradle, con el método de media3 que no existe, y cuatro veces antes con marcas
# de relleno.
#
# El contra no es relajar la puerta (la puerta imita a una prueba publicada, que
# sí mira el fichero entero). El contra es que la prosa **no pueda** escribir el
# literal: se registra una vez, con su descripción, y en el texto se llama a
# `mencionar()`, que devuelve la descripción y nunca la cadena.

PROHIBIDOS = {}


def prohibir(tema, nombre, literal, descripcion, incidente):
    """Registra un literal que no puede aparecer ni en código ni en prosa.

    `descripcion` es lo que devuelve `mencionar()`: cómo se habla de esto sin
    escribirlo. `incidente` es el commit o el fallo que enseñó a prohibirlo.
    """
    PROHIBIDOS.setdefault(tema, {})[nombre] = {
        "literal": literal, "descripcion": descripcion, "incidente": incidente,
    }
    return literal


def mencionar(tema, nombre):
    """La descripción de un literal prohibido, para usarla en prosa.

    Devuelve siempre la descripción, nunca el literal: llamar a esto en vez de
    escribir la cadena es lo que hace que la prosa no pueda delatarse.
    """
    p = PROHIBIDOS[tema][nombre]
    return p["descripcion"]


def literal_de(tema, nombre):
    """El literal, para las comprobaciones. Nunca para escribir prosa."""
    return PROHIBIDOS[tema][nombre]["literal"]


def separar_prosa(texto, lenguaje="kotlin"):
    """(código, prosa) de un fichero Kotlin o Gradle.

    La prosa son los comentarios y el KDoc. Separarlos importa porque las puertas
    del proyecto no son todas iguales: `ReglaDeAlmacenamientoTest` quita los
    comentarios antes de buscar (allí la prosa puede explicar lo que quiera) y las
    puertas de marcas no los quitan (allí la prosa no puede citar nada).
    """
    prosa, codigo = [], []
    if lenguaje == "python":
        # En Python la prosa son los # y las docstrings, que no empiezan por //.
        en_doc = False
        for linea in texto.split("\n"):
            t = linea.strip()
            if t.startswith('"""'):
                prosa.append(linea)
                if t.count('"""') == 1:
                    en_doc = not en_doc
                continue
            (prosa if (en_doc or t.startswith("#")) else codigo).append(linea)
        return "\n".join(codigo), "\n".join(prosa)
    for linea in texto.split("\n"):
        t = linea.strip()
        if t.startswith("//") or t.startswith("*") or t.startswith("/*"):
            prosa.append(linea)
        else:
            codigo.append(linea)
    bloques = re.findall(r"/\*[\s\S]*?\*/", texto)
    return "\n".join(codigo), "\n".join(prosa) + "\n" + "\n".join(bloques)


def auditar_espejo(texto, temas=None, donde=""):
    """Como `auditar_prosa` pero mirando el fichero entero, prosa incluida.

    Es lo que hace una prueba publicada que no quita comentarios: ahí la prosa
    tampoco puede citar. Las dos funciones existen porque las puertas del proyecto
    no son todas iguales, y confundirlas fue exactamente el fallo.
    """
    fuera = []
    for tema, nombres in PROHIBIDOS.items():
        if temas and tema not in temas:
            continue
        for nombre, p in nombres.items():
            for i, linea in enumerate(texto.split("\n"), 1):
                if p["literal"] in linea:
                    fuera.append((i, tema, nombre, p["literal"], donde))
    return fuera


def solo_codigo(texto):
    """El texto sin strings ni comentarios, para contar llaves y paréntesis.

    Contar sobre el texto crudo falla con cualquier paréntesis dentro de una
    cadena, y los ficheros de este proyecto están llenos de prosa.
    """
    codigo, _ = separar_prosa(texto)
    t = re.sub(r'"""[\s\S]*?"""', " ", codigo)
    t = t.replace('\\"', " ")
    t = re.sub(r'"[^"\n]*"', " ", t)
    t = re.sub(r"'[^'\n]*'", " ", t)
    return t


def auditar_prosa(texto, temas=None, donde="", lenguaje="kotlin"):
    """Violaciones de prosa: literales prohibidos escritos en comentarios.

    Mira **sólo la prosa**. Un detector necesita tener su aguja en el código (la
    lista de patrones prohibidos, las fixtures que reproducen un incidente), y eso
    no es una infracción: la infracción es explicarlo citándolo. Para puertas que
    miran el fichero entero está `auditar_espejo`.

    Se llama sobre cada fichero generado y sobre el mensaje del commit, que también
    es prosa y también se publica.
    """
    _, prosa = separar_prosa(texto, lenguaje)
    fuera = []
    for tema, nombres in PROHIBIDOS.items():
        if temas and tema not in temas:
            continue
        for nombre, p in nombres.items():
            for i, linea in enumerate(prosa.split("\n"), 1):
                if p["literal"] in linea:
                    fuera.append((i, tema, nombre, p["literal"], donde))
    return fuera


def auditar_texto_crudo(texto, donde=""):
    """Como `auditar_prosa` pero para textos que no son código: mensajes de commit.

    Un mensaje de commit no tiene comentarios, así que se mira entero.
    """
    fuera = []
    for tema, nombres in PROHIBIDOS.items():
        for nombre, p in nombres.items():
            if p["literal"] in texto:
                fuera.append((0, tema, nombre, p["literal"], donde))
    return fuera


# ══════════════════════════════════════════════════════════════════════════
#  2 · CENSO DE PRUEBAS PUBLICADAS. Leer antes de escribir.
# ══════════════════════════════════════════════════════════════════════════
#
# El módulo IPTV escribió en el directorio interno de la app sin saber que una
# prueba publicada desde hacía semanas lo prohibía. Costó un commit rojo. Y luego
# la prueba propia defendía el fallo, o sea que el rojo siguiente también.

def censar_pruebas(raiz_tests):
    """Qué lee y qué exige cada prueba publicada.

    Devuelve {fichero: {"lee": [rutas], "exige": [literales], "prohibe": [literales]}}.
    «Exige» y «prohíbe» se distinguen por la aserción más cercana hacia arriba,
    que es como se escribe Kotlin con mensajes largos: `assertTrue(` abre, el
    mensaje ocupa dos o tres líneas, y el `contains(...)` va al final.
    """
    censo = {}
    for d, _, ficheros in os.walk(raiz_tests):
        for f in sorted(ficheros):
            if not f.endswith(".kt"):
                continue
            ruta = os.path.join(d, f)
            lineas = open(ruta, encoding="utf-8").read().split("\n")
            entrada = {"lee": [], "exige": [], "prohibe": []}
            for i, linea in enumerate(lineas):
                for m in re.findall(r'File\(\s*(?:base|src|raiz|recursos|fuentes)?\s*,?\s*"([^"]+)"', linea):
                    entrada["lee"].append(m)
                for m in re.findall(r'leer\("([^"]+)"\)', linea):
                    entrada["lee"].append(m)
                for m in re.findall(r'contains\("([^"]{3,})"', linea):
                    cual = _asercion_cercana(lineas, i)
                    if cual is True:
                        entrada["exige"].append(m)
                    elif cual is False:
                        entrada["prohibe"].append(m)
            censo[os.path.relpath(ruta, raiz_tests)] = entrada
    return censo


def _asercion_cercana(lineas, i, ventana=8):
    """True si manda un assertTrue, False si un assertFalse, None si no se sabe."""
    for j in range(i, max(-1, i - ventana) - 1, -1):
        if "assertTrue" in lineas[j]:
            return True
        if "assertFalse" in lineas[j]:
            return False
    return None


def coincide_literal(texto, literal):
    """El literal como **token**, no como subcadena.

    Nació de un falso positivo: el mecanismo aprobado para los tokens y el método
    que migra las preferencias viejas llevan dentro el nombre de lo prohibido, y
    una comparación por subcadena los denunciaba. La regla es que el carácter
    anterior no sea de identificador; si el literal empieza por un símbolo no hace
    falta frontera.
    """
    if not literal:
        return False
    patron = (r"(?<![A-Za-z0-9_])" if literal[0].isalnum() or literal[0] == "_" else "") \
        + re.escape(literal)
    return re.search(patron, texto) is not None


def contradicciones(censo, prohibidos_por_ruta):
    """Pruebas que exigen la presencia de algo que el proyecto prohíbe.

    `prohibidos_por_ruta` es {prefijo de ruta: [literales]}. Devuelve una lista de
    textos legibles. Esto es lo que habría dicho «tu prueba nueva defiende un
    fallo» en vez de dejar que fallara otra prueba con un mensaje raro.
    """
    problemas = []
    for fichero, entrada in censo.items():
        for literal in entrada["exige"]:
            for prefijo, prohibidos in prohibidos_por_ruta.items():
                for lit in prohibidos:
                    # La prueba mala del incidente no escribía el literal pelado: lo
                    # llevaba dentro de una ruta («File(c.» + el nombre del directorio
                    # interno). Se busca el literal como token dentro de lo afirmado,
                    # que es lo que caza ese caso sin morder los nombres legítimos que
                    # lo contienen (ver coincide_literal).
                    if lit == literal or coincide_literal(literal, lit):
                        problemas.append("%s exige %r, que está prohibido en %s"
                                         % (fichero, literal, prefijo))
    return sorted(set(problemas))


# ══════════════════════════════════════════════════════════════════════════
#  3 · NOMBRES DE API AJENA. No recordar: verificar.
# ══════════════════════════════════════════════════════════════════════════
#
# El incidente: un método de la fábrica de fuentes de media3 que no existe, cuyo
# nombre se forma con el verbo de crear y el sustantivo de elemento; el bueno es el
# que nombra lo que devuelve, una fuente. Lo escribió la memoria en vez de la
# documentación, y ninguna prueba de JVM puede cazarlo: lo caza el compilador, en
# CI, cinco minutos después. Aquí se describe y no se escribe, que es la regla R1.

NOMBRES_API = {}


def api_verificada(nombre, fuente, comprobado):
    """Registra un nombre de API ajena con la fuente de la que se comprobó.

    `comprobado` es lo que se vio (una URL, una línea del árbol, una firma). Un
    generador llama a `exigir_api_verificada()` antes de publicar y falla si usa
    un nombre que no pasó por aquí.
    """
    NOMBRES_API[nombre] = {"fuente": fuente, "comprobado": comprobado}
    return nombre


def exigir_api_verificada(codigo, nombres):
    """De cada nombre usado en `codigo`, o está verificado o se dice dónde mirarlo."""
    sin_verificar = [n for n in nombres if n in codigo and n not in NOMBRES_API]
    return sin_verificar


# ══════════════════════════════════════════════════════════════════════════
#  4 · PUERTAS NUEVAS: ámbito exacto.
# ══════════════════════════════════════════════════════════════════════════
#
# Una puerta contra `*/` a mitad de línea disparó contra
# `excludes += '/META-INF/*/versions/*'`, que llevaba en build.gradle desde
# siempre. La puerta nueva miraba el fichero entero cuando sólo le interesaba lo
# añadido. Regla: las puertas se clasifican.

def aplicar_puerta(texto_original, texto_nuevo, puerta, espejo=False):
    """Pasa `puerta` por lo añadido, o por el fichero entero si `espejo`.

    `espejo=True` es para puertas que imitan a una prueba publicada: ésas van a
    mirar el fichero entero cuando se ejecuten, así que hay que mirarlas igual
    aquí, y es entonces cuando la prosa tiene que describir en vez de citar.
    Devuelve la lista de problemas.
    """
    if espejo:
        return puerta(texto_nuevo)
    anadido = _solo_anadido(texto_original, texto_nuevo)
    return puerta(anadido)


def _solo_anadido(antes, despues):
    """Las líneas de `despues` que no estaban en `antes`, en su orden."""
    viejas = {}
    for l in antes.split("\n"):
        viejas[l] = viejas.get(l, 0) + 1
    out = []
    for l in despues.split("\n"):
        if viejas.get(l, 0) > 0:
            viejas[l] -= 1
        else:
            out.append(l)
    return "\n".join(out)


def ancla(texto, viejo, donde, veces=1):
    """Un anclaje de sustitución tiene que aparecer exactamente `veces` veces.

    Devuelve el texto sustituido o lanza. Los anclajes que paran demasiado pronto
    empalman código en el ámbito equivocado, y eso no lo dice nadie hasta que
    compila.
    """
    n = texto.count(viejo)
    if n != veces:
        raise SystemExit("anclaje de %s: aparece %d veces, se esperaban %d → %r"
                         % (donde, n, veces, viejo[:70]))
    return texto.replace(viejo, viejo, 1) if veces == 0 else texto


# ══════════════════════════════════════════════════════════════════════════
#  5 · CONTEOS: conjuntos nombrados, no números a mano.
# ══════════════════════════════════════════════════════════════════════════
#
# «el layout declara 16 ids, se esperaban 15»: el número lo había contado yo a
# mano y estaba mal. Un número no dice cuál falta; un conjunto sí.

def comparar_conjuntos(nombre, obtenido, esperado):
    """Diferencias con nombres, para que el fallo diga qué sobra y qué falta."""
    faltan = sorted(set(esperado) - set(obtenido))
    sobran = sorted(set(obtenido) - set(esperado))
    if not faltan and not sobran:
        return []
    return ["%s: faltan %s · sobran %s" % (nombre, faltan or "—", sobran or "—")]


# ══════════════════════════════════════════════════════════════════════════
#  6 · ANDROID: hilos, recursos, almacenamiento.
# ══════════════════════════════════════════════════════════════════════════

def balancear(texto):
    """Símbolos sin cerrar o mal cerrados, con un escáner de estados.

    Contar llaves sobre el texto recortado con regex dio **tres falsos positivos**:
    una regex escrita dentro de una cadena, un apóstrofo en prosa, un KDoc largo.
    Un escáner que sabe en qué estado está cada carácter no los da, y además dice la
    línea donde se abrió lo que no se cerró, que es lo que se necesita para
    arreglarlo.
    """
    pila, problemas = [], []
    i, n, linea = 0, len(texto), 1
    cierra = {"}": "{", ")": "(", "]": "["}
    while i < n:
        if texto[i] == "\n":
            linea += 1
            i += 1
            continue
        if texto.startswith("//", i):
            j = texto.find("\n", i)
            i = n if j < 0 else j
            continue
        if texto.startswith("/*", i):
            j = texto.find("*/", i + 2)
            fin = n if j < 0 else j + 2
            linea += texto.count("\n", i, fin)
            i = fin
            continue
        if texto.startswith('"""', i):
            j = texto.find('"""', i + 3)
            if j < 0:
                problemas.append("cadena cruda sin cerrar (línea %d)" % linea)
                break
            linea += texto.count("\n", i, j)
            i = j + 3
            continue
        if texto[i] == '"':
            i += 1
            while i < n and texto[i] != '"':
                if texto[i] == "\\":
                    i += 1
                elif texto[i] == "\n":
                    linea += 1
                i += 1
            i += 1
            continue
        if texto[i] == "\'":
            i += 1
            while i < n and texto[i] != "\'":
                if texto[i] == "\\":
                    i += 1
                i += 1
            i += 1
            continue
        c = texto[i]
        if c in "{([":
            pila.append((c, linea))
        elif c in "})]":
            if not pila:
                problemas.append("línea %d: cierra %s sin nada abierto" % (linea, c))
            elif pila[-1][0] != cierra[c]:
                problemas.append("línea %d: cierra %s pero lo abierto es %s (línea %d)"
                                 % (linea, c, pila[-1][0], pila[-1][1]))
                pila.pop()
            else:
                pila.pop()
        i += 1
    for abre, lin in pila:
        problemas.append("sin cerrar: %s abierto en la línea %d" % (abre, lin))
    return problemas


def auditar_hilos(codigo, regiones, estado_de_pantalla, api_de_hilo_principal):
    """Dentro de una región de fondo no se toca la pantalla ni una API con Looper.

    ExoPlayer comprueba desde qué hilo se le llama y lanza si no es el suyo; y
    escribir el estado de la pantalla desde un hilo de fondo es una carrera que no
    se ve hasta que el usuario gira el móvil. `regiones` son los aperturas de
    lambda de fondo del fichero ("Thread({", "enSegundoPlano {").
    """
    problemas = []
    for apertura in regiones:
        if apertura not in codigo:
            continue
        # Todas las apariciones, no sólo la primera: una pantalla tiene un lambda de
        # fondo por acción, y mirar sólo el primero deja los demás sin auditar.
        for trozo in codigo.split(apertura)[1:]:
            # hasta el cierre de la región: el siguiente método de la clase
            fin = min([x for x in (trozo.find("\n    private fun"),
                                   trozo.find("\n    override fun"),
                                   trozo.find("\n    fun ")) if x >= 0] or [len(trozo)])
            region = trozo[:fin]
            problemas += _mirar_region(region, apertura, estado_de_pantalla, api_de_hilo_principal)
    return problemas


def _mirar_region(region, apertura, estado_de_pantalla, api_de_hilo_principal):
    """Lo que no puede pasar dentro de una región de fondo."""
    problemas = []
    for linea in region.split("\n"):
        t = linea.strip()
        if not t or t.startswith("//") or t.startswith("*"):
            continue
        if "binding." in t:
            problemas.append("%s: toca una vista desde el hilo de fondo → %s" % (apertura, t[:60]))
        for v in estado_de_pantalla:
            if re.search(r"(?<![=!<>])\b%s\s*=(?!=)" % re.escape(v), t):
                problemas.append("%s: escribe el estado %s desde el hilo de fondo" % (apertura, v))
        for api in api_de_hilo_principal:
            if api in t:
                problemas.append("%s: llama a %s, que exige su propio hilo" % (apertura, api))
    return problemas


# ══════════════════════════════════════════════════════════════════════════
#  6b · Almacenamiento: los mecanismos que el proyecto aprueba
# ══════════════════════════════════════════════════════════════════════════

MECANISMOS_APROBADOS = {
    "datos que no son tokens": "AlmacenExterno.archivo / AlmacenExterno.directorio",
    "preferencias": "core/Prefs (JSON en AlmacenExterno)",
    "base de datos": "modules/reader/BibliotecaDb con ruta absoluta",
    "tokens": "EncryptedSharedPreferences (la única excepción del interno)",
    "conseguir un módulo desde una pantalla": "core/Pantallas.modulo",
    "declarar un sitio que escribe": "core/InventoryStorage.sitios",
}

PROHIBIDO_ALMACENAMIENTO = ["filesDir", "cacheDir", "noBackupFilesDir",
                            "getSharedPreferences", "openFileOutput",
                            "?: context.filesDir", "?: filesDir",
                            'System.getProperty("java.io.tmpdir")']


def auditar_almacenamiento(codigo, excepciones=()):
    """Nada de almacenamiento interno salvo las excepciones declaradas del proyecto."""
    fuera = []
    for patron in PROHIBIDO_ALMACENAMIENTO:
        if patron in excepciones:
            continue
        for i, linea in enumerate(solo_codigo(codigo).split("\n"), 1):
            if patron in linea:
                fuera.append((i, patron, linea.strip()[:70]))
    return fuera


# ══════════════════════════════════════════════════════════════════════════
#  7 · RECURSOS: layouts, cadenas, idiomas.
# ══════════════════════════════════════════════════════════════════════════

def a_snake(nombre):
    """`fuenteNombre` → `fuente_nombre`, que es como ViewBinding lee los `@+id/`."""
    return "_".join(re.findall(r"[A-Z]?[a-z0-9]+", nombre)).lower()


def ids_de_xml(xml):
    return set(re.findall(r'android:id="@\+id/([a-z0-9_]+)"', xml))


def cruzar_ids(codigo_kt, xml_del_fragmento, xml_de_items):
    """Los IDs en las dos direcciones: ni el código pide vistas que no existen,
    ni el layout declara vistas que nadie usa (eso es un adorno)."""
    ids_frag, ids_items = ids_de_xml(xml_del_fragmento), ids_de_xml(xml_de_items)
    usa_frag = set(re.findall(r"binding\.([a-z][A-Za-z0-9]*)", codigo_kt)) - {"root"}
    usa_items = set(re.findall(r"\bb\.([a-z][A-Za-z0-9]*)", codigo_kt)) - {"root"}
    problemas = []
    problemas += comparar_conjuntos("vistas pedidas por el código y ausentes del layout",
                                    [a_snake(u) for u in usa_frag], sorted(ids_frag))
    problemas += comparar_conjuntos("vistas pedidas por los adapters y ausentes de sus items",
                                    [a_snake(u) for u in usa_items], sorted(ids_items))
    return problemas


def xml_valido(texto, donde=""):
    try:
        ET.fromstring(texto)
        return []
    except ET.ParseError as e:
        return ["%s no es XML válido: %s" % (donde, e)]


def escapar_recurso(texto):
    """Lo que necesita un recurso de Android: sin la barra, un apóstrofo no compila."""
    t = texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = t.replace("\\'", "'").replace('\\"', '"')
    t = t.replace("'", "\\'").replace('"', '\\"')
    return t


def auditar_matriz_idiomas(cadenas, idiomas, texto_base=None):
    """Matriz completa, sin huecos, y con los mismos marcadores en todos.

    `TraduccionesPresentesTest` exige que toda cadena de values/ esté en las
    catorce carpetas y no vacía: una cadena nueva son quince entradas.
    """
    problemas = []
    for clave, textos in cadenas:
        for idioma in ["es"] + list(idiomas):
            if idioma not in textos:
                problemas.append("%s: falta en %s" % (clave, idioma))
            elif not textos[idioma].strip():
                problemas.append("%s: vacía en %s" % (clave, idioma))
        base = sorted(re.findall(r"%\d\$[ds]", textos.get("es", "")))
        for idioma in idiomas:
            if sorted(re.findall(r"%\d\$[ds]", textos.get(idioma, ""))) != base:
                problemas.append("%s: marcadores distintos en %s" % (clave, idioma))
    return problemas


# ══════════════════════════════════════════════════════════════════════════
#  8 · ESCAPES ENTRE CAPAS. Python → Kotlin.
# ══════════════════════════════════════════════════════════════════════════

def auditar_escapes_kotlin(texto_generado):
    """Un raw string de Kotlin no procesa escapes; uno normal sí.

    Dos veces se publicó una prueba con las barras duplicadas porque el texto
    pasó por dos capas de Python. La comprobación va sobre el **valor evaluado**
    (con `ast`), nunca sobre el texto fuente del generador.
    """
    problemas = []
    for crudo in re.findall(r'Regex\("""([\s\S]*?)"""\)', texto_generado):
        if "\\\\" in crudo:
            problemas.append("raw string con doble barra (no coincidirá con nada): %s" % crudo[:50])
    for normal in re.findall(r'(?<!")\b(?:substringBefore|substringAfter|contains)\("((?:[^"\\]|\\.)*)"\)',
                             texto_generado):
        if "\\\\" in normal and "\\\\n" not in normal and '\\\\"' not in normal:
            problemas.append("string normal con escape dudoso: %s" % normal[:50])
    return problemas


def valor_evaluado(ruta_py, nombre):
    """El valor real de una constante de texto de un generador, sin ejecutarlo.

    Leer el texto fuente con una regex enseña los escapes de Python sin resolver,
    que es exactamente lo que hizo creer que había un fallo donde no lo había.
    """
    import ast
    for nodo in ast.parse(open(ruta_py, encoding="utf-8").read()).body:
        if isinstance(nodo, ast.Assign) and isinstance(nodo.value, ast.Constant) \
                and isinstance(nodo.value.value, str):
            for t in nodo.targets:
                if isinstance(t, ast.Name) and t.id == nombre:
                    return nodo.value.value
    raise KeyError(nombre)


# ══════════════════════════════════════════════════════════════════════════
#  9 · DIAGNÓSTICO DE UN RUN ROJO.
# ══════════════════════════════════════════════════════════════════════════

def diagnosticar_log(texto):
    """Los hechos de un log de CI, en el orden en que se miran.

    Los logs sólo salen con curl y un token; con urllib dan 403. Y un run que
    falla al compilar imprime «0 pruebas · 0 fallos», que parece un éxito.
    """
    errores = [re.sub(r".*cero-X-app/", "", m) for m in
               re.findall(r"e: file://\S+:\d+:\d+ .*", texto)]
    fallos = [l for l in texto.split("\n") if " FAILED" in l and "Task" not in l]
    resumen = re.findall(r"\d+ pruebas · \d+ fallos · \d+ errores · \d+ saltadas", texto)
    builds = re.findall(r"BUILD (SUCCESSFUL|FAILED) in [^\n]*", texto)
    return {"errores": errores[:12], "fallos": [f.strip()[:150] for f in fallos[:12]],
            "resumen": resumen[-1:] if resumen else [], "builds": builds}


# ══════════════════════════════════════════════════════════════════════════
#  Comentar en hilos ajenos
# ══════════════════════════════════════════════════════════════════════════

MARCAS_DE_DATO = [
    (r"https?://\S+", "un enlace"),
    (r"```", "código"),
    (r"\bv?\d+\.\d+(?:\.\d+)?\b", "una versión o una cifra"),
    (r"[?¿]", "una pregunta"),
    (r"\b(?:commit|patch|pull request|PR)\b", "una referencia al cambio"),
    (r"[A-Za-z0-9_./-]+\.(?:kt|java|xml|json|gradle|kts|py|ts|js|md|yml|yaml)\b",
     "un fichero"),
    (r"\b(?:error|crash|exception|traceback|stack trace|fallo|bug)\b", "un fallo concreto"),
    (r"\b(?:fixed|solucionado|arreglado|merged|incluido|duplicado|duplicate)\b",
     "un desenlace"),
    # Nació al leer los 30 textos que el resto de las marcas había llamado ruido: la
    # mayoría no eran cortesía, eran **retiradas y enmiendas** de issues generadas por
    # máquina («it was AI-generated and it is withdrawn», «me equivoqué»). Borrarlas
    # habría dejado la publicación original sin corregir, que es peor que el ruido.
    (r"\b(?:withdrawn|withdraw|retract(?:ed|ion)?|i was wrong|my mistake|i cannot "
     r"confirm|no puedo confirmarlo|AI-generated|machine-generated|generated text|"
     r"slop|retirad[oa]|me equiv[oó]|sem raz[ãa]o|sin raz[oó]n|was wrong|was "
     r"decoration|era decoraci[oó]n|accepted|aceptado|Hakl\u0131s\u0131n)\b",
     "una retirada o una enmienda"),
]


def aporta_dato(texto):
    """Qué cosas nuevas aporta un texto. Lista vacía = sólo cortesía.

    Es la pregunta que no me hice ayer: un cierre educado no informa de nada, y en un
    hilo cerrado donde el mantenedor ya contestó, quien lo recibe se lleva una
    notificación a cambio de ninguna información.
    """
    return [nombre for patron, nombre in MARCAS_DE_DATO
            if re.search(patron, texto or "", re.IGNORECASE)]


# Retirar o dar por cerrado no informa de nada por sí mismo: sólo vale mientras haya
# algo en pie que retirar.
CEREMONIA = {"una retirada o una enmienda", "un desenlace"}


def merece_respuesta(hilo, borrador=""):
    """(veredicto, motivo) antes de publicar un comentario en un hilo ajeno.

    `hilo` lleva: state, locked, respondio_mantenedor y **pendiente** —si queda algo
    nuestro sin resolver ahí: una petición en pie, una acusación sin responder, una
    pregunta dirigida a la cuenta—. `pendiente` se decide leyendo el hilo; ninguna
    heurística lo sabe, y fingir lo contrario es lo que produjo los 30 comentarios.
    """
    if hilo.get("locked"):
        return ("callar", "la discusión está bloqueada")
    datos = aporta_dato(borrador)
    # Por defecto `pendiente` es False: quien no ha leído el hilo lo bastante para
    # saber que queda algo nuestro en pie, no comenta. Callar es el fallo seguro de
    # esta regla; publicar de más fue el fallo real, y costó 30 comentarios.
    muerto = (hilo.get("state") == "closed" and hilo.get("respondio_mantenedor")
              and not hilo.get("pendiente", False))
    if muerto and (not datos or set(datos) <= CEREMONIA):
        return ("callar",
                "hilo cerrado, ya respondido y sin nada nuestro pendiente: retirar o "
                "agradecer ahí no cambia lo que nadie deba hacer")
    if datos:
        return ("responder", "aporta " + ", ".join(datos))
    if hilo.get("state") == "closed":
        return ("callar", "hilo cerrado y el borrador no aporta ningún dato")
    if hilo.get("pendiente", False):
        return ("responder", "hay algo nuestro pendiente en el hilo")
    return ("callar", "el borrador no aporta ningún dato")


def censar_acciones(acciones, clasificar, categoria_muerta="muerta", tolerancia=0.5):
    """De qué está hecho un mandato «todos», antes de ejecutarlo.

    Devuelve (lineas, alarma). La alarma salta cuando la categoría muerta pasa de la
    tolerancia: entonces se para y se pregunta, porque «cada comentario» incluía 31
    hilos cerrados y nadie lo dijo antes de publicar.
    """
    grupos = {}
    for a in acciones:
        grupos.setdefault(clasificar(a), []).append(a)
    if grupos and categoria_muerta not in grupos:
        raise ValueError(
            "la categoría muerta %r no aparece entre las producidas %s: el censo "
            "habría dicho que no había alarma contando cero en una categoría vacía"
            % (categoria_muerta, sorted(grupos)))
    total = len(acciones) or 1
    lineas = ["%-16s %3d  (%3d%%)" % (c, len(v), round(100 * len(v) / total))
              for c, v in sorted(grupos.items(), key=lambda kv: -len(kv[1]))]
    return lineas, (len(grupos.get(categoria_muerta, [])) / total) > tolerancia


def idempotente(aplicar, estado_inicial, ya_esta, veces=2):
    """Aplica una acción varias veces sobre un estado y devuelve el estado final.

    Es lo que un guion que escribe **fuera** debería comprobar de sí mismo: si se
    interrumpe a mitad y se vuelve a ejecutar, no puede dejar la marca dos veces ni
    perder el registro de lo que ya hizo. `ya_esta` mira el estado vivo, no un censo
    guardado antes de empezar.
    """
    estado = estado_inicial
    for _ in range(veces):
        if ya_esta(estado):
            continue
        estado = aplicar(estado)
    return estado


def yaml_valido(texto):
    """Problemas de sintaxis de un YAML. Levanta ImportError si no hay con qué mirar.

    Nació de un flujo publicado con la continuación de una sustitución de mandato
    escrita en la columna 0 dentro de un bloque de varias líneas: ni las pruebas de JVM
    ni el compilador leen un flujo, así que lo único que lo caza es el propio YAML, y
    GitHub lo reporta como un run fallido **sin ningún job** y con el nombre en forma de
    ruta. Levantar ImportError cuando falta la biblioteca es a propósito: una puerta que
    no se ejecutó no puede decir que pasó.
    """
    try:
        import yaml
    except ImportError:
        raise ImportError("sin una biblioteca de YAML no se puede validar un flujo; "
                          "instalarla, o no afirmar que el fichero es válido")
    try:
        yaml.safe_load(texto)
        return []
    except Exception as e:
        return [str(e).replace("\n", " ")[:220]]


def bloques_literales(texto):
    """Líneas sueltas dentro de un bloque literal, sin depender de ninguna biblioteca.

    Un bloque `clave: |` termina en la primera línea con menos sangría, y esa línea
    tiene que ser una clave o un elemento de lista. Si es otra cosa —la continuación de
    un mandato escrito en la columna 0, por ejemplo—, el fichero está roto aunque a ojo
    el bloque parezca seguir.
    """
    lineas = texto.split("\n")
    problemas = []
    i = 0
    while i < len(lineas):
        m = re.match(r"^(\s*)[^\s#][^:]*:\s*\|[-+]?\s*$", lineas[i])
        if not m:
            i += 1
            continue
        j = i + 1
        while j < len(lineas) and not lineas[j].strip():
            j += 1
        if j >= len(lineas):
            break
        sangria = len(lineas[j]) - len(lineas[j].lstrip())
        if sangria <= len(m.group(1)):
            i = j
            continue
        k = j
        while k < len(lineas):
            l = lineas[k]
            if not l.strip():
                k += 1
                continue
            if (len(l) - len(l.lstrip())) >= sangria:
                k += 1
                continue
            if re.match(r"^\s*(?:-\s)?[^\s:][^:]*:(?:\s|$)", l) or l.strip() == "...":
                break
            problemas.append("línea %d: %r cuelga fuera de la sangría del bloque que "
                             "empieza en la línea %d" % (k + 1, l.strip()[:60], i + 1))
            break
        i = max(k, i + 1)
    return problemas


# ────────────────────────────────────────────────────────────────────────────
#  R21 · Un paso que la prueba no ejecuta se ejecuta en un repo de juguete
# ────────────────────────────────────────────────────────────────────────────

def mandato_de_paso(texto, nombre):
    """Devuelve (guion, fallos) del paso llamado `nombre`, leído del YAML ya
    evaluado y no del texto del fichero: lo que importa es lo que verá el
    corredor. `fallos` no vacío si falta la biblioteca, si el flujo no se lee o
    si no hay ningún paso con ese nombre — el nombre se escribe a mano y un
    paso que no existe deja la comprobación sin nada que mirar."""
    try:
        import yaml
    except ImportError:
        return None, ["falta la biblioteca de YAML: la comprobación no puede decir que pasó"]
    try:
        d = yaml.safe_load(texto)
    except Exception as e:
        return None, ["el flujo no se lee como YAML: %s" % str(e).split("\n")[0]]
    if not isinstance(d, dict):
        return None, ["el flujo no evalúa a un mapa"]
    for jn, job in (d.get("jobs") or {}).items():
        for paso in (job or {}).get("steps") or []:
            if isinstance(paso, dict) and paso.get("name") == nombre:
                guion = paso.get("run")
                if guion is None:
                    return None, ["el paso %r no tiene `run:`" % nombre]
                return guion, []
    return None, ["no hay ningún paso llamado %r" % nombre]


def sintaxis_de_mandato(guion, shell="bash"):
    """`shell -n` sobre el guion de un paso. Devuelve [] si la sintaxis es
    correcta. Un YAML válido no dice nada del shell que lleva dentro: una
    comilla sin cerrar pasa el YAML y revienta en el corredor."""
    import os, subprocess, tempfile
    fd, ruta = tempfile.mkstemp(suffix=".sh")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(guion)
        p = subprocess.run([shell, "-n", ruta], capture_output=True, text=True)
    finally:
        os.unlink(ruta)
    if p.returncode == 0:
        return []
    return ["%s -n: %s" % (shell, (p.stderr.strip().split("\n") or ["?"])[0])]


def correr_mandato(guion, montar=None, entorno=None, shell="bash", cwd=None):
    """Ejecuta el guion de un paso en un directorio de trabajo y devuelve
    (salida, fallos). `montar(dir)` prepara el escenario antes de correr — un
    repo con dos tags, un fichero de secretos falso— porque un paso que sólo se
    ejecuta con una entrada concreta (publicar=true, una etiqueta manual) no
    corre nunca en la comprobación por omisión. Sin escenario no hay prueba."""
    import os, subprocess, tempfile
    import shutil
    base = cwd or tempfile.mkdtemp(prefix="paso-")
    propio = cwd is None
    try:
        if montar is not None:
            montar(base)
        env = dict(os.environ)
        env.update(entorno or {})
        p = subprocess.run([shell, "-e", "-c", guion], capture_output=True,
                           text=True, cwd=base, env=env, timeout=180)
    finally:
        if propio:
            shutil.rmtree(base, ignore_errors=True)
    fallos = [] if p.returncode == 0 else [
        "el guion salió con %d: %s" % (p.returncode, (p.stderr.strip().split("\n") or ["?"])[-1])]
    return p.stdout + p.stderr, fallos


# ────────────────────────────────────────────────────────────────────────────
#  R22 · Un bucle de espera distingue «todavía no» de «la llamada falló»
# ────────────────────────────────────────────────────────────────────────────

def sondeo_sano(status, cuerpo, claves=()):
    """Dice si una respuesta de API es utilizable o es un fallo vestido de
    espera. Devuelve [] si se puede trabajar con ella. Un cuerpo sin las
    claves esperadas NO es «todavía no hay datos»: puede ser un 401 con un
    mensaje de credenciales, y un bucle que lo trate como espera se pasa
    media hora imprimiendo líneas vacías mientras la credencial está caída."""
    if status != 200:
        return ["HTTP %d: la llamada falló; no es «todavía no», es un fallo" % status]
    try:
        d = json.loads(cuerpo)
    except Exception:
        return ["el cuerpo no es JSON: %r" % cuerpo[:80]]
    falta = [k for k in claves if not isinstance(d, dict) or k not in d]
    if falta:
        return ["faltan las claves %s: el cuerpo no es lo que el bucle espera (%s)"
                % (falta, str(d.get("message", ""))[:80])]
    return []


# ────────────────────────────────────────────────────────────────────────────
#  R23 · Quien mueve un literal de sitio busca quién más lo lee
# ────────────────────────────────────────────────────────────────────────────

def lectores_de_literal(textos, literal, como_cadena=True):
    """`textos` es un dict {nombre: contenido} de pruebas publicadas. Con
    `como_cadena=True` devuelve los nombres de las que contienen el literal
    ENTRE COMILLAS, o sea como blanco de búsqueda: ésas escanean fuentes o
    flujos por contenido y son un acoplamiento publicado —un commit que mueve
    o borra el literal tiene que adaptarlas o confirmarlas una por una. Con
    `como_cadena=False` devuelve cualquier prueba que lo contenga, incluidos
    los consumidores que lo usan como código propio (ModelosEjecutadosTest crea
    su entorno ONNX para ejercitar modelos: no lee las fuentes de la app y no
    se rompe porque el literal se mueva). Confundir las dos clases fue el
    primer mordisco de esta regla: el censo señaló a un consumidor que no
    necesitaba nada."""
    if como_cadena:
        blanco = '"%s"' % literal
        return sorted(n for n, t in textos.items() if blanco in t)
    return sorted(n for n, t in textos.items() if literal in t)
