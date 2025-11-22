# Exercise: Module Toolkit

Organize a study helper toolkit across multiple modules.

## Requirements

1. Create a `planner.py` file with:
   - A list of `LESSONS` (strings).
   - A function `add_lesson(title)` that appends to the list and returns it.
   - A function `find_lesson(keyword)` that returns matching lessons.
2. Create a `stats.py` file that exposes:
   - A constant `DEFAULT_TARGET = 100`.
   - A function `remaining(target, completed)`.
   - A function `percentage(completed, target=DEFAULT_TARGET)`.
3. Create a `runner.py` script that imports `planner` and `stats` to:
   - Print the current lesson list.
   - Add a new lesson based on user input.
   - Show remaining lessons and completion percentage.
4. Use `if __name__ == "__main__"` in `runner.py` so the script can be imported without executing logic.
5. Demonstrate the module by running `runner.py` (include usage instructions in comments).

## Stretch Ideas

- Add a `utils.py` module containing formatting helpers (e.g., `print_banner`).
- Use `argparse` in `runner.py` to accept command-line arguments instead of `input()`.
- Save the updated lesson list to JSON via a `storage.py` helper.

## Tips

- Keep module responsibilities focused: planner handles data, stats deals with numbers.
- Ensure modules are in the same folder so relative imports (`import planner`) work.
- Document each module with a brief docstring describing its purpose.
