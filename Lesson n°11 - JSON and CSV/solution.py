"""Lesson 11 - JSON and CSV (Solution)

Reference solution for the Learning Progress Exporter.
"""

import json
import csv
from pathlib import Path

ROOT = Path(__file__).parent
JSON_PATH = ROOT / "lessons.json"
CSV_PATH = ROOT / "lessons.csv"

lessons = [
    {"title": "Modules", "minutes": 40, "status": "done"},
    {"title": "Files", "minutes": 55, "status": "done"},
    {"title": "JSON & CSV", "minutes": 60, "status": "in-progress"},
]


def save_json(data):
    with open(JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_json():
    with open(JSON_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def add_entry(data, title, minutes, status):
    data.append({"title": title, "minutes": minutes, "status": status})
    save_json(data)


def export_csv(path, data):
    try:
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "minutes", "status"])
            writer.writeheader()
            writer.writerows(data)
        print(f"CSV exported to {path}")
    except OSError as error:
        print("Failed to export CSV:", error)


def summary(data):
    total_minutes = sum(item["minutes"] for item in data)
    completed = sum(1 for item in data if item["status"].lower() == "done")
    print(f"Total minutes: {total_minutes}")
    print(f"Completed lessons: {completed}/{len(data)}")


def main():
    save_json(lessons)
    print("JSON saved. Reloading to verify...")
    reloaded = load_json()
    print("Reloaded data:", reloaded)

    add_entry(reloaded, "APIs", 45, "planned")
    export_csv(CSV_PATH, reloaded)
    summary(reloaded)


if __name__ == "__main__":
    main()
