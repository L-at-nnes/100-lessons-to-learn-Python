# Exercise: Study Advisor

Build a script that recommends what to do next based on the learner's status.

## Requirements

1. Ask the user how many lessons they have completed (integer).
2. Ask for their current energy level (`low`, `medium`, or `high`).
3. Ask how many minutes they have available right now.
4. Use `if/elif/else` and logical operators to recommend one of these actions:
   - "Start a new lesson" if energy is high and minutes >= 30.
   - "Review notes" if energy is medium and minutes >= 15.
   - "Do a quick quiz" if energy is low but minutes >= 10.
   - "Plan tomorrow" if minutes < 10.
5. Print how many lessons remain out of 100, and congratulate the user if they've finished all.
6. Include at least one ternary expression (e.g., for a status label).

## Stretch Ideas

- Ask whether the learner prefers morning or evening sessions and personalize the message.
- Log the recommendation to a text file for habit tracking.
- Use `str.lower()` on the energy input so the comparisons stay consistent.

## Tips

- Convert numeric input to `int` before doing math.
- Keep the conditions mutually exclusive by checking from most specific to most general.
- After giving the recommendation, print a motivational message using f-strings.
