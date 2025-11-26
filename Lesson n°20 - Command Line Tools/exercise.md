# Exercise: Study CLI Assistant

Create a command-line assistant that manages study sessions.

## Requirements

1. Build a script `study_cli.py` using `argparse` with subcommands:
   - `log` storing a session (`topic`, `minutes`, optional `--note`).
   - `stats` printing total minutes and number of sessions from the log file.
2. Store sessions in a CSV file `sessions.csv` located next to the script.
3. Support `--log-path` option for both subcommands to override the file location.
4. When logging, append `timestamp,topic,minutes,note` to the CSV.
5. In `stats`, read the CSV and compute:
   - Total minutes.
   - Count of sessions.
   - Average minutes per session (rounded to 1 decimal).
6. Handle errors (missing file, invalid minutes) gracefully and exit with non-zero status.
7. Include instructions in comments showing sample commands.

## Stretch Ideas

- Add a `--json` flag to output stats in machine-friendly format.
- Support filtering stats by topic via `--topic`.
- Integrate environment variables for default log path.

## Tips

- Use `argparse.ArgumentParser(subparsers=...)` to separate commands.
- Use `csv.writer`/`csv.DictReader` for reliable CSV handling.
- Return exit codes (0 success, 1 error) so automation tools can detect failures.
