"""Lesson 01 - Getting Started (Solution)

This reference implementation mirrors the requirements from exercise.md.
Focus on understanding each comment and adapting it to your own style.
"""

# 1. Welcome message sets the tone for the session.
print("Welcome back to your Python journal!")

# 2. Store learner information in variables.
user_name = "Alex"  # change to your real name
lessons_done = 0     # update after each completed lesson

# 3. Showcase the current state using an f-string.
print(f"Learner: {user_name}")
print(f"Lessons completed so far: {lessons_done}")

# Blank line keeps the output readable.
print()

# 4. Update the total. Using += mirrors the mental model "take current value and add one".
lessons_done += 1
print(f"Updated total after today: {lessons_done}")

# 5. Leave a motivational note—this keeps the habit consistent.
print("Nice job! Post this progress on GitHub to keep the streak alive.")
