#!/usr/bin/env python3
# Construye el Index de anime con los bindings oficiales de la org
# (manga-fonte-extensoes/.github/scripts/index_pb2.py) y la serialización de
# publish-repo.py (deterministic + gzip mtime=0), y compara byte a byte con el
# pb variante generado por json_a_index_pb.py.
import gzip, json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent / "manga-fonte-extensoes"))
import index_pb2

repo = pathlib.Path("/var/tmp/nox/anime-extensoes")
exts = json.load(open(repo / "index.json"))
meta = json.load(open(repo / "repo.json"))["meta"]

pkgs = [e["pkg"] for e in exts]
assert pkgs == sorted(pkgs), "index.json no está ordenado por pkg (publish-repo.py ordena)"

idx = index_pb2.Index()
idx.name = meta["name"]; idx.badgeLabel = meta["shortName"]
idx.signingKey = meta["signingKeyFingerprint"]; idx.contact.website = meta["website"]
for e in exts:
    x = idx.extensionList.extensions.add()
    x.name = e["name"]; x.packageName = e["pkg"]
    x.resources.apkUrl = f"https://raw.githubusercontent.com/Awerkori/anime-extensoes/repo/apk/{e['apk']}"
    x.resources.iconUrl = f"https://cdn.jsdelivr.net/gh/Awerkori/anime-extensoes@repo/icon/{e['pkg']}.png"
    # Aritmética de la casa, derivada del pb vivo de manga (ground truth):
    # versionCode = libMaj*100000 + libMin*1000 + apkCode, con lib tomado de
    # extensionLib. En anime versionName "14.11" = lib 14 + versión de ext 11
    # (semántica Aniyomi): el "11" NO es libMinor; libMinor=0 → 1400011.
    v = e["version"].split(".")
    x.extensionLib = v[0] if len(v) == 2 else ".".join(v[:2])
    lb = x.extensionLib.split(".")
    lmaj, lmin = int(lb[0]), int(lb[1]) if len(lb) > 1 else 0
    x.versionCode = lmaj * 100000 + lmin * 1000 + int(e["code"])
    x.versionName = e["version"]
    x.contentWarning = 3 if e.get("nsfw") else 1
    for s in e.get("sources", []):
        src = x.sources.add()
        src.id = int(s["id"]); src.name = s["name"]; src.language = s["lang"]; src.homeUrl = s["baseUrl"]
data = gzip.compress(idx.SerializeToString(deterministic=True), mtime=0)
mio = pathlib.Path("/home/user/work/nox-index-pb/anime-index-variante-nox.pb").read_bytes()
print(f"org-bindings {len(data)} B · mi variante {len(mio)} B · IDENTICOS: {data == mio}")
if data != mio:
    for i in range(min(len(data), len(mio))):
        if data[i] != mio[i]:
            print(f"primera dif byte {i}: org {data[max(0,i-8):i+16]!r} vs mio {mio[max(0,i-8):i+16]!r}"); break
    pathlib.Path("/tmp/org-anime.pb").write_bytes(data)
sys.exit(0 if data == mio else 1)
