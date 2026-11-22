import subprocess
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SCRIPT = RAIZ / "bin" / "preparar-espacio-trabajo.sh"


class TestEspacioTrabajo(unittest.TestCase):
    def test_sintaxis_bash(self) -> None:
        res = subprocess.run(["bash", "-n", str(SCRIPT)], capture_output=True, text=True, check=False)
        self.assertEqual(res.returncode, 0, res.stderr)

    def test_verificacion_solo_lectura(self) -> None:
        res = subprocess.run(
            ["bash", str(SCRIPT), "--solo-verificar"],
            cwd=RAIZ,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("ESPACIO_DE_TRABAJO_LISTO", res.stdout)
        self.assertIn("COPIAS_OK", res.stdout)


if __name__ == "__main__":
    unittest.main()
