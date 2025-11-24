"""Lesson 16 - Iterators and Generators

Goal: build custom iterators, create generators, and leverage generator expressions.
"""

# 1. Any object with __iter__ returning an iterator can be looped over.
class Countdown:
    def __init__(self, start: int):
        self.start = start

    def __iter__(self):
        current = self.start
        while current > 0:
            yield current
            current -= 1


print("Countdown:", list(Countdown(5)))

# 2. Generator functions use yield to produce sequences lazily.
def pomodoro_sessions(count: int, duration: int):
    for number in range(1, count + 1):
        yield f"Session {number} - {duration} minutes"


for session in pomodoro_sessions(3, 25):
    print(session)

# 3. Generator expressions are compact.
topics = ["strings", "dicts", "oop", "async"]
uppercase = (topic.upper() for topic in topics)
print("Uppercase topics:", list(uppercase))

# 4. Infinite generator pattern.
def habit_tracker():
    week = 1
    while True:
        yield f"Week {week}: log your progress"
        week += 1


tracker = habit_tracker()
print(next(tracker))
print(next(tracker))

# 5. Custom iterator class implementing __next__.
class StudyQueue:
    def __init__(self, *lessons):
        self.lessons = list(lessons)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lessons):
            raise StopIteration
        lesson = self.lessons[self.index]
        self.index += 1
        return lesson


queue = StudyQueue("modules", "files", "json")
for lesson in queue:
    print("Queue item:", lesson)

# 6. Generator pipeline for data processing.
minutes_spent = [30, 45, 60]
filtered = (minutes for minutes in minutes_spent if minutes >= 45)
doubled = (value * 2 for value in filtered)
print("Pipeline result:", list(doubled))

# 7. Use yield from to delegate to another generator.
def daily_tasks():
    yield from ["plan", "code", "review"]
    yield "share"


print("Daily tasks:", list(daily_tasks()))

# 8. Wrap-up.
print("Iterators/generators let you handle data streams efficiently and elegantly.")
