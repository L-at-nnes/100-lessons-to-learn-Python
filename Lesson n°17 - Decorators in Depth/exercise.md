# Exercise: Productivity Decorator Suite

Create a set of decorators that enhance study-related functions.

## Requirements

1. Create `log_progress(func)` that prints before/after messages with timestamps.
2. Create `require_focus(level)` decorator factory that only runs the function when the provided `focus` argument meets the level.
3. Create `throttle(seconds)` decorator that prevents a function from running again until the cooldown has passed.
4. Create `cache_results(func)` that memoizes function outputs (use a dictionary).
5. Demonstrate the suite by decorating functions such as:
   - `plan_session(topic, focus)`
   - `solve_challenge(problem_id)` (simulate slow work with `time.sleep`).
   - `estimate_duration(topic)` returning minutes.
6. Show decorator stacking (e.g., logging + throttle).
7. Include comments explaining each decorator's use case.

## Stretch Ideas

- Build a class decorator that registers all functions in a global registry.
- Add an optional `logger` argument to `log_progress` to write to files.
- Use `functools.wraps` in every decorator to preserve metadata.

## Tips

- Use `time.time()` or `time.perf_counter()` to manage timestamps and cooldowns.
- For throttling, store the last-call time on the wrapper function itself.
- For caching, store results keyed by `args`/`kwargs` tuples; `functools.lru_cache` is an alternative but implement your own for practice.
