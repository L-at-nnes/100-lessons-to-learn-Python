"""Lesson 02 - Numbers and Input

Goal: manipulate integers/floats, use arithmetic operators, and convert user input into numbers.
"""

# 1. Integers (whole numbers) and floats (decimals) are the basic numeric types.
days_in_course = 100        # int
hours_per_day = 1.5         # float representing 1 hour 30 minutes
print("Course length in days:", days_in_course)
print("Hours per day:", hours_per_day)

# 2. Combine numbers with arithmetic operators.
total_hours = days_in_course * hours_per_day
print("Total hours if you stay consistent:", total_hours)

# 3. Division always returns a float in Python.
weeks = days_in_course / 7
print("Weeks needed:", weeks)

# 4. Floor division (//) and modulo (%) offer extra control.
full_weeks = days_in_course // 7     # drops the decimal part
remaining_days = days_in_course % 7  # remainder after dividing by 7
print("Full weeks:", full_weeks)
print("Remaining days:", remaining_days)

print()  # visual separator

# 5. Converting text to numbers. Imagine reading "42" from a file or API.
text_value = "42"
print("Raw value:", text_value, "type:", type(text_value))

number_value = int(text_value)  # raises ValueError if the text is not a whole number
print("Converted value:", number_value, "type:", type(number_value))

# You can also convert to float to capture decimals.
float_value = float("3.14")
print("Float value:", float_value)

print()

# 6. Using input() to capture user data.
# input() ALWAYS returns a string, so convert it before doing math.
minutes_today = input("How many minutes did you code today? ")
minutes_today = int(minutes_today)

# Convert minutes to hours (float) by dividing by 60.
hours_today = minutes_today / 60
print(f"Nice! That is {hours_today} hours of focused practice today.")

# 7. Track cumulative progress.
total_minutes = number_value + minutes_today  # reusing number_value from earlier (42)
print(f"If we add today's effort, your running total is {total_minutes} minutes.")

print("Remember: always validate input in real projects. For now, trust your own numbers.")
