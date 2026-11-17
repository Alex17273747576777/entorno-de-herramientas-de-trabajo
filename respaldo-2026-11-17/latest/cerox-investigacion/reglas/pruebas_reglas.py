#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejecuta el registro de reglas: primero contra sus propios incidentes, después
contra lo que hay publicado en el repo.

Una regla que no caza su propio incidente no es una regla. Por eso cada una lleva
dos fixtures y este guion falla si la mala no da problemas o la buena da alguno.

Uso:
    python3 -B pruebas_reglas.py            # fixtures + árbol (si está en /tmp/arbol)
    python3 -B pruebas_reglas.py --arbol DIR
"""
import os
import re
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from motor import (auditar_almacenamiento, auditar_escapes_kotlin, auditar_matriz_idiomas,
                   auditar_prosa, censar_pruebas, cruzar_ids, ids_de_xml, solo_codigo)
from registro import IDIOMAS, PROHIBIDOS_GLOBALES, PROHIBIDOS_POR_RUTA, REGLAS

AQUI = os.path.dirname(os.path.abspath(__file__))
ARBOL = "/tmp/arbol"
for i, a in enumerate(sys.argv):
    if a == "--arbol" and i + 1 < len(sys.argv):
        ARBOL = sys.argv[i + 1]
APP = os.path.join(ARBOL, "android/app")

fallos = []


def titulo(t):
    print("\n" + "═" * 78 + "\n" + t + "\n" + "═" * 78)


# ── 1 · Cada regla contra su propio incidente ───────────────────────────────

titulo("1 · FIXTURES: cada regla caza su incidente y no muerde el código bueno")

for r in REGLAS:
    mala, buena = dict(r["mala"]), dict(r["buena"])
    if r["id"] == "R15":
        # La fixture mala se construye: un artefacto re-descargable de verdad.
        tmp = tempfile.mkdtemp(prefix="regla15-")
        with open(os.path.join(tmp, "arbol.tgz"), "wb") as f:
            f.write(b"0" * 2048)
        mala = {"raiz": tmp}
    problemas_mala = r["comprobar"](**mala)
    problemas_buena = r["comprobar"](**buena)
    ok = bool(problemas_mala) and not problemas_buena
    print("  %s %-3s %-58s %s" % ("✓" if ok else "✗", r["id"], r["titulo"][:58],
                                  "caza %d · buena %d" % (len(problemas_mala), len(problemas_buena))))
    if not ok:
        fallos.append("%s no se comporta: mala=%r buena=%r" % (r["id"], problemas_mala[:1], problemas_buena[:1]))
    if problemas_mala:
        print("       incidente → %s" % str(problemas_mala[0])[:104])

# ── 2 · Las mismas reglas sobre lo publicado ────────────────────────────────

titulo("2 · ÁRBOL PUBLICADO: %s" % (ARBOL if os.path.isdir(APP) else "no está (bájalo por SHA)"))

if os.path.isdir(APP):
    IPTV = os.path.join(APP, "src/main/java/com/ceroX/app/modules/iptv")
    ficheros_iptv = sorted(f for f in os.listdir(IPTV) if f.endswith(".kt"))

    # R1 · prosa que no cita
    print("\n  R1 · prosa de los ficheros IPTV y de build.gradle")
    total = 0
    for f in ficheros_iptv:
        t = open(os.path.join(IPTV, f), encoding="utf-8").read()
        v = auditar_prosa(t, donde=f)
        total += len(v)
        for x in v:
            print("     ✗ %s:%d cita %s" % (f, x[0], x[3]))
    gradle = open(os.path.join(APP, "build.gradle"), encoding="utf-8").read()
    total += len(auditar_prosa(gradle, donde="build.gradle"))
    print("     %s %d citas prohibidas en %d ficheros" % ("✓" if total == 0 else "✗", total, len(ficheros_iptv) + 1))
    if total:
        fallos.append("R1: prosa publicada cita literales prohibidos")

    # R5 · censo de pruebas publicadas y contradicciones
    print("\n  R5 · censo de las pruebas publicadas")
    censo = censar_pruebas(os.path.join(APP, "src/test"))
    exige = sum(len(v["exige"]) for v in censo.values())
    prohibe = sum(len(v["prohibe"]) for v in censo.values())
    print("     %d ficheros de prueba · %d literales exigidos · %d prohibidos"
          % (len(censo), exige, prohibe))
    contra = []
    for fichero, entrada in censo.items():
        for lit in entrada["exige"]:
            for p in PROHIBIDOS_GLOBALES:
                # Contención mutua: la contradicción del incidente llevaba el
                # literal dentro de una ruta, no pelado.
                if lit == p or lit in p or p in lit:
                    contra.append("%s exige %r, que no puede aparecer en src/main" % (fichero, lit))
    print("     %s %d contradicciones entre pruebas publicadas" % ("✓" if not contra else "✗", len(contra)))
    for c in contra:
        print("       ✗ " + c)
    if contra:
        fallos.append("R5: pruebas publicadas que se contradicen")

    # R11 · almacenamiento
    print("\n  R11 · almacenamiento de los ficheros IPTV")
    malo = 0
    for f in ficheros_iptv:
        t = open(os.path.join(IPTV, f), encoding="utf-8").read()
        for x in auditar_almacenamiento(t):
            malo += 1
            print("     ✗ %s:%d %s" % (f, x[0], x[1]))
    print("     %s %d infracciones de almacenamiento" % ("✓" if malo == 0 else "✗", malo))
    if malo:
        fallos.append("R11: almacenamiento interno en IPTV")

    # R12 · matriz de idiomas
    print("\n  R12 · las 22 cadenas IPTV en los 15 idiomas")
    carpetas = {"es": "values"}
    for i in IDIOMAS:
        carpetas[i] = "values-" + i
    por_idioma = {}
    for idioma, carpeta in carpetas.items():
        ruta = os.path.join(APP, "src/main/res", carpeta, "strings.xml")
        por_idioma[idioma] = dict(re.findall(r'<string name="(iptv_[a-z_]+)">([^<]*)</string>',
                                             open(ruta, encoding="utf-8").read()))
    claves = sorted(por_idioma["es"])
    cadenas = [(c, {i: por_idioma[i].get(c, "") for i in por_idioma}) for c in claves]
    problemas = auditar_matriz_idiomas(cadenas, IDIOMAS)
    print("     %s %d claves × %d idiomas · %d problemas"
          % ("✓" if not problemas else "✗", len(claves), len(por_idioma), len(problemas)))
    for p in problemas[:6]:
        print("       ✗ " + p)
    if problemas:
        fallos.append("R12: matriz de traducciones incompleta")

    # R13 · layouts cruzados con el Fragment
    print("\n  R13 · IDs cruzados de la pantalla IPTV")
    frag_kt = open(os.path.join(IPTV, "IptvUiFragment.kt"), encoding="utf-8").read()
    lay = os.path.join(APP, "src/main/res/layout")
    xml_frag = open(os.path.join(lay, "fragment_iptv.xml"), encoding="utf-8").read()
    xml_items = [open(os.path.join(lay, x), encoding="utf-8").read()
                 for x in ("item_fuente_iptv.xml", "item_canal_iptv.xml")]
    problemas = cruzar_ids(frag_kt, xml_frag, "\n".join(xml_items))
    for xml in [xml_frag] + xml_items:
        for _a, v in re.findall(r'android:(text|hint)="([^"]*)"', xml):
            if not v.startswith("@string/"):
                problemas.append("texto sin traducir: %r" % v)
    print("     %s %d problemas · %d ids de fragmento · %d de items"
          % ("✓" if not problemas else "✗", len(problemas), len(ids_de_xml(xml_frag)),
             len(ids_de_xml("".join(xml_items)))))
    for p in problemas[:6]:
        print("       ✗ " + p)
    if problemas:
        fallos.append("R13: pantalla IPTV con ids o textos sueltos")

    # R6 · escapes de la prueba publicada de la pantalla
    print("\n  R6 · escapes de las pruebas publicadas")
    mal_esc = 0
    for d, _, fs in os.walk(os.path.join(APP, "src/test")):
        for f in fs:
            if not f.endswith(".kt"):
                continue
            t = open(os.path.join(d, f), encoding="utf-8").read()
            for p in auditar_escapes_kotlin(t):
                mal_esc += 1
                print("     ✗ %s: %s" % (f, p[:90]))
    print("     %s %d raw strings con dobles barras" % ("✓" if mal_esc == 0 else "✗", mal_esc))
    if mal_esc:
        fallos.append("R6: escapes rotos en pruebas publicadas")

# ── 3 · El workspace ────────────────────────────────────────────────────────

titulo("3 · WORKSPACE: nada re-descargable guardado")
r15 = [r for r in REGLAS if r["id"] == "R15"][0]
problemas = r15["comprobar"](raiz="/home/user")
print("  %s %d artefactos re-descargables en /home/user" % ("✓" if not problemas else "✗", len(problemas)))
for p in problemas[:8]:
    print("     ✗ " + p)
if problemas:
    fallos.append("R15: el workspace guarda cosas re-descargables")

# ── 4 · Autoaplicación: este registro tampoco cita lo que prohíbe ───────────

titulo("4 · AUTOAPLICACIÓN: el propio registro describe y no cita")
# La prosa de estos tres ficheros (comentarios # y docstrings) no puede citar lo
# que prohíbe. El código sí: la tabla de prohibiciones es el registro, y las
# fixtures reproducen el incidente componiendo el literal con literal_de().
propios = 0
for f in ("motor.py", "registro.py", "pruebas_reglas.py"):
    t = open(os.path.join(AQUI, f), encoding="utf-8").read()
    for x in auditar_prosa(t, donde=f, lenguaje="python"):
        propios += 1
        print("     ✗ %s:%d cita %s (%s)" % (f, x[0], x[3], x[1]))
print("  %s %d citas en la prosa del propio registro" % ("✓" if propios == 0 else "✗", propios))
if propios:
    fallos.append("autoaplicación: el registro se cita a sí mismo")

# ── Resumen ────────────────────────────────────────────────────────────────

titulo("RESUMEN")
print("  reglas registradas      %d" % len(REGLAS))
print("  temas                   %s" % ", ".join(sorted({r["tema"] for r in REGLAS})))
print("  literales prohibidos    %d en %d temas"
      % (sum(len(v) for v in __import__("motor").PROHIBIDOS.values()),
         len(__import__("motor").PROHIBIDOS)))
print("  líneas de evolución     %d" % sum(len(r["evolucion"]) for r in REGLAS))
if fallos:
    print("\n  ✗ %d FALLOS:" % len(fallos))
    for f in fallos:
        print("     · " + f)
    raise SystemExit(1)
print("\n  ✓ todo pasa: las %d reglas cazan su incidente y el árbol publicado está limpio"
      % len(REGLAS))
