"""Statistics module"""

DEFAULT_TARGET = 100


def remaining(target, completed):
    return max(target - completed, 0)


def percentage(completed, target=DEFAULT_TARGET):
    if target == 0:
        return 0
    return (completed / target) * 100
