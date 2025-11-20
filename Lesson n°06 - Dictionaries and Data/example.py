"""Lesson 06 - Dictionaries and Data

Goal: map keys to values with dictionaries, update entries, iterate, and handle nested data.
"""

# 1. Create a dictionary describing a learner profile.
profile = {
    "name": "Alex",
    "lessons_completed": 5,
    "favorite_topic": "strings",
    "streak_days": 4,
}

print("Profile:", profile)

# 2. Access values by key.
print("Student name:", profile["name"])
print("Lessons completed:", profile["lessons_completed"])

# 3. Add or update keys.
profile["favorite_topic"] = "lists"
profile["timezone"] = "UTC+1"
print("Updated profile:", profile)

# 4. Use get() when the key might not exist. Provide a default to avoid KeyError.
print("Preferred IDE:", profile.get("ide", "VS Code"))

# 5. Remove keys with pop().
removed = profile.pop("timezone")
print("Removed timezone:", removed)

# 6. Iterate through items to build a readable summary.
print("\nProfile summary:")
for key, value in profile.items():
    print(f"- {key}: {value}")

# 7. Combine dictionaries with update().
new_data = {"lessons_completed": 6, "current_focus": "dictionaries"}
profile.update(new_data)
print("\nAfter update:", profile)

# 8. Nested dictionaries model structured data.
lesson_log = {
    "lesson_01": {"topic": "setup", "status": "done"},
    "lesson_02": {"topic": "numbers", "status": "done"},
    "lesson_03": {"topic": "strings", "status": "done"},
    "lesson_04": {"topic": "conditionals", "status": "done"},
    "lesson_05": {"topic": "lists", "status": "in-progress"},
}

for lesson, data in lesson_log.items():
    topic = data["topic"].title()
    status = data["status"].upper()
    print(f"{lesson}: {topic} -> {status}")

# 9. Dictionary comprehension builds quick lookups.
status_lookup = {lesson: info["status"] for lesson, info in lesson_log.items()}
print("\nStatus lookup:", status_lookup)

# 10. Wrap up message.
print("\nDictionaries make it easy to associate labels with values and pass structured data around.")
