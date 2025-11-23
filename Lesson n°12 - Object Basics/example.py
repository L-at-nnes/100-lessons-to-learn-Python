"""Lesson 12 - Object Basics

Goal: define classes, instantiate objects, use attributes/methods, and practice initialization logic.
"""

# 1. Define a simple class.
class Lesson:
    def __init__(self, number, topic, duration):
        self.number = number
        self.topic = topic
        self.duration = duration  # minutes
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def summary(self):
        status = "done" if self.completed else "pending"
        return f"Lesson {self.number}: {self.topic} ({self.duration} min) -> {status}"


lesson = Lesson(12, "Object Basics", 45)
print(lesson.summary())

# 2. Update attributes after creation.
lesson.duration = 50
lesson.mark_completed()
print("After update:", lesson.summary())

# 3. Use __repr__ for debugging-friendly output.
class Course:
    def __init__(self, title):
        self.title = title
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def total_minutes(self):
        return sum(l.duration for l in self.lessons)

    def __repr__(self):
        return f"Course(title={self.title!r}, lessons={len(self.lessons)})"


course = Course("100 Lessons to Learn Python")
course.add_lesson(lesson)
course.add_lesson(Lesson(13, "Classes in depth", 55))
print(course)
print("Total course minutes:", course.total_minutes())

# 4. Use classmethods for alternative constructors.
class StudySession:
    def __init__(self, duration, topic):
        self.duration = duration
        self.topic = topic

    @classmethod
    def from_lesson(cls, lesson):
        return cls(lesson.duration, lesson.topic)


session = StudySession.from_lesson(lesson)
print("Session topic:", session.topic)

# 5. Static methods group related utilities.
class TimeUtils:
    @staticmethod
    def minutes_to_hours(minutes):
        return round(minutes / 60, 2)


print("Course hours:", TimeUtils.minutes_to_hours(course.total_minutes()))

# 6. Composition: Course uses Lesson objects.
lessons = [Lesson(14, "Objects review", 30), Lesson(15, "Small project", 90)]
for item in lessons:
    course.add_lesson(item)
print("Updated course minutes:", course.total_minutes())

# 7. Encapsulation via private attributes (conventionally using _ prefix).
class StudyTracker:
    def __init__(self):
        self._minutes_logged = 0

    def log(self, minutes):
        if minutes <= 0:
            raise ValueError("Minutes must be positive.")
        self._minutes_logged += minutes

    def report(self):
        return f"Minutes logged: {self._minutes_logged}"


tracker = StudyTracker()
tracker.log(30)
print(tracker.report())

# 8. __str__ for user-friendly string representation.
class Student:
    def __init__(self, name):
        self.name = name
        self.streak = 5

    def __str__(self):
        return f"{self.name} (streak: {self.streak} days)"


student = Student("Alex")
print(student)

# 9. Wrap up message.
print("Objects package data + behavior, making it easier to model real scenarios.")
