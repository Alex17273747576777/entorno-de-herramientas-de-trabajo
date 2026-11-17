# Ficha de auditoría — ShinKu

Ruta auditada: `/var/tmp/referencias/ShinKu`

## Eje 1 — manifiesto

- manifiestos: 11
- permisos distintos: 20
- componentes: 20 (6 exportados)
- sensibles (12): ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, RECEIVE_BOOT_COMPLETED, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, VIBRATE, WAKE_LOCK, WRITE_EXTERNAL_STORAGE

## Eje 2 — APIs usadas frente a permisos declarados

- fuentes analizadas: 1384
- permisos ejercidos en código: ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, WAKE_LOCK, WRITE_EXTERNAL_STORAGE
- ejercidos sólo en recursos XML (no en código): ninguno
- **permisos huérfanos** (declarados, sin uso detectado): RECEIVE_BOOT_COMPLETED
- **usos sin permiso declarado**: CHANGE_WIFI_STATE, READ_EXTERNAL_STORAGE, READ_MEDIA_IMAGES, READ_MEDIA_VIDEO

Que no aparezca la cadena no prueba que el permiso sobre: puede ejercerlo una
dependencia o un recurso XML. Y al revés: un uso sin declarar puede venir de un
manifiesto fusionado de otra biblioteca. Ambos se confirman leyendo, no grepando.

## Eje 3 — endpoints

- hosts distintos fuera del ruido: 83
- de su propia infraestructura: harrys-hq.github.io, square.github.io, gist.github.com, coil-kt.github.io

| host | menciones |
|---|---:|
| `harrys-hq.github.io` | 13 |
| `exhentai.org` | 7 |
| `issuetracker.google.com` | 6 |
| `mangadex.org` | 6 |
| `e-hentai.org` | 5 |
| `kitsu.app` | 5 |
| `mysite.com` | 3 |
| `api.openai.com` | 3 |
| `www.jitpack.io` | 2 |
| `square.github.io` | 2 |
| `youtrack.jetbrains.com` | 2 |
| `api.manga.com` | 2 |

## Eje 4 — telemetría en dependencias

- ficheros de build analizados: 24
- **SDK que entran en el APK**: firebase-analytics, firebase-crashlytics, google-services
- sólo declarados en el catálogo de versiones (no entran): ninguno
- aplicados dentro de un condicional (hay variante sin ellos): firebase-crashlytics, google-services

| SDK | qué es | dónde |
|---|---|---|
| `firebase-analytics` | analítica de Google | `app/build.gradle.kts:293` |
| `firebase-analytics` | analítica de Google | `gradle/libs.versions.toml:137` |
| `firebase-crashlytics` | reporte de fallos de Google | `app/build.gradle.kts:21` |
| `firebase-crashlytics` | reporte de fallos de Google | `build.gradle.kts:11` |
| `firebase-crashlytics` | reporte de fallos de Google | `gradle/libs.versions.toml:138` |
| `google-services` | plugin que cablea los servicios de Google | `app/build.gradle.kts:18` |
| `google-services` | plugin que cablea los servicios de Google | `gradle/libs.versions.toml:183` |

Cero coincidencias **no** prueba ausencia: un SDK puede llegar transitivo sin
dejar su nombre en un fichero de build. Probarlo exige el árbol de dependencias
resuelto, que sólo existe si el proyecto compila.
