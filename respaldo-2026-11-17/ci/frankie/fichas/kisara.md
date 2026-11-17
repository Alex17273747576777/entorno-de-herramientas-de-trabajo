# Ficha de auditoría — kisara

Ruta auditada: `/var/tmp/referencias/kisara`

## Eje 1 — manifiesto

- manifiestos: 15
- permisos distintos: 23
- componentes: 29 (7 exportados)
- sensibles (14): ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, MANAGE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, READ_EXTERNAL_STORAGE, READ_MEDIA_IMAGES, RECEIVE_BOOT_COMPLETED, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, WAKE_LOCK, WRITE_EXTERNAL_STORAGE

## Eje 2 — APIs usadas frente a permisos declarados

- fuentes analizadas: 2837
- permisos ejercidos en código: ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, MANAGE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, READ_EXTERNAL_STORAGE, READ_MEDIA_IMAGES, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, WAKE_LOCK, WRITE_EXTERNAL_STORAGE
- ejercidos sólo en recursos XML (no en código): ninguno
- **permisos huérfanos** (declarados, sin uso detectado): RECEIVE_BOOT_COMPLETED
- **usos sin permiso declarado**: CHANGE_WIFI_STATE, READ_MEDIA_VIDEO

Que no aparezca la cadena no prueba que el permiso sobre: puede ejercerlo una
dependencia o un recurso XML. Y al revés: un uso sin declarar puede venir de un
manifiesto fusionado de otra biblioteca. Ambos se confirman leyendo, no grepando.

## Eje 3 — endpoints

- hosts distintos fuera del ruido: 119
- de su propia infraestructura: komikku-app.github.io, square.github.io, github, gist.github.com, coil-kt.github.io

| host | menciones |
|---|---:|
| `komikku-app.github.io` | 15 |
| `huggingface.co` | 12 |
| `graphql.anilist.co` | 10 |
| `api.deepseek.com` | 7 |
| `exhentai.org` | 7 |
| `aniyomi.org` | 6 |
| `issuetracker.google.com` | 6 |
| `e-hentai.org` | 5 |
| `repo` | 5 |
| `kitsu.app` | 5 |
| `anilist.co` | 5 |
| `mysite.com` | 4 |

## Eje 4 — telemetría en dependencias

- ficheros de build analizados: 33
- **SDK que entran en el APK**: firebase-analytics, firebase-crashlytics
- sólo declarados en el catálogo de versiones (no entran): google-services
- aplicados dentro de un condicional (hay variante sin ellos): firebase-analytics, firebase-crashlytics

| SDK | qué es | dónde |
|---|---|---|
| `firebase-analytics` | analítica de Google | `gradle/libs.versions.toml:90` |
| `firebase-analytics` | analítica de Google | `telemetry/build.gradle.kts:26` |
| `firebase-crashlytics` | reporte de fallos de Google | `app/build.gradle.kts:19` |
| `firebase-crashlytics` | reporte de fallos de Google | `build.gradle.kts:11` |
| `firebase-crashlytics` | reporte de fallos de Google | `gradle/libs.versions.toml:91` |
| `firebase-crashlytics` | reporte de fallos de Google | `telemetry/build.gradle.kts:27` |
| `google-services` | plugin que cablea los servicios de Google | `gradle/libs.versions.toml:128` |

Cero coincidencias **no** prueba ausencia: un SDK puede llegar transitivo sin
dejar su nombre en un fichero de build. Probarlo exige el árbol de dependencias
resuelto, que sólo existe si el proyecto compila.
