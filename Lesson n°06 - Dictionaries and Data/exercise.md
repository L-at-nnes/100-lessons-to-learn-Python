# Exercise: Progress Dashboard

Build a script that stores information about three recent lessons using dictionaries.

## Requirements

1. Create a dictionary called `lessons` where each key is a lesson label (e.g., `"lesson_01"`).
2. Each value should be another dictionary with keys: `topic`, `status`, and `minutes_spent`.
3. Print a dashboard using a loop that shows each lesson label, topic (title case), status (upper case), and minutes spent.
4. Ask the user for a lesson label to update (e.g., `lesson_02`). If it exists, prompt for a new status and minutes, then update the nested dictionary.
5. After the update, print:
   - Total minutes spent across all lessons.
   - How many lessons are marked as `done`.
   - A dictionary comprehension that maps lesson labels to their status.
6. Handle the case where the user enters an unknown lesson label by printing a friendly error.

## Stretch Ideas

- Track additional metrics like `notes` or `difficulty` and show them in the dashboard.
- Allow multiple updates inside a `while` loop until the user types `exit`.
- Export the dashboard to JSON using the `json` module (preview of upcoming lessons).

## Tips

- Use `.items()` to loop over key/value pairs.
- Normalize user input with `.strip().lower()` before matching keys.
- The built-in `sum()` works well with comprehensions: `sum(info["minutes_spent"] for info in lessons.values())`.
