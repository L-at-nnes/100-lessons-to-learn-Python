"""Lesson 25 - SQLite Basics (Solution)

Reference solution for the Study Session Database exercise.
"""

import argparse
import sqlite3
from pathlib import Path
from typing import Iterable

DB_PATH = Path(__file__).parent / "sessions.db"

def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)

def init_db() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL,
                minutes INTEGER NOT NULL,
                mood TEXT DEFAULT 'neutral'
            )
            """
        )

def add_session(topic: str, minutes: int, mood: str) -> None:
    if minutes <= 0:
        raise ValueError("Minutes must be positive.")
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO sessions (topic, minutes, mood) VALUES (?, ?, ?)",
            (topic, minutes, mood),
        )

def list_sessions(min_minutes: int | None = None) -> Iterable[tuple[int, str, int, str]]:
    query = "SELECT id, topic, minutes, mood FROM sessions"
    params: tuple[int, ...] = ()
    if min_minutes is not None:
        query += " WHERE minutes >= ?"
        params = (min_minutes,)
    query += " ORDER BY id"
    with get_connection() as conn:
        return conn.execute(query, params).fetchall()

def stats() -> tuple[int, float]:
    with get_connection() as conn:
        total = conn.execute("SELECT SUM(minutes) FROM sessions").fetchone()[0] or 0
        count = conn.execute("SELECT COUNT(*) FROM sessions").fetchone()[0] or 0
    average = (total / count) if count else 0.0
    return total, average

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Study sessions database")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a session")
    add_parser.add_argument("topic")
    add_parser.add_argument("minutes", type=int)
    add_parser.add_argument("--mood", default="neutral")

    list_parser = subparsers.add_parser("list", help="List sessions")
    list_parser.add_argument("--min-minutes", type=int)

    subparsers.add_parser("stats", help="Show summary stats")
    return parser

def main(argv: list[str] | None = None) -> int:
    init_db()
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "add":
        try:
            add_session(args.topic, args.minutes, args.mood)
        except ValueError as exc:
            print("Error:", exc)
            return 1
        print("Session added.")
        return 0

    if args.command == "list":
        rows = list_sessions(args.min_minutes)
        if not rows:
            print("No sessions to display.")
            return 0
        print("ID | Topic | Minutes | Mood")
        for row in rows:
            print(f"{row[0]:02d} | {row[1]} | {row[2]} | {row[3]}")
        return 0

    if args.command == "stats":
        total, average = stats()
        print(f"Total minutes: {total}\nAverage per session: {average:.1f}")
        return 0

    parser.error("Unknown command")
    return 2

if __name__ == "__main__":
    raise SystemExit(main())
