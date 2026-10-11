import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


RAIZ_REPOSITORIO = Path(__file__).resolve().parents[1]


def ejecutar_caso(ruta_relativa):
    ruta_script = RAIZ_REPOSITORIO / ruta_relativa
    with tempfile.TemporaryDirectory() as directorio_temporal:
        return subprocess.run(
            [sys.executable, str(ruta_script)],
            cwd=directorio_temporal,
            capture_output=True,
            text=True,
            check=False,
        )


class PruebasEjecucionCasos(unittest.TestCase):
    def test_resumen_evento_autenticacion(self):
        resultado = ejecutar_caso("cases/01_resumen_evento_autenticacion/main.py")

        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("Resultado: failure", resultado.stdout)
        self.assertIn("¿El intento tuvo éxito? False", resultado.stdout)

    def test_clasificacion_fallos_cuenta(self):
        resultado = ejecutar_caso("cases/02_clasificacion_fallos_cuenta/main.py")

        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn(
            "adm_sys01: FAILURE, cuenta administrativa - relevante",
            resultado.stdout,
        )
        self.assertIn("rnunez: FAILURE, cuenta de usuario estándar", resultado.stdout)

    def test_analisis_logs_ignora_lineas_vacias_desde_otro_directorio(self):
        resultado = ejecutar_caso("cases/03_analisis_logs_autenticacion/main.py")

        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("Total de eventos: 18", resultado.stdout)
        self.assertIn("Fallos: 4", resultado.stdout)

    def test_ips_repetidas_ignora_lineas_vacias_y_valida_lista(self):
        resultado = ejecutar_caso("cases/04_ips_origen_repetidas/main.py")

        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("Líneas totales de fallos: 22", resultado.stdout)
        self.assertIn(
            "IP repetidas: ['10.10.20.167', '10.10.50.52', "
            "'10.10.31.226', '10.10.70.18', '10.10.60.147', "
            "'10.10.60.215']",
            resultado.stdout,
        )
        self.assertIn("IP que aparecen una sola vez: 2", resultado.stdout)


if __name__ == "__main__":
    unittest.main()

