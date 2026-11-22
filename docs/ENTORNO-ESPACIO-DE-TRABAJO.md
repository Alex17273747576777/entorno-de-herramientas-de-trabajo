# Configuración y preparación del espacio de trabajo

Guía reproducible para preparar una máquina o contenedor de trabajo sobre los repositorios de Alex17273747576777.

## Uso

```bash
# Comprobación de solo lectura y pruebas
make entorno

# Crear un informe JSON sin modificar el entorno
make entorno-reporte

# Perfil funcional: base, archivo, web, android o completo
bash bin/preparar-espacio-trabajo.sh --solo-verificar --perfil web --reporte-json /tmp/entorno.json

# Preparación local, identidad Git y sincronización de repos de un perfil
bash bin/preparar-espacio-trabajo.sh --perfil archivo --configurar-git --sincronizar /tmp/own-repos
```

## Perfiles y configuración

`entorno/repositorios.json` es la fuente única de repositorios. Los perfiles `archivo`, `web` y `android` sincronizan respectivamente `la-bandita-archivo`, `ruta-programacion-sistemas` y `normas-de-diseno`; `base` prepara solo este repositorio y `completo` incluye los cuatro. Las actualizaciones existentes usan `git pull --ff-only`; no se sobrescriben cambios divergentes.

## Validaciones

El script exige Python 3.11 o superior y Git; detecta `make`, `gcc`, `g++`, `node`, `curl`, `ruff`, `shellcheck` y Java, reportando su presencia o ausencia. Ejecuta `tests/pruebas.py` y la comprobación de copias, que admite el modo estricto para CI. Las herramientas adicionales son opcionales: el informe JSON indica las disponibles.

Por omisión, la preparación local aplica permisos restrictivos a credenciales existentes (`700` al directorio `~/.cerox-keys`, `600` a sus archivos y `~/.gh-credential`), sin mostrar su contenido. `--solo-verificar` no cambia permisos. `--configurar-git` configura identidad global Alex17273747576777; no toca credenciales ni remotos.

`--reporte-json ARCHIVO` crea directorios padre y genera un reporte con perfil, instante UTC y herramientas detectadas. No incluye valores secretos.
