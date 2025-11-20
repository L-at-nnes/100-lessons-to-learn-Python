"""Lesson 04 - Booleans and Conditionals

Goal: compare values, build decision trees with if/elif/else, and combine conditions with logical operators.
"""

# 1. Booleans represent truthy/falsey states.
completed_lesson = True
motivated = False
print("Completed:", completed_lesson)
print("Motivated:", motivated)

# 2. Comparison operators produce booleans.
def lessons_needed(target, completed):
    return target - completed

lessons_goal = 100
lessons_done = 3
remaining = lessons_needed(lessons_goal, lessons_done)
print("Remaining lessons:", remaining)
print("Goal met?", lessons_done >= lessons_goal)

# 3. Basic if statement.
if lessons_done < lessons_goal:
    print("Keep going, you're making progress!")

# 4. if/else handles two branches.
if motivated:
    print("Crack open the next lesson.")
else:
    print("Take a short break, then come back fresh.")

# 5. if/elif/else handles multiple scenarios.
if remaining == 0:
    print("Celebrate! You've finished all lessons.")
elif remaining <= 10:
    print("Final sprint! Only", remaining, "lessons left.")
else:
    print("Plenty of lessons remain, pace yourself.")

# 6. Combining conditions with and/or/not.
energy_level = "medium"  # could be "low", "medium", "high"
free_time_minutes = 45

if energy_level == "high" and free_time_minutes >= 30:
    print("Perfect time for a full lesson.")
elif energy_level == "medium" and free_time_minutes >= 15:
    print("Review notes or finish an exercise.")
elif energy_level == "low" or free_time_minutes < 15:
    print("Skim previous lessons or plan tomorrow's session.")
else:
    print("Log your status and pick it up later.")

print()

# 7. Truthy/falsey values: empty strings, zero, and empty collections are False.
notes = ""
if not notes:
    print("Your notes are empty—jot down a key takeaway.")

# 8. Ternary expressions provide inline decisions.
status = "ahead" if lessons_done > 4 else "on track"
print(f"Progress status: {status}")

# 9. Guard clauses keep logic readable.
def log_session(minutes):
    if minutes <= 0:
        print("Cannot log zero or negative minutes.")
        return
    print(f"Logged {minutes} minutes today. Great job!")

log_session(40)
log_session(0)

# 10. Wrap-up reminder.
print("Use booleans to make your scripts smart enough to react to real data.")
