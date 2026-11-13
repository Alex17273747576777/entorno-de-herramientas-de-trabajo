# cero-X · herramientas

Fuente canónica: `github.com/Alex17273747576777/cero-X-app` @ `c7191bf76bef`
(rama `fases-verificadas-2026-11-13`; `main` del remoto está en `1fdad35` y diverge).
Copiadas el 2026-11-13. Para comprobar que no derivaron:

```bash
./proyectos/cero-X/herramientas/comprobar-copias.sh   # COPIAS_OK o COPIAS_DERIVADAS, sale 1
```

| herramienta | bytes | sha256 (16 primeros) | para qué |
|---|---:|---|---|
| `latido.py` | 17681 | `c01767ea002f3cbc` | autoverificación del estado: árbol de Git, evidencia citada que exista, fechas de corte, pendientes con salida, identidad, toolchain, logs crudos, respaldos. Imprime `HEARTBEAT_OK` o clasifica en BLOQUEO y AVISO |
| `comprobar_entorno.py` | 3023 | `32cfd3daa7c607af` | presupuesto del workspace, JDK, SDK; imprime `ENTORNO_OK` |
| `preparar-entorno-android.sh` | 4899 | `38f86650d83c6074` | rearma JDK 21, SDK, build-tools, platform-tools y swap tras un reinicio del sandbox |
| `low-memory.gradle` | 479 | `a91d91bcce703473` | init script: heap de pruebas y `maven.repo.local` fuera del workspace para una máquina de 2 GiB |

`latido.py` es la pieza reutilizable: no sabe nada de Android. `comprobar-copias.sh`
no viene del proyecto, se escribió aquí, y es la contraparte de estas cuatro copias.
