# Exercise: Habit Tracker

Build a simple habit tracker that stores daily study tasks and marks them as complete.

## Requirements

1. Create a list called `tasks` with at least five practice activities (strings).
2. Print the list in a numbered format using a `for` loop and `enumerate`.
3. Ask the user how many tasks they completed today (integer).
4. Use a loop (for or while) to mark that many tasks as done by appending them to a new list `completed_tasks`.
5. Display two sections: one for completed tasks and one for remaining tasks.
6. Use list slicing or comprehension to display only the first 3 characters of each remaining task as a preview.
7. Print a final summary like "You finished X/Y tasks today!" using f-strings.

## Stretch Ideas

- Record timestamps or notes in tuples `(task, note)` inside the list.
- Allow the user to type which tasks they finished instead of using a number.
- Save the completed tasks to a file for future reference.

## Tips

- Defensive coding: ensure the number of completed tasks does not exceed the total.
- Use `.copy()` if you want to avoid mutating the original task list during iteration.
- A while loop is handy if you repeatedly pop from the front of the list.
