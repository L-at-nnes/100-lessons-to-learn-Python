"""Lesson 04 - Booleans and Conditionals (Solution)

Reference solution for the Study Advisor exercise.
"""

lessons_completed = int(input("How many lessons have you completed? "))
energy = input("Energy level (low/medium/high): ").strip().lower()
minutes_available = int(input("Minutes available right now: "))

remaining_lessons = 100 - lessons_completed
status = "finished" if remaining_lessons <= 0 else "in progress"

print()
print(f"Lessons remaining: {max(remaining_lessons, 0)}")
print(f"Status: {status}")

if remaining_lessons <= 0:
    print("Congratulations! You completed the program. Time to start a portfolio project.")
else:
    # Recommendations using combined conditions.
    if energy == "high" and minutes_available >= 30:
        print("Recommendation: Start a new lesson.")
    elif energy == "medium" and minutes_available >= 15:
        print("Recommendation: Review your notes or redo yesterday's exercise.")
    elif energy == "low" and minutes_available >= 10:
        print("Recommendation: Do a quick quiz or flashcards.")
    else:
        print("Recommendation: Plan tomorrow and protect your streak.")

print("Thanks for checking in. Small steps every day add up!")
