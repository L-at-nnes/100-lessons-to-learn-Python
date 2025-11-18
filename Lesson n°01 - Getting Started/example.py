"""Lesson 01 - Getting Started

Goal: understand how Python runs top to bottom, print text, and store values in variables.
"""

# Running this file from the terminal (or VS Code) lets you read the output step by step.
# Use:  python example.py

# 1. Print is our first debugging friend: it shows text in the console.
print("Hello, Python learner!")

# 2. Variables save information so we can reuse them later.
# The syntax is: name = value
name = "Alex"
lessons_completed = 0

# 3. You can combine literal text and variables in a single print.
print("Welcome", name, "you've completed", lessons_completed, "lessons so far.")

# 4. f-strings keep the code readable once there are many variables.
print(f"Let's study together, {name}! Today is lesson {lessons_completed + 1}.")

# 5. Printing blank lines is an easy way to separate sections.
print()

# 6. We can update variables over time.
lessons_completed = lessons_completed + 1  # same as lessons_completed += 1
print("Progress update! Lessons finished:", lessons_completed)

# 7. Use comments to explain *why* you do something. The # symbol ignores everything to its right.
# For example, we can track motivation with a simple score:
motivation_score = 10  # keep this number high by coding regularly
print(f"Motivation score: {motivation_score}/10")

# 8. Final message encouraging habit building.
print("Great job! Commit this lesson to GitHub to record your progress.")
