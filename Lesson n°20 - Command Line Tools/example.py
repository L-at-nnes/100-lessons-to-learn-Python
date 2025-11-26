"""Lesson 20 - Command Line Tools

Goal: build CLI scripts with argparse, environment variables, and exit codes.
"""

import argparse
import os
from pathlib import Path

DEFAULT_LOG = Path(__file__).parent / "cli_log.txt"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Track study sessions from the terminal.")
    parser.add_argument("topic", help="Topic you studied")
    parser.add_argument("minutes", type=int, help="Minutes spent on the session")
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG, help="Where to store the log")
    parser.add_argument("--tag", action="append", help="Optional tags (can repeat)")
    parser.add_argument("--quiet", action="store_true", help="Hide confirmation output")
    return parser.parse_args()

def write_log(path: Path, topic: str, minutes: int, tags: list[str] | None) -> None:
    tags_display = ",".join(tags or []) or "no-tags"
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{topic};{minutes};{tags_display}\n")

def main() -> int:
    args = parse_args()
    api_key = os.getenv("STUDY_API_KEY")
    if api_key:
        print("API key detected—ready to sync later.")

    try:
        write_log(args.log, args.topic, args.minutes, args.tag)
    except OSError as exc:
        print("File error:", exc)
        return 1

    if not args.quiet:
        print(f"Logged {args.minutes} minutes on {args.topic} -> {args.log}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
