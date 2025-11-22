"""Lesson 09 - Modules and Imports

Goal: organize code across files, import built-in modules, and create reusable helpers.
"""

# 1. Import specific functions from standard modules.
from math import sqrt, pi

print("Square root of 81:", sqrt(81))
print("Circle area (r=5):", pi * 5 ** 2)

# 2. Import entire modules when you need multiple names.
import random

print("Random choice:", random.choice(["practice", "review", "rest"]))
print("Random integer 1-10:", random.randint(1, 10))

# 3. Alias modules for convenience.
import datetime as dt

today = dt.date.today()
print("Today is", today)

# 4. Use pathlib to work with files.
from pathlib import Path

root = Path(__file__).parent
print("This file lives in:", root)
print("Repository contents:")
for path in sorted(root.iterdir()):
    print("-", path.name)

# 5. Create a custom module and import it.
# See helper.py in the same folder.
import helper

helper.print_header("Lesson Planner")
print("Next lesson number:", helper.next_lesson_number(["lesson_01", "lesson_02", "lesson_03"]))

# 6. from module import * is discouraged but shown for completeness.
from helper import MOTTO
print("Motto:", MOTTO)

# 7. Demonstrate if __name__ == "__main__" usage in helper module.
# Running this script executes helper.main() only when helper is run directly.

# 8. Importing JSON to serialize data.
import json

lesson_summary = {
    "lesson": 9,
    "topic": "Modules and Imports",
    "completed": True,
}
print("JSON summary:", json.dumps(lesson_summary))

# 9. Show module search path for troubleshooting.
import sys
print("\nPython module search paths:")
for path in sys.path:
    print("-", path)

# 10. Wrap up reminder.
print("Organize code into modules to keep projects scalable and maintainable.")
