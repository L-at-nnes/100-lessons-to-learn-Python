"""Planner module"""

LESSONS = ["lesson_01", "lesson_02", "lesson_03"]


def add_lesson(title):
    LESSONS.append(title)
    return LESSONS


def find_lesson(keyword):
    keyword = keyword.lower()
    return [lesson for lesson in LESSONS if keyword in lesson.lower()]
