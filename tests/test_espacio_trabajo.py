import json
import subprocess
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SCRIPT = RAIZ / "bin" / "preparar-espacio-trabajo.sh"


class TestEspacioTrabajo(unittest.TestCase):
    def ejecutar(self, *args):
        return subprocess.run(["bash", str(SCRIPT), *args], cwd=RAIZ, capture_output=True, text=True, check=False)

    def test_sintaxis_bash(self):
        res = subprocess.run(["bash", "-n", str(SCRIPT)], capture_output=True, text=True, check=False)
        self.assertEqual(res.returncode, 0, res.stderr)

    def test_verificacion_solo_lectura(self):
        res = self.ejecutar("--solo-verificar")
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("ESPACIO_DE_TRABAJO_LISTO", res.stdout)
        self.assertIn("COPIAS_OK", res.stdout)
        for herramienta in ("ruff", "shellcheck", "java"):
            self.assertIn(herramienta, res.stdout)

    def test_perfil_invalido_rechazado(self):
        res = self.ejecutar("--perfil", "desconocido")
        self.assertEqual(res.returncode, 2)

    def test_reporte_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            destino = Path(tmp) / "sub" / "reporte.json"
            res = self.ejecutar("--solo-verificar", "--perfil", "web", "--reporte-json", str(destino))
            self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
            datos = json.loads(destino.read_text(encoding="utf-8"))
            self.assertEqual(datos["perfil"], "web")
            self.assertIn("generado_utc", datos)
            self.assertIn("python3", datos["herramientas_disponibles"])

    def test_configuracion_repositorios_por_perfil(self):
        cfg = json.loads((RAIZ / "entorno/repositorios.json").read_text(encoding="utf-8"))
        nombres = {r["nombre"] for r in cfg["repositorios"]}
        self.assertEqual(nombres, {"entorno-de-herramientas-de-trabajo", "la-bandita-archivo", "ruta-programacion-sistemas", "normas-de-diseno"})
        self.assertTrue(all(r["url"].startswith("https://github.com/") and r["perfil"] for r in cfg["repositorios"]))


if __name__ == "__main__":
    unittest.main()
