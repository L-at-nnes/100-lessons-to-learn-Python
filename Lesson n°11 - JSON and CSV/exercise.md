# Exercise: Learning Progress Exporter

Build a script that tracks lesson progress in JSON and exports a CSV summary.

## Requirements

1. Store lesson entries in a list of dictionaries with keys: `title`, `minutes`, `status`.
2. Save the list as JSON to `lessons.json` with indentation.
3. Load the JSON file back to verify it matches the original data.
4. Export a CSV file `lessons.csv` with headers `title`, `minutes`, `status`.
5. Provide a function `add_entry(data, title, minutes, status)` that updates the in-memory list and re-saves JSON.
6. Provide a function `export_csv(path, data)` that writes the CSV and handles errors (e.g., invalid path) with `try/except`.
7. Print a short summary showing total minutes and count of completed lessons.

## Stretch Ideas

- Accept user input to add entries dynamically.
- Include a timestamp field when exporting CSV.
- Use `pathlib.Path` for all path manipulation.

## Tips

- Use `json.dump(data, file, indent=2)` for readable JSON.
- For CSV, `csv.DictWriter` keeps column order consistent.
- Keep responsibilities separated: data handling vs. file export.
