#!/usr/bin/env python3
"""Pruebas del entorno — sin frameworks, sin instalar nada."""
import pathlib, subprocess, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))
from lib import medicion, auditoria

fallos = 0


def check(nombre, cond, detalle=""):
    global fallos
    if cond:
        print(f"  ok    {nombre}")
    else:
        fallos += 1
        print(f"  FALLO {nombre} {detalle}")


print("· medicion")
texto = ("# Título\n\n"
         + ("Frase de prosa suficientemente larga para contar como párrafo real. " * 4)
         + "\n\n"
         + ("Otra frase distinta también larga que no repite la anterior para nada. " * 4))
ruta = RAIZ / ".tmp-prueba.md"
ruta.write_text(texto, encoding="utf-8")
m = medicion.medir(str(ruta))
check("cuenta caracteres", m["caracteres_archivo"] == len(texto))
check("detecta párrafos", m["parrafos"] == 2, f"(vio {m['parrafos']})")
check("palabras > 0", m["palabras"] > 10)

print("· auditoria")
a = auditoria.auditar(str(ruta))
check("sin repetición = limpio", a["pct_relleno"] == 0.0, f"({a['pct_relleno']})")
rep = "Párrafo idéntico que se repite varias veces seguidas en el mismo archivo de prueba. " * 4
ruta.write_text(rep.strip() + "\n\n" + rep.strip() + "\n\n" + rep.strip(), encoding="utf-8")
a2 = auditoria.auditar(str(ruta))
check("detecta repetición", a2["bloques_repetidos"] >= 1, f"({a2['bloques_repetidos']})")
check("marca relleno", a2["veredicto"] == "RELLENO", f"({a2['veredicto']})")
check("cuenta lo repetido", a2["caracteres_repetidos"] > 0)

print("· veredicto")
estado, notas = medicion.veredicto({"caracteres_prosa": 1000})
check("corto no apto", estado == "NO APTO" and any("FALTA" in n for n in notas))
estado2, notas2 = medicion.veredicto({"caracteres_prosa": 90_000})
check("largo no apto", estado2 == "NO APTO" and any("EXCESO" in n for n in notas2))
estado3, _ = medicion.veredicto({"caracteres_prosa": 50_000})
check("en banda apto", estado3 == "APTO")

print("· estricto sin repetidos")
p = "Prosa repetida suficientemente larga como para superar el filtro de párrafos. " * 4
ruta.write_text("\n\n".join([p] * 200), encoding="utf-8")
mr = medicion.medir(str(ruta))
check("relleno supera mínimo bruto", mr["caracteres_prosa"] >= medicion.MIN_FACEBOOK)
check("útil cuenta una copia", mr["caracteres_utiles"] == len(p.strip()))
check("relleno no sale APTO", medicion.veredicto(mr)[0] == "NO APTO")

print("· cli")
out = subprocess.run([sys.executable, str(RAIZ / "bin" / "medir-pieza"), str(ruta), "--json"],
                     capture_output=True, text=True)
check("cli json corre", out.returncode == 1 and '"pct_relleno"' in out.stdout)

for formato in ([], ["--tabla"]):
    result = subprocess.run([sys.executable, str(RAIZ / "bin/medir-pieza"), str(ruta), *formato], capture_output=True, text=True)
    check("cli rechaza relleno " + str(formato), result.returncode == 1)
ruta.unlink(missing_ok=True)
print()
print("TODO BIEN" if fallos == 0 else f"{fallos} FALLOS")
sys.exit(1 if fallos else 0)
