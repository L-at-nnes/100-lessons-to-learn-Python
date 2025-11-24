"""Lesson 14 - Magic Methods

Goal: customize object behavior with dunder (double-underscore) methods.
"""

from functools import total_ordering


@total_ordering
class Lesson:
    def __init__(self, number, topic, minutes):
        self.number = number
        self.topic = topic
        self.minutes = minutes

    # __repr__ for debugging, __str__ for humans
    def __repr__(self):
        return f"Lesson(number={self.number!r}, topic={self.topic!r}, minutes={self.minutes!r})"

    def __str__(self):
        return f"Lesson {self.number} - {self.topic} ({self.minutes} min)"

    # Comparison operators let us sort/compare lessons easily
    def __eq__(self, other):
        if not isinstance(other, Lesson):
            return NotImplemented
        return self.number == other.number

    def __lt__(self, other):
        if not isinstance(other, Lesson):
            return NotImplemented
        return self.number < other.number

    # Arithmetic-style method for merging durations
    def __add__(self, other):
        if not isinstance(other, Lesson):
            return NotImplemented
        total_minutes = self.minutes + other.minutes
        return Lesson(
            number=max(self.number, other.number),
            topic=f"{self.topic} + {other.topic}",
            minutes=total_minutes,
        )

    # len() proxy
    def __len__(self):
        return self.minutes


lesson_a = Lesson(14, "Magic Methods", 50)
lesson_b = Lesson(15, "Operator Overloading", 60)

print(lesson_a)
print(repr(lesson_a))
print("Equal?", lesson_a == lesson_b)
print("Shorter?", lesson_a < lesson_b)
print("Combined lesson:", lesson_a + lesson_b)
print("Minutes via len():", len(lesson_a))

print()

# 2. __contains__ and __iter__ for custom containers.
class Playlist:
    def __init__(self, *lessons):
        self.lessons = list(lessons)

    def __iter__(self):
        return iter(self.lessons)

    def __contains__(self, item):
        return item in self.lessons

    def __len__(self):
        return len(self.lessons)

    def __getitem__(self, index):
        return self.lessons[index]


playlist = Playlist(lesson_a, lesson_b)
print("Playlist length:", len(playlist))
print("First item:", playlist[0])
print("Has lesson 14?", lesson_a in playlist)
for entry in playlist:
        print("Playlist entry:", entry)

print()

# 3. __call__ lets objects behave like functions.
class HabitReminder:
    def __init__(self, message):
        self.message = message

    def __call__(self, name):
        return f"Hey {name}, {self.message}"


reminder = HabitReminder("time to review your notes!")
print(reminder("Alex"))

# 4. Context manager with __enter__/__exit__
class StudyLog:
    def __init__(self, path):
        self.path = path
        self.file = None

    def __enter__(self):
        self.file = open(self.path, "a", encoding="utf-8")
        self.file.write("--- Session start ---\n")
        return self.file

    def __exit__(self, exc_type, exc, tb):
        self.file.write("--- Session end ---\n\n")
        self.file.close()
        # suppress exceptions? return False to propagate
        return False


with StudyLog("lesson14.log") as log:
    log.write("Practiced magic methods.\n")

print("Context manager finished, file closed.")

# 5. Wrap up
print("Dunder methods let your objects integrate naturally with Python syntax.")
