"""Lesson 03 - Strings and Formatting

Goal: manipulate strings, use helpful methods, slice pieces, and format data clearly.
"""

# 1. Strings can be surrounded by single or double quotes.
first_name = "Alex"
last_name = 'Coder'
print(first_name, last_name)

# 2. Concatenation joins strings, but f-strings are cleaner.
full_name = first_name + " " + last_name
print("Concatenated:", full_name)

# 3. f-strings let you embed expressions directly.
print(f"Hello, {first_name} {last_name}! Ready for more Python?")

# 4. Triple quotes create multi-line text, perfect for instructions.
appeal = """Remember:
- Practice every day
- Commit your progress
- Celebrate small wins
"""
print(appeal)

# 5. String methods transform data without altering the original.
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Title case:", full_name.title())

# 6. Strip removes whitespace at both ends.
raw_input = "   keep learning   "
print("Raw length:", len(raw_input))
print("Stripped length:", len(raw_input.strip()))

# 7. Slicing extracts parts: string[start:end].
username = "python_beginner"
first_five = username[:5]   # from start up to index 5 (exclusive)
last_four = username[-4:]   # last four characters
print("First five chars:", first_five)
print("Last four chars:", last_four)

# 8. Replace and split help tidy data.
welcome_message = "Coding is fun, coding is empowering!"
print(welcome_message.replace("coding", "learning"))
print(welcome_message.lower().split(","))

# 9. Formatting columns with ljust/rjust keeps CLI output readable.
title = "Lesson"
status = "Status"
print(title.ljust(10), status)
print("01".ljust(10), "Done")
print("02".ljust(10), "In progress")
print("03".ljust(10), "Queued")

# 10. Wrap up with a formatted recap message.
lesson_number = 3
concept = "strings and formatting"
print()
print(f"Lesson {lesson_number}: Today we explored {concept}.")
print("Challenge: document a favorite quote using slicing + formatting tricks.")
