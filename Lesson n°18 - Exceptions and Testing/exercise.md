# Exercise: Safe Logger with Tests

Create a logger module that validates input, saves data, and includes basic tests.

## Requirements

1. Build a `logger.py` module containing:
   - A function `sanitize_minutes(value: str) -> int` that raises `ValueError` for invalid input.
   - A function `write_entry(path: Path, minutes: int)` that appends the entry and raises errors as needed.
   - A function `log_flow(path: Path, raw_value: str)` that orchestrates the flow with try/except.
2. Add docstrings explaining error handling decisions.
3. Create a `test_logger.py` file with tests using Python’s built-in `unittest` module:
   - Test valid inputs, invalid inputs, and file writing.
   - Use `tempfile.TemporaryDirectory` to avoid writing to real files.
4. Demonstrate running the tests via `python -m unittest test_logger.py`.

## Stretch Ideas

- Add a custom exception `LogPermissionError` that wraps `PermissionError`.
- Use `unittest.mock` to simulate `write_entry` failures.
- Add CLI support in `logger.py` to run the flow directly.

## Tips

- When testing file writes, read the file back to assert the content.
- Keep functions small so they are easy to test.
- Use `with self.assertRaises(ValueError): ...` in tests for negative paths.
