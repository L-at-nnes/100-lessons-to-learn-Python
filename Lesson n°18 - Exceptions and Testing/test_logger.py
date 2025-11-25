import tempfile
import unittest
from pathlib import Path

from solution import sanitize_minutes, write_entry, log_flow, LogPermissionError


class TestLogger(unittest.TestCase):
    def test_sanitize_minutes_valid(self):
        self.assertEqual(sanitize_minutes("30"), 30)

    def test_sanitize_minutes_invalid_empty(self):
        with self.assertRaises(ValueError):
            sanitize_minutes(" ")

    def test_sanitize_minutes_negative(self):
        with self.assertRaises(ValueError):
            sanitize_minutes("-5")

    def test_write_entry_creates_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "log.txt"
            write_entry(path, 25)
            self.assertTrue(path.exists())
            content = path.read_text(encoding="utf-8")
            self.assertIn("Logged 25 minutes", content)

    def test_log_flow_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "log.txt"
            result = log_flow(path, "15")
            self.assertEqual(result, 15)

    def test_log_flow_invalid_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "log.txt"
            result = log_flow(path, "bad")
            self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
