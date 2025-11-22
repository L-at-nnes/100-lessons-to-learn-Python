# Exercise: Error-Resistant Logger

Create a command-line logger that stores study notes and gracefully handles common errors.

## Requirements

1. Ask the user for a lesson title and notes.
2. Write the entry to `study_notes.txt` in append mode. Include a timestamp.
3. Create a function `read_notes()` that prints the entire log. If the file is missing, inform the user.
4. Create a function `export_summary(target_path)` that copies the log to another file using `pathlib.Path` methods.
5. Handle exceptions:
   - `FileNotFoundError` when reading or exporting.
   - `PermissionError` when writing to a restricted location (simulate by exporting to an invalid path).
6. Ensure files are closed properly (use context managers).
7. Add docstrings and inline comments explaining why each try/except block is present.

## Stretch Ideas

- Support multiple log files by letting the user pass a filename.
- Use JSON lines format instead of plain text.
- Add a function that counts how many entries exist and prints the latest entry.

## Tips

- Use `datetime.datetime.now().isoformat()` for timestamps.
- Store the log path in a constant so it is easy to reuse.
- In `export_summary`, guard against overwriting by checking if the target already exists.
