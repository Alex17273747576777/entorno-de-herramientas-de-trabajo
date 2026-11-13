# cero-X · herramientas

Fuente canónica: [`cero-X-app`](https://github.com/Alex17273747576777/cero-X-app)
@ `8bf07470dfe1`, rama **`fases-verificadas-2026-11-13`**. El `main` del remoto está en
`1fdad35` y **diverge**: los detalles y los 8 ficheros a mirar antes de fusionar están en
[`RESPALDOS.md`](RESPALDOS.md). Copiadas el 2026-11-13. Licencia de la fuente:
**GPL-3.0**, ver [`../LICENCIAS.md`](../LICENCIAS.md).

## Cómo se comprueba que no derivaron

```bash
./proyectos/comprobar-copias.sh                     # local: avisa si el espejo quedó atrás
./proyectos/comprobar-copias.sh --estricto-origen   # CI: antiguo o incomprobable = rojo
```

Salidas: `COPIAS_OK` 0 · `COPIAS_DERIVADAS` 1 · `COPIAS_SIN_MANIFIESTO` 2 ·
`COPIAS_PARCIALES` 0 con aviso y 3 en modo estricto · `COPIAS_ANTIGUAS` 0 con aviso y 1 en
modo estricto.

Los hashes viven en `herramientas/MANIFIESTO.sha256` y los genera `sha256sum`. La primera
versión de esta contraparte llevaba los hashes incrustados en el propio script, por
proyecto; se sustituyó por el comprobador general con manifiestos, que escala a proyectos
futuros y no repite código.

**Y esa segunda versión seguía contestando media pregunta** (falla C7 del registro):
comparaba las copias contra un manifiesto generado de esas mismas copias, así que sólo
cazaba a quien editaba la copia sin actualizar el manifiesto. El 2026-11-13 cuatro
herramientas de cero-X cambiaron en su repo, el espejo se quedó atrás y el script imprimió
`ok cero-X (6 ficheros sin derivar)` con EXIT=0. Ahora el manifiesto declara su origen en
comentarios —`# origen-repo:`, `# origen-rama:`, `# origen-commit:` y una
`# origen-ruta <copia>: <ruta>` por fichero, que `sha256sum -c --strict` ignora— y el
script descarga cada fichero por URL cruda de GitHub y contesta dos preguntas:

| | pregunta | si falla |
|---|---|---|
| FIEL | la copia == el fichero en el commit registrado | `INFIEL`, sale 1: la copia se editó aquí, o el commit anotado no es del que se copió |
| AL DÍA | la copia == el fichero en la punta de la rama | `ANTIGUA`, sale 1 en modo estricto y aviso sin él: hay que republicar |

Los repos son públicos, así que la comparación no necesita credencial. Detalle que costó
cuatro 404 al montarlo: las herramientas de cero-X **no existen en su rama por defecto**,
viven en `fases-verificadas-2026-11-13`, y por eso el manifiesto declara la rama.

Cinco caminos medidos con ruptura deliberada, el código sin pipe: sano 0; copia editada
`DERIVA-INTERNA` 1; commit registrado falso `INFIEL` 1; espejo fiel a un commit viejo
`ANTIGUA` 1 en estricto y 0 con aviso sin él —éste es el escenario de hoy—; sin red
`COPIAS_PARCIALES` 3 en estricto y 0 diciendo qué no se comprobó.

| fichero | bytes | sha256 | qué hace |
|---|---:|---|---|
| `LICENSE-de-origen.txt` | 35,149 | `3972dc9744f6499f` | GPL-3.0 de la fuente. Las copias siguen siendo GPL-3.0 aunque este repo no declare licencia |
| `NOTICE-de-origen.txt` | 6,784 | `c17bb886fd34f706` | aviso de la fuente, conservado junto a las copias |
| `comprobar_entorno.py` | 4,973 | `72a98183ac99ee6f` | presupuesto del workspace, JDK y SDK; imprime `ENTORNO_OK` |
| `latido.py` | 22,664 | `10443327b60c30f9` | autoverificación del estado del proyecto: árbol de Git, evidencia citada que exista, fechas de corte, pendientes con criterio de salida, y desde el 2026-11-13 también el remoto Git (`comprobar_remoto`: remoto existente, URL sin token embebido, helper ejecutable, alguna forma de autenticarse y rama con upstream), identidad, toolchain, logs crudos y respaldos. Imprime `HEARTBEAT_OK` o clasifica en `BLOQUEO` y `AVISO`. **No sabe nada de Android: es la pieza reutilizable** |
| `low-memory.gradle` | 563 | `8ee1d1754e429c8c` | init script: heap de pruebas y `maven.repo.local` fuera del workspace, para una máquina de 2 GiB |
| `preparar-entorno-android.sh` | 4,981 | `b32de7f5ffa53500` | rearma JDK 21, SDK, build-tools, platform-tools y swap tras un reinicio del sandbox |

## Dónde está el resto

- [`entorno/LIMITES-MEDIDOS.md`](entorno/LIMITES-MEDIDOS.md): qué no se puede hacer en el sandbox, con la medida de cada límite.
- [`entorno/RECETA-DE-REARME.md`](entorno/RECETA-DE-REARME.md): qué rearmar y en qué orden tras un reinicio.
- [`fallas/REGISTRO-DE-FALLAS.md`](fallas/REGISTRO-DE-FALLAS.md): 16 fallas reales y la comprobación que caza cada una.
- [`RESPALDOS.md`](RESPALDOS.md): divergencia con el remoto, copias en Drive con sus md5, y autenticación sin escribir el token en ningún sitio.
