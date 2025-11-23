"""Lesson 13 - Inheritance and Polymorphism

Goal: extend classes, override methods, leverage super(), and use polymorphism to simplify code.
"""

# 1. Base class defines shared behavior.
class Lesson:
    def __init__(self, number, topic, duration):
        self.number = number
        self.topic = topic
        self.duration = duration

    def summary(self):
        return f"Lesson {self.number}: {self.topic} ({self.duration} min)"


# 2. Subclass customizing new behavior.
class VideoLesson(Lesson):
    def __init__(self, number, topic, duration, resolution="1080p"):
        super().__init__(number, topic, duration)
        self.resolution = resolution

    def summary(self):
        base = super().summary()
        return f"{base} [video: {self.resolution}]"


# 3. Another subclass.
class ProjectLesson(Lesson):
    def __init__(self, number, topic, duration, repo_url):
        super().__init__(number, topic, duration)
        self.repo_url = repo_url

    def summary(self):
        return f"{super().summary()} [project repo: {self.repo_url}]"


lessons = [
    Lesson(13, "Inheritance", 40),
    VideoLesson(14, "Polymorphism", 50),
    ProjectLesson(15, "Mini project", 90, "https://github.com/example"),
]

for lesson in lessons:
    print(lesson.summary())

# 4. Polymorphism: treat different subclasses uniformly.
def log_lessons(items):
    for item in items:
        print("Logging:", item.summary())


log_lessons(lessons)

# 5. Use isinstance for type-specific logic (sparingly).
for lesson in lessons:
    if isinstance(lesson, ProjectLesson):
        print("Project repo:", lesson.repo_url)

# 6. Mixins add optional behavior.
class PrintableMixin:
    def printable(self):
        return f"Printable summary -> {self.summary()}"


class PrintableVideoLesson(PrintableMixin, VideoLesson):
    pass


printable = PrintableVideoLesson(16, "Decorators", 35)
print(printable.printable())

# 7. Abstract base classes define contracts (preview).
from abc import ABC, abstractmethod


class Tracker(ABC):
    @abstractmethod
    def record(self):
        """Record a progress update."""


class MinutesTracker(Tracker):
    def __init__(self):
        self.minutes = 0

    def record(self, amount):
        self.minutes += amount
        print(f"Minutes logged: {self.minutes}")


tracker = MinutesTracker()
tracker.record(30)

# 8. Multiple inheritance order resolution.
class NotificationMixin:
    def notify(self, message):
        print(f"[Notification] {message}")


class NotifyingLesson(NotificationMixin, Lesson):
    def summary(self):
        msg = super().summary()
        self.notify(msg)
        return msg


notifying = NotifyingLesson(17, "Composition", 45)
print("Notifying summary:", notifying.summary())

# 9. Wrap-up.
print("Inheritance lets you reuse core logic and specialize only what changes.")
