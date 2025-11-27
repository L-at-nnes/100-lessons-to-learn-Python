"""Lesson 23 - HTTP Requests (Solution)

Reference implementation for the API Dashboard exercise.
"""

import argparse
import csv
import json
import os
from pathlib import Path
from typing import Any

import requests

CACHE_DIR = Path(__file__).parent / "data"
CACHE_DIR.mkdir(exist_ok=True)
STATS_PATH = Path(__file__).parent / "stats.csv"
API_URL = "https://api.github.com/repos/{owner}/{repo}"

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="GitHub repo dashboard")
    parser.add_argument("owner")
    parser.add_argument("repo")
    parser.add_argument("--offline", action="store_true", help="Read cached data if available")
    parser.add_argument("--save", action="store_true", help="Append stars to stats.csv")
    return parser

def cache_path(owner: str, repo: str) -> Path:
    return CACHE_DIR / f"{owner}_{repo}.json"

def load_from_cache(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def save_cache(path: Path, data: dict[str, Any]) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

def fetch_repo(owner: str, repo: str, token: str | None = None) -> dict[str, Any]:
    url = API_URL.format(owner=owner, repo=repo)
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()

def print_summary(data: dict[str, Any]) -> None:
    print(f"Repo: {data['full_name']}")
    print(f"Description: {data.get('description')}")
    print(f"Stars: {data['stargazers_count']} | Forks: {data['forks_count']}")
    print(f"Open issues: {data['open_issues_count']} | Last push: {data['pushed_at']}")

def append_stats(owner: str, repo: str, stars: int) -> None:
    header_needed = not STATS_PATH.exists()
    with open(STATS_PATH, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if header_needed:
            writer.writerow(["repository", "stars"])
        writer.writerow([f"{owner}/{repo}", stars])

def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    path = cache_path(args.owner, args.repo)

    token = os.getenv("GITHUB_TOKEN")
    data = None

    if args.offline:
        data = load_from_cache(path)
        if data is None:
            print("No cache found; fetching from API...")

    if data is None:
        try:
            data = fetch_repo(args.owner, args.repo, token)
        except requests.exceptions.RequestException as exc:
            print("Network error:", exc)
            return 1
        save_cache(path, data)

    print_summary(data)

    if args.save:
        append_stats(args.owner, args.repo, data["stargazers_count"])
        print("Stats saved.")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
