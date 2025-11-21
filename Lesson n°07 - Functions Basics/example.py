"""Lesson 07 - Functions Basics

Goal: define reusable blocks with functions, pass arguments, return values, and document behavior.
"""

# 1. Define a simple function using def.
def greet():
    print("Hello, coder! Let's build habits.")

# Call the function to execute its block.
greet()

# 2. Functions with parameters let you pass data in.
def greet_person(name):
    print(f"Welcome back, {name}! Keep the streak alive.")

greet_person("Alex")

# 3. Return values send data back to the caller.
def lessons_left(total=100, completed=0):
    return max(total - completed, 0)

remaining = lessons_left(completed=7)
print("Lessons remaining:", remaining)

# 4. Functions can return multiple values as tuples.
def progress_summary(completed, total=100):
    remaining = lessons_left(total, completed)
    percent = (completed / total) * 100
    return remaining, percent

remaining, percent = progress_summary(10)
print(f"Remaining: {remaining} | Percent: {percent:.1f}%")

# 5. Use default parameter values to keep calls concise.
def schedule_session(minutes=30, topic="review"):
    print(f"Schedule: {minutes} minutes on {topic}.")

schedule_session()
schedule_session(45, "functions")

# 6. Document functions with docstrings.
def log_session(minutes):
    """Log a study session, validating the minutes."""
    if minutes <= 0:
        print("Minutes must be positive.")
        return
    print(f"Logged {minutes} minutes. Great work!")

print(log_session.__doc__)
log_session(25)

# 7. *args packs extra positional arguments into a tuple.
def add_to_plan(*topics):
    plan = list(topics)
    print("New topics in plan:", plan)

add_to_plan("sets", "dicts", "functions")

# 8. **kwargs captures named arguments.
def update_profile(**kwargs):
    print("Profile updates:", kwargs)

update_profile(name="Alex", timezone="UTC+1", status="motivated")

# 9. Functions can be stored and passed around like data.
def celebrate():
    print("🎉 You completed another lesson!")

callbacks = [greet, celebrate]
for action in callbacks:
    action()

# 10. Wrap up reminder.
print("Functions convert repeated steps into reliable tools. Keep practicing!")
