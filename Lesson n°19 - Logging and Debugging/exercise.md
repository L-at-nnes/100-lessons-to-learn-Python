# Exercise: Diagnostic Toolkit

Build a small module that standardizes logging for a study automation script.

## Requirements

1. Configure a logger with file + console handlers, log format, and default INFO level.
2. Provide helper functions:
   - `log_start(task_name)` -> INFO level start message.
   - `log_success(task_name, minutes)` -> INFO level completion.
   - `log_failure(task_name, error)` -> ERROR level message plus stack trace.
3. Build a `simulate_task(task_name, minutes, fail=False)` function that:
   - Calls `log_start`.
   - Sleeps briefly to simulate work.
   - Raises a `RuntimeError` when `fail=True`, caught internally and logged.
4. Add a CLI entry point (under `if __name__ == "__main__":`) that runs three tasks with different outcomes.
5. Include instructions for using IDE breakpoints (commented) and show how to switch to DEBUG level via an environment variable or command-line flag.

## Stretch Ideas

- Send logs to JSON format for easier parsing.
- Integrate `logging.config.dictConfig` for advanced setups.
- Emit structured context (e.g., `extra={"task": task_name}`) to filter logs later.

## Tips

- Use `logger.exception` within except blocks to capture traceback automatically.
- Use `time.sleep()` to simulate long-running work.
- Wrap log setup in a function so tests can reinitialize handlers cleanly.
