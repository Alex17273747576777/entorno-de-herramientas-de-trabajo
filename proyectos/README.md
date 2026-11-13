# Proyectos · capa por proyecto del espacio de trabajo

*Abierta el 2026-11-13. El resto del repo sigue siendo la caja de herramientas de
La Bandita (`bin/`, `lib/`, `tests/`, `piezas/`, `muestras/`); esto no la mueve.*

Este repositorio dejó de ser sólo un sitio de publicación. Cada proyecto vivo tiene
aquí un directorio con lo que **no tiene casa en ningún otro sitio**: las recetas de
entorno, los límites medidos de la máquina, el registro de fallas con su contraparte
y el registro de respaldos. El código de cada proyecto vive en su propio repo, con su
propio historial y su propio CI; aquí vive lo que se pierde cuando un contenedor se
recicla.

## Convención

```
proyectos/
  comprobar-copias.sh  contraparte general: coherencia interna + comparación contra el repo de origen
  LICENCIAS.md         licencia medida de cada fuente y qué implica para las copias
  fallas-comunes/      las fallas del modo de trabajar, no de un proyecto
  <nombre>/
    HERRAMIENTAS.md      qué aporta el proyecto, con sha256 y commit de origen
    herramientas/        copias + MANIFIESTO.sha256 + licencia de origen
    entorno/             qué se pierde al reiniciar, cómo se rearma, qué NO se puede hacer aquí
    fallas/              cada falla real, cómo se detectó y qué la caza ahora
    RESPALDOS.md         copias externas con hashes e identificadores
```

Un proyecto entra con lo que aplique. Si un bloque no aplica, **se escribe por qué en vez
de dejarlo vacío**: un hueco sin explicar no se distingue de un hueco sin hacer. Los dos
registros sin copias (`bandwidth-hero-proxy2`, `la-bandita-archivo`) son el ejemplo: dicen
qué se midió y por qué no se copia nada.

Dos reglas para lo que se copia aquí:

1. **La copia canónica vive en el proyecto.** Esto es un espejo para reutilizar, no
   la fuente. Por eso cada directorio `herramientas/` lleva su `MANIFIESTO.sha256`, que
   declara de dónde viene (`# origen-repo/rama/commit` y una `# origen-ruta` por fichero),
   y `proyectos/comprobar-copias.sh` los recorre todos y contesta dos preguntas: si las
   copias son **fieles** al commit registrado y si están **al día** con la punta de la rama.
   Sale 1 si algo derivó o quedó atrás en modo estricto, **2 si no encontró ningún
   manifiesto** y 3 si en modo estricto no pudo comparar contra el origen, porque un
   comprobador que pasa por no tener nada que comprobar —o por no poder comprobarlo— es el
   mismo cero silencioso que las fallas que registra. Un espejo que deriva en silencio
   miente dos veces. Ver la falla C7: la versión anterior sólo contestaba la primera mitad.
2. **Ningún secreto entra aquí.** Ni tokens, ni claves, ni `google-services.json`, ni
   hashes de firma privados. Ver `docs/POLITICA-DE-ALMACENAMIENTO.md`.

## Proyectos actuales

|
| proyecto | repo | licencia medida | qué hay aquí |
|---|---|---|---|
| cero-X | [`cero-X-app`](https://github.com/Alex17273747576777/cero-X-app) | GPL-3.0 | 4 herramientas + licencia y aviso de origen, límites medidos del sandbox, receta de rearme, 16 fallas con contraparte, divergencia del remoto y 3 respaldos |
| gltools-reborn | [`gltools-reborn`](https://github.com/Alex17273747576777/gltools-reborn) | Apache-2.0 | 6 ficheros: censo del APK, auditoría de releases, preparación de firma, verificación de versión y sus dos tests (7 + 15 comprobaciones) |
| normas-de-diseno | [`normas-de-diseno`](https://github.com/Alex17273747576777/normas-de-diseno) | sin declarar | 5 procedimientos: censar catálogo, elegir y desmontar, cerrar tramo, incidencias, auditar reglas. Sus 3 tests no se copian y el motivo está medido |
| bandwidth-hero-proxy2 | [`bandwidth-hero-proxy2`](https://github.com/Alex17273747576777/bandwidth-hero-proxy2) | MIT | registro sin copias: sus 4 utilidades sólo tienen sentido dentro del proxy |
| la-bandita-archivo | [`la-bandita-archivo`](https://github.com/Alex17273747576777/la-bandita-archivo) | MIT | registro sin copias: 182 herramientas archivadas por etapas; se copiarán bajo demanda |

Además, dos ficheros que cruzan proyectos:

| ruta | qué |
|---|---|
| `LICENCIAS.md` | la licencia medida de cada fuente y qué implica para las copias. Este repo **sí** declara licencia desde el 2026-11-13: GPL-3.0 en `LICENSE`, la única compatible con copiar a la vez GPL-3.0, Apache-2.0 y MIT |
| `fallas-comunes/REGISTRO.md` | 7 fallas del modo de trabajar, no de un proyecto: el pipe que se come el código de salida, `pytest` recogiendo cero tests, un test copiado que ya no prueba nada |
| `comprobar-copias.sh` | la contraparte de todas las copias, con manifiestos por proyecto |

Los proyectos futuros entran con la misma forma: crear el directorio, copiar con
`MANIFIESTO.sha256` generado por `sha256sum` (nunca hashes transcritos a mano), declarar
el origen en la cabecera de comentarios y rellenar los bloques. `comprobar-copias.sh` los
recoge solo, sin que haya que registrarlos en ningún sitio; si un manifiesto no declara su
origen, lo dice como `SIN-ORIGEN` en vez de darlo por bueno.
