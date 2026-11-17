# normas-de-diseno · herramientas

Fuente canónica: [`normas-de-diseno`](https://github.com/Alex17273747576777/normas-de-diseno)
rama `main` @ `bd9af9a47913` (medido el 2026-11-17 por API; el espejo se republicó entero ese
día porque `01-censar-catalogo-appteka.py` había crecido de 5.532 a 6.608 bytes y el espejo se
había quedado tres commits atrás — `comprobar-copias.sh --estricto-origen` lo dijo en rojo).
Copiadas de `procedimientos/`. Ver `proyectos/LICENCIAS.md`.

Los ocho ficheros llevan aquí el mismo modo que en el origen: 755 los seis que se invocan como
comando, 644 los dos que se llaman con `python3`. Comprobado uno por uno contra el árbol de
`main`, no supuesto.

Son procedimientos, no librerías: cada uno es un tramo de trabajo completo con su porqué
en la cabecera. Sirven para cualquier proyecto Android que publique APK.

| fichero | bytes | sha256 | qué hace |
|---|---:|---|---|
| `01-censar-catalogo-appteka.py` | 6.608 | `bcbf3470ae6e48d8` | censa el catálogo de Appteka categoría por categoría por su API interna `/api/proxy/list`. Leer el HTML da una foto falsa: sólo trae la primera página y lo más reciente |
| `02-elegir-y-desmontar.sh` | 2.731 | `e071f24b3a73fb78` | elegir apps de las que aprender y desmontarlas. Mirar capturas no basta: el diseño vive en Compose. no en `res/`. así que `aapt2` solo no lo cuenta |
| `03-cerrar-tramo.sh` | 10.074 | `51d13ea22f5f2327` | cerrar un tramo: probar. firmar. publicar. dejar constancia. Son 18 pasos y siempre se olvida uno; la vez que se olvidó el `versionCode` el APK se instaló encima del anterior sin actualizarse |
| `04-incidencias.sh` | 3.734 | `d84c568f25217e16` | crear incidencias por API sin temporales ni interpolación de títulos en código |
| `06-auditar-publicado.sh` | 5.851 | `b0a582c0cee00120` | auditar un repo ajeno ya publicado y escribir el informe fechado en `informes/AAAA-MM-DD-<repo>-<sha7>.md`. con el sha256 del auditor dentro. Nació de la regla «toda compuerta nueva se prueba contra un repo ajeno» |
| `06-auditar-reglas.sh` | 4.318 | `217d42d3ebd30b06` | auditar las reglas: si están todas. si se numeran sin saltos y si el disco coincide con el repo. Nació de un `git status` con cuatro permisos cambiados. sin remoto y cuatro commits sin subir. El CI de normas lo invoca como `./procedimientos/06-auditar-reglas.sh`. así que en origen está en 755 |
| `07-diff-de-censos.py` | 13.409 | `0e501f15c71daa7c` | comparar dos censos fechados y decir qué cambió de verdad: altas. bajas. mudanzas de categoría y cambios de campo. separando los campos que importan de los de ruido. Sale 2 si no hay dos censos. en vez de inventarse un diff vacío |
| `auditar_diseno_generico.py` | 39.041 | `6625334b39e5193a` | el auditor de diseño portable: R0-R15 sobre cualquier repo Kotlin/Compose. midiendo matiz. alfa. ARGB duplicado. contraste WCAG 2.1 real y la escalera de superficies. CLI `RUTA [--estricto] [--json]`. exit 0/1/2. Declaró 5 incumplimientos en cero-X-app el 2026-11-17 |

Comprobación de deriva: `./proyectos/comprobar-copias.sh`.

## Lo que deliberadamente NO se copió

Los tres tests de la fuente (`tests/test_procedimientos.py`, `test_habilidades.py`,
`test_kit_diseno.py`) **no están aquí**, y se probó antes de decidirlo:

```text
$ python3 -B test_procedimientos.py     # copiado solo a /tmp/prueba-nd
Ran 7 tests in 0.062s
FAILED (failures=1, errors=5)
```

Resuelven `ROOT = Path(__file__).resolve().parents[1]` y recorren `ROOT/"procedimientos"`,
o sea que esperan la forma del repo entero. Copiados sueltos no prueban nada: serían un
cascarón que parece cobertura. Sus comprobaciones siguen corriendo en el CI de
`normas-de-diseno`, que es donde tienen sentido.

Los cinco procedimientos sí son autocontenidos: `01` habla con la API de Appteka, `04`
con la de GitHub y `06` con `normas/` de su repo, pero ninguno importa un módulo hermano.
