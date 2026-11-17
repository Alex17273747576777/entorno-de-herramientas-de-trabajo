# Respaldo de emergencia · 2026-11-17 16:05Z

**Por qué existe este directorio.** Se vació el espacio de trabajo por orden del dueño (74 MB en
`/home/user`, 1,7 GB en `/var/tmp`, 147 MB en `/tmp`), conservando sólo `work/cero-X-app`,
`work/edt` y el llavero `.cerox-keys/tokens.txt`. Todo lo que había en repos git ya estaba publicado
y verificado contra GitHub antes de borrar —`local == remoto` en los seis frentes—, así que no se
perdió nada de eso.

**Lo que sí se habría perdido para siempre** son estos diez directorios de trabajo, que **no son
repos git ni tenían copia en ningún sitio**, más las dos guías de la raíz. Se copiaron aquí antes de
borrar, y este repo (`entorno-de-herramientas-de-trabajo`) se empuja a GitHub, que es el disco según
la política de la casa.

Cada entrada está descrita por lo que **contiene de verdad** (listado generado al respaldar, no de
memoria).

## `ai-107-respaldo/` · 6 ficheros · 44,417 B · huella del conjunto `2d3ccb488789d3db`
Extensiones: `.kt`×4, `.patch`×1, `.md`×1
Primeros ficheros (orden alfabético):
- `cambios.patch`
- `nuevos/docs/ASISTENTE-Y-COMPETENCIA.md`
- `nuevos/modules/aihub/ClienteChat.kt`
- `nuevos/modules/aihub/CredencialesChat.kt`
- `nuevos/tests/ClienteChatTest.kt`
- `nuevos/ui/ia/AsistenteChat.kt`

## `auditoria-apks/` · 1 ficheros · 103,438 B · huella del conjunto `4570d8e16c94650f`
Extensiones: `.apk`×1
Primeros ficheros (orden alfabético):
- `mangadex.apk`

## `biblioteca-masiva/` · 19 ficheros · 113,325 B · huella del conjunto `8281bdfc682c755c`
Extensiones: `.txt`×6, `.py`×4, `.md`×3, `.kt`×3, `.patch`×3
Primeros ficheros (orden alfabético):
- `ISSUE-ANIZEN-BIBLIOTECA.md`
- `ISSUE-SHINKU-BIBLIOTECA.md`
- `LEEME.md`
- `mediciones/Arnes.kt`
- `mediciones/Log.kt`
- `mediciones/Medida.kt`

## `ci/` · 190 ficheros · 2,979,474 B · huella del conjunto `33e3cb6fba0453f8`
Extensiones: `.gz`×99, `.json`×26, `.txt`×25, `.md`×15, `.tsv`×7, `.log`×6
Primeros ficheros (orden alfabético):
- `.gradle/8.11.1/checksums/checksums.lock`
- `.gradle/8.11.1/fileChanges/last-build.bin`
- `.gradle/8.11.1/fileHashes/fileHashes.lock`
- `.gradle/8.11.1/gc.properties`
- `.gradle/buildOutputCleanup/buildOutputCleanup.lock`
- `.gradle/buildOutputCleanup/cache.properties`

## `feed-novedades/` · 70 ficheros · 456,192 B · huella del conjunto `f2d294406e0d2640`
Extensiones: `.kt`×50, `.md`×6, `.sq`×6, `.patch`×3, `(sin)`×2, `.txt`×1
Primeros ficheros (orden alfabético):
- `COMO-APLICAR.md`
- `ISSUE-ANIZEN.md`
- `ISSUE-SHINKU.md`
- `PLAN-FEED-SHINKU-ANIZEN.md`
- `VERIFICACION-SIMBOLOS.md`
- `codigo/anizen/LICENSE`

## `gltools/` · 39 ficheros · 178,714 B · huella del conjunto `be3c06475a806374`
Extensiones: `.kt`×14, `.png`×5, `.md`×4, `(sin)`×4, `.gradle`×3, `.xml`×3
Primeros ficheros (orden alfabético):
- `.gitattributes`
- `.gitignore`
- `LICENSE`
- `PROBADO.md`
- `PROCEDENCIA.md`
- `README.md`

## `guias/` · 2 ficheros · 27,580 B · huella del conjunto `d55c206a43ff7aa2`
Extensiones: `.md`×2
Primeros ficheros (orden alfabético):
- `guia-programacion-de-novato-a-experto.md`
- `guia-suite-adobe-a-codigo-abierto.md`

## `latest/` · 32 ficheros · 2,961,273 B · huella del conjunto `8b615700673f9b8a`
Extensiones: `.py`×17, `.png`×11, `.json`×2, `.md`×1, `.kt`×1
Primeros ficheros (orden alfabético):
- `cerox-investigacion/LEEME.md`
- `cerox-investigacion/comentarios-retirados.json`
- `cerox-investigacion/h_commit.py`
- `cerox-investigacion/h_fix.py`
- `cerox-investigacion/h_fix2.py`
- `cerox-investigacion/i_commit.py`

## `nox-index-pb/` · 24 ficheros · 190,788 B · huella del conjunto `bd8c11449c71b000`
Extensiones: `.py`×10, `.md`×3, `.sh`×2, `.pb`×2, `.log`×1, `.txt`×1
Primeros ficheros (orden alfabético):
- `INFORME-CONVERSION.md`
- `PR-anime-cuerpo-v2.md`
- `PR-anime-cuerpo.md`
- `SHA-PR-ANIME.txt`
- `anime-index-spec-aniyomi.pb`
- `anime-index.pb`

## `referencias/` · 118 ficheros · 686,594 B · huella del conjunto `d17dafae45bada27`
Extensiones: `.kt`×55, `.java`×29, `.lock`×6, `.bin`×6, `.properties`×5, `.txt`×3
Primeros ficheros (orden alfabético):
- `ExtensionManager.kt`
- `JarExtensionManager.kt`
- `Page-host.kt`
- `inventario.txt`
- `kisara-app-build.gradle.kts`
- `kisara-libs.versions.toml`

## `vm/` · 23 ficheros · 307,671 B · huella del conjunto `e62d88476962e0f6`
Extensiones: `.txt`×15, `.sh`×3, `.png`×2, `.log`×2, `.md`×1
Primeros ficheros (orden alfabético):
- `env.sh`
- `evidence/RESUMEN.md`
- `evidence/adb-version.txt`
- `evidence/android-responde.txt`
- `evidence/arranque-intento2.log`
- `evidence/arranque.txt`

---

**Total: 524 ficheros · 8,049,466 B (7.7 MB).**

## Escaneo de secretos antes de publicar

`grep -rlE "ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}"` sobre este directorio, sobre los diez
originales y sobre los `.git/config` de lo conservado: **0 coincidencias**. El llavero vive fuera de
todo repositorio, en `/home/user/.cerox-keys/tokens.txt`, y sus permisos se corrigieron en esta misma
ronda de `644` a **`600`** (directorio a `700`): estaban en 644 otra vez tras un reinicio, que es
exactamente lo que describe FALLA-006.

**Aviso al dueño:** los ocho tokens se pegaron en el chat durante esta orden, así que están en el
registro de la conversación. El archivo local coincide con lo pegado (mismas ocho claves, mismas
longitudes y huellas). Si ese registro es visible para alguien más, lo prudente es **revocar y
regenerar** los cuatro distintos —`GP_EXPLORA_1/2/3` (= `GHP_A/B/C`) y `GP` (= `GP2`)—; yo no puedo
revocarlos desde aquí.

## Lo que NO se respaldó, y por qué

- **Los clones de repos** (`/var/tmp/propios/{gltools-reborn,normas-de-diseno}`,
  `/var/tmp/la-bandita-archivo`, `/var/tmp/feed/shinku`, `/var/tmp/reikai`, `work/gltools` como clon):
  todo estaba publicado y verificado contra GitHub, o es un repo ajeno re-clonable.
- **El toolchain** (`/var/tmp/jdk` 499 MB, `/var/tmp/kc*` 436 MB, `/var/tmp/jars`, `/tmp/ktlint`
  69 MB, `/tmp/yi` con yarn): se reconstruye con `entorno/restaurar-toolchain-kotlin.sh`, y las
  recetas que ese guion no cubre están escritas en `proyectos/feed-novedades/pr37/KTLINT-COMO-ORACULO.md`
  (ktlint 1.8.0) y `proyectos/cero-X/HERRAMIENTAS.md` (yarn 1.22.22 con `npm install yarn` en `/tmp/yi`,
  porque `corepack enable` da EACCES sin root).
- **`/tmp/arena-workspace`**: es de la plataforma, no mío.
