# Exercise: Mentor Dashboard

Design a small object-oriented system to track mentor/mentee sessions.

## Requirements

1. Create a `Mentee` class with attributes: `name`, `level`, `sessions_completed`.
2. Create methods:
   - `record_session(duration)` increments completed sessions and stores total minutes.
   - `progress()` returns a string summary.
3. Create a `Mentor` class with attributes: `name`, `mentees` (list).
4. Add methods to `Mentor`:
   - `add_mentee(mentee)` appends to the list.
   - `report()` prints mentee progress (calls `progress()` on each).
5. Add a `Session` class storing `mentor`, `mentee`, `duration`, and `topic`.
   - Provide a `describe()` method returning a formatted string.
6. Demonstrate the system by:
   - Creating at least two mentees and one mentor.
   - Recording sessions.
   - Printing a report with total minutes and number of sessions.

## Stretch Ideas

- Track session history inside `Mentee` for more detailed reporting.
- Implement `__str__` or `__repr__` methods for cleaner debug output.
- Use class methods to instantiate `Session` objects from dictionaries.

## Tips

- Keep objects responsible for their own data (`Mentee` should manage its stats).
- Use helper methods to avoid duplicating logic when calculating totals.
- Call `mentor.report()` after mutations to ensure the latest data is displayed.
