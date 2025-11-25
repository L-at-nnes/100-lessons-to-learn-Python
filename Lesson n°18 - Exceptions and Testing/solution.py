"""Lesson 18 - Exceptions and Testing (Solution)

Safe logger implementation and unit tests.
"""

from pathlib import Path
from typing import Optional


class LogPermissionError(PermissionError):
    """Custom exception to signal permission issues when writing logs."""

def sanitize_minutes(value: str) -> int:
    """Convert raw input to minutes, raising ValueError on bad input."""
    if not value.strip():
        raise ValueError("Minutes cannot be empty.")
    try:
        minutes = int(value)
    except ValueError as exc:
        raise ValueError("Minutes must be an integer.") from exc
    if minutes <= 0:
        raise ValueError("Minutes must be positive.")
    return minutes

def write_entry(path: Path, minutes: int) -> None:
    """Append a log entry to the given path."""
    try:
        with open(path, "a", encoding="utf-8") as file:
            file.write(f"Logged {minutes} minutes\n")
    except PermissionError as exc:
        raise LogPermissionError("Cannot write to log file.") from exc

def log_flow(path: Path, raw_value: str) -> Optional[int]:
    """End-to-end flow with exception handling. Returns minutes on success."""
    try:
        minutes = sanitize_minutes(raw_value)
        write_entry(path, minutes)
    except ValueError as exc:
        print("Input error:", exc)
        return None
    except LogPermissionError as exc:
        print("File error:", exc)
        return None
    else:
        print("Log entry saved.")
        return minutes




