#!/usr/bin/env python3
"""
Diff entre censos de Appteka: qué apareció, qué desapareció y qué cambió (incidencia #2).

Por qué existe: un censo es una foto. Con una sola foto no se puede saber qué cambió, y recorrer el
catálogo entero otra vez para comparar a mano es justo el trabajo que nadie hace. Este script
compara dos snapshots fechados y dice:

  · apps NUEVAS de código abierto, con su repositorio de origen (para no repetir el recorrido);
  · apps que YA NO ESTÁN (retiradas, o dejaron de declarar código abierto);
  · apps que CAMBIARON de versión, de tamaño, de autor o de repositorio;
  · apps que CAMBIARON DE CATEGORÍA — que sin este caso parecerían «una nueva y una desaparecida».

Ese último es el que más importa. Comparar categoría por categoría sin más daría falsos movimientos:
si Appteka reclasifica una app, el diff ingenuo la cuenta dos veces y las dos mal. Aquí las apps se
identifican por PAQUETE en todo el censo, no por (categoría, id), y el cambio de categoría se
informa como lo que es.

Uso:
    python3 07-diff-de-censos.py                    # los dos últimos censos de censo/
    python3 07-diff-de-censos.py --dir OTRO_DIR     # otra carpeta de snapshots
    python3 07-diff-de-censos.py --viejo 2026-11-08 --nuevo 2026-11-17
    python3 07-diff-de-censos.py --max 40           # cuántas apps listar por sección
    python3 07-diff-de-censos.py --markdown         # además escribe censo/diff-<viejo>-<nuevo>.md

Salida: 0 = diff hecho · 2 = no hay dos censos que comparar (se dice claro, no se finge un diff vacío).
"""
from __future__ import annotations

import argparse
import gzip
import json
import re
import sys
from pathlib import Path

FECHA_EN_NOMBRE = re.compile(r"censo-(\d{4}-\d{2}-\d{2})\.json(\.gz)?$")

# Campos de una app que, si cambian, merecen línea propia. El orden es el de importancia para quien
# busca apps: primero de dónde viene, luego qué versión, luego quién la firma.
# `tamano` y `descargas` van aparte a propósito: las descargas suben solas cada día y el tamaño
# cambia con cada versión, así que meterlos aquí ahogaría los cambios que sí importan bajo miles de
# líneas de ruido. Se cuentan, no se listan.
CAMPOS_QUE_IMPORTAN = ("fuente", "version", "autor", "nombre")
CAMPOS_DE_RUIDO = ("tamano", "descargas")


def snapshots(directorio: Path) -> list[tuple[str, Path]]:
    """(fecha, ruta) de cada snapshot, ordenados por fecha. Acepta .json y .json.gz."""
    out = []
    if not directorio.is_dir():
        return out
    for p in sorted(directorio.iterdir()):
        m = FECHA_EN_NOMBRE.search(p.name)
        if m:
            out.append((m.group(1), p))
    return sorted(out)


def cargar(ruta: Path) -> dict:
    abrir = gzip.open if ruta.suffix == ".gz" else open
    with abrir(ruta, "rt", encoding="utf-8") as f:
        return json.load(f)


def aplanar(censo: dict) -> dict[str, dict]:
    """paquete -> {categoria, id, y los campos de la app}.

    Se aplana por PAQUETE a propósito: es la única clave estable. El id interno de Appteka puede
    cambiar y la categoría también; el paquete no.

    El representante se elige de forma CANÓNICA, no por orden de aparición. Éste fue un bug real que
    sólo cazó una prueba con cambios conocidos: en Appteka una misma app sale en varias categorías
    (26.572 paquetes de 36.540 salen en más de una), y si el representante es «la primera vez que
    aparece», basta que el fichero tenga las claves en otro orden —un `sort_keys` al reescribirlo,
    por ejemplo— para que el diff INVENTE 410 cambios de categoría y 2.896 cambios de datos que no
    ocurrieron. Aquí las categorías se ordenan alfabéticamente, el representante es siempre el de la
    primera, y el cambio de categoría se juzga por el CONJUNTO de categorías, no por una.
    """
    apariciones: dict[str, list[tuple[str, str, dict]]] = {}
    for categoria, bloque in censo.items():
        for aid, app in (bloque.get("apps") or {}).items():
            paquete = app.get("paquete") or aid
            apariciones.setdefault(paquete, []).append((categoria, aid, app))
    plano: dict[str, dict] = {}
    multi = 0
    for paquete, sitios in apariciones.items():
        sitios.sort(key=lambda t: (t[0], t[1]))          # canónico: categoría y luego id
        categoria, aid, app = sitios[0]
        entrada = dict(app)
        entrada["categoria"] = categoria
        entrada["categorias"] = [c for c, _, _ in sitios]
        entrada["id"] = aid
        plano[paquete] = entrada
        if len(sitios) > 1:
            multi += 1
    if multi:
        print(f"  {multi} paquetes salen en más de una categoría; el representante es la primera en "
              "orden alfabético y el diff mira el CONJUNTO de categorías", file=sys.stderr)
    return plano


def comparar(viejo: dict, nuevo: dict) -> dict:
    a, b = aplanar(viejo), aplanar(nuevo)
    nuevas = sorted(set(b) - set(a))
    fuera = sorted(set(a) - set(b))
    movidas, cambiadas, ruido = [], [], []
    for paquete in sorted(set(a) & set(b)):
        antes, ahora = a[paquete], b[paquete]
        cats_antes, cats_ahora = set(antes.get("categorias", [])), set(ahora.get("categorias", []))
        if cats_antes != cats_ahora:
            movidas.append((paquete,
                            ", ".join(sorted(cats_antes)) or "(ninguna)",
                            ", ".join(sorted(cats_ahora)) or "(ninguna)",
                            ahora.get("nombre", "")))
        diffs = {}
        for campo in CAMPOS_QUE_IMPORTAN:
            if antes.get(campo) != ahora.get(campo):
                diffs[campo] = (antes.get(campo), ahora.get(campo))
        if diffs:
            cambiadas.append((paquete, ahora.get("nombre", ""), diffs))
        for campo in CAMPOS_DE_RUIDO:
            if antes.get(campo) != ahora.get(campo):
                ruido.append(campo)
    return {
        "nuevas": [(p, b[p].get("nombre", ""), b[p].get("categoria", ""), b[p].get("fuente", ""),
                    b[p].get("version", "")) for p in nuevas],
        "fuera": [(p, a[p].get("nombre", ""), a[p].get("categoria", ""), a[p].get("fuente", ""))
                  for p in fuera],
        "movidas": movidas,
        "cambiadas": cambiadas,
        "ruido": {c: ruido.count(c) for c in CAMPOS_DE_RUIDO if ruido.count(c)},
        # Las dos cifras, siempre juntas. `listados_*` son entradas (categoría, app), que es lo que
        # suma `total` en cada categoría; `paquetes_*` son las apps DE VERDAD. En el censo del
        # 2026-11-08 hay 36.540 listados y sólo 9.968 paquetes distintos: una app sale en 3,67
        # categorías de media y `app.morphe.manager` sale en 352. Dar sólo la primera cifra fue el
        # error del titular del README; aquí no se puede repetir.
        "totales": {
            "categorias_viejo": len(viejo), "categorias_nuevo": len(nuevo),
            "listados_viejo": sum(c.get("total", 0) for c in viejo.values()),
            "listados_nuevo": sum(c.get("total", 0) for c in nuevo.values()),
            "paquetes_viejo": len(a), "paquetes_nuevo": len(b),
        },
        "por_categoria": {
            cat: {
                "antes": viejo.get(cat, {}).get("total", 0),
                "ahora": nuevo.get(cat, {}).get("total", 0),
            } for cat in sorted(set(viejo) | set(nuevo))
        },
        "categorias_nuevas": sorted(set(nuevo) - set(viejo)),
        "categorias_fuera": sorted(set(viejo) - set(nuevo)),
    }


def lineas(r: dict, fecha_vieja: str, fecha_nueva: str, maximo: int) -> list[str]:
    t = r["totales"]
    dl = t["listados_nuevo"] - t["listados_viejo"]
    dp = t["paquetes_nuevo"] - t["paquetes_viejo"]
    L = [
        f"DIFF DE CENSOS · {fecha_vieja} → {fecha_nueva}",
        f"  apps distintas (por paquete): {t['paquetes_viejo']} → {t['paquetes_nuevo']}  ({dp:+d})",
        f"  listados (categoría, app):    {t['listados_viejo']} → {t['listados_nuevo']}  ({dl:+d})",
        f"  categorías: {t['categorias_viejo']} → {t['categorias_nuevo']}",
        "",
        f"NUEVAS ({len(r['nuevas'])}) — apps de código abierto que no estaban:",
    ]
    for p, nombre, cat, fuente, ver in r["nuevas"][:maximo]:
        L.append(f"  + {nombre or p} · {p} · {cat} · v{ver}")
        if fuente:
            L.append(f"      {fuente}")
    if len(r["nuevas"]) > maximo:
        L.append(f"  … y {len(r['nuevas']) - maximo} más (--max para verlas todas)")
    if not r["nuevas"]:
        L.append("  (ninguna)")

    L += ["", f"FUERA ({len(r['fuera'])}) — estaban y ya no:"]
    for p, nombre, cat, fuente in r["fuera"][:maximo]:
        L.append(f"  - {nombre or p} · {p} · {cat}")
        if fuente:
            L.append(f"      {fuente}")
    if len(r["fuera"]) > maximo:
        L.append(f"  … y {len(r['fuera']) - maximo} más")
    if not r["fuera"]:
        L.append("  (ninguna)")

    L += ["", f"CAMBIARON DE CATEGORÍA ({len(r['movidas'])}) — no son altas ni bajas:"]
    for p, antes, ahora, nombre in r["movidas"][:maximo]:
        L.append(f"  ~ {nombre or p} · {p} · {antes} → {ahora}")
    if not r["movidas"]:
        L.append("  (ninguna)")

    L += ["", f"CAMBIARON DE DATOS ({len(r['cambiadas'])}):"]
    por_campo: dict[str, int] = {}
    for _p, _n, diffs in r["cambiadas"]:
        for c in diffs:
            por_campo[c] = por_campo.get(c, 0) + 1
    if por_campo:
        L.append("  por campo: " + " · ".join(f"{c}={n}" for c, n in
                                              sorted(por_campo.items(), key=lambda kv: -kv[1])))
    mostradas = [c for c in r["cambiadas"]
                 if any(k in c[2] for k in ("fuente", "version", "autor"))]
    for p, nombre, diffs in mostradas[:maximo]:
        det = " · ".join(f"{c}: {a!r} → {b!r}" for c, (a, b) in diffs.items()
                         if c in ("fuente", "version", "autor"))
        L.append(f"  * {nombre or p} · {p} · {det}")
    if len(mostradas) > maximo:
        L.append(f"  … y {len(mostradas) - maximo} más")
    if not r["cambiadas"]:
        L.append("  (ninguna)")
    if r.get("ruido"):
        L += ["", "  (aparte, cambios que son ruido de contador y no se listan: "
              + " · ".join(f"{c} en {n} apps" for c, n in r["ruido"].items()) + ")"]

    if r["categorias_nuevas"]:
        L += ["", f"CATEGORÍAS NUEVAS: {', '.join(r['categorias_nuevas'])}"]
    if r["categorias_fuera"]:
        L += ["", f"CATEGORÍAS QUE DESAPARECIERON: {', '.join(r['categorias_fuera'])}"]

    movidas_cat = [(c, v["antes"], v["ahora"]) for c, v in r["por_categoria"].items()
                   if v["antes"] != v["ahora"]]
    if movidas_cat:
        L += ["", f"CATEGORÍAS CON CAMBIO DE TOTAL ({len(movidas_cat)}):"]
        for c, antes, ahora in sorted(movidas_cat, key=lambda x: -abs(x[2] - x[1]))[:maximo]:
            L.append(f"  {c:28} {antes:6} → {ahora:6}  ({ahora - antes:+d})")
    return L


def main() -> int:
    ap = argparse.ArgumentParser(description="Diff entre dos censos fechados de Appteka")
    ap.add_argument("--dir", default=None,
                    help="carpeta con los snapshots (por defecto, censo/ junto a este script)")
    ap.add_argument("--viejo", default=None, help="fecha del censo antiguo (AAAA-MM-DD)")
    ap.add_argument("--nuevo", default=None, help="fecha del censo nuevo (AAAA-MM-DD)")
    ap.add_argument("--max", type=int, default=25, help="apps a listar por sección (25)")
    ap.add_argument("--markdown", action="store_true", help="escribir además un informe .md")
    a = ap.parse_args()

    aqui = Path(__file__).resolve().parent
    directorio = Path(a.dir) if a.dir else (aqui.parent / "censo")
    disponibles = snapshots(directorio)
    if len(disponibles) < 2:
        print(f"NO HAY DOS CENSOS QUE COMPARAR en {directorio}", file=sys.stderr)
        print(f"  encontrados: {[f for f, _ in disponibles] or 'ninguno'}", file=sys.stderr)
        print("  Para tener diff hacen falta dos recorridos fechados. Se hacen con:", file=sys.stderr)
        print("      python3 procedimientos/01-censar-catalogo-appteka.py", file=sys.stderr)
        print("  que guarda censo/censo-AAAA-MM-DD.json.gz. Este script NO se inventa un diff vacío "
              "cuando falta la segunda foto: eso sería un verde falso.", file=sys.stderr)
        return 2

    fechas = {f: p for f, p in disponibles}
    fv = a.viejo or disponibles[-2][0]
    fn = a.nuevo or disponibles[-1][0]
    for f in (fv, fn):
        if f not in fechas:
            print(f"NO EXISTE el censo del {f}. Disponibles: {', '.join(sorted(fechas))}",
                  file=sys.stderr)
            return 2
    if fv == fn:
        print("el censo viejo y el nuevo son el mismo: nada que comparar", file=sys.stderr)
        return 2

    viejo, nuevo = cargar(fechas[fv]), cargar(fechas[fn])
    r = comparar(viejo, nuevo)
    L = lineas(r, fv, fn, a.max)
    print("\n".join(L))

    if a.markdown:
        destino = directorio / f"diff-{fv}-a-{fn}.md"
        destino.write_text(
            f"# Diff de censos · {fv} → {fn}\n\n"
            f"Hecho con `procedimientos/07-diff-de-censos.py` sobre "
            f"`{fechas[fv].name}` y `{fechas[fn].name}`.\n\n```\n" + "\n".join(L) + "\n```\n",
            encoding="utf-8")
        print(f"\ninforme escrito: {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
