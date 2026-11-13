# la-bandita-archivo · registro

Fuente canónica: [`la-bandita-archivo`](https://github.com/Alex17273747576777/la-bandita-archivo)
rama `main` (medido el 2026-11-13: **18.909 ficheros**, 191.450 KB, HTML, **MIT**).
Contenido: 13.918 `.json`, 3.965 `.md`, 557 `.html`, 175 `.py`, 163 `.txt`, 47 `.png`,
30 `.tsv`, 10 `.xhtml`. Dos workflows: `pagina.yml` y `vara.yml`.

## No se copia nada, y el motivo es el tamaño del riesgo

El árbol tiene **182 candidatos a herramienta**, pero casi todos viven bajo
`Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/_herramientas/` y
`_herramientas-casa/`: son las herramientas de etapas ya cerradas del archivo
(`forja-catalogo.py` en cuatro versiones, `lupa-v3` a `lupa-v6`, `mapa-completo.py`,
`montador-serie.py`, `placas-censo.py`, `gen-piece.py`, `verificar-suelo.py`).

Es decir: son herramientas **archivadas a propósito**, con su historia de versiones en el
nombre. Copiar 182 ficheros de versiones sucesivas a un espejo crearía 182 sitios donde
derivar en silencio, y la única que se usaría es la última. El archivo ya cumple su
función, que es conservar; no hace falta duplicarlo para reutilizarlo.

Lo que se registra aquí es dónde buscar: si un proyecto futuro necesita un forjador de
catálogo o una lupa, se saca de `_herramientas/` la versión más alta, se copia con su
`MANIFIESTO.sha256` y su `HERRAMIENTAS.md`, y entonces entra en `comprobar-copias.sh`
como las demás. Copiar bajo demanda y con contraparte; no por si acaso.

Su auditoría, en `docs/AUDITORIA-REMOTA-2026-11-10.md` de este repo: manifiesto canónico
y `cosign` fijado.
