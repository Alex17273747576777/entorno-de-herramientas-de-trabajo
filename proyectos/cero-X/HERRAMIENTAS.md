# cero-X · herramientas

Fuente canónica: [`cero-X-app`](https://github.com/Alex17273747576777/cero-X-app)
@ `2dc023ef5a72`, rama **`main`**. La divergencia que había con `main` **se fusionó y se
empujó el 2026-11-13** (PR #7, `merged=True`); el detalle histórico de esa divergencia y
de la fusión está en [`RESPALDOS.md`](RESPALDOS.md). Copiadas el 2026-11-13 y repuntadas a
`main` el mismo día. Licencia de la fuente: **GPL-3.0**, ver [`../LICENCIAS.md`](../LICENCIAS.md).

Los 6 ficheros espejados son byte a byte idénticos en el commit viejo de la rama
(`8d531c2`) y en `main` (`2dc023e`), medido con `git rev-parse <sha>:<ruta>`: el repunte
cambió la referencia de rama, no el contenido. Aun así se repuntó a `main` porque un
espejo «al día» con una rama congelada dice verdad hoy y se queda atrás sin avisar el día
que `main` cambie un fichero espejado (falla C7b del registro común).

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
cuatro 404 al montarlo: cuando se copió, las herramientas de cero-X **no existían en su
rama por defecto** (`main`), vivían sólo en `fases-verificadas-2026-11-13`, y por eso el
manifiesto declaraba esa rama. Tras la fusión del 2026-11-13 ya están en `main`, y el
manifiesto se repuntó a la rama viva (ver la nota de arriba y la falla C7b).

Cinco caminos medidos con ruptura deliberada, el código sin pipe: sano 0; copia editada
`DERIVA-INTERNA` 1; commit registrado falso `INFIEL` 1; espejo fiel a un commit viejo
`ANTIGUA` 1 en estricto y 0 con aviso sin él; sin red `COPIAS_PARCIALES` 3 en estricto y 0
diciendo qué no se comprobó. Tras el repunte a `main` el estado es el sano (0), no el
`ANTIGUA`: medido el 2026-11-13 con `--estricto-origen`, `COPIAS_OK … al día con main`.

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
- [`fallas/REGISTRO-DE-FALLAS.md`](fallas/REGISTRO-DE-FALLAS.md): 18 fallas reales y la comprobación que caza cada una.
- [`RESPALDOS.md`](RESPALDOS.md): divergencia con el remoto, copias en Drive con sus md5, y autenticación sin escribir el token en ningún sitio.
