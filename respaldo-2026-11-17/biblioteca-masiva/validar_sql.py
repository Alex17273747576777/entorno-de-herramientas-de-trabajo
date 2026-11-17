import re, sqlite3, sys
def ddl(t):
    t = re.sub(r'(?m)^import .*;$','',t)
    return [re.sub(r'\s+AS\s+Boolean','',s) for s in re.findall(r'CREATE (?:TABLE|INDEX)[\s\S]*?;', t)]
def consultas(t):
    t = re.sub(r'(?m)^import .*;$','',t)
    cuerpo = re.sub(r'CREATE (?:TABLE|INDEX)[\s\S]*?;','',t)
    return {m.group(1): re.sub(r':\w+','?',m.group(2)).strip()
            for m in re.finditer(r'(?m)^(\w+):\s*\n([\s\S]*?);', cuerpo)}
CASOS=[("ShinKu","/var/tmp/feed/shinku/data/src/main/sqldelight/com/shinku/reader/data/merge_group.sq",
        "/var/tmp/feed/shinku/data/src/main/sqldelight/com/shinku/reader/migrations/42.sqm","merge_group_manga","mangas","manga_id",
        "CREATE TABLE mangas(_id INTEGER NOT NULL PRIMARY KEY, favorite INTEGER NOT NULL DEFAULT 0)"),
       ("AniZen","/var/tmp/feed/anizen/data/src/main/sqldelight/tachiyomi/data/merge_group.sq",
        "/var/tmp/feed/anizen/data/src/main/sqldelight/tachiyomi/data/migrations/147.sqm","merge_group_anime","animes","anime_id",
        "CREATE TABLE animes(_id INTEGER NOT NULL PRIMARY KEY, favorite INTEGER NOT NULL DEFAULT 0)")]
fallos=[]
def chk(nombre, cond, msg):
    print(("    ✓ " if cond else "    ✗ ")+msg)
    if not cond: fallos.append(f"{nombre}: {msg}")
for nombre, sq, sqm, tabla, padre, col, ddl_padre in CASOS:
    print(f"\n########## {nombre} ##########")
    texto=open(sq).read(); q=consultas(texto); d_sq=ddl(texto); d_sqm=ddl(open(sqm).read())
    # 1. ruta de instalación limpia (.sq) y 2. ruta de actualización (.sqm)
    for etiqueta, sent in (("instalación limpia (.sq)", d_sq), ("actualización (.sqm)", d_sqm)):
        con=sqlite3.connect(":memory:"); con.execute("PRAGMA foreign_keys=ON"); con.execute(ddl_padre)
        for s in sent: con.execute(s)
        t=[r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")]
        i=sorted(r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='index' AND name LIKE 'merge%'"))
        chk(nombre, "merge_group" in t and tabla in t, f"{etiqueta}: {len(sent)} DDL OK, tablas {sorted(x for x in t if x.startswith('merge'))}")
        chk(nombre, len(i)==2, f"{etiqueta}: 2 índices {i}")
        con.close()
    # 3. comportamiento real sobre la ruta limpia
    con=sqlite3.connect(":memory:"); con.execute("PRAGMA foreign_keys=ON"); con.execute(ddl_padre)
    for s in d_sq: con.execute(s)
    con.execute(f"INSERT INTO {padre}(_id) VALUES (10),(11),(12)")
    con.execute("INSERT INTO merge_group(override_source_ranking) VALUES (0)")
    gid=con.execute(q["selectLastInsertedRowId"]).fetchone()[0]
    con.execute(q["insertGroup"],(0,))
    con.execute(q["insertMember"],(gid,10,0)); con.execute(q["insertMember"],(gid,11,1))
    chk(nombre, con.execute(q["getGroupId"],(10,)).fetchone()[0]==gid, f"getGroupId(10) -> grupo {gid}")
    chk(nombre, [r[0] for r in con.execute(q["getMembers"],(gid,))]==[10,11], "getMembers ordena por source_priority, id")
    chk(nombre, con.execute(q["getMemberships"]).fetchall()==[(10,gid),(11,gid)], "getMemberships devuelve 2 pertenencias")
    for caso, args, porqué in [
        ("doble pertenencia",(gid,10,2),f"UNIQUE({col}) impide que una entrada esté en dos grupos"),
        ("grupo inexistente",(99999,12,0),"FK(group_id) rechaza un grupo que no existe"),
        (f"{padre} inexistente",(gid,99999,0),f"FK({col}) rechaza una entrada que no existe")]:
        try:
            con.execute(q["insertMember"],args); chk(nombre, False, f"{porqué} — NO se rechazó")
        except sqlite3.IntegrityError as e: chk(nombre, True, f"{porqué} ({e})")
    con.execute(f"DELETE FROM {padre} WHERE _id=11")
    chk(nombre, [r[0] for r in con.execute(f"SELECT {col} FROM {tabla}")]==[10], f"cascade: al borrar {padre}(11) su pertenencia desaparece")
    con.execute("DELETE FROM merge_group WHERE _id=?", (gid,))
    chk(nombre, con.execute(f"SELECT count(*) FROM {tabla}").fetchone()[0]==0, "cascade: al borrar el grupo se vacían sus miembros")
    con.execute(q["insertMember"],(gid,12,0)) if False else None
    con.close()
    chk(nombre, set(q)=={"getGroupId","getMembers","getMemberships","insertGroup","insertMember","removeMember","deleteGroup","selectLastInsertedRowId"}, f"las 8 consultas declaradas existen: {sorted(q)}")
print("\n================ RESULTADO ================")
print("FALLOS:", fallos if fallos else "NINGUNO"); print("SQLite:", sqlite3.sqlite_version)
sys.exit(1 if fallos else 0)
