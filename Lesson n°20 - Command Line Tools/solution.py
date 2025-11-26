"""Lesson 20 - Command Line Tools (Solution)

Study CLI Assistant reference implementation.
"""

import argparse
import csv
import sys
from datetime import datetime
from pathlib import Path

DEFAULT_LOG = Path(__file__).parent / "sessions.csv"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Study CLI Assistant")
    parser.add_argument("--log-path", type=Path, default=DEFAULT_LOG, help="Path to sessions CSV")
    subparsers = parser.add_subparsers(dest="command", required=True)

    log_parser = subparsers.add_parser("log", help="Log a study session")
    log_parser.add_argument("topic")
    log_parser.add_argument("minutes", type=int)
    log_parser.add_argument("--note", default="", help="Optional note")

    stats_parser = subparsers.add_parser("stats", help="Show study statistics")
    stats_parser.add_argument("--topic", help="Filter by topic")

    return parser


def ensure_file(path: Path) -> None:
    if not path.exists():
        path.write_text("timestamp,topic,minutes,note\n", encoding="utf-8")

def log_session(path: Path, topic: str, minutes: int, note: str) -> int:
    if minutes <= 0:
        print("Minutes must be positive.")
        return 1
    ensure_file(path)
    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.utcnow().isoformat(), topic, minutes, note])
    print(f"Logged {minutes} minutes on {topic} -> {path}")
    return 0

def show_stats(path: Path, topic: str | None) -> int:
    if not path.exists():
        print("No sessions logged yet.")
        return 1
    total_minutes = 0
    count = 0
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if topic and row["topic"] != topic:
                continue
            total_minutes += int(row["minutes"])
            count += 1
    if count == 0:
        print("No sessions match the criteria.")
        return 1
    average = total_minutes / count
    print(f"Sessions: {count} | Total minutes: {total_minutes} | Average: {average:.1f}")
    return 0

def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "log":
        return log_session(args.log_path, args.topic, args.minutes, args.note)
    if args.command == "stats":
        return show_stats(args.log_path, args.topic)
    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    sys.exit(main())
