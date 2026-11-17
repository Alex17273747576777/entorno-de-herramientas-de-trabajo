#!/usr/bin/env python3
# json_a_index_pb.py — convierte index.json/index.min.json de repos tipo Keiyoushi/Yuzono
# al formato binario index.pb (= repo.json "index_v2"): gzip(proto(Index)).
# Esquema aprendido por ingeniería inversa del par vivo manga-extensoes
# (index.json + index.min.json + index.pb), no documentado por el skill Nox.
#
# Schema (proto3-like, numeros de campo observados):
#   Index { 1 name, 2 shortName/badgeLabel, 3 signingKeyFingerprint, 4 {1 website},
#           101 { 1 repeated Plugin } }
#   Plugin { 1 name, 2 pkg, 3 {1 apkUrl, 2 iconUrl, 501 jarUrl}, 4 extensionLib,
#            5 versionCode(varint), 6 versionName, 7 contentWarning(varint enum),
#            8 repeated Source }
#   Source { 1 id(varint), 2 name, 3 language, 4 homeUrl, 5 mirrorUrls(repetido),
#            6 message(opcional) }
# Dos specs de Extension (ver plugin_pb): "nox" (variante viva del manga-extensoes,
# sources=8, jarUrl=501) y "aniyomi" (spec oficial aniyomiorg/extensions-lib/index,
# isTorrent=8, sources=9), que es la que manda el skill Nox para anime/Yuzono.
# Uso:
#   python3 json_a_index_pb.py roundtrip <repo manga>   # prueba dorada: bytes identicos
#   python3 json_a_index_pb.py generar <repo anime> <tag-release|repo> <salida.pb> [spec]
import gzip, json, sys, zlib, pathlib

def vi(n):
    out = bytearray()
    while True:
        b = n & 0x7F
        n >>= 7
        out.append(b | (0x80 if n else 0))
        if not n:
            return bytes(out)

def tag(fn, wt):
    return vi((fn << 3) | wt)

def fld_s(fn, s):
    # proto3: un campo de cadena con valor por defecto ("") NO se serializa.
    # Las bibliotecas protobuf lo omiten; escribirlo rompe la paridad byte a byte
    # (caso real: 4 fuentes de anime con baseUrl vacía, 8 bytes de más).
    if not s:
        return b""
    b = s.encode()
    return tag(fn, 2) + vi(len(b)) + b

def fld_i(fn, n):
    # proto3: varint en valor por defecto (0) tampoco se serializa.
    if n == 0:
        return b""
    return tag(fn, 0) + vi(n)

def fld_m(fn, b):
    return tag(fn, 2) + vi(len(b)) + b

CW = {"CONTENT_WARNING_SAFE": 1, "CONTENT_WARNING_MIXED": 2, "CONTENT_WARNING_NSFW": 3, None: 1}

def source_pb(s, spec="nox"):
    b = fld_i(1, int(s["id"])) + fld_s(2, s.get("name", s.get("name", "")))
    b += fld_s(3, s.get("language", s.get("lang", "")))
    b += fld_s(4, s.get("homeUrl", s.get("baseUrl", "")))
    for u in s.get("mirrorUrls", []):
        b += fld_s(5, u)
    if s.get("message"):
        # El proto de la ORG (Awerkori/manga-fonte-extensoes/.github/scripts/index.proto,
        # linaje mihonapp/tachiyomix con jarUrl=501) pone Source.message en el campo 7;
        # el spec oficial de Aniyomi lo pone en el 6. Cada spec lleva el suyo.
        b += fld_s(7 if spec == "nox" else 6, s["message"])
    # versionId NO se codifica: en el proto comunitario el campo 6 de Source es
    # contentRating (enum SAFE=0..PORNOGRAPHIC=3); codificar versionId=1 ahi haria
    # que todo cliente leyera "CONTENT_RATING_SUGGESTIVE". El index de manga de
    # Nox no da ninguna evidencia de que versionId viaje en el pb: se omite.
    return b

def plugin_pb(e, cw_enum, spec="nox"):
    # spec "nox"  = variante viva del index.pb de Awerkori/manga-extensoes
    #               (sources=8, jarUrl=501, sin isTorrent): prueba dorada byte a byte.
    # spec "aniyomi" = spec oficial aniyomiorg/extensions-lib/index/index.proto
    #               (isTorrent=8, sources=9, Source.message=6, Resources sin 501):
    #               la que manda el skill Nox para el ecosistema anime (Yuzono).
    b = fld_s(1, e["name"]) + fld_s(2, e.get("packageName") or e.get("pkg"))
    res = e.get("resources")
    if res:
        r = fld_s(1, res["apkUrl"]) + fld_s(2, res["iconUrl"])
        if spec == "nox" and res.get("jarUrl"):
            r += fld_s(501, res["jarUrl"])
        b += fld_m(3, r)
    b += fld_s(4, e.get("extensionLib", ""))
    b += fld_i(5, int(e.get("versionCode", e.get("code", 0))))
    b += fld_s(6, e.get("versionName", e.get("version", "")))
    b += fld_i(7, cw_enum)
    if spec == "aniyomi" and (e.get("torrent") or e.get("isTorrent")):
        b += fld_i(8, 1)
    tag_src = 9 if spec == "aniyomi" else 8
    for s in e.get("sources", []):
        b += fld_m(tag_src, source_pb(s, spec))
    return b

def index_pb(meta, exts, cws, spec="nox"):
    b = fld_s(1, meta["name"]) + fld_s(2, meta["shortName"]) + fld_s(3, meta["signingKey"])
    b += fld_m(4, fld_s(1, meta["website"]))
    inner = b"".join(fld_m(1, plugin_pb(e, cw, spec)) for e, cw in zip(exts, cws))
    return b + fld_m(101, inner)

def gzip_exact(data, ref_header):
    co = zlib.compressobj(9, zlib.DEFLATED, -15)
    body = co.compress(data) + co.flush()
    out = ref_header + body
    out += zlib.crc32(data).to_bytes(4, "little") + (len(data) & 0xFFFFFFFF).to_bytes(4, "little")
    return out

def leer_repo(repo):
    p = pathlib.Path(repo)
    full = json.load(open(p / "index.json"))
    if isinstance(full, dict) and "extensionList" in full:
        meta = {"name": full["name"], "shortName": full["badgeLabel"],
                "signingKey": full["signingKey"], "website": full["contact"]["website"]}
        exts = full["extensionList"]["extensions"]
        cws = [CW.get(e.get("contentWarning"), 1) for e in exts]
    else:
        rj = json.load(open(p / "repo.json"))["meta"]
        meta = {"name": rj["name"], "shortName": rj["shortName"],
                "signingKey": rj["signingKeyFingerprint"], "website": rj["website"]}
        exts = full
        cws = [3 if e.get("nsfw") else 1 for e in exts]
    return meta, exts, cws

# --------------------------------------------------------------------------------------
# Compuerta de spec (FALLA-010, 2026-11-17)
#
# El PR Awerkori/anime-extensoes#3 se cerró sin fusionar porque el binario publicado llevaba
# Extension.sources en el campo 8 (esquema de la org / Nox Mangá) cuando los clientes Aniyomi
# esperan el 9. La primera revisión del PR llevaba el spec correcto; el segundo commit lo
# "corrigió" al proto de la org y esa corrección era la regresión. Verificado por bytes:
#   anime-index.pb              17.663 B  campos Extension [1..8]  326 fuentes  -> NOX
#   anime-index-spec-aniyomi.pb 17.664 B  campos Extension [1..7,9] 326 fuentes  -> ANIYOMI
#   index.pb de la rama index-pb del PR: idéntico byte a byte a anime-index.pb
#
# Lección: la intención no se verifica, los bytes sí. Esta compuerta lee el fichero YA ESCRITO
# y comprueba el número de campo real, y `generar` se niega a producir spec=nox para un
# repositorio consumido por clientes Aniyomi salvo orden explícita.
# --------------------------------------------------------------------------------------
CAMPO_SOURCES = {"nox": 8, "aniyomi": 9}
# Repos cuyos clientes son Aniyomi/Yuzono: el spec oficial es `aniyomi` (sources=9).
REPOS_ANIYOMI = ("anime-extensoes", "anime-fonte-extensoes", "anime-extensions")


def _varint(b, i):
    v = 0; sh = 0
    while True:
        x = b[i]; i += 1; v |= (x & 0x7F) << sh; sh += 7
        if not x & 0x80:
            return v, i


def _walk(b):
    i = 0; out = []
    while i < len(b):
        k, i = _varint(b, i); fn = k >> 3; wt = k & 7
        if wt == 0:
            v, i = _varint(b, i); out.append((fn, 0, v))
        elif wt == 2:
            ln, i = _varint(b, i); out.append((fn, 2, b[i:i + ln])); i += ln
        elif wt == 5:
            out.append((fn, 5, b[i:i + 4])); i += 4
        elif wt == 1:
            out.append((fn, 1, b[i:i + 8])); i += 8
        else:
            raise ValueError(f"wiretype {wt} en campo {fn} (offset {i})")
    return out


def spec_observado(ruta):
    """Devuelve (n_extensiones, campos_de_extension, spec_observado) leyendo los bytes."""
    b = pathlib.Path(ruta).read_bytes()
    raw = gzip.decompress(b) if b[:2] == b"\x1f\x8b" else b
    top = {f: v for f, w, v in _walk(raw) if w == 2}
    pay = top.get(101, b"")
    if pay[:2] == b"\x1f\x8b":
        pay = gzip.decompress(pay)
    exts = [v for f, w, v in _walk(pay) if f == 1]
    campos = set()
    for e in exts:
        campos |= {f for f, w, _ in _walk(e)}
    spec = "nox" if 8 in campos else "aniyomi" if 9 in campos else "?"
    return len(exts), sorted(campos), spec


def comprobar_spec(ruta, esperado=None):
    """Salida 0 si el fichero lleva el spec esperado; 1 si no. Imprime la evidencia."""
    n, campos, obs = spec_observado(ruta)
    linea = f"{ruta}: {n} extensiones · campos Extension {campos} · spec observado {obs}"
    if esperado is None:
        print(linea); return 0
    if obs == esperado:
        print("✓ " + linea + f" · coincide con lo pedido ({esperado})"); return 0
    print("✗ " + linea + f" · SE PIDIO {esperado} (campo sources={CAMPO_SOURCES[esperado]}) "
          f"Y EL FICHERO LLEVA sources={CAMPO_SOURCES.get(obs, '?')}")
    print("  Un cliente del otro ecosistema leería esas fuentes como campos desconocidos.")
    return 1


def repo_es_aniyomi(repo):
    return any(k in str(repo) for k in REPOS_ANIYOMI)


def main():
    modo = sys.argv[1]
    repo = pathlib.Path(sys.argv[2])
    if modo == "roundtrip":
        meta, exts, cws = leer_repo(repo)
        data = index_pb(meta, exts, cws)
        orig = (repo / "index.pb").read_bytes()
        header = orig[:10]
        mio = gzip_exact(data, header)
        print(f"original {len(orig)} B · generado {len(mio)} B · identicos: {mio == orig}")
        if mio != orig:
            do = gzip.decompress(orig)
            print(f"  descomprimidos: orig {len(do)} vs mio {len(data)} · iguales: {do == data}")
            if do != data:
                for i in range(min(len(do), len(data))):
                    if do[i] != data[i]:
                        print(f"  primera dif en byte {i}: orig {do[i-8:i+16]!r} vs mio {data[i-8:i+16]!r}")
                        break
        sys.exit(0 if mio == orig else 1)
    if modo == "generar":
        tagrel, salida = sys.argv[3], pathlib.Path(sys.argv[4])
        spec = sys.argv[5] if len(sys.argv) > 5 else "nox"
        meta, exts, cws = leer_repo(repo)
        for e in exts:
            if "resources" not in e:
                pkg = e.get("packageName") or e.get("pkg")
                if tagrel == "repo":
                    base = f"https://raw.githubusercontent.com/Awerkori/{repo.name}/repo/apk"
                    e["resources"] = {
                        "apkUrl": f"{base}/{e.get('apk')}",
                        "iconUrl": f"https://cdn.jsdelivr.net/gh/Awerkori/{repo.name}@repo/icon/{pkg}.png"}
                else:
                    base = f"https://github.com/Awerkori/{repo.name}/releases/download/{tagrel}"
                    e["resources"] = {
                        "apkUrl": f"{base}/{e.get('apk')}",
                        "jarUrl": f"{base}/{e.get('apk').replace('.apk', '.jar')}",
                        "iconUrl": f"https://cdn.jsdelivr.net/gh/Awerkori/{repo.name}@repo/icon/{pkg.split('.')[-1]}.png"}
            if not e.get("extensionLib"):
                v = e.get("version", "").split(".")
                e["extensionLib"] = v[0] if len(v) == 2 else ".".join(v[:2])
            if not e.get("versionCode"):
                v = [int(x) for x in e.get("version", "0.0.0").split(".")]
                lib = e["extensionLib"].split(".")
                lmaj, lmin = int(lib[0]), int(lib[1]) if len(lib) > 1 else 0
                e["versionCode"] = lmaj * 100000 + lmin * 1000 + int(e.get("code", 0))
        data = index_pb(meta, exts, cws, spec)
        header = bytes([0x1F, 0x8B, 0x08, 0x00, 0, 0, 0, 0, 0x02, 0x03])
        out = gzip_exact(data, header)
        if repo_es_aniyomi(repo) and spec == "nox" and "--forzar-nox" not in sys.argv:
            print(f"✗ NEGADO: {repo} lo consumen clientes Aniyomi, cuyo spec oficial es "
                  f"`aniyomi` (Extension.sources=9). Pediste spec=nox (sources=8), que es el "
                  f"esquema de la org/Nox Mangá y dejaría esas fuentes como campos desconocidos.")
            print("  Es exactamente el defecto que cerró Awerkori/anime-extensoes#3 (FALLA-010).")
            print("  Usa spec=aniyomi, o --forzar-nox si de verdad sabes lo que haces.")
            sys.exit(1)
        salida.write_bytes(out)
        print(f"generado {salida} · {len(out)} B · {len(exts)} extensiones · spec {spec} · gzip(deflate9, mtime=0)")
        rc = comprobar_spec(salida, spec)
        if rc:
            salida.unlink(missing_ok=True)
            print("  fichero retirado: lo escrito no coincide con el spec pedido")
        sys.exit(rc)
    if modo == "verificar-spec":
        # uso: verificar-spec <fichero.pb> [nox|aniyomi]
        sys.exit(comprobar_spec(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None))
    print("modo: roundtrip|generar|verificar-spec")
    sys.exit(2)

if __name__ == "__main__":
    main()
