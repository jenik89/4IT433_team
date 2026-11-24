"""Tests for T8 script contract: passing and failing table and README checks."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
TABLE_SCRIPT = ROOT / ".github/scripts/check_table_names.py"
README_SCRIPT = ROOT / ".github/scripts/check_readme_sections.py"

TEST_CONFIG = """
[tables]
scan_dir = "fabric"
allowed_prefixes = ["bronze_", "silver_"]
name_pattern = "^[a-z][a-z0-9_]*$"
strict = false

[readme]
path = "README.md"
min_content_chars = 10
placeholders = ["todo"]

[[readme.sections]]
id = "tym"
title = "Tým"
keywords = ["tym", "team"]
level = "error"
"""


class CheckerTests(unittest.TestCase):
    def run_checker(self, script: Path, code: str, readme: str):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            (base / ".github").mkdir()
            (base / ".github/pr-checks.toml").write_text(TEST_CONFIG, encoding="utf-8")
            notebook = base / "fabric/demo.Notebook/notebook-content.py"
            notebook.parent.mkdir(parents=True)
            notebook.write_text(code, encoding="utf-8")
            (base / "README.md").write_text(readme, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(script)],
                cwd=base,
                capture_output=True,
                text=True,
                check=False,
            )

    def test_valid_table_name_passes(self):
        code = 'def write(df):\n    df.write.saveAsTable("bronze_cestujici")\n'
        result = self.run_checker(TABLE_SCRIPT, code, "## Tým\nV týmu jsou aktivní členové.")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_table_prefix_fails(self):
        code = 'def write(df):\n    df.write.saveAsTable("cestujici")\n'
        result = self.run_checker(TABLE_SCRIPT, code, "## Tým\nV týmu jsou aktivní členové.")
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_complete_readme_passes(self):
        result = self.run_checker(
            README_SCRIPT,
            "print('ok')\n",
            "# Demo\n## Tým\nV týmu jsou aktivní členové s různými rolemi.\n",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_readme_section_fails(self):
        result = self.run_checker(
            README_SCRIPT,
            "print('ok')\n",
            "# Demo\n## Architektura\nPopis technické architektury projektu.\n",
        )
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
