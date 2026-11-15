#!/bin/bash
# Auditar las reglas: ¿están todas, se numeran sin saltos, y coincide el disco con el repositorio?
#
# Por qué existe: el 10-11-2026 el `git status` de `normas/` mostraba cuatro procedimientos con
# el permiso cambiado que nadie había revisado, no había remoto configurado y al disco le
# faltaban cuatro commits. Unas reglas que dicen «todo va al repositorio» mientras el repositorio
# local va por detrás son un adorno. Esto lo detecta en vez de confiar.
#
# Uso:  ./procedimientos/06-auditar-reglas.sh                    (desde la raíz de normas/)
#       REPO_PRODUCTO=/ruta/al/producto ./procedimientos/06-auditar-reglas.sh --estricto
# Sale 0 si todo cuadra; 1 si algo no.
set -uo pipefail

ESTRICTO=0
for a in "$@"; do [ "$a" = "--estricto" ] && ESTRICTO=1; done
FALLOS=0
SIN_COMPROBAR=0
fallo()         { printf '  ✗ %s\n' "$*"; FALLOS=$((FALLOS+1)); }
bien()          { printf '  ✓ %s\n' "$*"; }
no_comprobado() { printf '  · %s\n' "$*"; SIN_COMPROBAR=$((SIN_COMPROBAR+1)); }
paso()          { printf '\n▸ %s\n' "$*"; }

paso "Las reglas están escritas y numeradas"
REGLAS=REGLAS-OBLIGATORIAS.md
[ -f "$REGLAS" ] || { fallo "no existe $REGLAS"; exit 1; }
NUMEROS=$(grep -oP '^## \K\d+(?=\.)' "$REGLAS" | tr '\n' ' ')
CUANTAS=$(echo "$NUMEROS" | wc -w)
ESPERADOS=$(seq -s ' ' 1 "$CUANTAS")
if [ "$(echo "$NUMEROS" | sed 's/ *$//')" = "$(echo "$ESPERADOS" | sed 's/ *$//')" ]; then
  bien "$CUANTAS reglas, numeradas 1..N sin saltos"
else
  fallo "la numeración tiene saltos: [$NUMEROS]"
fi

paso "Cada regla tiene quien la vigile"
grep -q "03-cerrar-tramo.sh" "$REGLAS" && bien "regla 1 · la limpieza la hace el cierre" \
  || fallo "regla 1 sin procedimiento"
PROD="${REPO_PRODUCTO:-}"
if [ -n "$PROD" ] && [ -d "$PROD/.github" ]; then
  grep -rq "version_actual.py" "$PROD/.github/scripts" 2>/dev/null \
    && bien "regla 2 · el CI compara la versión del APK con build.gradle" \
    || fallo "regla 2 sin comprobación automática"
  grep -q "verificar_version.py" "$PROD/.github/workflows/version.yml" 2>/dev/null \
    && bien "regla 3 · no se publica sin verificar el APK" || fallo "regla 3 sin puerta"
else
  no_comprobado "reglas 2 y 3 · falta REPO_PRODUCTO (el del producto, no éste)"
fi
if [ -d /opt/android-sdk ]; then
  fallo "regla 10 · hay SDK local: se estaría compilando aquí"
else
  bien "regla 10 · sin SDK local, la compilación es en la nube"
fi
BASURA=$(find "$HOME" -maxdepth 1 \( -name "uploads" -o -name "appteka" -o -name "*.png" \
  -o -name "*.jpg" -o -name "*.apk" \) 2>/dev/null | wc -l)
[ "$BASURA" -eq 0 ] && bien "regla 11 · el espacio de trabajo sólo tiene credenciales" \
  || fallo "regla 11 · hay $BASURA cosas que no son credenciales en \$HOME"

paso "El disco y el repositorio coinciden"
if git rev-parse --git-dir >/dev/null 2>&1; then
  git fetch -q origin 2>/dev/null || true
  REMOTO=$(git remote get-url origin 2>/dev/null || echo "")
  if [ -z "$REMOTO" ]; then
    fallo "regla 12 · sin remoto: lo que se cambie aquí no va a ninguna parte"
  else
    bien "regla 12 · remoto: $REMOTO"
    # El token no puede viajar dentro de la URL del remoto.
    case "$REMOTO" in *"@"*"x-access-token"*|*ghp_*|*github_pat_*) fallo "regla 12 · el token está dentro de la URL del remoto" ;; esac
    SUCIO=$(git status --porcelain | wc -l)
    [ "$SUCIO" -eq 0 ] && bien "regla 12 · sin cambios sin subir" \
      || fallo "regla 12 · hay $SUCIO cambios sin subir"
    ATRAS=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo 0)
    [ "$ATRAS" -eq 0 ] && bien "regla 12 · al día con el repositorio" \
      || fallo "regla 12 · faltan $ATRAS commits del repositorio en el disco"
  fi
  MALOS=$(git diff --summary | grep -c "mode change 100755 => 100644" || true)
  [ "$MALOS" -eq 0 ] && bien "permisos de los scripts como en el repositorio" \
    || fallo "$MALOS scripts han perdido el permiso de ejecución (¿core.fileMode?)"
else
  fallo "esto no es un repositorio git"
fi

printf '\n'
if [ "$ESTRICTO" -eq 1 ] && [ "$SIN_COMPROBAR" -gt 0 ]; then
  echo "REGLAS: $SIN_COMPROBAR comprobación(es) sin hacer y se exigían (--estricto)"; exit 1
fi
if [ "$FALLOS" -eq 0 ]; then echo "REGLAS: sin fallos ($SIN_COMPROBAR sin comprobar)"; exit 0; fi
echo "REGLAS: $FALLOS fallo(s), $SIN_COMPROBAR sin comprobar"; exit 1
