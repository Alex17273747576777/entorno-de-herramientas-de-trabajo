# Fallas comunes · las que no son de un proyecto sino del modo de trabajar

*Corte 2026-11-13. Mismo criterio que el registro de cero-X: sólo fallas que pasaron,
con cómo se detectaron y qué las caza ahora. Éstas salieron al montar esta capa.*

| # | falla | cómo se detectó | contraparte |
|---|---|---|---|
| C1 | Leer `$?` después de un pipe: `./comprobar-copias.sh \| tail -4; echo EXIT=$?` devolvió 0 cuando el script salía 1 | al revisar la salida: el texto decía `COPIAS_DERIVADAS` y el código 0. El código era de `tail`, no del script | medir el código **sin pipe**: `script >/tmp/s.txt 2>&1; echo $?`, y leer el texto por separado. Los cuatro caminos de la contraparte se volvieron a medir así y dieron 0, 1, 1, 2 |
| C2 | `pytest -q test_censo_apk.py` dio «no tests ran» y exit 5, que se leyó como «el test no corre solo» | el fichero no tiene funciones `test_*`: es un script de asertos con `def construir` y `def falla`. Ejecutado directo da `7 comprobaciones, todas en verde` | el runner correcto está escrito en `HERRAMIENTAS.md` de cada proyecto: `python3 -B <fichero>`, que es como lo corre su CI original (`version.yml:34`). Antes de declarar que un test no funciona, mirar cómo lo invoca su propio CI |
| C3 | Copiar un test creyendo que es autocontenido | `tests/test_procedimientos.py` hace `ROOT = Path(__file__).resolve().parents[1]` y recorre `ROOT/"procedimientos"`. Copiado solo: `Ran 7 tests … FAILED (failures=1, errors=5)` | se ejecutó la copia antes de decidir: falló, y por eso **no** se copió. Un test que no corre en su nueva casa es un cascarón: ocupa sitio y parece cobertura |
| C4 | Copiar herramientas GPL-3.0 y Apache-2.0 a un repo sin `LICENSE` | `license.spdx_id` por API: cero-X-app GPL-3.0, gltools-reborn Apache-2.0, este repo None | `proyectos/LICENCIAS.md` con la licencia medida de cada fuente y cada copia acompañada de su `LICENSE-de-origen.txt`. Decidir la licencia del repo queda anotado como decisión del dueño, no se inventa |
| C5 | Un comprobador que pasa porque no encontró nada que comprobar | camino 4 de la prueba: sin manifiestos, la versión obvia del script imprimiría éxito | `comprobar-copias.sh` sale con **2** y escribe `COPIAS_SIN_MANIFIESTO`. Es el cero silencioso aplicado al propio verificador: 0 coincidencias puede significar «limpio» o «no miré» |
| C6 | `make copias` apuntando al script que se acababa de sustituir | `make: …/comprobar-copias.sh: No such file or directory`, Error 127 | al reemplazar una herramienta, grep del repo buscando quién la invoca. La llamada rota apareció en el mismo turno porque se ejecutó `make` después del cambio, no antes |

## Lo que tienen en común

C1, C2, C3 y C5 son la misma familia que domina el registro de cero-X: **una
comprobación que devuelve algo que se parece a un éxito y no lo es.** Un pipe que se
come el código de salida, un runner que recoge cero tests, un test copiado que ya no
prueba nada, un verificador que no tenía nada que verificar. Ninguno falla de forma
ruidosa. La defensa no es mirar más, es **ejecutar el camino roto a propósito** y
comprobar que la herramienta se queja cuando debe.
