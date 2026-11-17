import re, sqlite3
def ddl(t): 
    t=re.sub(r'(?m)^import .*;$','',t)
    return [re.sub(r'\s+AS\s+Boolean','',s) for s in re.findall(r'CREATE (?:TABLE|INDEX)[\s\S]*?;', t)]
def extra(t):  # sólo las sentencias de datos de la CABECERA, antes de la primera consulta etiquetada
    t=re.sub(r'(?m)^import .*;$','',t)
    cab=re.split(r'(?m)^\w+:\s*$', t)[0]          # todo lo que precede a la primera etiqueta
    cab=re.sub(r'CREATE (?:TABLE|INDEX)[\s\S]*?;','',cab)
    return [re.sub(r':\w+','?',x).strip() for x in re.findall(r'(?m)^(INSERT[\s\S]*?);', cab)]
def todas(t):  # TODAS las sentencias de un .sqm, en orden (ALTER incluidos), sin comentarios
    lineas=[l for l in t.split("\n") if not l.strip().startswith("--")]
    return [x.strip() for x in ";".join(lineas).split(";") if x.strip()]

def consultas(t):
    t=re.sub(r'(?m)^import .*;$','',t); c=re.sub(r'CREATE (?:TABLE|INDEX)[\s\S]*?;','',t)
    return {m.group(1): re.sub(r':\w+','?',m.group(2)).strip() for m in re.finditer(r'(?m)^(\w+):\s*\n([\s\S]*?);', c)}
PADRE="CREATE TABLE saved_search(_id INTEGER NOT NULL PRIMARY KEY, source INTEGER NOT NULL, name TEXT NOT NULL)"
NUEVO_DIR="data/src/main/sqldelight/com/shinku/reader"
fc_nuevo=open(f"{NUEVO_DIR}/data/feed_categories.sq").read(); fss_nuevo=open(f"{NUEVO_DIR}/data/feed_saved_search.sq").read()
mig=open(f"{NUEVO_DIR}/migrations/43.sqm").read(); fss_viejo=open("/tmp/fss_viejo.sq").read()
fallos=[]
def chk(c,m):
    print(("    ✓ " if c else "    ✗ ")+m)
    if not c: fallos.append(m)
def esquema(con,tabla):
    return [(r[1],r[2],r[3],r[4],r[5]) for r in con.execute(f"PRAGMA table_info({tabla})")]
def indices(con):
    return sorted(r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='index' AND name NOT LIKE 'sqlite_%'"))
print("=== ruta A: instalación limpia (DDL de los .sq nuevos) ===")
a=sqlite3.connect(":memory:"); a.execute("PRAGMA foreign_keys=ON"); a.execute(PADRE)
for f in (fc_nuevo,fss_nuevo):
    for s in ddl(f): a.execute(s)
    for s in extra(f): a.execute(s)
print(f"    tablas: {sorted(r[0] for r in a.execute('SELECT name FROM sqlite_master WHERE type=\"table\"'))}")
print("=== ruta B: actualización desde 41 (DDL viejo + 43.sqm) ===")
b=sqlite3.connect(":memory:"); b.execute("PRAGMA foreign_keys=ON"); b.execute(PADRE)
for s in ddl(fss_viejo): b.execute(s)
b.execute("INSERT INTO feed_saved_search(_id,source,saved_search,global) VALUES (1,7,NULL,1)")  # datos de antes de migrar
b.executescript(re.sub(r'\s+AS\s+Boolean','',mig))   # el .sqm entero, en orden, como lo haría SQLDelight
print("=== comparación de esquemas (lo que verifica SQLDelight) ===")
for t in ("feed_saved_search","feed_categories"):
    chk(esquema(a,t)==esquema(b,t), f"PRAGMA table_info({t}) idéntico en ambas rutas")
    if esquema(a,t)!=esquema(b,t):
        print("      limpia:",esquema(a,t)); print("      actual:",esquema(b,t))
chk(indices(a)==indices(b), f"índices idénticos: {indices(a)}")
print("=== los datos anteriores a la migración sobreviven ===")
fila=b.execute("SELECT _id,source,global,category,feed_order,search_type FROM feed_saved_search WHERE _id=1").fetchone()
chk(fila==(1,7,1,1,0,1), f"la fila antigua queda con los valores por defecto correctos: {fila}")
chk(b.execute("SELECT name FROM feed_categories WHERE _id=1").fetchone()[0]=="Global", "la pestaña de sistema existe tras migrar")
print("=== las consultas nuevas funcionan ===")
qfc=consultas(fc_nuevo); qfss=consultas(fss_nuevo)
q={f'cat_{k}':v for k,v in qfc.items()} | {f'fss_{k}':v for k,v in qfss.items()}
a.execute("INSERT INTO saved_search(_id,source,name) VALUES (5,7,'x')")   # padre real para la FK
a.execute("INSERT INTO feed_saved_search(_id,source,saved_search,global) VALUES (1,7,5,1)")
for nom in ("fss_selectAllGlobalByCategory","fss_countGlobalByCategory","fss_insert","cat_selectAll","cat_selectById","cat_insert","cat_delete","cat_update","cat_updateLang","cat_updateExplore","cat_selectLastInsertedRowId"):
    try:
        n=q[nom].count("?")
        # saved_search=5 existe (insertado arriba); el resto de parámetros con valores válidos
        args=(7,5,1) if nom=="fss_insert" else tuple(["x"]+[1]*(n-1)) if n and nom.endswith(("insert",)) else tuple([1]*n)
        a.execute(q[nom], args)
        print(f"    ✓ {nom}")
    except Exception as e: fallos.append(f"{nom}: {e}"); print(f"    ✗ {nom}: {e}")
print("\nRESULTADO:", "SIN FALLOS" if not fallos else f"{len(fallos)} FALLOS {fallos}")
