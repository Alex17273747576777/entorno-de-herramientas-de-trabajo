#!/usr/bin/env python3
"""Pruebas de la frontera entre uso público y mención normativa citada."""
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vara_bandita


class PruebasMencionNormativa(unittest.TestCase):
    def auditar_texto(self, texto, modo_norma=False, meta_min=45001):
        fd, ruta = tempfile.mkstemp(suffix=".md", text=True)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as archivo:
                archivo.write(texto)
            return vara_bandita.auditar(
                ruta, meta_min=meta_min, tope_max=10**9, modo_norma=modo_norma
            )
        finally:
            os.unlink(ruta)

    def test_pieza_publica_no_exime_una_cita_marcada(self):
        texto = (
            vara_bandita.MARCA_MENCION_INICIO
            + "La navaja suiza de"
            + vara_bandita.MARCA_MENCION_FIN
        )
        _, _, resultado, veredicto, _ = self.auditar_texto(texto, modo_norma=False)
        self.assertEqual(veredicto, "ROJO")
        self.assertTrue(any("frase prohibida" in x for x in resultado["rojo"]))
        self.assertTrue(any("marcadores" in x.lower() for x in resultado["rojo"]))

    def test_pieza_publica_bloquea_porcentaje_con_espacio(self):
        _, _, resultado, veredicto, _ = self.auditar_texto("100 % segura")
        self.assertEqual(veredicto, "ROJO")
        self.assertTrue(any("100 % segura" in x for x in resultado["rojo"]))

    def test_umbral_mecanico_es_mayor_que_45000(self):
        _, n_bajo, bajo, _, _ = self.auditar_texto("x" * 45000)
        _, n_pasa, pasa, _, _ = self.auditar_texto("x" * 45001)
        self.assertEqual(n_bajo, 45000)
        self.assertTrue(any("meta de sustentación 45,001" in x for x in bajo["amarillo"]))
        self.assertEqual(n_pasa, 45001)
        self.assertTrue(any("dentro de banda" in x for x in pasa["info"]))

    def test_norma_excluye_solo_el_bloque_didactico_marcado(self):
        texto = (
            "Prosa normativa sin fórmula vetada.\n"
            + vara_bandita.MARCA_MENCION_INICIO
            + "La navaja suiza de"
            + vara_bandita.MARCA_MENCION_FIN
        )
        _, _, resultado, veredicto, _ = self.auditar_texto(texto, modo_norma=True)
        self.assertNotIn("ROJO", veredicto)
        self.assertFalse(resultado["rojo"])
        self.assertTrue(any("menciones pedagógicas" in x.lower() for x in resultado["info"]))

    def test_norma_no_excluye_frase_que_queda_fuera_del_bloque(self):
        texto = (
            vara_bandita.MARCA_MENCION_INICIO
            + "Cita didáctica delimitada"
            + vara_bandita.MARCA_MENCION_FIN
            + "\nTodo el mundo sabe"
        )
        _, _, resultado, veredicto, _ = self.auditar_texto(texto, modo_norma=True)
        self.assertEqual(veredicto, "ROJO")
        self.assertTrue(any("frase prohibida" in x for x in resultado["rojo"]))

    def test_marcadores_desbalanceados_bloquean_la_norma(self):
        texto = vara_bandita.MARCA_MENCION_INICIO + "Cita sin cierre"
        _, _, resultado, veredicto, _ = self.auditar_texto(texto, modo_norma=True)
        self.assertEqual(veredicto, "ROJO")
        self.assertTrue(any("mal formados" in x for x in resultado["rojo"]))

    def test_marcadores_anidados_bloquean_la_norma(self):
        texto = (
            vara_bandita.MARCA_MENCION_INICIO
            + "A"
            + vara_bandita.MARCA_MENCION_INICIO
            + "B"
            + vara_bandita.MARCA_MENCION_FIN
            + vara_bandita.MARCA_MENCION_FIN
        )
        _, _, resultado, veredicto, _ = self.auditar_texto(texto, modo_norma=True)
        self.assertEqual(veredicto, "ROJO")
        self.assertTrue(any("mal formados" in x for x in resultado["rojo"]))

    def test_enmascarado_conserva_numeros_de_linea(self):
        texto = (
            "Línea normal\n"
            + vara_bandita.MARCA_MENCION_INICIO
            + "\nTodo el mundo sabe\n"
            + vara_bandita.MARCA_MENCION_FIN
            + "\nNadie te cuenta esto"
        )
        _, _, resultado, _, _ = self.auditar_texto(texto, modo_norma=True)
        self.assertTrue(any(x.startswith("L5 ") for x in resultado["rojo"]))


if __name__ == "__main__":
    unittest.main()
