"""Lesson 07 - Functions Basics (Solution)

Reference implementation for the Study Buddy Functions exercise.
"""

def log_task(task, minutes):
    """Print a formatted message describing the task and minutes spent."""
    print(f"Task: {task} | Minutes: {minutes}")


def minutes_to_hours(minutes):
    """Return hours rounded to two decimals."""
    return round(minutes / 60, 2)


def plan_session(topic, *, duration=30, focus="practice"):
    print(f"Planning {duration} minutes on {topic} with focus on {focus}.")


def summarize_day(*tasks):
    count = len(tasks)
    print(f"You logged {count} tasks today.")
    return count


def update_stats(stats, **updates):
    stats.update(updates)
    return stats


# Demonstration
log_task("Review dictionaries", 40)
log_task("Build mini-project", 55)

print("Hours for 90 minutes:", minutes_to_hours(90))

plan_session("functions", duration=45, focus="deep dive")
plan_session("refactor", focus="cleanup")

summarize_day("review", "practice", "quiz")

progress_stats = {"total_minutes": 95, "lessons": 7}
print("Before:", progress_stats)
updated = update_stats(progress_stats, total_minutes=150, streak_days=5)
print("After:", updated)

print("Toolkit ready—compose these helpers into larger workflows!")
