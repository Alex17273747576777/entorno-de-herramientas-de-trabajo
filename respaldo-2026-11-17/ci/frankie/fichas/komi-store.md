# Ficha de auditoría — komi-store

Ruta auditada: `/var/tmp/referencias/komi-store`

## Eje 1 — manifiesto

- manifiestos: 29
- permisos distintos: 11
- componentes: 9 (2 exportados)
- sensibles (7): FOREGROUND_SERVICE, INTERNET, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, RECEIVE_BOOT_COMPLETED, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES

## Eje 2 — APIs usadas frente a permisos declarados

- fuentes analizadas: 1240
- permisos ejercidos en código: FOREGROUND_SERVICE, INTERNET, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, RECEIVE_BOOT_COMPLETED, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES
- ejercidos sólo en recursos XML (no en código): ninguno
- **permisos huérfanos** (declarados, sin uso detectado): ninguno
- **usos sin permiso declarado**: READ_MEDIA_IMAGES, READ_MEDIA_VIDEO

Que no aparezca la cadena no prueba que el permiso sobre: puede ejercerlo una
dependencia o un recurso XML. Y al revés: un uso sin declarar puede venir de un
manifiesto fusionado de otra biblioteca. Ambos se confirman leyendo, no grepando.

## Eje 3 — endpoints

- hosts distintos fuera del ruido: 36
- de su propia infraestructura: github-store.org, api.github-store.org, github.moeyy.xyz, uploads.github.com, objects.githubusercontent.com

| host | menciones |
|---|---:|
| `repo1.maven.org` | 1417 |
| `dl.google.com` | 725 |
| `codeberg.org` | 8 |
| `github-store.org` | 7 |
| `cdn.simpleicons.org` | 5 |
| `fastly.jsdelivr.net` | 4 |
| `ghfast.top` | 4 |
| `komistore.app` | 3 |
| `avatar` | 3 |
| `translate.disroot.org` | 3 |
| `api.github-store.org` | 2 |
| `gh-proxy.com` | 2 |

## Eje 4 — telemetría en dependencias

- ficheros de build analizados: 49
- **SDK que entran en el APK**: ninguno
- sólo declarados en el catálogo de versiones (no entran): ninguno
- aplicados dentro de un condicional (hay variante sin ellos): ninguno


Cero coincidencias **no** prueba ausencia: un SDK puede llegar transitivo sin
dejar su nombre en un fichero de build. Probarlo exige el árbol de dependencias
resuelto, que sólo existe si el proyecto compila.
