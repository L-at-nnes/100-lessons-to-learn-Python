"""Lesson 09 - Modules and Imports (Solution)

Reference implementation for the Module Toolkit exercise.
"""

import planner
import stats


def display_lessons():
    print("Current lessons:")
    for index, lesson in enumerate(planner.LESSONS, start=1):
        print(f"{index}. {lesson}")


def add_user_lesson():
    new_title = input("Add a lesson title: ")
    planner.add_lesson(new_title)
    print("Lesson added!\n")


def show_stats():
    completed = len(planner.LESSONS)
    remaining = stats.remaining(stats.DEFAULT_TARGET, completed)
    percent = stats.percentage(completed)
    print(f"Lessons completed: {completed}")
    print(f"Lessons remaining: {remaining}")
    print(f"Completion: {percent:.1f}%")


def main():
    display_lessons()
    add_user_lesson()
    display_lessons()
    show_stats()


if __name__ == "__main__":
    main()
