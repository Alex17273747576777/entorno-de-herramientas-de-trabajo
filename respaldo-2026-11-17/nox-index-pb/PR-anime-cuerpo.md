## Qué añade

- **`index.pb`** (nuevo, 17.664 B): el índice binario `index_v2` con las **272 extensiones** del `index.json` de la rama `repo`.
- **`repo.json`**: añade la clave `"index_v2"` apuntando a `https://raw.githubusercontent.com/Awerkori/anime-extensoes/repo/index.pb` (misma forma que ya usa `Awerkori/manga-extensoes`).

## Cómo se generó

- Esquema: **spec oficial de Aniyomi** (`aniyomiorg/extensions-lib/index/index.proto`), el mismo que documenta el `AGENTS.md` de `yuzono/anime-extensions` para el índice (`Extension.isTorrent=8`, `sources=9`, `Source.message=6`).
- Serialización: protobuf deterministic + `gzip` (deflate 9, `mtime=0`, XFL=2, OS=3) — idéntica a `publish-repo.py` de Yuzono.
- Reglas de URLs (el repo no publica releases; los APK viven en `apk/`):
  - `apkUrl` = `https://raw.githubusercontent.com/Awerkori/anime-extensoes/repo/apk/<archivo>.apk`
  - `iconUrl` = `https://cdn.jsdelivr.net/gh/Awerkori/anime-extensoes@repo/icon/<packageName>.png`
  - sin `jarUrl` (0 de 272 jars en el árbol) y sin `isTorrent` (la clave `torrent` no aparece en ninguna entrada del `index.json`).
- `extensionLib` = primer componente de `versionName` («14.11» → «14»); `versionCode` = libMajor·100000 + libMinor·1000 + code del JSON.
- `contentWarning`: `nsfw=1 → CONTENT_WARNING_NSFW(3)`, `nsfw=0 → CONTENT_WARNING_SAFE(1)`.

## Verificación

- Decodificación independiente del pb generado: **272/272 entradas** con `name`, `packageName`, `resources`, `extensionLib`, `versionCode`, `versionName`, `contentWarning` y `sources` (campo 9); `contentWarning` {SAFE: 191, NSFW: 81}; meta idéntica al `repo.json` (nombre, badgeLabel, huella `144f44e8…dad`).
- El conversor usado reproduce **byte a byte** el `index.pb` oficial de `Awerkori/manga-extensoes` desde su `index.json` (122.491 B idénticos, incluida la cabecera gzip): prueba dorada de que la serialización es fiel.

## Limitaciones honestas

- El `nsfw` del `index.json` de anime sólo distingue 0/1: `CONTENT_WARNING_MIXED` no es recuperable de ese dato fuente (en manga sí existe y el conversor lo respeta).
- Ningún cliente real (Nox/Aniyomi/Anikku) ha cargado este `index.pb` todavía; la verificación es estructural y contra el spec oficial.
- `Source.message` y `mirrorUrls` van vacíos porque el `index.json` no trae esos datos.

Generado siguiendo el workflow de la skill `Awerkori/nox-extension-developer` (snapshots oficiales keiyoushi `86462af` / yuzono `cc462c8`, 2026-11-15).