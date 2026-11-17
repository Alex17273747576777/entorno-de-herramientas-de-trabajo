# Ficha de auditoría — houri

Ruta auditada: `/var/tmp/referencias/houri`

## Eje 1 — manifiesto

- manifiestos: 17
- permisos distintos: 22
- componentes: 23 (7 exportados)
- sensibles (14): ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, MANAGE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, READ_EXTERNAL_STORAGE, READ_MEDIA_IMAGES, RECEIVE_BOOT_COMPLETED, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, WAKE_LOCK, WRITE_EXTERNAL_STORAGE

## Eje 2 — APIs usadas frente a permisos declarados

- fuentes analizadas: 1739
- permisos ejercidos en código: ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, MANAGE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, READ_EXTERNAL_STORAGE, READ_MEDIA_IMAGES, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, WAKE_LOCK, WRITE_EXTERNAL_STORAGE
- ejercidos sólo en recursos XML (no en código): ninguno
- **permisos huérfanos** (declarados, sin uso detectado): RECEIVE_BOOT_COMPLETED
- **usos sin permiso declarado**: CHANGE_WIFI_STATE, READ_MEDIA_VIDEO

Que no aparezca la cadena no prueba que el permiso sobre: puede ejercerlo una
dependencia o un recurso XML. Y al revés: un uso sin declarar puede venir de un
manifiesto fusionado de otra biblioteca. Ambos se confirman leyendo, no grepando.

## Eje 3 — endpoints

- hosts distintos fuera del ruido: 103
- de su propia infraestructura: komikku-app.github.io, square.github.io, gist.github.com, coil-kt.github.io

| host | menciones |
|---|---:|
| `ichigo.moe` | 16 |
| `komikku-app.github.io` | 13 |
| `www.idpf.org` | 9 |
| `issuetracker.google.com` | 8 |
| `huggingface.co` | 7 |
| `e-hentai.org` | 6 |
| `exhentai.org` | 5 |
| `www.anime-planet.com` | 5 |
| `kitsu.app` | 5 |
| `purl.org` | 4 |
| `mangadex.org` | 4 |
| `houri` | 4 |

## Eje 4 — telemetría en dependencias

- ficheros de build analizados: 40
- **SDK que entran en el APK**: firebase-analytics, firebase-crashlytics, google-services
- sólo declarados en el catálogo de versiones (no entran): ninguno
- aplicados dentro de un condicional (hay variante sin ellos): firebase-analytics, firebase-crashlytics, google-services

| SDK | qué es | dónde |
|---|---|---|
| `firebase-analytics` | analítica de Google | `gradle/libs.versions.toml:97` |
| `firebase-analytics` | analítica de Google | `telemetry/build.gradle.kts:25` |
| `firebase-crashlytics` | reporte de fallos de Google | `app/build.gradle.kts:19` |
| `firebase-crashlytics` | reporte de fallos de Google | `build.gradle.kts:11` |
| `firebase-crashlytics` | reporte de fallos de Google | `gradle/libs.versions.toml:98` |
| `firebase-crashlytics` | reporte de fallos de Google | `telemetry/build.gradle.kts:26` |
| `google-services` | plugin que cablea los servicios de Google | `app/build.gradle.kts:22` |
| `google-services` | plugin que cablea los servicios de Google | `gradle/libs.versions.toml:140` |

Cero coincidencias **no** prueba ausencia: un SDK puede llegar transitivo sin
dejar su nombre en un fichero de build. Probarlo exige el árbol de dependencias
resuelto, que sólo existe si el proyecto compila.
