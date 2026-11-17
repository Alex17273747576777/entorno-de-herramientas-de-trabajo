"""Compara el esquema de pestañas de feed entre ShinKu y AniZen.

Por qué existe: el plan (work/feed-novedades/PLAN-FEED-SHINKU-ANIZEN.md) sostiene que ambas apps deben
describir las pestañas con los MISMOS nombres de tabla y columna, para que un backup de una se pueda
restaurar en la otra. Era una afirmación de diseño; aquí se comprueba mecánicamente contra el DDL real de
los dos repos, y lo que difiere se declara en vez de taparse.
"""
import re, sqlite3, sys
D = "/var/tmp/feed"
def ddl(t):
    t = re.sub(r"(?m)^import .*;$", "", t)
    return re.sub(r"\s+AS\s+Boolean", "", "\n".join(re.findall(r"CREATE (?:TABLE|INDEX)[\s\S]*?;", t)))
def columnas(con, tabla):
    try: return {r[1]: (r[2], "NOT NULL" if r[3] else "", r[4]) for r in con.execute(f"PRAGMA table_info({tabla})")}
    except sqlite3.OperationalError: return {}
PADRE = {"shinku": "CREATE TABLE saved_search(_id INTEGER NOT NULL PRIMARY KEY)",
         "anizen": "CREATE TABLE saved_search(_id INTEGER NOT NULL PRIMARY KEY)"}
FICHA = {"shinku": ("data/feed_categories.sq", "data/feed_saved_search.sq"),
         "anizen": ("feed_categories.sq", "feed_saved_search.sq")}
BASE = {"shinku": f"{D}/shinku/data/src/main/sqldelight/com/shinku/reader/",
        "anizen": f"{D}/anizen/data/src/main/sqldelight/tachiyomi/data/"}
esq, fallos = {}, []
for app in ("shinku", "anizen"):
    con = sqlite3.connect(":memory:")
    con.executescript(PADRE[app])
    for f in FICHA[app]:
        try: con.executescript(ddl(open(BASE[app] + f).read()))
        except sqlite3.OperationalError as e:
            print(f"  ✗ {app}: no pude montar {f}: {e}"); fallos.append(f"{app}:{f}")
    esq[app] = con
if fallos: print("RESULTADO:", fallos); sys.exit(1)
print("=== nombres de tabla (lo que decide la intercambiabilidad de backups) ===")
for t in ("feed_categories", "feed_saved_search"):
    a, b = bool(columnas(esq["shinku"], t)), bool(columnas(esq["anizen"], t))
    print(f"  {'✓' if a and b else '✗'} {t}: ShinKu={'sí' if a else 'NO'} AniZen={'sí' if b else 'NO'}")
print("=== columna a columna ===")
for t in ("feed_categories", "feed_saved_search"):
    cs, ca = columnas(esq["shinku"], t), columnas(esq["anizen"], t)
    comunes = sorted(set(cs) & set(ca)); solo_s = sorted(set(cs) - set(ca)); solo_a = sorted(set(ca) - set(cs))
    print(f"  {t}: comunes={len(comunes)} {comunes}")
    if solo_s: print(f"    sólo ShinKu: {solo_s}")
    if solo_a: print(f"    sólo AniZen: {solo_a}")
    for c in comunes:
        if cs[c][0] != ca[c][0]: print(f"    ~ {c}: tipo ShinKu={cs[c][0]} AniZen={ca[c][0]}")
print("=== las columnas que el plan exige para el tope por pestaña ===")
for c in ("category", "feed_order", "search_type"):
    en_s = c in columnas(esq["shinku"], "feed_saved_search"); en_a = c in columnas(esq["anizen"], "feed_saved_search")
    print(f"  {'✓' if en_s and en_a else '✗'} {c}: ShinKu={en_s} AniZen={en_a}")
print("=== RESULTADO ===")
print("  los nombres de tabla coinciden en ambas apps:",
      all(columnas(esq["shinku"], t) and columnas(esq["anizen"], t) for t in ("feed_categories", "feed_saved_search")))
print("  las tres columnas del tope por pestaña están en ambas:",
      all(c in columnas(esq[a], "feed_saved_search") for c in ("category", "feed_order", "search_type") for a in esq))
