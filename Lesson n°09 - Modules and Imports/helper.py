"""Helper utilities for Lesson 09."""

MOTTO = "Ship learning, one commit at a time!"


def print_header(title):
    print("=" * 40)
    print(title.upper())
    print("=" * 40)


def next_lesson_number(labels):
    """Return the next lesson number based on list of labels like 'lesson_01'."""
    numbers = [int(label.split("_")[1]) for label in labels]
    return max(numbers, default=0) + 1


def main():
    print("Helper module executed directly. Running quick demo...")
    print_header("Demo")
    print("Next lesson:", next_lesson_number(["lesson_05", "lesson_06"]))


if __name__ == "__main__":
    main()
