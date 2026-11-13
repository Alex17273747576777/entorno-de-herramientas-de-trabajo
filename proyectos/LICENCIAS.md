# Licencias de lo que se copia aquí

*Medido por la API de GitHub el 2026-11-13, no supuesto. `license.spdx_id` de cada repo.*

| repo del que se copia | licencia medida | ficheros versionados | qué implica para las copias |
|---|---|---:|---|
| `cero-X-app` | **GPL-3.0** | 555 | las copias siguen siendo GPL-3.0: se acompañan de `LICENSE-de-origen.txt` y `NOTICE-de-origen.txt` |
| `gltools-reborn` | **Apache-2.0** | 173 | las copias siguen siendo Apache-2.0, con su `LICENSE-de-origen.txt`; Apache-2.0 pide conservar atribución |
| `normas-de-diseno` | **None** | 41 | sin licencia declarada, formalmente «todos los derechos reservados». Es del mismo dueño que este repo, así que copiar no es el problema; **declararla sí falta** |
| `bandwidth-hero-proxy2` | MIT | 20 | no se copia nada (ver su `HERRAMIENTAS.md`) |
| `la-bandita-archivo` | MIT | 18.909 | no se copia nada (ver su `HERRAMIENTAS.md`) |
| **este repo** | **GPL-3.0** desde el 2026-11-13 | — | decisión del dueño delegada; ver abajo el porqué de compatibilidad |

## Decidido el 2026-11-13: este repo es **GPL-3.0**

El dueño delegó la elección. Se eligió GPL-3.0 y no otra por una razón de
compatibilidad, no de gusto: **ya hay código GPL-3.0 dentro** (las herramientas de
`cero-X-app`), y GPL-3.0 es la única licencia de las candidatas que puede contenerlo.

- Las copias de `gltools-reborn` son **Apache-2.0**, que es compatible con GPL-3.0 en
  esta dirección: código Apache-2.0 puede formar parte de una obra GPL-3.0. Al revés no.
- Las fuentes **MIT** (`bandwidth-hero-proxy2`, `la-bandita-archivo`) también son
  compatibles hacia GPL-3.0. De ésas no se copió nada, pero queda dicho por si se copia.
- Una licencia permisiva (MIT, Apache-2.0) para el repo **no habría sido válida**: no se
  puede relicenciar como permisivo el código GPL-3.0 que ya está dentro.
- `normas-de-diseno` no declara licencia. Sus cinco procedimientos entran aquí bajo
  GPL-3.0 como el resto del repo; sigue faltando declararla en su propio repo.

Consecuencia que hay que decir en voz alta: `bin/medir-pieza`, `lib/`, `tests/`,
`docs/`, `entorno/`, `muestras/` y `piezas/` —la caja de medición de La Bandita, que
hasta hoy no tenía licencia— **pasan a estar bajo GPL-3.0** al vivir en este repo. Es
el efecto normal de añadir un `LICENSE` a un repositorio que no lo tenía, y es
reversible sólo reescribiendo la historia o moviendo ese código a otro repo.

Cada copia conserva su `LICENSE-de-origen.txt` (y el `NOTICE-de-origen.txt` en el caso
GPL), que es la atribución que Apache-2.0 pide conservar.

### Lo que sigue sin resolverse

Ninguna de las herramientas copiadas lleva cabecera de licencia **en el propio fichero**
(comprobado en `latido.py`, `comprobar_entorno.py`, `censo_apk.py`,
`verificar_version.py` y `03-cerrar-tramo.sh`: ninguna contiene `GPL`, `Apache`,
`SPDX`, `MIT` ni `Copyright` en sus primeras 20 líneas). El `LICENSE` del repo cubre el
conjunto, pero el fichero suelto, fuera de su carpeta, no dice de dónde viene. Poner
cabecera SPDX en cada uno es un cambio en las fuentes canónicas, no en las copias, y
por eso no se hizo aquí: se haría en cada repo y las copias se refrescarían después,
que para eso está `comprobar-copias.sh`.
