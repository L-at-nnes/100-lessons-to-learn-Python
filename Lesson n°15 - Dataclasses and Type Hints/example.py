"""Lesson 15 - Dataclasses and Type Hints

Goal: use dataclasses to reduce boilerplate and leverage type hints for clarity.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional


@dataclass
class Lesson:
    number: int
    topic: str
    minutes: int
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)

    def summary(self) -> str:
        return f"Lesson {self.number}: {self.topic} ({self.minutes} min)"


lesson = Lesson(15, "Dataclasses", 40, tags=["typing", "oop"])
print(lesson)
print(lesson.summary())

# 2. Frozen dataclasses act like lightweight immutable objects.
@dataclass(frozen=True)
class Plan:
    lessons: List[int]


plan = Plan([1, 2, 3])
print(plan)

# 3. Post-init hooks validate or derive data.
@dataclass
class StudyBlock:
    topic: str
    minutes: int
    notes: Optional[str] = None

    def __post_init__(self):
        if self.minutes <= 0:
            raise ValueError("Minutes must be positive")


block = StudyBlock("Typing practice", 25)
print(block)

# 4. Type hints clarify dictionaries and nested structures.
Schedule = Dict[str, List[Lesson]]

schedule: Schedule = {
    "monday": [lesson],
    "tuesday": [Lesson(16, "Type hints", 50)],
}
print("Schedule:", schedule)

# 5. Functions with typed parameters/return values help IDEs.
def total_minutes(blocks: List[StudyBlock]) -> int:
    return sum(block.minutes for block in blocks)


blocks = [block, StudyBlock("Review", 30)]
print("Total minutes:", total_minutes(blocks))

# 6. Dataclass ordering
@dataclass(order=True)
class Milestone:
    priority: int
    description: str


milestones = [Milestone(2, "Project"), Milestone(1, "Refactor")]
print(sorted(milestones))

# 7. Type alias for readability
LessonID = int


def fetch_lesson(lesson_id: LessonID) -> Optional[Lesson]:
    print(f"Fetching lesson {lesson_id}")
    return lesson if lesson_id == lesson.number else None


print(fetch_lesson(15))
print(fetch_lesson(99))

# 8. Wrap-up message.
print("Dataclasses + type hints keep code concise and self-documenting.")
