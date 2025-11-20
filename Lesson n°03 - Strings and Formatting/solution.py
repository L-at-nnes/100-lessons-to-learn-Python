"""Lesson 03 - Strings and Formatting (Solution)

Reference implementation for the Quote Formatter exercise.
"""

quote = input("Enter your favorite quote: ")
author = input("Who said it? ")

# Keep a trimmed version for counting characters accurately.
trimmed_quote = quote.strip()
character_count = len(trimmed_quote)
preview = trimmed_quote[:10]
title_case_author = author.title()

display_block = f"""
"{trimmed_quote}"
- {title_case_author}
"""

print(display_block)
print(f"Character count (trimmed): {character_count}")
print(f"Preview (first 10 characters): '{preview}'")

# Bonus formatting: uppercase reminder for inspiration.
print("Stay inspired and keep coding!".upper())
