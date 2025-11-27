"""Lesson 25 - SQLite Basics

Goal: create a SQLite database, run queries, and fetch results with sqlite3.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "study.db"


def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL,
                minutes INTEGER NOT NULL,
                notes TEXT
            )
            """
        )

def log_session(topic: str, minutes: int, notes: str | None = None) -> None:
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO sessions (topic, minutes, notes) VALUES (?, ?, ?)",
            (topic, minutes, notes),
        )

def fetch_sessions(min_minutes: int = 0) -> list[tuple[int, str, int, str | None]]:
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT id, topic, minutes, notes FROM sessions WHERE minutes >= ?",
            (min_minutes,),
        )
        return cursor.fetchall()

def main() -> None:
    init_db()
    log_session("Decorators", 40, "Focus on wraps")
    log_session("Async", 55)
    sessions = fetch_sessions(min_minutes=30)
    for session in sessions:
        print(session)

if __name__ == "__main__":
    main()
