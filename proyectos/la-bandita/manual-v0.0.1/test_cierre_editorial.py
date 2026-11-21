"""Control del cierre escrito; no certifica originalidad, verdad o atribución completa."""
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import vara_bandita

CIERRE = """## Notas al pie
Corte documental con sus límites.

—¿Qué decide el dato?
—Lo que la evidencia permite.

La Bandita informa a partir de fuentes fechadas.
Este caso pide comprobar antes de actuar.

## Créditos
Autores públicos de los recursos, con sus enlaces.
Arena AI: asistencia editorial.
Alex17273747576777: dueño de La Bandita.
"""


class CierreEditorial(unittest.TestCase):
    def revisar(self, texto, norma=False):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "pieza.md"
            p.write_text(texto)
            return vara_bandita.auditar(p, meta_min=0, tope_max=10**9, modo_norma=norma)[2]

    def test_cierre_correcto_pasa(self):
        self.assertFalse(self.revisar(CIERRE)["rojo"])

    def test_firma_sin_punto_bloquea(self):
        txt = CIERRE.replace("fuentes fechadas.", "fuentes fechadas")
        self.assertTrue(any("firma exacta" in s for s in self.revisar(txt)["rojo"]))

    def test_seccion_despues_de_creditos_bloquea(self):
        self.assertTrue(self.revisar(CIERRE + "\n## Apéndice\nDato posterior.\n")["rojo"])

    def test_creditos_invertidos_bloquean(self):
        txt = CIERRE.replace("Arena AI: asistencia editorial.\nAlex17273747576777: dueño de La Bandita.",
                             "Alex17273747576777: dueño de La Bandita.\nArena AI: asistencia editorial.")
        self.assertTrue(self.revisar(txt)["rojo"])

    def test_meme_ausente_bloquea(self):
        txt = CIERRE.replace("—¿Qué decide el dato?\n—Lo que la evidencia permite.\n", "")
        self.assertTrue(self.revisar(txt)["rojo"])

    def test_remate_cuatro_lineas_bloquea(self):
        txt = CIERRE.replace("Este caso pide comprobar antes de actuar.", "Primera.\nSegunda.\nTercera.\nCuarta.")
        self.assertTrue(self.revisar(txt)["rojo"])

    def test_creditos_ingles_y_firma_marcada(self):
        txt = CIERRE.replace("## Créditos", "## Credits").replace(
            "La Bandita informa a partir de fuentes fechadas.",
            "**La Bandita informa a partir de fuentes fechadas.**")
        self.assertFalse(self.revisar(txt)["rojo"])

    def test_norma_no_exige_cierre_de_pieza(self):
        self.assertFalse(self.revisar("Norma de trabajo sin cierre de publicación.", norma=True)["rojo"])

    def test_pieza_no_usa_cita_normativa_como_exencion(self):
        txt = CIERRE + "\n<!-- VARA:MENCION:INICIO -->Texto<!-- VARA:MENCION:FIN -->"
        self.assertTrue(self.revisar(txt)["rojo"])

    def test_texto_despues_del_credito_final_bloquea(self):
        self.assertTrue(self.revisar(CIERRE + "Texto añadido fuera del cierre.\n")["rojo"])


if __name__ == "__main__":
    unittest.main()
