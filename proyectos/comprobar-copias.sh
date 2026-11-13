#!/bin/sh
# Contraparte general de las copias de herramientas.
#
# La copia canónica de cada herramienta vive en el repo de su proyecto. Esto es un
# espejo para reutilizar, y un espejo que deriva en silencio miente dos veces: dice
# que la herramienta hace lo que hacía y ya no lo hace.
#
# HAY DOS PREGUNTAS DISTINTAS Y LA VERSIÓN ANTERIOR SÓLO CONTESTABA MEDIA.
#
#   Interna: ¿las copias casan con los hashes de su propio MANIFIESTO.sha256?
#   Origen:  ¿casan con el fichero del repo de origen?
#
# La interna es auto-referencial: el manifiesto se generó de las propias copias, así
# que sólo caza a quien edita la copia sin actualizar el manifiesto. El 2026-11-13 se
# midió el fallo: cuatro herramientas de cero-X habían cambiado en su repo, el espejo
# se quedó atrás y este script imprimió «ok cero-X (6 ficheros sin derivar)» con
# EXIT=0. Decía la verdad sobre la pregunta interna y mentía sobre la única que
# importaba. Es la falla 7 del registro.
#
# Por eso cada MANIFIESTO.sha256 declara su origen en comentarios (`# origen-repo:`,
# `# origen-rama:`, `# origen-commit:` y una línea `# origen-ruta <copia>: <ruta>` por
# fichero; sha256sum -c --strict ignora los comentarios) y este script descarga cada
# fichero del origen por URL cruda de GitHub y lo compara. Los repos son públicos, así
# que no hace falta credencial.
#
# Del origen se contestan dos cosas:
#   FIEL    la copia == el fichero en el commit registrado  → nadie adulteró el espejo
#   AL DÍA  la copia == el fichero en la punta de la rama   → el espejo no quedó atrás
#
# Salidas:
#   0  todo casa y está al día
#   1  deriva interna, o copia infiel al commit registrado, o (con --estricto-origen)
#      copia antigua respecto a la punta de la rama
#   2  no se encontró NINGÚN manifiesto: que un comprobador pase porque no había nada
#      que comprobar es el mismo cero silencioso que las fallas 1-5 del registro
#   3  con --estricto-origen, el origen no se pudo comparar (sin red, sin curl o sin
#      declarar el origen). Sin esa bandera se imprime SIN-ORIGEN y se sale 0, pero
#      diciendo explícitamente que la comparación no se hizo: un verde que no dice qué
#      comprobó es un verde hueco.
#
# Uso:
#   ./proyectos/comprobar-copias.sh                     # local: avisa si quedó atrás
#   ./proyectos/comprobar-copias.sh --estricto-origen   # CI: antiguo o incomprobable = rojo
set -u
ESTRICTO=0
for argumento in "$@"; do
    if [ "$argumento" = "--estricto-origen" ]; then ESTRICTO=1; fi
done

cd "$(dirname "$0")/.."
CRUDO="https://raw.githubusercontent.com"
TMP="${TMPDIR:-/tmp}/copias.$$"
mkdir -p "$TMP"
trap 'rm -rf "$TMP"' EXIT INT TERM

manifiestos=0; ficheros=0; internas=0; infieles=0; antiguas=0; sin_origen=0; al_dia=0

sha256_de() { sha256sum "$1" 2>/dev/null | cut -d' ' -f1; }

# Abreviar un SHA a 12 caracteres para los mensajes. Contar signos de interrogación en
# una expansión de parámetro es frágil y no se ve mal hasta que imprime basura.
corto() { echo "$1" | cut -c1-12; }

for m in proyectos/*/herramientas/MANIFIESTO.sha256; do
    [ -f "$m" ] || continue
    manifiestos=$((manifiestos + 1))
    proyecto=$(echo "$m" | cut -d/ -f2)
    dir="proyectos/$proyecto/herramientas"

    # 1) Coherencia interna.
    if (cd "$dir" && sha256sum -c --strict MANIFIESTO.sha256) >"$TMP/interna" 2>&1; then
        n=$(grep -c ': OK$' "$TMP/interna" 2>/dev/null) || n=0
        ficheros=$((ficheros + n))
    else
        echo "  DERIVA-INTERNA $proyecto: las copias no casan con su propio manifiesto"
        sed 's/^/               /' "$TMP/interna"
        internas=$((internas + 1))
        continue
    fi

    # 2) Contra el origen.
    repo=$(sed -n 's/^# origen-repo: //p' "$m" | head -1)
    rama=$(sed -n 's/^# origen-rama: //p' "$m" | head -1)
    commit=$(sed -n 's/^# origen-commit: //p' "$m" | head -1)
    if [ -z "$repo" ] || [ -z "$commit" ]; then
        echo "  SIN-ORIGEN $proyecto: el manifiesto no declara '# origen-repo:' y '# origen-commit:'"
        echo "               → sin eso sólo se puede comprobar coherencia interna, que no detecta"
        echo "                 que el espejo quedó atrás. Declarar repo, rama, commit y origen-ruta."
        sin_origen=$((sin_origen + 1))
        continue
    fi
    if ! command -v curl >/dev/null 2>&1; then
        echo "  SIN-ORIGEN $proyecto: no hay curl en este equipo"
        echo "               → coherencia interna comprobada; la comparación con $repo NO se hizo."
        sin_origen=$((sin_origen + 1))
        continue
    fi
    punta=""
    if [ -n "$rama" ]; then
        if curl -fsSL --max-time 30 -o "$TMP/punta" "$CRUDO/$repo/$rama/README.md" 2>/dev/null; then
            punta="$rama"
        fi
    fi

    infiel=0; antiguo=0; comparados=0
    rutas=$(grep '^# origen-ruta ' "$m" 2>/dev/null) || rutas=""
    if [ -z "$rutas" ]; then
        echo "  SIN-ORIGEN $proyecto: declara el commit pero ninguna línea '# origen-ruta copia: ruta'"
        sin_origen=$((sin_origen + 1))
        continue
    fi
    OLDIFS=$IFS
    IFS='
'
    for linea in $rutas; do
        IFS=$OLDIFS
        copia=$(echo "$linea" | sed 's/^# origen-ruta \([^:]*\): .*/\1/' | sed 's/ *$//')
        ruta=$(echo "$linea" | sed 's/^# origen-ruta [^:]*: //')
        [ -f "$dir/$copia" ] || { echo "  INFIEL   $proyecto/$copia: declarada en el manifiesto y no existe"; infiel=$((infiel+1)); continue; }
        if ! curl -fsSL --max-time 30 -o "$TMP/f" "$CRUDO/$repo/$commit/$ruta" 2>/dev/null; then
            echo "  SIN-ORIGEN $proyecto/$copia: no se pudo descargar $repo@$commit:$ruta"
            echo "               → ¿el commit o la ruta están mal? ¿el fichero vive en otra rama?"
            sin_origen=$((sin_origen + 1))
            continue
        fi
        comparados=$((comparados + 1))
        if [ "$(sha256_de "$TMP/f")" != "$(sha256_de "$dir/$copia")" ]; then
            echo "  INFIEL   $proyecto/$copia: no casa con $repo@$(corto "$commit")$ruta"
            echo "               → la copia se editó aquí, o el commit registrado no es el que se copió."
            infiel=$((infiel + 1))
        elif [ -n "$punta" ]; then
            if curl -fsSL --max-time 30 -o "$TMP/p" "$CRUDO/$repo/$punta/$ruta" 2>/dev/null; then
                if [ "$(sha256_de "$TMP/p")" != "$(sha256_de "$dir/$copia")" ]; then
                    echo "  ANTIGUA  $proyecto/$copia: fiel al commit registrado, pero el origen avanzó"
                    echo "               → republicar desde $repo ($rama:$ruta) y anotar el commit nuevo."
                    antiguo=$((antiguo + 1))
                fi
            else
                echo "  SIN-PUNTA $proyecto/$copia: no se pudo leer la punta de '$rama' (¿rama renombrada o borrada?)"
                sin_origen=$((sin_origen + 1))
            fi
        fi
    done
    IFS=$OLDIFS

    infieles=$((infieles + infiel))
    if [ "$infiel" -ne 0 ]; then
        echo "  x        $proyecto: $infiel fichero(s) infiel(es) al commit registrado"
    elif [ "$antiguo" -ne 0 ]; then
        antiguas=$((antiguas + antiguo))
        echo "  ANTIGUA  $proyecto ($comparados comparados: fieles a $(corto "$commit") pero $antiguo quedó atrás de la rama)"
    elif [ -z "$punta" ]; then
        echo "  ok       $proyecto ($comparados fieles al commit registrado; punta de la rama no comprobada)"
        sin_origen=$((sin_origen + 1))
    else
        al_dia=$((al_dia + 1))
        echo "  ok       $proyecto ($comparados ficheros: internos, fieles a $(corto "$commit") y al día con $rama)"
    fi
done

if [ "$manifiestos" -eq 0 ]; then
    echo "COPIAS_SIN_MANIFIESTO: no hay ningún proyectos/*/herramientas/MANIFIESTO.sha256 que comprobar"
    echo "  Eso no es un éxito. Si se esperaba encontrar copias, el recorrido está roto."
    exit 2
fi
if [ "$internas" -ne 0 ] || [ "$infieles" -ne 0 ]; then
    echo "COPIAS_DERIVADAS: $manifiestos manifiestos, $ficheros hashes internos, $internas con deriva interna, $infieles ficheros infieles al origen"
    exit 1
fi
if [ "$antiguas" -ne 0 ]; then
    if [ "$ESTRICTO" -eq 1 ]; then
        echo "COPIAS_ANTIGUAS: $antiguas fichero(s) fieles a su commit registrado pero detrás de la rama"
        echo "  En modo estricto eso es rojo: el espejo existe para reutilizar la herramienta, y una"
        echo "  herramienta de hace tres commits no es la herramienta. Republicar y anotar el commit nuevo."
        exit 1
    fi
    echo "COPIAS_ANTIGUAS: $antiguas fichero(s) detrás de su rama (fieles al commit registrado)"
    echo "  AVISO, no error: sin --estricto-origen se informa y se sale 0. La comparación contra el"
    echo "  origen SÍ se hizo, así que esto no es el verde hueco de antes; es un espejo que hay que repasar."
    exit 0
fi
if [ "$sin_origen" -ne 0 ]; then
    echo "COPIAS_PARCIALES: $manifiestos manifiestos, $ficheros hashes internos, pero $sin_origen comprobación(es) contra el origen NO se pudieron hacer"
    if [ "$ESTRICTO" -eq 1 ]; then
        echo "  En modo estricto eso es rojo: un verde que no dice qué comprobó es un verde hueco."
        exit 3
    fi
    echo "  AVISO, no error: sin --estricto-origen se sale 0 diciendo qué falta. La coherencia interna"
    echo "  sí se comprobó; la comparación con el repo de origen no."
    exit 0
fi
echo "COPIAS_OK: $manifiestos manifiestos, $ficheros hashes internos, $al_dia proyecto(s) comparados contra su origen y al día"
