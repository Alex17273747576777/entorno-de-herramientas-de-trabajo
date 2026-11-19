# Restauración del respaldo 2026-11-17

El árbol `respaldo-2026-11-17/` fue sustituido por el archivo comprimido
`respaldo-2026-11-17.tar.xz` para cumplir el límite de almacenamiento sin perder
su contenido. El archivo se comprobó con `xz -t` y se extrajo a un directorio
volátil de verificación: los SHA-256 de los 525 ficheros y los modos de todos
los elementos coincidieron con el árbol original.

Verifica el archivo con `sha256sum -c respaldo-2026-11-17.tar.xz.sha256` y
restáuralo desde `work/edt` con `tar -xJpf respaldo-2026-11-17.tar.xz`.
