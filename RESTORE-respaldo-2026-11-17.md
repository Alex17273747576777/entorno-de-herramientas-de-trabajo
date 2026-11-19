# Restauración del respaldo 2026-11-17

El árbol `respaldo-2026-11-17/` fue sustituido por el archivo comprimido
`respaldo-2026-11-17.tar.xz` para cumplir el límite de almacenamiento sin perder
su contenido: los SHA-256 de los 525 ficheros y los modos de todos los elementos
coincidieron con el árbol original. El archivo contiene 744 elementos, su
integridad se comprobó con `xz -t` y su hash es
`203d6871381b729c011b6da40b7647203276be4f02dc3508223abdabaec4bd36`
(lo coteja `respaldo-2026-11-17.tar.xz.sha256`).

Como el repositorio ya espeja ese blob (commit `b361f51`, rama `main`) y el
entorno tiene un límite de almacenamiento, no se conserva una copia suelta del
archivo en el disco; sigue disponible en `.git` y en el remoto. Para recuperar el
archivo exacto desde este repositorio:

```sh
git cat-file blob HEAD:respaldo-2026-11-17.tar.xz > respaldo-2026-11-17.tar.xz
sha256sum -c respaldo-2026-11-17.tar.xz.sha256
tar -xJpf respaldo-2026-11-17.tar.xz
```

Si el blob no estuviera en la rama local, el remoto lo conserva en
`origin/main` (o en el historial de commits anteriores).
