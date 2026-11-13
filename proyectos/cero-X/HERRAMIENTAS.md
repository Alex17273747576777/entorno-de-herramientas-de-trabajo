# cero-X · herramientas

Fuente canónica: [`cero-X-app`](https://github.com/Alex17273747576777/cero-X-app)
@ `8bf07470dfe1`, rama **`fases-verificadas-2026-11-13`**. El `main` del remoto está en
`1fdad35` y **diverge**: los detalles y los 8 ficheros a mirar antes de fusionar están en
[`RESPALDOS.md`](RESPALDOS.md). Copiadas el 2026-11-13. Licencia de la fuente:
**GPL-3.0**, ver [`../LICENCIAS.md`](../LICENCIAS.md).

## Cómo se comprueba que no derivaron

```bash
./proyectos/comprobar-copias.sh    # COPIAS_OK · COPIAS_DERIVADAS (sale 1) · COPIAS_SIN_MANIFIESTO (sale 2)
```

Los hashes viven en `herramientas/MANIFIESTO.sha256` y los genera `sha256sum`. La primera
versión de esta contraparte llevaba los hashes incrustados en el propio script, por
proyecto; se sustituyó por el comprobador general con manifiestos, que escala a proyectos
futuros y no repite código.

| fichero | bytes | sha256 | qué hace |
|---|---:|---|---|
| `LICENSE-de-origen.txt` | 35,149 | `3972dc9744f6499f` | GPL-3.0 de la fuente. Las copias siguen siendo GPL-3.0 aunque este repo no declare licencia |
| `NOTICE-de-origen.txt` | 6,784 | `c17bb886fd34f706` | aviso de la fuente, conservado junto a las copias |
| `comprobar_entorno.py` | 3,023 | `32cfd3daa7c607af` | presupuesto del workspace, JDK y SDK; imprime `ENTORNO_OK` |
| `latido.py` | 17,681 | `c01767ea002f3cbc` | autoverificación del estado del proyecto: árbol de Git, evidencia citada que exista, fechas de corte, pendientes con criterio de salida, identidad, toolchain, logs crudos y respaldos. Imprime `HEARTBEAT_OK` o clasifica en `BLOQUEO` y `AVISO`. **No sabe nada de Android: es la pieza reutilizable** |
| `low-memory.gradle` | 479 | `a91d91bcce703473` | init script: heap de pruebas y `maven.repo.local` fuera del workspace, para una máquina de 2 GiB |
| `preparar-entorno-android.sh` | 4,899 | `38f86650d83c6074` | rearma JDK 21, SDK, build-tools, platform-tools y swap tras un reinicio del sandbox |

## Dónde está el resto

- [`entorno/LIMITES-MEDIDOS.md`](entorno/LIMITES-MEDIDOS.md): qué no se puede hacer en el sandbox, con la medida de cada límite.
- [`entorno/RECETA-DE-REARME.md`](entorno/RECETA-DE-REARME.md): qué rearmar y en qué orden tras un reinicio.
- [`fallas/REGISTRO-DE-FALLAS.md`](fallas/REGISTRO-DE-FALLAS.md): 16 fallas reales y la comprobación que caza cada una.
- [`RESPALDOS.md`](RESPALDOS.md): divergencia con el remoto, copias en Drive con sus md5, y autenticación sin escribir el token en ningún sitio.
