# Diagnóstico de la integración continua propia · 2026-11-17

**Hora real al empezar:** `Tue, 17 Nov 2026 23:23:30 GMT` leída de la cabecera `Date:` de
`api.github.com` (no del reloj del sandbox). En Santo Domingo, UTC−4: **19:23:30 del martes
17-nov-2026**. Desvío del reloj del sandbox contra esa cabecera: **35 segundos**. Hasta hoy el
desvío medido era de unas 3,5 horas; ya no. Sigue sin fiarse de él: la hora se pide fuera.

**Ventana auditada:** últimos 7 días, o sea desde 2026-11-10 23:23Z.

**Por qué existe este documento:** una auditoría contra la API en vivo —no contra la memoria ni
contra el verde local— destapó que **cuatro repositorios propios estaban en rojo** mientras el
parte del turno anterior decía «verificado». Ver `FALLAS-Y-CONTRAPARCHES.md`, FALLA-015.

---

## 1. Los cuatro frentes rojos, con la causa medida

| repo | flujo | estado antes | última corrida | paso fallido | causa raíz (medida, no supuesta) |
|---|---|---|---|---|---|
| `entorno-de-herramientas-de-trabajo` | `pruebas` | 6 de 6 en `failure` | `44122394723` sobre `bd22fec6` | `Run ./proyectos/comprobar-copias.sh --estricto-origen` | **exit 126**: el fichero estaba commiteado en modo `100644` y el flujo lo invoca como `./…` |
| `normas-de-diseno` | `procedimientos` | 6 de 6 en `failure` | `44079202112` sobre `fe45074d` | `Auditar las reglas (numeración, vigías y sincronía)` | **exit 126**: mismo motivo, `procedimientos/06-auditar-reglas.sh` en `100644` |
| `la-bandita-archivo` | `vara` | `failure` desde el 15-nov; último verde `42869190307` sobre `4d257e9c` (10-nov) | `44084212035` sobre `bfaa811b` | `Tablero de tareas al día` | el repo versiona el derivado `docs/TAREAS.md` (90 filas) y **no versiona su materia prima**: `Arena-Reimagined/01-PUBLICACIONES` no existe en el árbol de `main` (19.005 blobs, `truncated=False`). La compuerta no podía pasar nunca y lo decía con un mensaje que apuntaba a otro sitio |
| `gltools-reborn` | `pruebas` | 4 en `failure` | `44080586389` sobre `d9c743fc` | `Compilar y probar el núcleo` → `:app:pruebasNucleo` | `[FALLO] el vidrio es la excepción, no la norma 4 usos`. Los 4 eran 2 **declaraciones** (`Tema.kt:161`, `:167`) y 2 menciones en la **prosa** de un comentario de bloque (`Tema.kt:87`). Usos reales en pantallas: **0** |

En verde durante la misma auditoría: `cero-X-app` 6 de 6 (`44076096239`) y
`bandwidth-hero-proxy2` 5 de 6 (el fallo es de Dependabot sobre una rama ajena).

**Los dos 126 no son la misma falla que el 126 local.** En la CI el fichero sale del checkout con
el modo que registró git. En el sandbox, además, el entorno había restaurado cinco ficheros sin su
bit de ejecución con el índice diciendo `100755` (mtime 23:24:04, el arranque del turno):
`entorno/restaurar-toolchain-kotlin.sh`, `proyectos/restaurar-toolchain-kotlin.sh`,
`proyectos/biblioteca-masiva/vigilar-frentes.sh`,
`respaldo-2026-11-17/nox-index-pb/vigilar-frentes.sh` y
`respaldo-2026-11-17/feed-novedades/codigo/shinku/LICENSE`. Se devolvieron los cinco. Y quedó la
letra chica: `git update-index --chmod=+x` cambia el **índice**, no el disco; hacen falta las dos
cosas y la prueba es ejecutar el fichero.

## 2. Qué se arregló y cómo se verificó cada arreglo

**normas-de-diseno → `bd9af9a4`.** Sólo el modo de `procedimientos/06-auditar-reglas.sh`, de
`100644` a `100755`, por API (blob→tree→commit→ref) para no re-clonar. El blob es el mismo: ni un
byte de contenido. Verificado por el árbol de `main`, que es donde el modo se ve —el endpoint de
contenidos no lo devuelve.

**entorno-de-herramientas-de-trabajo → commit de este turno.** `chmod +x` en el índice y en el
disco para los tres ficheros que se invocan como comando (`proyectos/comprobar-copias.sh`,
`bin/checkpoint.sh`, `entorno/gh-credential.sh`). Arreglar el modo **destapó un fallo real que el
126 tapaba**: con el script corriendo, `--estricto-origen` salió 1 porque el espejo de
`proyectos/normas-de-diseno/herramientas/` estaba tres commits atrás —`01-censar-catalogo-appteka.py`
había crecido de 5.532 a 6.608 bytes—. La compuerta hizo exactamente su trabajo. Se repubicó el
espejo entero desde `bd9af9a4`, se añadieron los tres procedimientos que faltaban
(`06-auditar-publicado.sh`, `07-diff-de-censos.py`, `auditar_diseno_generico.py`), se regeneró
`MANIFIESTO.sha256` desde el disco y se actualizaron `HERRAMIENTAS.md` y los modos, uno a uno
contra el árbol del origen. **Prueba de que el espejo no es un cascarón:** el auditor genérico se
ejecuta desde la copia y devuelve un resultado, y `07-diff-de-censos.py` sin dos censos sale 2 en
vez de inventarse un diff vacío.

**la-bandita-archivo → `bfeb4c3f`.** `tools/tareas.py --revisar` separa las dos cosas que decía con
el mismo mensaje, y el paso del flujo pasa a llamarse «Tablero íntegro (y al día cuando hay
piezas)» con el veredicto leído en el texto del informe (`fallos: NINGUNO`), como la vara y la
autoprueba. Añade tres comprobaciones que no existían: la regla 2 que el propio tablero anunciaba
sin tenerla, la integridad del tablero contra sí mismo, y la correspondencia tablero↔piezas —antes
un tablero viejo pasaba en verde—. Nueve casos sintéticos y verificación **sobre los bytes
publicados** en `main`. Arregla de paso un mensaje falso: con ids duplicados `[1,1]` el escaneo de
huecos anunciaba además «se salta de 001 a 001».

**gltools-reborn → `feb46487`.** Auxiliar `soloCodigo()` (fuera comentarios de línea y de bloque,
fuera el contenido de las cadenas de una y tres comillas) más `DECLARA_MODIFICADOR`, aplicados a
los tres sitios del fichero que cuentan apariciones. **El tope de la ley no cambia: sigue siendo 2.**
El código publicado se compiló literalmente dentro de un arnés con kotlinc 2.3.10 sobre JDK 17
(`EXIT=0`) y se corrió contra las 14 fuentes reales de `ui/` más seis mutaciones. La regex vieja,
en esos mismos siete casos: 4, 7, 9, 6, 7, 5, 6.

| caso | ley nueva | ley vieja |
|---|---|---|
| fuentes reales de `main` | 0 usos → **verde** | 4 → rojo |
| 3 llamadas reales inyectadas | 3 usos → **rojo** | 7 → rojo |
| 5 menciones dentro de `/* */` | 0 → verde | 9 → rojo por prosa |
| 2 llamadas reales (el tope) | 2 → verde | 6 → rojo |
| 2 reales + 1 dentro de una cadena | 2 → verde | 7 → rojo |
| una declaración nueva en una pantalla | 0 → verde | 5 → rojo |
| una mención en cadena de triple comilla | 0 → verde | 6 → rojo |

## 3. Lo que la auditoría destapó de paso

**`cero-X-app` tiene 5 incumplimientos de diseño medidos**, no supuestos. Los encontró el auditor
genérico ejecutado desde el espejo nuevo, sobre el clon local en `855547210c`:

| regla | ley | qué midió |
|---|---|---|
| R1 violeta de plantilla | `REGLAS.md` PROHIBIDO | `CeroXPrimary #6200EE`, matiz **265°**, dentro del rango prohibido 246-341° (`ui/theme/Color.kt:10`) |
| R9 iconos de texto | `REGLAS.md` PROHIBIDO | un `✓` como icono en `ui/idiomas/IdiomasActivity.kt:431` |
| R10 emojis | `REGLAS.md` PROHIBIDO | la misma línea |
| R13 contraste acentos | WCAG 2.1, componentes no textuales 3:1 | `CeroXPrimary` sobre `CeroXDarkBackground` = **2.46:1** |
| R13 contraste acentos | WCAG 2.1, componentes no textuales 3:1 | `CeroXPrimary` sobre `CeroXDarkSurface` = **2.19:1** |

No se cambió ningún color en este turno y la razón se escribe aquí en vez de esconderse: un acento
tiene orden (primario sobre fondo, sobre superficie, y el texto que va encima), y arreglar un
contraste con aritmética ya produjo una vez un fondo invertido. Sin pantalla encendida se mide y se
declara; no se retoca. `#6200EE` es además el violeta por defecto de Material, o sea exactamente el
tic que la regla prohíbe. **Queda como incidencia abierta contra mi propio repo.**

## 4. Lo que NO se verificó, dicho claro

- `:app:pruebasNucleo` entero con Gradle: en el sandbox no hay SDK de Android. Lo comprueba la
  corrida que dispara `feb46487`. Sí se compiló y se corrió, con kotlinc y JDK 17, el código exacto
  de los tres sitios dentro de un arnés.
- `make verificar` y el resto de las ocho compuertas de la-bandita: exigen el clon de 18.464
  ficheros versionados, que no está en el sandbox por la orden de almacenamiento de hoy. Se probó la
  herramienta cambiada sobre árboles sintéticos y sobre los bytes publicados.
- La correspondencia tablero↔piezas en la CI: imposible mientras `01-PUBLICACIONES` no esté
  versionado. **Decisión del dueño**, no de un commit.
- Los tres `126` no se volvieron a ver en verde hasta que corrieron las corridas nuevas: el
  diagnóstico es del log y del árbol, la confirmación es de la CI.

## 5. Regla nueva de procedimiento

Después de publicar un commit propio, la verificación incluye
`GET /repos/Alex17273747576777/<repo>/actions/runs?per_page=N`, y si hay `failure`, leer el log del
job siguiendo el 302 **sin** la cabecera `Authorization`. Verde local no es verde publicado, y un
parte que dice «verificado» tiene que nombrar qué se midió y dónde.
