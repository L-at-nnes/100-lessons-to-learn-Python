"""Lesson 10 - Files and Exceptions (Solution)

Reference implementation for the Error-Resistant Logger.
"""

from datetime import datetime
from pathlib import Path

LOG_PATH = Path(__file__).parent / "study_notes.txt"


def append_entry(title, notes):
    """Append a timestamped entry to the log."""
    timestamp = datetime.now().isoformat(timespec="seconds")
    entry = f"[{timestamp}] {title}\n{notes}\n\n"

    try:
        with open(LOG_PATH, "a", encoding="utf-8") as file:
            file.write(entry)
        print("Entry saved.")
    except PermissionError as error:
        print("Permission denied while writing to the log:", error)


def read_notes():
    try:
        contents = LOG_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("No notes found yet. Start logging your progress!")
    else:
        print("Current log:\n")
        print(contents)


def export_summary(target_path):
    target = Path(target_path)
    try:
        data = LOG_PATH.read_text(encoding="utf-8")
        # Prevent accidental overwrite.
        if target.exists():
            print("Target already exists. Pick a different path.")
            return
        target.write_text(data, encoding="utf-8")
        print(f"Summary exported to {target}")
    except FileNotFoundError as error:
        print("Cannot export because the source log is missing.", error)
    except PermissionError as error:
        print("Permission error while writing the summary:", error)


def main():
    title = input("Lesson title: ")
    notes = input("Notes: ")
    append_entry(title, notes)
    read_notes()

    export_path = input("Export summary path (optional): ").strip()
    if export_path:
        export_summary(export_path)


if __name__ == "__main__":
    main()
