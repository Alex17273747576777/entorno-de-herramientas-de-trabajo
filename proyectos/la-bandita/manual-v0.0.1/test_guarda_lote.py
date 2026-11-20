import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

GUARDA = Path(__file__).with_name("guarda_lote.py")


def maestro(repetitor: str, semilla: int = 1) -> str:
    """Texto largo (>45.001 caracteres) con vocabulario propio por semilla:
    no dispara el umbral de semejanza y cumple el piso mecánico."""
    partes = []
    total = 0
    i = 0
    while total < 46_500:
        i += 1
        chunk = (f"{repetitor} sección {semilla}.{i} explica el caso concreto con fuentes "
                 f"fechadas, decisión propia y evidencia verificable número {semilla}-{i}. ")
        partes.append(chunk)
        total += len(chunk)
    return "".join(partes)


class GuardaLote(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.bitacora = self.dir / "bitacora.jsonl"

    def tearDown(self):
        self.tmp.cleanup()

    def run_guarda(self, *args, env=None):
        import os
        entorno = dict(os.environ)
        if env:
            entorno.update(env)
        return subprocess.run(
            # Una prueba aislada mide su fixture, no otros proyectos del workspace.
            [sys.executable, str(GUARDA), *args, "--raiz", str(self.dir)],
            capture_output=True, text=True, env=entorno)

    def escribir(self, nombre, texto):
        ruta = self.dir / nombre
        ruta.write_text(texto, encoding="utf-8")
        return ruta

    def test_par_largo_distinto_da_verde(self):
        es = self.escribir("a.md", maestro("español"))
        en = self.escribir("b.md", maestro("english", 7))
        salida = self.run_guarda("verificar", "--pieza", "01", "--es", str(es),
                                 "--en", str(en), "--bitacora", str(self.bitacora),
                                 env={"CORTE_FECHA": "2026-11-10"})
        self.assertEqual(salida.returncode, 0, salida.stdout + salida.stderr)
        entrada = json.loads(self.bitacora.read_text(encoding="utf-8").strip())
        self.assertEqual(entrada["veredicto"], "VERDE")
        self.assertEqual(entrada["fecha_procedencia"].split(" ")[0], "CORTE_FECHA")

    def test_almacenamiento_sobre_limite_bloquea(self):
        es = self.escribir("es.md", maestro("español"))
        en = self.escribir("en.md", maestro("english", 7))
        with (self.dir / "limite.bin").open("wb") as f:
            f.truncate(50_000_000)
        salida = self.run_guarda("verificar", "--pieza", "01", "--es", str(es),
                                 "--en", str(en), "--bitacora", str(self.bitacora))
        self.assertEqual(salida.returncode, 1)
        self.assertIn("almacenamiento", salida.stdout)
        self.assertIn("detener la escritura", salida.stdout)

    def test_maestro_corto_da_rojo(self):
        es = self.escribir("c.md", "muy corto")
        en = self.escribir("d.md", maestro("english", 7))
        salida = self.run_guarda("verificar", "--pieza", "02", "--es", str(es),
                                 "--en", str(en), "--bitacora", str(self.bitacora),
                                 env={"CORTE_FECHA": "2026-11-10"})
        self.assertEqual(salida.returncode, 1)
        self.assertIn("FALLO", salida.stdout)

    def test_rojos_previos_bloquean_hasta_override_registrado(self):
        es_corto = self.escribir("e.md", "corto")
        en = self.escribir("f.md", maestro("english", 7))
        primero = self.run_guarda("verificar", "--pieza", "03", "--es", str(es_corto),
                                  "--en", str(en), "--bitacora", str(self.bitacora),
                                  env={"CORTE_FECHA": "2026-11-10"})
        self.assertEqual(primero.returncode, 1)
        es_largo = self.escribir("e2.md", maestro("español", 8))
        bloqueado = self.run_guarda("verificar", "--pieza", "03", "--es", str(es_largo),
                                    "--en", str(en), "--bitacora", str(self.bitacora),
                                    env={"CORTE_FECHA": "2026-11-10"})
        self.assertEqual(bloqueado.returncode, 1)
        self.assertIn("ROJO previa", bloqueado.stdout)
        override = self.run_guarda("verificar", "--pieza", "03", "--es", str(es_largo),
                                   "--en", str(en), "--bitacora", str(self.bitacora),
                                   "--aceptar-riesgo", "corpus previo revisado y vigente",
                                   env={"CORTE_FECHA": "2026-11-10"})
        self.assertEqual(override.returncode, 0, override.stdout)
        entradas = [json.loads(l) for l in
                    self.bitacora.read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertEqual(entradas[-1]["aceptar_riesgo"], "corpus previo revisado y vigente")

    def test_similitud_contra_referencia_da_rojo(self):
        texto = maestro("mismo texto exacto")
        es = self.escribir("g.md", texto)
        en = self.escribir("h.md", maestro("english distinct", 9))
        ref = self.escribir("ref.md", texto)
        salida = self.run_guarda("verificar", "--pieza", "04", "--es", str(es),
                                 "--en", str(en), "--referencia", str(ref),
                                 "--bitacora", str(self.bitacora),
                                 env={"CORTE_FECHA": "2026-11-10"})
        self.assertEqual(salida.returncode, 1)
        self.assertIn("similitud", salida.stdout)


if __name__ == "__main__":
    unittest.main()
