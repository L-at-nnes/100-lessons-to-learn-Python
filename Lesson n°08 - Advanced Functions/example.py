"""Lesson 08 - Advanced Functions

Goal: explore lambda expressions, higher-order functions, closures, decorators, and recursion basics.
"""

# 1. Lambda functions provide quick anonymous functions.
double = lambda x: x * 2
print("Double 4:", double(4))

# 2. map/filter reduce repetition when processing iterables.
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(double, numbers))
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print("Numbers:", numbers)
print("Doubled:", doubled_numbers)
print("Even:", even_numbers)

# 3. List comprehensions often replace map/filter for readability.
squared = [n * n for n in numbers]
print("Squared:", squared)

# 4. Closures capture surrounding state.
def make_goal_tracker(initial_goal):
    progress = 0

    def add_session(minutes):
        nonlocal progress
        progress += minutes
        remaining = max(initial_goal - progress, 0)
        return progress, remaining

    return add_session

tracker = make_goal_tracker(300)  # minutes per week
print("Tracker update #1:", tracker(60))
print("Tracker update #2:", tracker(90))

# 5. Decorators wrap functions to extend behavior.
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with", args, kwargs)
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result

    return wrapper

@log_call
def complete_lesson(lesson_id):
    print(f"Lesson {lesson_id} complete!")

complete_lesson(8)

# 6. Recursive functions call themselves to solve smaller subproblems.
def countdown(n):
    if n <= 0:
        print("Time to start!")
    else:
        print(n)
        countdown(n - 1)

countdown(3)

# 7. Recursion can also compute values.
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Factorial 5:", factorial(5))

# 8. Combine decorators with arguments using higher-order functions.
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def cheer():
    print("Keep coding!")

cheer()

# 9. Use lambdas inline for quick data sorting.
lessons = [
    {"id": 1, "minutes": 30},
    {"id": 2, "minutes": 45},
    {"id": 3, "minutes": 20},
]

lessons_sorted = sorted(lessons, key=lambda lesson: lesson["minutes"], reverse=True)
print("Lessons sorted by minutes desc:", lessons_sorted)

# 10. Wrap-up reminder about balancing simplicity and power.
print("Advanced functions give you tremendous flexibility. Use them when they clarify intent.")
