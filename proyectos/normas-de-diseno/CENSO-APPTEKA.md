# Censo de Appteka · límites medidos y receta (2026-11-17)

*El código vive en `normas-de-diseno/procedimientos/01-censar-catalogo-appteka.py` y los snapshots en
`normas-de-diseno/censo/`. Aquí va lo que se midió al ejecutarlos, que no tiene otra casa.*

## Lo que cuesta un recorrido completo

| dato | valor medido |
|---|---|
| categorías | 42 |
| tamaño de página | 96 entradas |
| páginas totales | ~381 |
| latencia por petición | **3-4,5 s** (medida con peticiones aisladas, no deducida) |
| duración del recorrido | **~25 minutos** |
| snapshot resultante | 1.578.165 B comprimido (el del 08-11: 1.486.750 B) |
| código de salida | **0** si está completo, **2** si falta alguna página |

El `timeout=30` con 4 reintentos ya estaba en `pedir()` desde el principio. La vez que paré el proceso
creyendo que estaba colgado (pid 13660) fue un error mío: iba lento porque el servidor va lento.
**Regla:** antes de matar un proceso largo se mide la latencia real de una petición aislada y se
multiplica; y se lanza con `python3 -u` cuando la salida pasa por `tee`, porque Python bufferiza y el
`log_tail` sale vacío aunque el proceso trabaje.

## La cifra que se malinterpreta sola

**37.284 no son 37.284 apps.** Son listados `(categoría, app)`:

- **10.026 paquetes distintos** · media 3,72 apariciones · máximo **361** (`app.morphe.manager`)
- 5.961 apps salen en una sola categoría; 1.000 salen en más de siete
- detrás: `com.leadaxe.lxbox` 183×, `com.nebula.karing` 165×, `sh.haven.app` 153×,
  `online.novaproxy.nova_client` 138×

Comando reproductor (el mismo que está en `censo/README.md`):

```bash
python3 -c "import gzip,json,collections as c; d=json.load(gzip.open('censo/censo-2026-11-17.json.gz','rt',encoding='utf-8')); p=[a.get('paquete') or i for x in d.values() for i,a in x['apps'].items()]; print(len(p),'listados ·',len(set(p)),'paquetes distintos'); print(c.Counter(p).most_common(5))"
```

En el snapshot del 08-11 las mismas cifras eran 36.540 listados / 9.968 paquetes / máximo 352.
Copiar el 352 en el README del 17 fue FALLA-012.

## El diff, y por qué no se puede leer sin la prueba previa

```bash
python3 procedimientos/07-diff-de-censos.py                        # los dos últimos del directorio
python3 procedimientos/07-diff-de-censos.py --markdown --max 40    # informe publicable
python3 procedimientos/07-diff-de-censos.py --viejo 2026-11-08 --nuevo 2026-11-17
```

Salidas: **0** con diff, **1** error, **2** si no hay dos censos o la fecha no existe (y lo dice: no se
inventa un diff vacío, que sería un verde falso).

Resultado real 08-11 → 17-11: **+58 paquetes** (9.968 → 10.026), +744 listados, **64 altas**, **6
bajas**, **8 mudanzas** de categoría y **76 apps con datos cambiados** (`version=62 · autor=33 ·
fuente=9 · nombre=5`). Aparte, ruido de contador que **no** se lista como cambio: `tamano` en 63 apps
y `descargas` en 3.859.

Dos decisiones que sólo se justifican con la prueba:

1. **El representante de cada paquete es canónico** (`sitios.sort(key=lambda t:(t[0],t[1]))`) y la
   mudanza se juzga por el **conjunto** de categorías. La primera versión elegía «por orden de
   aparición» y sobre estos mismos datos se inventó **410 mudanzas y 2.896 cambios** que no existían.
2. **La prueba con cambios conocidos es obligatoria antes de creerle al diff.** Se sintetizan dos
   censos en `/tmp` con exactamente 6 cambios inyectados (2 altas, 1 baja, 1 mudanza, 1 versión, 1
   fuente) y el script tiene que devolver **esos 6 y ninguno más**. Los snapshots sintéticos van en
   `/tmp`, nunca dentro del repo: un censo falso versionado habría entrado en el histórico.

## Lo que el censo no dice

Las 64 altas son lo que devolvió la API de Appteka. **No se comprobó una por una** que el repositorio
exista ni que la app sea de código abierto: el censo recoge lo que el catálogo declara. Y con dos fotos
se puede decir qué cambió, no a qué ritmo — la tendencia exige una tercera.
