# Exercise: Study Buddy Functions

Create a mini toolkit of functions to manage daily study sessions.

## Requirements

1. Write a function `log_task(task, minutes)` that prints a formatted message.
2. Write a function `minutes_to_hours(minutes)` that returns the hours (float) rounded to 2 decimals.
3. Write a function `plan_session(topic, *, duration=30, focus="practice")` that uses keyword-only parameters.
4. Write a function `summarize_day(*tasks)` that counts how many tasks were logged.
5. Write a function `update_stats(stats, **updates)` that receives a dictionary and keyword arguments to merge into it.
6. Demonstrate these functions in the script by calling them with sample data.
7. Include docstrings for at least two functions to explain their purpose.

## Stretch Ideas

- Return summary data from `summarize_day` (e.g., tasks, average minutes).
- Use a dictionary to track `total_minutes` and update it inside `log_task`.
- Create a `main()` function to organize the script flow and call it at the end.

## Tips

- Keyword-only parameters are defined after `*`, e.g., `def foo(*, bar): ...`.
- When updating dictionaries, use `stats.update(updates)` or manual assignment.
- Keep function names descriptive to make the script read like a set of commands.
