"""Lesson 05 - Lists and Loops (Solution)

Reference solution for the Habit Tracker.
"""

tasks = [
    "review notes",
    "watch tutorial",
    "write code",
    "read docs",
    "solve quiz",
]

print("Today's tasks:")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

completed_count = int(input("How many tasks did you complete today? "))
completed_count = max(0, min(completed_count, len(tasks)))  # clamp inside valid range

completed_tasks = []
remaining_tasks = tasks.copy()

for _ in range(completed_count):
    completed_tasks.append(remaining_tasks.pop(0))

print()
print("Completed tasks:")
for task in completed_tasks:
    print(f"- {task}")

print("\nRemaining tasks (preview):")
for task in remaining_tasks:
    preview = task[:3]
    print(f"- {task} (preview: {preview}...)")

print()
print(f"You finished {len(completed_tasks)}/{len(tasks)} tasks today!")
