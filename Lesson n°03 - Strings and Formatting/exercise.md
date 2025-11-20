# Exercise: Quote Formatter

Create a script that takes a quote and author from the user and prints a polished summary.

## Requirements

1. Ask the user for their favorite quote (can include punctuation).
2. Ask for the author name.
3. Store both as strings, keeping the original capitalization.
4. Display the quote inside quotes, followed by the author on the next line.
5. Show the author in Title Case even if the user typed it differently.
6. Count how many characters the quote contains (excluding leading/trailing spaces) and print the number.
7. Slice the first 10 characters of the quote and show them as a preview.
8. Use at least one f-string and one multi-line string to format the output.

## Stretch Ideas

- Highlight the quote with ASCII art (e.g., lines made of `-` or `*`).
- Replace double spaces inside the quote with single spaces for cleaner text.
- Let the user input a year and append it in parentheses using f-strings.

## Tips

- Remember: `strip()` removes outer whitespace, while `replace()` changes specific substrings.
- Title casing: `author.title()` keeps names consistent.
- When slicing, guard against short quotes using `quote[:10]` (Python handles short strings gracefully).
