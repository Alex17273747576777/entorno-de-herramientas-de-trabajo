.PHONY: prueba medir limpiar

prueba:
	python3 tests/pruebas.py

medir:
	./bin/medir-pieza muestras/p*.md --tabla

limpiar:
	find . -name __pycache__ -type d -exec rm -rf {} + 2>/dev/null; rm -f .tmp-prueba.md; true
