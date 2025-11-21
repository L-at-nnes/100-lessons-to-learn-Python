"""Lesson 08 - Advanced Functions (Solution)

Reference implementation for the Automation Helpers exercise.
"""

tasks = [
    {"name": "review notes", "minutes": 20, "completed": False},
    {"name": "practice loops", "minutes": 35, "completed": True},
    {"name": "build mini project", "minutes": 50, "completed": False},
]


def filter_tasks(task_list, predicate):
    return [task for task in task_list if predicate(task)]


def make_timer(goal_minutes):
    progress = 0

    def add(minutes):
        nonlocal progress
        progress += minutes
        remaining = max(goal_minutes - progress, 0)
        return progress, remaining

    return add


def notify(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Done with {func.__name__}.\n")
        return result

    return wrapper


@notify
def process_task(task):
    print(f"Processing task: {task['name']} ({task['minutes']} min)")


def print_schedule(task_list, index=0):
    if index >= len(task_list):
        print("End of schedule. Keep going!")
        return
    task = task_list[index]
    print(f"- {task['name']} ({task['minutes']} min)")
    print_schedule(task_list, index + 1)


# Demonstration
incomplete_tasks = filter_tasks(tasks, lambda t: not t["completed"])
print("Incomplete tasks:", incomplete_tasks)

weekly_timer = make_timer(120)
print("Timer update #1:", weekly_timer(30))
print("Timer update #2:", weekly_timer(45))

process_task(tasks[0])

print("Remaining schedule:")
print_schedule(incomplete_tasks)

print("Automation helpers ready—mix and match to boost productivity!")
