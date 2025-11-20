"""Lesson 06 - Dictionaries and Data (Solution)

Reference implementation of the Progress Dashboard.
"""

lessons = {
    "lesson_01": {"topic": "setup", "status": "done", "minutes_spent": 30},
    "lesson_02": {"topic": "numbers", "status": "done", "minutes_spent": 45},
    "lesson_03": {"topic": "strings", "status": "review", "minutes_spent": 25},
}

print("Current dashboard:")
for label, info in lessons.items():
    topic = info["topic"].title()
    status = info["status"].upper()
    minutes = info["minutes_spent"]
    print(f"- {label}: {topic} | {status} | {minutes} min")

lesson_to_update = input("Which lesson do you want to update? (e.g., lesson_02) ").strip().lower()

if lesson_to_update in lessons:
    new_status = input("Enter the new status: ").strip()
    new_minutes = int(input("Minutes spent this session: ").strip())

    lessons[lesson_to_update]["status"] = new_status
    lessons[lesson_to_update]["minutes_spent"] = new_minutes

    print("\nDashboard updated!")
else:
    print("Unknown lesson label. No changes applied.")

print()
print("Summary:")
total_minutes = sum(info["minutes_spent"] for info in lessons.values())
lessons_done = sum(1 for info in lessons.values() if info["status"].lower() == "done")
status_map = {label: info["status"] for label, info in lessons.items()}

print(f"Total minutes: {total_minutes}")
print(f"Lessons marked done: {lessons_done}")
print("Status map:", status_map)

print("Keep tracking your progress—data makes motivation visible!")
