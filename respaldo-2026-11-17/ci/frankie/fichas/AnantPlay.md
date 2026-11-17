# Ficha de auditoría — AnantPlay

Ruta auditada: `/var/tmp/referencias/android`

## Eje 1 — manifiesto

- manifiestos: 1
- permisos distintos: 12
- componentes: 14 (2 exportados)
- sensibles (8): FOREGROUND_SERVICE, INTERNET, POST_NOTIFICATIONS, RECEIVE_BOOT_COMPLETED, REQUEST_INSTALL_PACKAGES, SYSTEM_ALERT_WINDOW, WAKE_LOCK, WRITE_EXTERNAL_STORAGE

## Eje 2 — APIs usadas frente a permisos declarados

- fuentes analizadas: 37
- permisos ejercidos en código: FOREGROUND_SERVICE, INTERNET, POST_NOTIFICATIONS, REQUEST_INSTALL_PACKAGES, SYSTEM_ALERT_WINDOW, WAKE_LOCK, WRITE_EXTERNAL_STORAGE
- ejercidos sólo en recursos XML (no en código): ninguno
- **permisos huérfanos** (declarados, sin uso detectado): RECEIVE_BOOT_COMPLETED
- **usos sin permiso declarado**: ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, READ_EXTERNAL_STORAGE, READ_MEDIA_VIDEO, REQUEST_DELETE_PACKAGES

Que no aparezca la cadena no prueba que el permiso sobre: puede ejercerlo una
dependencia o un recurso XML. Y al revés: un uso sin declarar puede venir de un
manifiesto fusionado de otra biblioteca. Ambos se confirman leyendo, no grepando.

## Eje 3 — endpoints

- hosts distintos fuera del ruido: 23
- de su propia infraestructura: anantplay.github.io

| host | menciones |
|---|---:|
| `media.tenor.com` | 3 |
| `punchplay.tv` | 2 |
| `www.youtube.com` | 2 |
| `schemas.xmlsoap.org` | 2 |
| `anime-kitsu.strem.fun` | 2 |
| `arm.haglund.dev` | 2 |
| `host` | 2 |
| `api.simkl.com` | 1 |
| `simkl.com` | 1 |
| `site` | 1 |
| `phone` | 1 |
| `purl.org` | 1 |

## Eje 4 — telemetría en dependencias

- ficheros de build analizados: 0
- **SDK que entran en el APK**: ninguno
- sólo declarados en el catálogo de versiones (no entran): ninguno
- aplicados dentro de un condicional (hay variante sin ellos): ninguno


Cero coincidencias **no** prueba ausencia: un SDK puede llegar transitivo sin
dejar su nombre en un fichero de build. Probarlo exige el árbol de dependencias
resuelto, que sólo existe si el proyecto compila.
