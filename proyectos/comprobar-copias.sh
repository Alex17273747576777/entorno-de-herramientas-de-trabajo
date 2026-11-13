#!/bin/sh
# Contraparte general de las copias de herramientas.
#
# La copia canónica de cada herramienta vive en el repo de su proyecto. Esto es un
# espejo para reutilizar, y un espejo que deriva en silencio miente dos veces: dice
# que la herramienta hace lo que hacía y ya no lo hace.
#
# Cada proyectos/<p>/herramientas/ trae su MANIFIESTO.sha256. Este script los recorre
# y verifica con sha256sum -c --strict. Sale 0 si todo casa, 1 si algo derivó o falta,
# y 2 si no encontró NINGÚN manifiesto: que un comprobador pase porque no había nada
# que comprobar es el mismo cero silencioso que las fallas 1-5 del registro.
#
# Uso: ./proyectos/comprobar-copias.sh   (o make copias)
set -u
cd "$(dirname "$0")/.."
derivadas=0; manifiestos=0; ficheros=0
for m in proyectos/*/herramientas/MANIFIESTO.sha256; do
    [ -f "$m" ] || continue
    manifiestos=$((manifiestos + 1))
    proyecto=$(echo "$m" | cut -d/ -f2)
    (cd "proyectos/$proyecto/herramientas" && sha256sum -c --strict MANIFIESTO.sha256 >/tmp/copias.$$ 2>&1)
    rc=$?
    n=$(grep -c ': OK$' /tmp/copias.$$ 2>/dev/null || echo 0)
    ficheros=$((ficheros + n))
    if [ "$rc" -eq 0 ]; then
        echo "  ok       $proyecto ($n ficheros sin derivar)"
    else
        echo "  DERIVA   $proyecto"
        sed 's/^/             /' /tmp/copias.$$
        derivadas=$((derivadas + 1))
    fi
    rm -f /tmp/copias.$$
done
if [ "$manifiestos" -eq 0 ]; then
    echo "COPIAS_SIN_MANIFIESTO: no hay ningún proyectos/*/herramientas/MANIFIESTO.sha256 que comprobar"
    echo "  Eso no es un éxito. Si se esperaba encontrar copias, el recorrido está roto."
    exit 2
fi
if [ "$derivadas" -ne 0 ]; then
    echo "COPIAS_DERIVADAS: $derivadas proyecto(s) de $manifiestos"
    exit 1
fi
echo "COPIAS_OK: $manifiestos manifiestos, $ficheros ficheros verificados"
