# Exercise: Study Planner Operators

Create objects that feel native when combined, compared, and iterated.

## Requirements

1. Build a `StudyBlock` class with attributes `topic`, `minutes`, `notes` (list of strings).
2. Implement magic methods:
   - `__str__`/`__repr__` for friendly + debug output.
   - `__len__` returning minutes.
   - `__add__` combining two blocks (merge minutes + concatenate notes).
   - `__bool__` returning `False` if minutes is 0 (so blocks can be used in conditions).
3. Build a `BlockQueue` container class that stores `StudyBlock` instances and supports:
   - Iteration (`__iter__`).
   - Length checks (`__len__`).
   - Indexing (`__getitem__`).
   - Membership tests (`__contains__`).
4. Add a callable `ProgressNotifier` object (`__call__`) that takes a block and prints a message like "🎯 Completed topic in X min".
5. Demonstrate the system by:
   - Creating at least three study blocks.
   - Combining blocks with `+`.
   - Filtering truthy blocks in a list comprehension.
   - Iterating over the queue and notifying for each block.

## Stretch Ideas

- Implement comparison methods (`__lt__`, `__eq__`) to sort blocks by minutes.
- Turn `BlockQueue` into a context manager that logs start/end times.
- Add `__enter__`/`__exit__` to `ProgressNotifier` to open/close a log file.

## Tips

- Always return `NotImplemented` when an operation involves an unsupported type.
- Use `list(self.blocks)` inside `__iter__` to avoid exposing internals if you plan to mutate while iterating.
- When combining blocks, create a new instance instead of mutating existing ones.
