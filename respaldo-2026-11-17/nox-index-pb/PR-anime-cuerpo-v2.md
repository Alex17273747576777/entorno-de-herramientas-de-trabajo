## Qué añade

- **`index.pb`** (nuevo, 17.663 B): el índice binario `index_v2` con las **272 extensiones** del `index.json` de la rama `repo`.
- **`repo.json`**: añade la clave `"index_v2"` apuntando a `https://raw.githubusercontent.com/Awerkori/anime-extensoes/repo/index.pb` (misma forma que ya usa `Awerkori/manga-extensoes`).

## Esquema: el proto de la propia organización

El formato canónico del ecosistema es `.github/scripts/index.proto` de **`Awerkori/manga-fonte-extensoes`** (linaje `mihonapp/tachiyomix`, con la divergencia `Resources.jarUrl = 501` declarada en el propio archivo): `Extension.sources = 8`, `Source.message = 7`, `ContentWarning {SAFE=1, MIXED=2, NSFW=3}`. Es el mismo proto con el que se genera el `index.pb` del repo hermano `manga-extensoes`, y por tanto el que esperan los clientes de la familia Nox.

*(La primera revisión de esta rama usó el spec de `aniyomiorg/extensions-lib` —`sources=9`—, que es incompatible con el proto de la casa. Corregido en el segundo commit.)*

## Serialización y verificación

- Idéntica a `publish-repo.py` de la org: protobuf `SerializeToString(deterministic=True)` + `gzip(mtime=0)`; cabecera XFL=2/OS=3 como el `index.pb` vivo de manga.
- **Paridad byte a byte con los bindings oficiales:** el payload descomprimido (101.811 B) coincide exactamente con el que produce `index_pb2.py` de `manga-fonte-extensoes` sobre los mismos datos.
- El conversor usado reproduce además **byte a byte** el `index.pb` oficial de `Awerkori/manga-extensoes` desde su `index.json` (127.828 B idénticos en la cabeza actual `64d2caef`): prueba dorada de fidelidad.
- proto3: los 4 `sources` con `baseUrl` vacío (`googledriveindex`, `jellyfin`×3) se omiten, como hace toda biblioteca protobuf.

## Reglas de URLs (el repo no publica releases; los APK viven en `apk/`)

- `apkUrl` = `https://raw.githubusercontent.com/Awerkori/anime-extensoes/repo/apk/<archivo>.apk`
- `iconUrl` = `https://cdn.jsdelivr.net/gh/Awerkori/anime-extensoes@repo/icon/<packageName>.png`
- sin `jarUrl` (0 de 272 jars en el árbol).
- `extensionLib` = «14» (primer componente de `versionName`); `versionCode` = libMaj·100000 + libMin·1000 + code del APK → 14·100000+0+11 = 1400011 (la misma aritmética del `index.pb` de manga: verificada contra sus 1.702 entradas, `versionCode % 1000 == code` en todas).
- `contentWarning`: `nsfw=1 → NSFW(3)`, `nsfw=0 → SAFE(1)`.

## Limitaciones honestas

- El `nsfw` del `index.json` de anime sólo distingue 0/1: `CONTENT_WARNING_MIXED` no es recuperable de ese dato fuente (en manga sí existe y se respeta).
- Ningún cliente real de la familia Nox ha cargado este `index.pb` todavía; la verificación es estructural, contra el proto de la org y contra sus bindings.
- `Source.message` y `mirrorUrls` van vacíos porque el `index.json` no trae esos datos.

Generado siguiendo el workflow de la skill `Awerkori/nox-extension-developer` (snapshots keiyoushi `86462af` / yuzono `cc462c8`, 2026-11-15) y las herramientas de la org (`index.proto`, `index_pb2.py`, `publish-repo.py` de `manga-fonte-extensoes`; `create-repo.py`/`merge-repo.py` de `anime-fonte-extensoes`).