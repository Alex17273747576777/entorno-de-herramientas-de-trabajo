# La Bandita — casa de reglas y archivo medido

*Una casa que verifica antes de recomendar. Todo dato que aparece aquí tiene fecha, método y evidencia; lo que no se pudo medir se declara hueco, nunca se rellena.*

**TL;DR —** desde el **15 de noviembre de 2026** este repositorio es una **casa de reglas y un entorno de trabajo**: la ley, la medida operativa y las habilidades, más un **archivo medido** (la guía maestra de 70 fichas y un registro de 6.838 fichas con su evidencia cruda). Las series de canal fueron **retiradas** ese mismo día por orden del dueño: la carpeta `Arena-Reimagined/01-PUBLICACIONES/` ya no existe (458 ficheros borrados; el historial git y las actas los conservan). Todo lo que se declara aquí se comprueba con un comando: `make verificar` (registro + sello + compuertas G0 a G17 + autoprueba sintética). Con prisa: `make doctor`. A leer: `guia-maestra/`. A auditar: `ARQUITECTURA.md` y `REGLAS/INDICE-DE-REGLAS.md`.

---

## El retiro del 15 de noviembre de 2026

Por orden del dueño se **borraron todas las publicaciones**: 458 ficheros rastreables de `Arena-Reimagined/01-PUBLICACIONES/`, carpeta que ya no existe. La constancia vive en el **ADDENDUM DE RETIRO** de `CORAZON-LA-BANDITA.md` y en el **Addendum 3** de `docs/ACTA-RESELLADO-2026-11-14.md`. No se reescribió nada para disimular: lo retirado permanece en el historial git de este repositorio y en las actas históricas. La regla de la casa sigue siendo la misma —lo que se publicó una vez no se retoca— y lo que se retira, se retira con acta fechada.

El sitio generado (`site/`) quedó congelado tal como estaba antes del retiro: es un artefacto histórico, no un producto vivo.

La casa quedó en **tres capas vivas y un archivo**:

| Capa | Dónde | Qué contiene |
|---|---|---|
| **1 · Ley** | `CORAZON-LA-BANDITA.md` · `CIMIENTOS/` · `PROCESOS/` | Principios, precedencia, criterios obligatorios, manual de estilo; §14 sincronizado con las bandas |
| **2 · Medida operativa** | `REGLAS/INDICE-DE-REGLAS.md` · `docs/bandas.json` · `Makefile` · `tools/vara.py` · `tools/vara_idiomas.py` | Índice de reglas fechado, presupuesto por canal, compuertas **G0 a G17** y **G20 a G23**, ritual de sellado |
| **3 · Habilidades** | `SKILLS/` · `Arena-Reimagined/HABILIDADES/` · `ENTORNO-DE-TRABAJO/` | Habilidades ejecutables, entorno con su LEEME de supervivencia, registro de fallas y contraparches, moldes por idioma |
| **Archivo** | `guia-maestra/` · `registry/` · `ARCHIVO-HISTORICO/` · `attestations/` | 70 fichas medidas en 12 capítulos, 6.838 fichas con payload crudo, la memoria por meses, sellos SHA-256 encadenados |

**Cambiar una regla cuesta cuatro pasos** (consta en `REGLAS/INDICE-DE-REGLAS.md`): nota fechada en CORAZON, `docs/bandas.json` sincronizado el mismo día, acta y resello si se toca material sellado, y entrada en el índice. No hay atajo.

---

## Estado hoy (15 de noviembre de 2026)

| Qué | Valor del corte | Cómo se comprueba |
|---|---|---|
| Compuertas de la casa | `fallos: NINGUNO` | `make verificar` |
| Banditas por idioma | G20 a G23 sobre los moldes | `python3 tools/vara_idiomas.py` |
| Fichas del registro | 6.838 válidas | `python3 tools/registro_construir.py --verificar` |
| Sello | lote del día, huella encadenada a la anterior | `python3 tools/atestar.py --verificar` |
| Guía maestra | `guia-maestra/` · 12 capítulos · 70 fichas | `make medir-guia` |
| Publicaciones | **retiradas** el 2026-11-15 | Addendum 3 del acta |

Las cifras del lote vigente (fecha, archivos, huella y huella anterior) se leen de su JSON en `attestations/`: ningún número se escribe a mano donde un archivo puede decirlo.

---

## Arranque en tres comandos

```bash
make doctor      # ¿está todo en su sitio?
make verificar   # registro + sello + vara (G0-G17) + autoprueba → «fallos: NINGUNO»
make ayuda       # los destinos del Makefile, con una línea cada uno
```

No hace falta nada más que Python 3.11 o superior. Quien abre un turno de trabajo tiene seis reglas de supervivencia en `ENTORNO-DE-TRABAJO/LEEME-DEL-ENTORNO.md` —leer el checkpoint antes de empezar, `/var/tmp` no es persistencia, espejar ediciones el mismo turno, invocar los guiones con `bash`, overlay de sellos con glob completo, y sello local sólo con acta—. Las fallas y sus contraparches tienen registro propio y fechado: `ENTORNO-DE-TRABAJO/FALLAS-Y-CONTRAPARCHES.md`.

Las llaves viven **fuera del repositorio**, con permisos `600`. Ninguna herramienta las imprime ni las escribe en el árbol.

---

## Documentación, para quien llega

| Quiero… | Voy a |
|---|---|
| Entender cómo está hecho y por qué | [`ARQUITECTURA.md`](ARQUITECTURA.md) |
| Ver el índice de reglas y cómo se cambian | [`REGLAS/INDICE-DE-REGLAS.md`](REGLAS/INDICE-DE-REGLAS.md) |
| Saber qué hace cada herramienta | [`docs/CODIGO.md`](docs/CODIGO.md) |
| Encontrar la traducción de rutas antiguas | [`MAPA-DEL-ARCHIVO.md`](MAPA-DEL-ARCHIVO.md) |
| Ver qué falta y qué está declarado | [`docs/TAREAS.md`](docs/TAREAS.md) |
| Encontrar un documento | [`docs/INDICE.md`](docs/INDICE.md) |
| Aportar algo | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Reportar un fallo de seguridad | [`SECURITY.md`](SECURITY.md) — en privado, 48 h |
| Saber qué cambió y cuándo | [`CHANGELOG.md`](CHANGELOG.md) |
| Convivir sin fricción | [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) |
| Pedir ayuda sin perder tiempo | [`SUPPORT.md`](SUPPORT.md) |

Los archivos de salud comunitaria siguen la práctica estándar de GitHub, las confirmaciones siguen [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/), el registro de cambios sigue [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) y la licencia por archivo sigue las prácticas de [REUSE](https://reuse.software/) de la FSFE. Adoptar la convención no es moda: es que otro pueda auditar sin preguntarnos nada.

---

## Procedencia, sin adornos

El historial git de una etapa anterior se perdió truncado por límites del entorno. El contenido se restauró **verificado por SHA-256** contra el catálogo sellado —cero fallos— y no como clon de la historia. Esa etapa está citada en `Arena-Reimagined/02-ARCHIVO/` y su manifiesto en `ARCHIVO-HISTORICO/MANIFIESTO-2026-10.md`. El historial posterior sí está completo en este repositorio, confirmación por confirmación.

---

## Licencias

| Qué | Licencia | Archivo |
|---|---|---|
| Código (`tools/`, flujos) | MIT | [`LICENSE`](LICENSE) |
| Contenido editorial (guía, docs) | CC BY-SA 4.0 | [`LICENSE-CONTENIDO`](LICENSE-CONTENIDO) |
| Datos y registro (fichas, censos) | CC BY 4.0 | [`LICENSE-DATOS`](LICENSE-DATOS) |
| Marca, nombre y sello de verificación | Reservados | [`NOTICE`](NOTICE) |

Los metadatos de proyectos de terceros se citan con fines de verificación y conservan la licencia de su origen. **Este archivo no relicencia código ajeno ni aloja paquetes de nadie.**

*La Bandita informa a partir de fuentes fechadas.*
