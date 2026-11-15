# LEEME DEL ENTORNO DE TRABAJO — La Bandita

*Corte: noche del sábado 14 de noviembre de 2026 (UTC-4). Este es el lugar donde el trabajo
sobrevive a reinicios, timeouts y turnos: la meta-capa de la casa.*

## Qué hay aquí

- **`FALLAS-Y-CONTRAPARCHES.md`** — registro canónico: cada falla que tumba trabajo entra con
  síntoma, causa, contraparche y estado. Regla del dueño: registrar y contraparchear **antes**
  de proseguir.
- **`bin/checkpoint.sh`** — `bash bin/checkpoint.sh escribir|leer`. El checkpoint dice tarea,
  hecho y siguiente paso; el turno siguiente retoma de ahí, nunca de cero.
- **`bin/reaplicar-estructura.sh`** — reconstruye un clon nuevo desde el espejo en un mando
  (carpetas, herramientas, bandas, notas del CORAZON, overlay de sellos). Idempotente.
- **`moldes/`** — maestra 01 es-dominicano y master 01 en-ingles, medidos en vivo contra la API
  de GitHub y con firma 💓: el ejemplo de pieza buena aunque las publicaciones estén retiradas.

## Reglas de supervivencia (nacidas de fallas reales)

1. Al abrir turno: leer el checkpoint. Al cerrar hito: escribirlo.
2. `/var/tmp` se borra en cada reinicio: el clon no es persistencia. La persistencia es el
   espejo en `edt/proyectos/la-bandita-archivo/reestructura-idiomas/` y, cuando haya push
   (exige `GHP_A`), el remoto.
3. Todo fichero **nuevo** y toda **edición** se espejan el mismo turno (FALLA-003): las
   ediciones viven además como fichero propio en el espejo (notas del CORAZON, parches).
4. Las herramientas se invocan con `bash <ruta>`: los reinicios quitan el bit de ejecución.
5. Overlay de sellos con glob completo (`lote-*.*`), no por nombre (FALLA-004).
6. Sello local sólo con acta (CORAZON l.806); push sólo con `GHP_A`, que hoy no está.

## Relación con las capas de habilidades

- `SKILLS/` y `Arena-Reimagined/HABILIDADES/` guardan las habilidades de **oficio** (censo de
  pieza, cotejar cifras, envío por canal…).
- Este entorno guarda las habilidades de **supervivencia** (checkpoint, reaplicar) y el
  registro de fallas. Una habilidad nueva nacida de una falla entra en los dos lados: su
  carpeta en `SKILLS/` y su entrada en el registro de aquí.
