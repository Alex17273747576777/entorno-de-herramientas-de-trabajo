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
proyectos/<nombre>/
  HERRAMIENTAS.md      qué aporta el proyecto, con sha256 y commit de origen
  herramientas/        copias de las herramientas reutilizables + su contraparte
  entorno/             qué se pierde al reiniciar, cómo se rearma, qué NO se puede hacer aquí
  fallas/              cada falla real, cómo se detectó y qué la caza ahora
  RESPALDOS.md         copias externas con hashes e identificadores
```

Dos reglas para lo que se copia aquí:

1. **La copia canónica vive en el proyecto.** Esto es un espejo para reutilizar, no
   la fuente. Por eso cada directorio `herramientas/` lleva su contraparte: un script
   que compara el sha256 de la copia contra el fijado en el manifiesto y sale con 1 si
   derivó. Un espejo que deriva en silencio miente dos veces.
2. **Ningún secreto entra aquí.** Ni tokens, ni claves, ni `google-services.json`, ni
   hashes de firma privados. Ver `docs/POLITICA-DE-ALMACENAMIENTO.md`.

## Proyectos actuales

| proyecto | repo | qué hay aquí |
|---|---|---|
| cero-X | [`cero-X-app`](https://github.com/Alex17273747576777/cero-X-app) | herramientas de verificación, límites medidos del sandbox, 16 fallas con contraparte, 3 respaldos |

Los proyectos futuros entran con la misma forma. Añadir uno es crear el directorio y
rellenar los cuatro bloques; si un bloque no aplica, se escribe por qué en vez de
dejarlo vacío: un hueco sin explicar no se distingue de un hueco sin hacer.
