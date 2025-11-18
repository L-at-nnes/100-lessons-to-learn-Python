# Exercise: Daily Study Calculator

Write a script that helps you plan and track your study time.

## Requirements

1. Ask the user for their study target in minutes for today.
2. Ask how many minutes they actually studied.
3. Convert both answers to integers so you can do math with them.
4. Compute how many minutes remain to hit the goal (can be negative if goal exceeded).
5. Convert the remaining minutes to hours with decimals.
6. Display a friendly summary using f-strings. Include at least two separate print statements.
7. Add comments explaining key steps (conversion, calculations, etc.).

## Stretch Ideas

- Use `abs()` to display the difference as a positive number while still mentioning whether the user is ahead or behind schedule.
- Format the hours with `round(value, 2)` to keep the output tidy.
- Ask for the number of study sessions and compute an average session length.

## Tips

- Remember that `input()` returns a string; call `int()` right away to work with numbers.
- Keep variable names such as `target_minutes` or `minutes_studied` so the printout reads naturally.
- Test your script with several values (goal met, exceeded, or missed) to ensure the math is correct.
