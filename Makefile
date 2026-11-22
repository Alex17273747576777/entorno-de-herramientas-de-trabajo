.PHONY: prueba medir limpiar copias copias-estrictas copias-tests entorno entorno-reporte latido todo

prueba:
	python3 tests/pruebas.py
	python3 -m unittest discover -s tests -p "test_*.py" -v

entorno:
	bash bin/preparar-espacio-trabajo.sh --solo-verificar

entorno-reporte:
	bash bin/preparar-espacio-trabajo.sh --solo-verificar --reporte-json /tmp/entorno-reporte.json


medir:
	./bin/medir-pieza muestras/p*.md --tabla

limpiar:
	find . -name __pycache__ -type d -exec rm -rf {} + 2>/dev/null; rm -f .tmp-prueba.md; true

copias:
	./proyectos/comprobar-copias.sh

copias-estrictas:
	./proyectos/comprobar-copias.sh --estricto-origen

copias-tests:
	python3 -B proyectos/gltools-reborn/herramientas/test_censo_apk.py
	python3 -B proyectos/gltools-reborn/herramientas/test_preparar_firma.py

latido:
	cd /home/user/work/cero-X-app && python3 tools/latido.py --entorno || \
		echo "latido: el proyecto no está en este equipo; la copia de herramientas/ se verifica con 'make copias'"

todo: prueba copias-estrictas copias-tests

shellcheck:
	@if command -v shellcheck >/dev/null 2>&1; then shellcheck bin/*.sh proyectos/*.sh; else echo "shellcheck no instalado; omitiendo (opcional)"; fi
