"""Lesson 10 - Files and Exceptions

Goal: read/write files safely, handle exceptions, and build simple logging utilities.
"""

from pathlib import Path

ROOT = Path(__file__).parent
LOG_FILE = ROOT / "study_log.txt"

# 1. Write text to a file using context managers.
with open(LOG_FILE, "w", encoding="utf-8") as file:
    file.write("Lesson log\n")
    file.write("==========\n")

# 2. Append new entries without overwriting previous ones.
with open(LOG_FILE, "a", encoding="utf-8") as file:
    file.write("Lesson 10: Files and Exceptions\n")
    file.write("Notes: Practiced reading/writing + try/except.\n")

print(f"Log created at {LOG_FILE}")

# 3. Read the file back to verify.
with open(LOG_FILE, "r", encoding="utf-8") as file:
    contents = file.read()
    print("\nCurrent log contents:\n", contents)

# 4. Handle missing files gracefully.
missing_path = ROOT / "nonexistent.txt"
try:
    missing_path.read_text(encoding="utf-8")
except FileNotFoundError as error:
    print("Missing file detected:", error)

# 5. Example of user input with exception handling.
def read_minutes():
    try:
        return int(input("How many minutes did you code today? "))
    except ValueError:
        print("Please enter a valid integer.")
        return 0

minutes = read_minutes()
print(f"Logged {minutes} minutes.")

# 6. Custom exception to enforce rules.
class NegativeMinutesError(ValueError):
    pass

def log_minutes(minutes):
    if minutes < 0:
        raise NegativeMinutesError("Minutes cannot be negative.")
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"Logged minutes: {minutes}\n")

try:
    log_minutes(minutes)
except NegativeMinutesError as error:
    print("Validation error:", error)

# 7. Use try/except/finally to guarantee cleanup.
try:
    file = open(ROOT / "temp.txt", "w", encoding="utf-8")
    file.write("Temporary notes...")
finally:
    file.close()
    print("Temporary file closed.")

# 8. Delete temporary files with unlink if needed.
temp_path = ROOT / "temp.txt"
if temp_path.exists():
    temp_path.unlink()
    print("Temporary file removed.")

# 9. Wrap up message.
print("Use file handling + exceptions to keep programs reliable and user-friendly.")
