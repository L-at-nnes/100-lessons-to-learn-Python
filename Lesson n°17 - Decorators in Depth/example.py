"""Lesson 17 - Decorators in Depth

Goal: build reusable wrappers, accept arguments, and stack decorators.
"""

import functools
import time


# 1. Basic decorator that logs calls.
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result

    return wrapper


@log_call
def study(topic):
    print(f"Studying {topic}")


study("decorators")

# 2. Decorator with arguments.
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def hydrate():
    print("Drink water!")


hydrate()

# 3. Decorator stacking.

@log_call
@repeat(2)
def review(topic):
    print(f"Reviewing {topic}")


review("iterators")

# 4. Timing decorator for performance checks.
def time_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"{func.__name__} took {duration:.4f}s")
        return result

    return wrapper


@time_execution
def heavy_workload():
    sum(i * i for i in range(1_000_00))


heavy_workload()

# 5. Decorator for caching results.
@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci 30:", fibonacci(30))

# 6. Decorator to enforce arguments.
def require_motivation(func):
    @functools.wraps(func)
    def wrapper(motivation, *args, **kwargs):
        if motivation < 5:
            print("Motivation too low. Take a break.")
            return None
        return func(motivation, *args, **kwargs)

    return wrapper


@require_motivation
def tackle_project(motivation):
    print(f"Motivation {motivation} -> Ready to build!")


tackle_project(3)
tackle_project(8)

# 7. Class decorator.
def track_instances(cls):
    cls.instances = []
    orig_init = cls.__init__

    def __init__(self, *args, **kwargs):
        orig_init(self, *args, **kwargs)
        cls.instances.append(self)

    cls.__init__ = __init__
    return cls


@track_instances
class Lesson:
    def __init__(self, title):
        self.title = title


Lesson("Decorators 101")
Lesson("Decorators Deep Dive")
print("Tracked instances:", Lesson.instances)

# 8. Wrap up.
print("Decorators let you add behavior around functions/classes without cluttering business logic.")
