#!/usr/bin/env python3
"""Comprueba cobertura estructural del registro de aceptación del manual.

No juzga la validez semántica de cada fila: verifica que las 70 secciones
numeradas tengan un criterio, dos ejemplos distintos y una consecuencia no vacía.
La revisión humana de correspondencia sigue siendo obligatoria.
"""
import re
import unittest
from pathlib import Path

MANUAL = Path(__file__).with_name("MANUAL-v0.0.1.md")


class CoberturaReglasManual(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.texto = MANUAL.read_text(encoding="utf-8")
        inicio = cls.texto.index("## 9.9 Matriz de cobertura")
        fin = cls.texto.index("# PARTE X", inicio)
        cls.matriz = cls.texto[inicio:fin]
        cls.secciones = set(re.findall(r"^## (\d+\.\d+)\b", cls.texto, re.M))
        cls.filas = []
        for linea in cls.matriz.splitlines():
            if re.match(r"^\|\s*\d+\.\d+\s*\|", linea):
                celdas = [c.strip() for c in linea.strip("|").split("|")]
                cls.filas.append(celdas)

    def test_cada_seccion_numerada_tiene_una_prueba(self):
        ids = [fila[0] for fila in self.filas]
        self.assertEqual(len(ids), len(set(ids)), "ID de sección duplicado en la matriz")
        self.assertEqual(set(ids), self.secciones)

    def test_cada_fila_tiene_criterio_dos_ejemplos_y_consecuencia(self):
        self.assertEqual(len(self.filas), 70)
        cabecera = next(linea for linea in self.matriz.splitlines() if linea.startswith("| ID |"))
        celdas_cabecera = [c.strip() for c in cabecera.strip("|").split("|")]
        self.assertEqual(
            celdas_cabecera,
            ["ID", "Criterio observable", "✅ Caso que pasa", "❌ Caso que falla", "Consecuencia"],
        )
        for fila in self.filas:
            self.assertEqual(len(fila), 5, f"{fila[0]} no tiene cinco campos")
            self.assertTrue(all(fila), f"{fila[0]} tiene un campo vacío")
            self.assertNotEqual(fila[2], fila[3], f"{fila[0]} repite el mismo caso positivo y negativo")
            self.assertGreaterEqual(len(fila[4]), 20, f"{fila[0]} no declara una acción/consecuencia suficiente")


if __name__ == "__main__":
    unittest.main()
