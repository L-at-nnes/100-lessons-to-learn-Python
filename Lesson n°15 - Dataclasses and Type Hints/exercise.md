# Exercise: Study Report Generator

Use dataclasses and type hints to assemble a report for recent lessons.

## Requirements

1. Create a dataclass `LessonSummary` with fields:
   - `number` (int)
   - `title` (str)
   - `minutes` (int)
   - `status` (str, default "pending")
   - `tags` (List[str], default empty list)
2. Add a method `is_complete()` that returns True when status is "done".
3. Create a dataclass `Report` with fields:
   - `lessons` (List[LessonSummary])
   - `author` (str)
   - `generated_at` (datetime, default `datetime.utcnow()`)
4. Inside `Report`, implement:
   - `total_minutes()` returning the sum of lesson minutes.
   - `completion_percentage()` returning percent complete.
   - `tag_map()` returning a Dict[str, List[int]] mapping tag -> lesson numbers.
5. Write a function `render_report(report: Report) -> str` that builds a multi-line string summary.
6. Demonstrate the generator by creating at least three lessons, assembling a report, and printing `render_report(...)`.

## Stretch Ideas

- Mark `Report` as `frozen=True` to keep it immutable once created.
- Use `field(default_factory=list)` so lists are not shared.
- Add type aliases for clarity (e.g., `Tag = str`).

## Tips

- `default_factory=list` is required when your default is a new list per instance.
- Type hints are optional at runtime but help static analysis and IDEs.
- Use f-strings inside `render_report` to keep formatting readable.
