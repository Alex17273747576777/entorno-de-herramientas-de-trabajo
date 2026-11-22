# Configuración y preparación del espacio de trabajo

Guía reproducible para preparar cualquier máquina o contenedor nuevo antes de trabajar sobre los repositorios propios (`entorno-de-herramientas-de-trabajo`, `la-bandita-archivo`, `ruta-programacion-sistemas` y `normas-de-diseno`).

## Uso rápido

```bash
# 1. Verificación en modo solo lectura (sin alterar permisos ni clonar)
make entorno

# 2. Preparar permisos locales (700/600 en credenciales) + sincronizar repos hermanos
bash bin/preparar-espacio-trabajo.sh --sincronizar /tmp/own-repos
```

## Qué valida `bin/preparar-espacio-trabajo.sh`

1. **Toolchain base:** `python3 >= 3.11` y `git` (más detección informativa de `make`, `gcc`, `g++`, `node`, `curl`).
2. **Higiene de credenciales locales:** fuerza `chmod 700` sobre `~/.cerox-keys` y `chmod 600` sobre los archivos de tokens locales sin imprimir secretos.
3. **Integridad del entorno:** ejecuta `tests/pruebas.py` y `./proyectos/comprobar-copias.sh` (o `--estricto-origen` si se solicita).
4. **Sincronización opcional (`--sincronizar DIR`):** clona o actualiza por `--ff-only` `ruta-programacion-sistemas`, `la-bandita-archivo` y `normas-de-diseno`.
