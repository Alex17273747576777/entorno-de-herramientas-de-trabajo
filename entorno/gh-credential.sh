#!/bin/sh
# Credential helper de Git. No contiene ningún secreto: lee la clave del único
# archivo que la tiene, /home/user/.cerox-keys/tokens.txt (modo 0600), y la
# devuelve sólo cuando Git la pide. Así el token no acaba en .git/config ni en
# la URL del remoto, que es lo que docs/POLITICA-DE-ALMACENAMIENTO.md prohíbe.
case "$1" in
  get) printf 'username=x-access-token\npassword=%s\n' \
         "$(grep -E '^GP=' /home/user/.cerox-keys/tokens.txt | head -1 | cut -d= -f2- | tr -d '\r\n')" ;;
esac
