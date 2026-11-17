# Ficha de auditoría — Reikai

Ruta auditada: `/var/tmp/referencias/Reikai`

## Eje 1 — manifiesto

- manifiestos: 16
- permisos distintos: 19
- componentes: 25 (7 exportados)
- sensibles (10): ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, WAKE_LOCK, WRITE_EXTERNAL_STORAGE

## Eje 2 — APIs usadas frente a permisos declarados

- fuentes analizadas: 2027
- permisos ejercidos en código: ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, WRITE_EXTERNAL_STORAGE
- ejercidos sólo en recursos XML (no en código): ninguno
- **permisos huérfanos** (declarados, sin uso detectado): WAKE_LOCK
- **usos sin permiso declarado**: CHANGE_WIFI_STATE, READ_EXTERNAL_STORAGE, READ_MEDIA_IMAGES

Que no aparezca la cadena no prueba que el permiso sobre: puede ejercerlo una
dependencia o un recurso XML. Y al revés: un uso sin declarar puede venir de un
manifiesto fusionado de otra biblioteca. Ambos se confirman leyendo, no grepando.

## Eje 3 — endpoints

- hosts distintos fuera del ruido: 77
- de su propia infraestructura: square.github.io, gist.github.com

| host | menciones |
|---|---:|
| `exhentai.org` | 7 |
| `e-hentai.org` | 6 |
| `kitsu.app` | 5 |
| `graphql.anilist.co` | 3 |
| `d.android.com` | 3 |
| `mysite.com` | 3 |
| `www.jitpack.io` | 2 |
| `square.github.io` | 2 |
| `shikimori.io` | 2 |
| `issuetracker.google.com` | 2 |
| `api.manga.com` | 2 |
| `imagecdn.manga.com` | 2 |

## Eje 4 — telemetría en dependencias

- ficheros de build analizados: 26
- **SDK que entran en el APK**: firebase-analytics, firebase-crashlytics
- sólo declarados en el catálogo de versiones (no entran): google-services
- aplicados dentro de un condicional (hay variante sin ellos): firebase-analytics, firebase-crashlytics

| SDK | qué es | dónde |
|---|---|---|
| `firebase-analytics` | analítica de Google | `gradle/libs.versions.toml:151` |
| `firebase-analytics` | analítica de Google | `telemetry/build.gradle.kts:28` |
| `firebase-crashlytics` | reporte de fallos de Google | `app/build.gradle.kts:3` |
| `firebase-crashlytics` | reporte de fallos de Google | `build.gradle.kts:14` |
| `firebase-crashlytics` | reporte de fallos de Google | `gradle/libs.versions.toml:153` |
| `firebase-crashlytics` | reporte de fallos de Google | `telemetry/build.gradle.kts:29` |
| `google-services` | plugin que cablea los servicios de Google | `gradle/libs.versions.toml:233` |

Cero coincidencias **no** prueba ausencia: un SDK puede llegar transitivo sin
dejar su nombre en un fichero de build. Probarlo exige el árbol de dependencias
resuelto, que sólo existe si el proyecto compila.
