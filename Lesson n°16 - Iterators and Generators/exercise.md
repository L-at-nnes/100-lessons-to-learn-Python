# Exercise: Habit Stream

Create iterators and generators that manage a stream of learning activities.

## Requirements

1. Build a custom iterator `ActivityLog` that takes a list of tuples `(date, minutes)` and yields formatted strings; stop when entries are exhausted.
2. Write a generator `streak_tracker(days)` that yields streak milestones, e.g., "Day 1", "Day 2", ... up to `days`.
3. Create a generator `rolling_average(entries, window=3)` that yields the average minutes for the current window size.
4. Use generator expressions to filter only entries >= 30 minutes and calculate total minutes lazily.
5. Demonstrate the system by:
   - Printing the `ActivityLog` entries.
   - Iterating over `streak_tracker(5)`.
   - Printing the rolling averages for a sample list.
   - Computing the sum of filtered minutes without converting the generator to a list.

## Stretch Ideas

- Add a `reset()` method to `ActivityLog` to restart iteration.
- Yield dictionaries instead of strings for extra flexibility.
- Add error handling to `rolling_average` for windows larger than the dataset.

## Tips

- Generators remember their state; once exhausted, recreate them if you need to iterate again.
- For rolling averages, keep a sliding window (list or deque) and update totals as you iterate.
- Use `sum(generator)` to consume a generator directly.
