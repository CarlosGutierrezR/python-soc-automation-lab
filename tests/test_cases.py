import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def run_case(relative_path):
    script_path = REPOSITORY_ROOT / relative_path
    with tempfile.TemporaryDirectory() as temporary_directory:
        return subprocess.run(
            [sys.executable, str(script_path)],
            cwd=temporary_directory,
            capture_output=True,
            text=True,
            check=False,
        )


class CaseExecutionTests(unittest.TestCase):
    def test_auth_event_summary(self):
        result = run_case("cases/01_auth_event_summary/main.py")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Result: failure", result.stdout)
        self.assertIn("Was this attempt successful? False", result.stdout)

    def test_account_failure_classification(self):
        result = run_case("cases/02_account_failure_classification/main.py")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("adm_sys01: FAILURE, admin account - notable", result.stdout)
        self.assertIn("rnunez: FAILURE, standard user account", result.stdout)

    def test_auth_log_parser_ignores_empty_lines_from_any_working_directory(self):
        result = run_case("cases/03_auth_log_parser/main.py")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Total events: 18", result.stdout)
        self.assertIn("Failures: 4", result.stdout)

    def test_repeated_source_ips_ignore_empty_lines_from_any_working_directory(self):
        result = run_case("cases/04_repeated_source_ips/main.py")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Total failed-login lines: 22", result.stdout)
        self.assertIn("IPs that occurred only once: 2", result.stdout)


if __name__ == "__main__":
    unittest.main()

