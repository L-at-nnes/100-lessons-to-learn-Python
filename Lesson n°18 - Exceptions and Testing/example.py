"""Lesson 18 - Exceptions and Testing

Goal: harden scripts with robust exception handling and basic unit tests.
"""

from pathlib import Path

LOG_PATH = Path(__file__).parent / "lesson18.log"


def read_minutes() -> int:
    raw = input("Minutes studied today: ")
    if not raw.strip():
        raise ValueError("Minutes cannot be empty.")
    minutes = int(raw)
    if minutes <= 0:
        raise ValueError("Minutes must be positive.")
    return minutes


def save_minutes(minutes: int) -> None:
    with open(LOG_PATH, "a", encoding="utf-8") as file:
        file.write(f"Logged {minutes} minutes\n")


def log_session():
    try:
        minutes = read_minutes()
        save_minutes(minutes)
    except ValueError as exc:
        print("Input error:", exc)
    except OSError as exc:
        print("File error:", exc)
    else:
        print("Session logged successfully!")
    finally:
        print("End of logging attempt.")


if __name__ == "__main__":
    log_session()
