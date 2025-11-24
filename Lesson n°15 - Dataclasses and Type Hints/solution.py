"""Lesson 15 - Dataclasses and Type Hints (Solution)

Reference implementation for the Study Report Generator exercise.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict


@dataclass
class LessonSummary:
    number: int
    title: str
    minutes: int
    status: str = "pending"
    tags: List[str] = field(default_factory=list)

    def is_complete(self) -> bool:
        return self.status.lower() == "done"


@dataclass
class Report:
    lessons: List[LessonSummary]
    author: str
    generated_at: datetime = field(default_factory=datetime.utcnow)

    def total_minutes(self) -> int:
        return sum(lesson.minutes for lesson in self.lessons)

    def completion_percentage(self) -> float:
        if not self.lessons:
            return 0.0
        completed = sum(1 for lesson in self.lessons if lesson.is_complete())
        return (completed / len(self.lessons)) * 100

    def tag_map(self) -> Dict[str, List[int]]:
        tags: Dict[str, List[int]] = {}
        for lesson in self.lessons:
            for tag in lesson.tags:
                tags.setdefault(tag, []).append(lesson.number)
        return tags


def render_report(report: Report) -> str:
    lines = [
        f"Study Report by {report.author}",
        f"Generated at: {report.generated_at.isoformat(timespec='seconds')}",
        "",
    ]

    for lesson in report.lessons:
        status = "✅" if lesson.is_complete() else "⌛"
        lines.append(
            f"{status} Lesson {lesson.number}: {lesson.title}"
            f" ({lesson.minutes} min) [{lesson.status}]"
        )

    lines.append("")
    lines.append(f"Total minutes: {report.total_minutes()}")
    lines.append(f"Completion: {report.completion_percentage():.1f}%")
    lines.append("Tag map: " + str(report.tag_map()))
    return "\n".join(lines)


lessons = [
    LessonSummary(15, "Dataclasses", 40, status="done", tags=["typing"]),
    LessonSummary(16, "Type hints", 50, status="in-progress", tags=["typing", "best-practices"]),
    LessonSummary(17, "Project", 90, tags=["project"]),
]

report = Report(lessons=lessons, author="Alex")
print(render_report(report))
