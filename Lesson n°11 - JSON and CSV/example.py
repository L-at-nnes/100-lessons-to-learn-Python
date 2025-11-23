"""Lesson 11 - JSON and CSV

Goal: serialize structured data with JSON, work with CSV files, and keep code organized when exchanging data.
"""

from pathlib import Path
import json
import csv

ROOT = Path(__file__).parent
json_path = ROOT / "progress.json"
csv_path = ROOT / "progress.csv"

# 1. Represent Python data (dict + list) and save it as JSON.
progress_data = {
    "student": "Alex",
    "lessons": [
        {"id": 9, "topic": "Modules", "minutes": 40},
        {"id": 10, "topic": "Files", "minutes": 55},
    ],
}

with open(json_path, "w", encoding="utf-8") as file:
    json.dump(progress_data, file, indent=2)
print(f"JSON written to {json_path}")

# 2. Load JSON from disk back into Python objects.
with open(json_path, "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
print("Loaded JSON:", loaded_data)

# 3. Use json.dumps for quick display or API payloads.
payload = json.dumps(progress_data)
print("Payload string:", payload)

# 4. Write CSV headers + rows.
headers = ["lesson_id", "topic", "minutes"]
with open(csv_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for item in progress_data["lessons"]:
        writer.writerow({
            "lesson_id": item["id"],
            "topic": item["topic"],
            "minutes": item["minutes"],
        })
print(f"CSV written to {csv_path}")

# 5. Read CSV back using DictReader.
with open(csv_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("Row:", row)

# 6. Convert CSV rows into JSON-friendly structures.
lessons_from_csv = []
with open(csv_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        lessons_from_csv.append({
            "id": int(row["lesson_id"]),
            "topic": row["topic"],
            "minutes": int(row["minutes"]),
        })
print("Lessons re-created from CSV:", lessons_from_csv)

# 7. Append to existing JSON file safely (read + modify + write).
with open(json_path, "r", encoding="utf-8") as file:
    current = json.load(file)

current["lessons"].append({"id": 11, "topic": "JSON & CSV", "minutes": 60})
with open(json_path, "w", encoding="utf-8") as file:
    json.dump(current, file, indent=2)
print("Updated JSON with new lesson.")

# 8. Use Path.read_text/write_text for quick operations.
summary_path = ROOT / "summary.json"
summary_path.write_text(json.dumps({"total_minutes": 95}), encoding="utf-8")
print("Summary file created.")

# 9. Wrap up.
print("JSON handles nested data; CSV is perfect for tabular exports. Use both as needed.")
