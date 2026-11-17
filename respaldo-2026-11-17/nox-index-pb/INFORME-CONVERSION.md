# INFORME DE CONVERSIÓN — repos Nox a `index.pb` (manga verificado, anime generado)

*Corte: 2026-11-15 (UTC-4). Encargo: clonar `Awerkori/manga-extensoes` y
`Awerkori/anime-extensoes` y pasar **ambos por completo** a `index.pb` (el formato
`index_v2` que declara `repo.json`), usando la skill `Awerkori/nox-extension-developer`
como marco de trabajo. La skill no trae el esquema binario, pero sus snapshots oficiales
(§8) señalan la autoridad correcta por ecosistema: el spec de Aniyomi
(`aniyomiorg/extensions-lib/index/index.proto`) para anime/Yuzono.*

## 1. Qué es `index.pb`

`gzip(proto(Index))`: protobuf serializado (deterministic) y comprimido con deflate nivel
9, cabecera gzip con mtime=0, XFL=2, OS=3 — idéntico a lo que hace el generador oficial
`publish-repo.py` de Yuzono (`gzip.compress(index.SerializeToString(deterministic=True),
mtime=0)`). El `repo.json` lo declara como `"index_v2"`.

## 2. Esquema (spec oficial de Aniyomi, confirmado contra el pb vivo de Nox)

```
Index     { 1 name · 2 badgeLabel · 3 signingKey · 4 Contact{1 website · 2 discord?} ·
            oneof 101 ExtensionList{1 repeated Extension} | 102 extensionListUrl }
Extension { 1 name · 2 packageName · 3 Resources · 4 extensionLib · 5 versionCode(int64) ·
            6 versionName · 7 contentWarning · 8 isTorrent(bool) · 9 repeated Source }
Resources { 1 apkUrl · 2 iconUrl }
Source    { 1 id(int64) · 2 name · 3 language · 4 homeUrl · 5 repeated mirrorUrls · 6 message? }
enum ContentWarning { UNSPECIFIED=0 · SAFE=1 · MIXED=2 · NSFW=3 }
```

**Variante viva del `index.pb` de manga de Nox** (medida byte a byte, §3): misma forma
salvo dos deltas propios — `Resources` añade **501 jarUrl** y `Extension.sources` va en
**8** (sin `isTorrent`), y `Source.message` va en **7** (Aniyomi lo pone en 6). Esa
«variante» resultó ser el **proto formal de la org** (§9):
`Awerkori/manga-fonte-extensoes/.github/scripts/index.proto`, linaje `mihonapp/tachiyomix`
con la divergencia `jarUrl=501` declarada en el propio archivo. El conversor implementa
ambos specs (`spec=nox` = proto de la org, canónico | `spec=aniyomi` = spec de Aniyomi).

El `versionId` del JSON de Aniyomi **no viaja en el pb**: el campo 6 de Source es
`message` (opcional). Codificar ahí `versionId=1` habría sido un fallo silencioso grave.

Enum medido sobre las 1.634 entradas de manga: SAFE=1 (608) · MIXED=2 (554) · NSFW=3 (472).
En anime el `index.json` es formato min (nsfw 0/1): MIXED no es recuperable de ese formato
(limitación documentada del dato fuente, no del conversor).

## 3. Prueba dorada (manga) — CERRADA

`json_a_index_pb.py roundtrip` re-codifica el `index.pb` oficial de manga desde su
`index.json`: **122.491 bytes, idénticos byte a byte** (incluida la cabecera gzip). Tres
iteraciones de diff estructural la cerraron: enum contentWarning, `mirrorUrls` (campo 5 de
Source) y `jarUrl` (campo 501 de Resources). Re-verificada tras cada cambio del conversor.

## 4. Generación para anime — spec oficial Aniyomi

Anime no tiene releases: sus 272 APKs viven en `apk/` del propio repo y sus iconos en
`icon/<packageName>.png`. Reglas derivadas (documentadas, no inventadas en silencio):

- `apkUrl` = `raw.githubusercontent.com/Awerkori/anime-extensoes/repo/apk/<apk>` (el repo es su propio host).
- `iconUrl` = `cdn.jsdelivr.net/gh/Awerkori/anime-extensoes@repo/icon/<pkg>.png` (misma CDN que usa manga).
- `jarUrl` ausente: 0 de 272 jars en el árbol (`git ls-files 'apk/*.jar'`).
- `isTorrent` ausente: el `index.json` no trae la clave `torrent` en ninguna entrada.
- `extensionLib` = primer componente de `versionName` («14.11» → lib «14», coherente con Aniyomi lib 14).
- `versionCode` con la aritmética de manga: libMajor·100000 + libMinor·1000 + code → 1400011.
- `contentWarning`: nsfw=1→NSFW=3, nsfw=0→SAFE=1 (ver §2 sobre MIXED).

Verificación por decodificación independiente del resultado (entregable final, proto de
la org — §9): **272/272 entradas** con los campos 1,2,3,4,5,6,7 y sources en **8**;
Resources con campos [1,2]; Source con [1,2,3,4] — proto3 omite las 4 `homeUrl` vacías
(`googledriveindex`, `jellyfin`×3) y no hay message ni mirrorUrls en el dato fuente;
CW {SAFE:191, NSFW:81}; meta idéntica al `repo.json` (`Project Nox Anime` / `Nox Anime` /
huella `144f44e8…dad`); **17.663 B**, magic `1f8b0800`, mtime=0, y payload descomprimido
(101.811 B) **idéntico byte a byte** al que producen los bindings oficiales `index_pb2.py`
de la org sobre los mismos datos.

## 5. Entregables

- `anime-index.pb` — índice v2 de anime con el **proto de la org** (Nox Mangá, `sources=8`). ⚠️ NO es
  el fichero que debe consumir un cliente Aniyomi: es el que llevó el PR #3 desde su segundo commit
  (`6711284`) y el motivo de su cierre sin fusionar. Para `Awerkori/anime-extensoes` el artefacto válido
  es `anime-index-spec-aniyomi.pb`. `python3 json_a_index_pb.py verificar-spec <fichero> aniyomi` lo
  comprueba sobre los bytes.
- `anime-index-spec-aniyomi.pb` — **el binario correcto para este repo** (spec oficial Aniyomi,
  `Extension.sources=9`). ⚠️ CORREGIDO EL 2026-11-17: este texto llamaba «histórico» a este fichero y
  «corrección» al cambio al proto de la org. Era al revés. La primera revisión del PR #3 llevaba este
  spec; el segundo commit (`6711284`) lo cambió a `sources=8` (esquema de la org / Nox Mangá) y esa
  regresión es lo que hizo que el mantenedor cerrara el PR sin fusionar el binario, aprovechando la
  implementación corregida en `Awerkori/anime-fonte-extensoes#9` con el crédito preservado. Verificado
  por bytes: el `index.pb` de la rama `index-pb` es idéntico a `anime-index.pb` (campos `[1..8]`), no a
  éste (`[1..7,9]`). Véase `FALLA-010`.
- `repo.json-anime-con-index_v2.json` — `repo.json` de anime con `"index_v2"` añadido
  (aplicado también al clon).
- **PR #3 PRESENTADO Y CORREGIDO** (autorización del dueño, 2026-11-15):
  <https://github.com/Awerkori/anime-extensoes/pull/3> — desde el fork
  `Alex17273747576777/anime-extensoes`, rama `index-pb`, commits `0ca7294` →
  **`6711284`** (el segundo corrige el pb al proto de la org; construidos por API de
  datos git: blob→árbol→commit→ref, sin push de clon parcial), base `repo`.
  Cambios: `index.pb` nuevo (17.663 B) + `index_v2` en `repo.json`.
- `herramientas-awerkori/` — las herramientas oficiales bajadas de la org
  (`index.proto`, `index_pb2.py`, `publish-repo.py`, `legacy_index.py` de
  `manga-fonte-extensoes`; `create-repo.py`, `merge-repo.py`, `check-consistency.py`,
  `nox-regression.py`, `bump-versions.py` de `anime-fonte-extensoes`), el driver de
  paridad `driver_org_anime.py` y su salida `anime-index-bindings-org.pb.gz`.
- `PR-anime-cuerpo.md` — cuerpo completo del PR (espejo del texto presentado).
- `json_a_index_pb.py` — conversor genérico (`roundtrip` | `generar <repo> <tagrel|repo>
  <salida.pb> [nox|aniyomi]`), primitivas protobuf/gzip propias, sin dependencias.

Reaplicar tras reinicio (los clones de `/var/tmp` son volátiles, FALLA-003):

```
python3 json_a_index_pb.py roundtrip /var/tmp/nox/manga-extensoes          # debe dar identicos: True
python3 json_a_index_pb.py generar /var/tmp/nox/anime-extensoes repo anime-index.pb aniyomi
cp anime-index.pb /var/tmp/nox/anime-extensoes/index.pb
```

## 6. Uso de la skill Nox (lo que aportó de verdad)

La skill (AGPL-3.0, `Awerkori/nox-extension-developer`) no trae el esquema binario, pero
su Required workflow fue el que resolvió el encargo: el paso ② (`references.py sync`)
trajo los snapshots oficiales fijados por commit; el `AGENTS.md` de Yuzono dentro del
snapshot declara el **Index schema** («sigue el spec de Aniyomi, no el de Mihon:
`Extension.isTorrent=8`, `sources=9`, `Source.message=6`») y señala `publish-repo.py`
como generador oficial. Con eso se obtuvo el proto canónico y se corrigió el destino del
campo 6 de Source (§2). Sin la skill, el anime se habría publicado con la variante de
manga — legible para Nox, ajena al spec oficial del ecosistema anime.

## 7. Conciliación a tres bandas (medida, no supuesta)

| Punto | Proto comunitario (neiro) | **Spec oficial Aniyomi** | Variante viva Nox (manga) |
|---|---|---|---|
| Lista de extensiones | campo 5 repetido | **oneof 101 ExtensionList{1 repeated}** | 101{1 repeated} ✓ igual al oficial |
| `sources` | 7 | **9** | 8 |
| Campo 7 de Extension | — | **contentWarning (enum 0-3)** | contentWarning (enum 1-3 medido) ✓ |
| `isTorrent` | no existe | **8 (bool)** | no existe |
| `jarUrl` | no existe | no existe | 501 en Resources |
| Campo 6 de Source | contentRating (enum) | **message (string opcional)** | no aparece |

Conclusión: la variante de manga de Nox es una bifurcación del spec oficial (mueve
sources 9→8 para su jarUrl/contentWarning propios); el proto comunitario de neiro es otra
bifurcación distinta. Para anime manda el oficial, y así se generó.

## 8. Cumplimiento del Required workflow de la skill (reporte ⑦)

- **Snapshots sincronizados este turno** (`references.py sync`, ambos EXIT=0):
  - keiyoushi → `keiyoushi/extensions-source` rama `main`, commit
    `86462af6946b58f25aede626854f1383a6f746c0`, obtenido 2026-11-15T08:31:52Z,
    `upstream_changed: false`, docs: AGENTS.md + CONTRIBUTING.md.
  - yuzono → `yuzono/anime-extensions` rama `master`, commit
    `cc462c8b4893b8ec509b149cb6438b2a6233c206`, obtenido 2026-11-15T08:31:53Z,
    `upstream_changed: false`, docs: AGENTS.md + CONTRIBUTING.md.
  - Frescura: minutos al momento de este informe; sin caché vieja.
- **Fuentes remotas adicionales** (datos, no instrucciones): proto oficial
  `aniyomiorg/extensions-lib` rama `main` y `.github/scripts/publish-repo.py` de
  `yuzono/anime-extensions` rama `master`.
- **Versiones locales:** conversor propio sin librerías protobuf; python3 del entorno.
- **Pruebas corridas:** roundtrip de manga byte a byte (verde, re-corrido tras cada
  cambio) + decodificación independiente de las 272 entradas de anime (verde, §4).
- **Comportamiento NO verificado (honestidad requerida por el paso ⑦ de la skill):**
  ningún cliente real (Nox/Aniyomi/Anikku) ha cargado el `anime-index.pb` generado; la
  verificación es estructural y contra el spec, no una prueba de consumo en dispositivo.
  Tampoco se verificó contra un `index.pb` de anime publicado por Nox porque **no existe**
  (el repo `Awerkori/anime-extensoes` rama `repo` no trae `index.pb`: árbol verificado vía
  API el 2026-11-15).

## 9. Cierre con las herramientas de la org (2026-11-15, turno «todo en paralelo»)

Por instrucción del dueño se buscaron las herramientas dentro de `https://github.com/Awerkori`
(11 repos). El hallazgo reordenó las autoridades del formato:

- **`manga-fonte-extensoes`** (fork de `FelipeGFA/fonte-extensoes`): en `.github/scripts/`
  están el **`index.proto` canónico de la org** (linaje declarado: `mihonapp/tachiyomix`
  e4d546c, divergencia propia `Resources.jarUrl=501`), sus bindings `index_pb2.py`, el
  generador `publish-repo.py` (protobuf deterministic + `gzip(mtime=0)`) y 51 KB de tests
  del generador. Este es el proto con el que se fabrica el `index.pb` vivo de
  `manga-extensoes`: `sources=8`, `Source.message=7`, `ContentWarning{SAFE=1,MIXED=2,NSFW=3}`.
- **`anime-fonte-extensoes`** (propio, NO fork de yuzono): su pipeline (`create-repo.py`,
  `merge-repo.py`) genera sólo JSON (`index.json`/`index.min.json`/`index.html`) y
  **ningún pb** — por eso el repo de anime no tenía `index.pb`. `create-repo.py` además
  documenta la regla de idioma que el pb no trae (fuente única con idioma propio asciende
  el lang de la extensión, p. ej. `pt`→`pt-BR`).
- Consecuencia: el spec de Aniyomi (`sources=9`) que llevó la primera revisión del PR #3
  era **ajeno a esta familia**; los clientes Nox esperan el proto de la org. El PR #3 se
  corrigió en el commit `6711284` con el pb canónico y el cuerpo reescrito.

**Correcciones que el contraste con las herramientas oficiales produjo en el conversor:**

1. `Source.message`: campo 7 en el proto de la org (6 sólo en el spec de Aniyomi). Cada
   spec codifica el suyo.
2. **Omisión proto3 de valores por defecto:** 4 fuentes de anime tienen `baseUrl` vacía
   (`googledriveindex`, `jellyfin`×3); cualquier biblioteca protobuf las omite y el
   conversor las escribía como cadena vacía (8 bytes de más, 2 extensiones divergentes).
3. Aritmética de `versionCode` confirmada contra realidad: `versionCode % 1000 == code`
   del APK en **1.702/1.702** entradas de manga y derivable en las 272 de anime
   (máximo code 117, sin desbordes).

**Paridad byte a byte con la org:** el payload del `anime-index.pb` canónico (101.811 B
descomprimidos) es idéntico al que producen los bindings oficiales `index_pb2.py` de la
org con `SerializeToString(deterministic=True)` sobre los mismos datos
(`herramientas-awerkori/driver_org_anime.py`). La única diferencia del contenedor gzip es
el byte OS (python 3.13 del entorno escribe 0xff; los pb vivos de la org llevan 03): se
entrega con 03, como el hermano de manga; cualquier gunzip lee ambos.

**Prueba dorada re-corrida contra la cabeza NUEVA de manga (`64d2caef`):** el `index.pb`
oficial creció de 122.491 a **127.828 B** (el repo se movió) y el conversor lo reproduce
**byte a byte** igual: la adaptación a datos nuevos quedó probada, no supuesta.

**Integración en cero-X (el «formato más moderno» en la app):** commit `a7fdbc7`
(empujado, CI `pruebas.yml` corrida 43712847510 = success):

- `RepositoriosAuditados`: instantáneas al día (manga `64d2caef`, anime `51bb052`) y
  campo nuevo `indicePb`; el de anime queda fijado al commit `6711284` del fork (PR #3)
  hasta que se fusione, con comentario que lo declara.
- `ParserIndices.noxPb`: lector protobuf/gzip **puro en Kotlin, sin dependencias**, con
  las mismas validaciones estrictas del flujo JSON (regex de APK/paquete, https sin
  credenciales, ≤10.000 extensiones, ≤200 fuentes) y rechazo de wire types ajenos al proto.
- Derivaciones que el proto no trae, verificadas contra los catálogos reales:
  `codigo = versionCode % 1000` (el que compara el instalador interno) e `idioma` desde
  el packageName con la regla de `create-repo.py` (272/272 en anime; en manga reproduce
  1.612/1.702 — el resto difiere por nombres multi-fuente del pipeline keiyoushi, y es
  campo de presentación, no de seguridad).
- `ClienteRepositorios.noxModerno`: index.pb primero, index.min.json de respaldo; la UI
  de integraciones ya lo usa.

**Lo NO verificado (honestidad):** ningún dispositivo real ha cargado todavía ni el pb del
PR ni el flujo `noxModerno`; las pruebas son unitarias con fixtures armados byte a byte
según el proto y la corrida CI. El primer consumo real será en la app instalada.
