# Licencias de lo que se copia aquí

*Medido por la API de GitHub el 2026-11-13, no supuesto. `license.spdx_id` de cada repo.*

| repo del que se copia | licencia medida | ficheros versionados | qué implica para las copias |
|---|---|---:|---|
| `cero-X-app` | **GPL-3.0** | 555 | las copias siguen siendo GPL-3.0: se acompañan de `LICENSE-de-origen.txt` y `NOTICE-de-origen.txt` |
| `gltools-reborn` | **Apache-2.0** | 173 | las copias siguen siendo Apache-2.0, con su `LICENSE-de-origen.txt`; Apache-2.0 pide conservar atribución |
| `normas-de-diseno` | **None** | 41 | sin licencia declarada, formalmente «todos los derechos reservados». Es del mismo dueño que este repo, así que copiar no es el problema; **declararla sí falta** |
| `bandwidth-hero-proxy2` | MIT | 20 | no se copia nada (ver su `HERRAMIENTAS.md`) |
| `la-bandita-archivo` | MIT | 18.909 | no se copia nada (ver su `HERRAMIENTAS.md`) |
| **este repo** | **None** | — | **no declara licencia** |

## El problema real, dicho sin rodeos

Este repositorio **no tiene `LICENSE`** y acaba de recibir dentro copias de código
GPL-3.0 y Apache-2.0. Mientras todo sea del mismo dueño y nadie reutilice nada, no
pasa nada. En cuanto alguien tome una herramienta de aquí, no sabrá bajo qué términos
puede usarla, y en el caso de las de cero-X la respuesta correcta es «GPL-3.0, aunque
el repo que la aloja no lo diga».

Ninguna de las herramientas copiadas lleva cabecera de licencia en el propio fichero
(comprobado en `latido.py`, `comprobar_entorno.py`, `censo_apk.py`,
`verificar_version.py` y `03-cerrar-tramo.sh`: ninguna contiene `GPL`, `Apache`,
`SPDX`, `MIT` ni `Copyright` en sus primeras 20 líneas). O sea que el fichero suelto,
fuera de su repo, no dice de dónde viene.

Decidir la licencia de este repo es del dueño, no mío, y no se inventa en un commit.
Lo que sí se hizo es dejar la procedencia por escrito aquí y junto a cada copia, que
es lo que se puede hacer sin decidir por nadie.
