"""Lesson 02 - Numbers and Input (Solution)

A sample implementation of the Daily Study Calculator.
Feel free to modify the messaging so it feels personal.
"""

# Request user data. Convert immediately to avoid mixing strings with numbers.
target_minutes = int(input("How many minutes do you want to study today? "))
minutes_studied = int(input("How many minutes did you actually study? "))

# Difference can be positive (still need time) or negative (goal exceeded).
minutes_remaining = target_minutes - minutes_studied
hours_remaining = minutes_remaining / 60  # float result

print()  # blank line to separate input from the summary

print(f"Target: {target_minutes} minutes")
print(f"Completed: {minutes_studied} minutes")
print(f"Remaining minutes: {minutes_remaining}")
print(f"Remaining hours (can be negative if goal exceeded): {hours_remaining}")

# Optional friendly nudge.
if minutes_remaining > 0:
    print("Keep going, you are close to finishing your target!")
else:
    print("Fantastic! You have met or surpassed today's goal.")
