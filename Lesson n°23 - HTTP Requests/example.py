"""Lesson 23 - HTTP Requests

Goal: consume REST APIs with requests, handle errors, and serialize responses.
"""

import json
import os
from pathlib import Path

import requests

API = "https://api.quotable.io/random"
LOG_PATH = Path(__file__).parent / "quotes.jsonl"

def fetch_quote(tag: str | None = None) -> dict:
    params = {"tags": tag} if tag else None
    response = requests.get(API, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def log_quote(data: dict) -> None:
    with open(LOG_PATH, "a", encoding="utf-8") as file:
        file.write(json.dumps(data) + "\n")

def main() -> None:
    tag = os.getenv("QUOTE_TAG")
    try:
        quote = fetch_quote(tag)
    except requests.exceptions.RequestException as exc:
        print("API error:", exc)
        return
    print(f"{quote['content']} — {quote['author']}")
    log_quote(quote)

if __name__ == "__main__":
    main()
