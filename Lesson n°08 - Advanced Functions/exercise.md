# Exercise: Automation Helpers

Create a suite of advanced functions to help automate repetitive study/learning tasks.

## Requirements

1. Create a list of tasks, each represented as a dictionary with keys: `name`, `minutes`, and `completed` (boolean).
2. Write a function `filter_tasks(tasks, predicate)` that returns a new list filtered by the predicate (higher-order function).
3. Write a `make_timer(goal_minutes)` closure that tracks cumulative minutes across multiple calls.
4. Write a decorator `notify` that prints "Starting" and "Done" around any function you wrap.
5. Write a recursive function `print_schedule(tasks, index=0)` that prints the schedule one item at a time.
6. Demonstrate the automation helpers:
   - Use `filter_tasks` with a lambda to fetch incomplete tasks.
   - Use `make_timer` to log progress across at least two sessions.
   - Use `@notify` on a function that processes a task.
   - Call `print_schedule` to list remaining tasks.
7. Include comments explaining why each advanced feature (closure, decorator, recursion) is helpful.

## Stretch Ideas

- Allow the predicate to be optional; if omitted, default to returning all tasks.
- Add a decorator parameter to control whether notifications are printed.
- Replace the recursive schedule printer with an iterative equivalent and compare the readability.

## Tips

- Closures require `nonlocal` when modifying captured variables.
- Decorators should accept `*args`/`**kwargs` to remain flexible.
- Recursion needs a base case to prevent infinite loops.
