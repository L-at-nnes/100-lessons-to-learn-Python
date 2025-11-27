# Exercise: Study Session Database

Build a CLI tool that records study sessions in SQLite.

## Requirements

1. Use the built-in `sqlite3` module with a database file named `sessions.db` stored next to the script.
2. Create a table `sessions(id INTEGER PRIMARY KEY, topic TEXT, minutes INTEGER, mood TEXT)`.
3. Provide subcommands using `argparse`:
   - `add` with arguments `topic`, `minutes`, `--mood`.
   - `list` with optional `--min-minutes` filter.
   - `stats` returning total minutes and average per topic.
4. Use parameterized queries and commit changes.
5. Display results in a readable table (simple string formatting is fine).
6. Handle invalid input (non-integer minutes) and database errors gracefully.
7. Include docstrings and comments explaining the schema.

## Stretch Ideas

- Add a `delete <id>` subcommand.
- Support exporting to CSV via `.mode csv` SQL commands or Python code.
- Use `tabulate` library for prettier output when available.

## Tips

- Keep one helper `get_connection()` to centralize database access.
- Use `with conn:` context manager so commits happen automatically.
- Wrap CLI logic in `main()` so tests can import individual functions.
