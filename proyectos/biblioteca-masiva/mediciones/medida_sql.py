import sqlite3, time, re, random
sq = open("/tmp/merge_group_az.sq").read()
ddl = [re.sub(r'\s+AS\s+Boolean','',s) for s in re.findall(r'CREATE (?:TABLE|INDEX)[\s\S]*?;', re.sub(r'(?m)^import .*;$','',sq))]
N = 50_000; GRUPOS = 5_000
con = sqlite3.connect(":memory:"); con.execute("PRAGMA foreign_keys=OFF")
con.execute("CREATE TABLE animes(_id INTEGER NOT NULL PRIMARY KEY, title TEXT NOT NULL, favorite INTEGER NOT NULL DEFAULT 0, date_added INTEGER NOT NULL DEFAULT 0)")
for s in ddl: con.execute(s)
random.seed(7)
con.executemany("INSERT INTO animes(_id,title,favorite) VALUES (?,?,1)", [(i, f"entrada {i:07d}") for i in range(1, N+1)])
con.executemany("INSERT INTO merge_group_anime(group_id,anime_id,source_priority) VALUES (?,?,0)", [((i % GRUPOS)+1, i) for i in range(1, N+1)])
con.execute("DELETE FROM merge_group"); con.executemany("INSERT INTO merge_group(_id) VALUES (?)", [(g,) for g in range(1, GRUPOS+1)])
con.commit()
print(f"SQLite {sqlite3.sqlite_version} · biblioteca simulada: {N} entradas favoritas, {GRUPOS} grupos, {con.execute('SELECT count(*) FROM merge_group_anime').fetchone()[0]} pertenencias")
t0=time.perf_counter(); filas=con.execute("SELECT anime_id, group_id FROM merge_group_anime").fetchall(); t1=time.perf_counter()
memb=dict((a,g) for a,g in filas); ms_load=(t1-t0)*1000
print(f"  A) cargar TODA la pertenencia (getMemberships, 1 pasada): {ms_load:.2f} ms  -> {len(memb)} filas")
t0=time.perf_counter(); vistos=set(); sobrev=0
for a,g in filas:
    if g not in vistos: vistos.add(g); sobrev+=1
t1=time.perf_counter(); print(f"  B) colapsar a uno por grupo en memoria (dedupeByMergeGroup): {(t1-t0)*1000:.2f} ms -> {sobrev} supervivientes")
print(f"  TOTAL ruta con pertenencia guardada (A+B): {ms_load + (t1-t0)*1000:.2f} ms para {N} entradas")
MUESTRAS=150
ids=random.sample(range(1,N+1),MUESTRAS)
t0=time.perf_counter()
for i in ids:
    t=con.execute("SELECT title FROM animes WHERE _id=?", (i,)).fetchone()[0].lower()
    con.execute("SELECT _id FROM animes WHERE favorite = 1 AND _id != ? AND lower(title) LIKE '%'||?||'%'", (i,t)).fetchall()
t1=time.perf_counter(); por=(t1-t0)/MUESTRAS*1000
print(f"  C) detección por escaneo de título (el patrón real de animes.sq:128): {por:.2f} ms POR entrada ({MUESTRAS} muestras)")
print(f"     extrapolado a las {N} entradas de la biblioteca: {por*N/1000:.1f} s  ({(por*N/1000)/60:.1f} min)")
print(f"  D) cociente: el escaneo por título cuesta {(por*N)/(ms_load+(t1-t0)*1000):.0f}× más que la pertenencia guardada en esta máquina")
t0=time.perf_counter(); con.execute("SELECT group_id FROM merge_group_anime WHERE anime_id=?", (N//2,)).fetchone(); t1=time.perf_counter()
print(f"  E) una consulta getGroupId con el índice: {(t1-t0)*1000:.4f} ms")
