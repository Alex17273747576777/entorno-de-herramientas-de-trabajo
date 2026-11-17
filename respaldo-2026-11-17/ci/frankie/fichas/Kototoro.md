# Ficha de auditoría — Kototoro

Ruta auditada: `/var/tmp/referencias/Kototoro`

## Eje 1 — manifiesto

- manifiestos: 16
- permisos distintos: 24
- componentes: 96 (20 exportados)
- sensibles (13): ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, MANAGE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, RECEIVE_BOOT_COMPLETED, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, VIBRATE, WAKE_LOCK, WRITE_EXTERNAL_STORAGE

## Eje 2 — APIs usadas frente a permisos declarados

- fuentes analizadas: 3485
- permisos ejercidos en código: ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, MANAGE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, WAKE_LOCK, WRITE_EXTERNAL_STORAGE
- ejercidos sólo en recursos XML (no en código): ninguno
- **permisos huérfanos** (declarados, sin uso detectado): RECEIVE_BOOT_COMPLETED
- **usos sin permiso declarado**: CHANGE_WIFI_STATE, READ_EXTERNAL_STORAGE, READ_MEDIA_IMAGES

Que no aparezca la cadena no prueba que el permiso sobre: puede ejercerlo una
dependencia o un recurso XML. Y al revés: un uso sin declarar puede venir de un
manifiesto fusionado de otra biblioteca. Ambos se confirman leyendo, no grepando.

## Eje 3 — endpoints

- hosts distintos fuera del ruido: 173
- de su propia infraestructura: keiyoushi.github.io, maven.pkg.github.com, gist.github.com, codeload.github.com, models.github.ai

| host | menciones |
|---|---:|
| `huggingface.co` | 41 |
| `opencollective.com` | 17 |
| `shikimori.io` | 16 |
| `anilist.co` | 15 |
| `api.mangaupdates.com` | 13 |
| `schemas.xmlsoap.org` | 12 |
| `api.simkl.com` | 12 |
| `api.myanimelist.net` | 10 |
| `www.modelscope.cn` | 10 |
| `api.bgm.tv` | 9 |
| `kitsu.app` | 9 |
| `myanimelist.net` | 8 |

## Eje 4 — telemetría en dependencias

- ficheros de build analizados: 42
- **SDK que entran en el APK**: acra
- sólo declarados en el catálogo de versiones (no entran): ninguno
- aplicados dentro de un condicional (hay variante sin ellos): ninguno

| SDK | qué es | dónde |
|---|---|---|
| `acra` | reporte de fallos abierto (ACRA) | `app/src/main/AndroidManifest.xml:444` |
| `acra` | reporte de fallos abierto (ACRA) | `gradle/libs.versions.toml:133` |

Cero coincidencias **no** prueba ausencia: un SDK puede llegar transitivo sin
dejar su nombre en un fichero de build. Probarlo exige el árbol de dependencias
resuelto, que sólo existe si el proyecto compila.
