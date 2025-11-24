"""Lesson 16 - Iterators and Generators (Solution)

Reference solution for the Habit Stream exercise.
"""

from collections import deque
from typing import Iterable, Iterator, Tuple


class ActivityLog:
    def __init__(self, entries: Iterable[Tuple[str, int]]):
        self.entries = list(entries)
        self.index = 0

    def __iter__(self) -> "ActivityLog":
        return self

    def __next__(self) -> str:
        if self.index >= len(self.entries):
            raise StopIteration
        date, minutes = self.entries[self.index]
        self.index += 1
        return f"{date}: {minutes} minutes"

    def reset(self) -> None:
        self.index = 0


def streak_tracker(days: int) -> Iterator[str]:
    for day in range(1, days + 1):
        yield f"Day {day}"


def rolling_average(entries: Iterable[int], window: int = 3) -> Iterator[float]:
    buffer = deque(maxlen=window)
    for value in entries:
        buffer.append(value)
        yield sum(buffer) / len(buffer)


entries = [
    ("2025-11-20", 25),
    ("2025-11-21", 40),
    ("2025-11-22", 35),
]

log = ActivityLog(entries)
for record in log:
    print(record)

print("Streak milestones:")
for text in streak_tracker(5):
    print(text)

minutes = [25, 40, 35, 50, 20]
print("Rolling averages:", list(rolling_average(minutes, window=3)))

filtered_total = sum(value for value in minutes if value >= 30)
print("Filtered total minutes >= 30:", filtered_total)
