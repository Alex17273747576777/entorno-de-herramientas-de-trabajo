#!/bin/sh
# Contraparte de las copias: verifica que ninguna herramienta copiada aquí haya
# derivado en silencio de la canónica. La copia canónica vive en el repo del
# proyecto; esto es un espejo para reutilizar, y un espejo que deriva miente.
# Fuente: github.com/Alex17273747576777/cero-X-app @ c7191bf76bef
set -e
cd "$(dirname "$0")"
fallos=0
if [ "$(sha256sum "latido.py" | cut -d" " -f1)" != "c01767ea002f3cbc493c5d6692fb9044d294e820b6a23d873b3c5a7419ea26c2" ]; then echo "  DERIVA: latido.py"; fallos=1; else echo "  ok  latido.py"; fi
if [ "$(sha256sum "comprobar_entorno.py" | cut -d" " -f1)" != "32cfd3daa7c607af6b1764af3d90873ca4f1584745d3eab954ef2e26b8a8b468" ]; then echo "  DERIVA: comprobar_entorno.py"; fallos=1; else echo "  ok  comprobar_entorno.py"; fi
if [ "$(sha256sum "low-memory.gradle" | cut -d" " -f1)" != "a91d91bcce703473d9789378d0b20a37a9334534281d89f65a914dab73d112c3" ]; then echo "  DERIVA: low-memory.gradle"; fallos=1; else echo "  ok  low-memory.gradle"; fi
if [ "$(sha256sum "preparar-entorno-android.sh" | cut -d" " -f1)" != "38f86650d83c607432848c739c817cf2e2b2f056e285b14dae2e5b99667cb5a1" ]; then echo "  DERIVA: preparar-entorno-android.sh"; fallos=1; else echo "  ok  preparar-entorno-android.sh"; fi
if [ "$fallos" -ne 0 ]; then echo "COPIAS_DERIVADAS"; exit 1; fi
echo "COPIAS_OK"
