# Ficha de auditoría — Kiroku

Ruta auditada: `/var/tmp/referencias/Kiroku`

## Eje 1 — manifiesto

- manifiestos: 1
- permisos distintos: 21
- componentes: 72 (17 exportados)
- sensibles (13): ACCESS_NETWORK_STATE, BLUETOOTH_CONNECT, FOREGROUND_SERVICE, INTERNET, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, READ_EXTERNAL_STORAGE, RECEIVE_BOOT_COMPLETED, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, SCHEDULE_EXACT_ALARM, WAKE_LOCK, WRITE_EXTERNAL_STORAGE

## Eje 2 — APIs usadas frente a permisos declarados

- fuentes analizadas: 507
- permisos ejercidos en código: FOREGROUND_SERVICE, INTERNET, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, READ_EXTERNAL_STORAGE, RECEIVE_BOOT_COMPLETED, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, SCHEDULE_EXACT_ALARM, WAKE_LOCK, WRITE_EXTERNAL_STORAGE
- ejercidos sólo en recursos XML (no en código): ninguno
- **permisos huérfanos** (declarados, sin uso detectado): BLUETOOTH_CONNECT
- **usos sin permiso declarado**: USE_EXACT_ALARM

Que no aparezca la cadena no prueba que el permiso sobre: puede ejercerlo una
dependencia o un recurso XML. Y al revés: un uso sin declarar puede venir de un
manifiesto fusionado de otra biblioteca. Ambos se confirman leyendo, no grepando.

## Eje 3 — endpoints

- hosts distintos fuera del ruido: 58
- de su propia infraestructura: avatars.githubusercontent.com, square.github.io

| host | menciones |
|---|---:|
| `anilist.co` | 24 |
| `s4.anilist.co` | 15 |
| `myanimelist.net` | 8 |
| `www.youtube.com` | 6 |
| `api.jikan.moe` | 4 |
| `aniyomi.org` | 3 |
| `www.gradle.org` | 2 |
| `dns.google` | 2 |
| `cloudflare-dns.com` | 2 |
| `bit.ly` | 2 |
| `avatars.githubusercontent.com` | 2 |
| `gcore.jsdelivr.net` | 2 |

## Eje 4 — telemetría en dependencias

- ficheros de build analizados: 5
- **SDK que entran en el APK**: firebase-analytics, firebase-crashlytics, google-services
- sólo declarados en el catálogo de versiones (no entran): ninguno
- aplicados dentro de un condicional (hay variante sin ellos): ninguno

| SDK | qué es | dónde |
|---|---|---|
| `firebase-analytics` | analítica de Google | `app/build.gradle:117` |
| `firebase-crashlytics` | reporte de fallos de Google | `app/build.gradle:51` |
| `firebase-crashlytics` | reporte de fallos de Google | `build.gradle:21` |
| `google-services` | plugin que cablea los servicios de Google | `app/build.gradle:50` |

Cero coincidencias **no** prueba ausencia: un SDK puede llegar transitivo sin
dejar su nombre en un fichero de build. Probarlo exige el árbol de dependencias
resuelto, que sólo existe si el proyecto compila.
