"""Lesson 13 - Inheritance and Polymorphism (Solution)

Reference implementation for the Resource Library exercise.
"""

from abc import ABC, abstractmethod


class Resource(ABC):
    def __init__(self, title, minutes, tags=None):
        self.title = title
        self.minutes = minutes
        self.tags = tags or []

    @abstractmethod
    def describe(self):
        """Return a string that describes the resource."""


class SharableMixin:
    def share(self):
        return f"Share '{self.title}' with your peers!"


class VideoResource(SharableMixin, Resource):
    def __init__(self, title, minutes, platform, tags=None):
        super().__init__(title, minutes, tags)
        self.platform = platform

    def describe(self):
        return f"[Video] {self.title} ({self.minutes} min) on {self.platform}"


class ArticleResource(Resource):
    def __init__(self, title, minutes, author, tags=None):
        super().__init__(title, minutes, tags)
        self.author = author

    def describe(self):
        return f"[Article] {self.title} by {self.author} ({self.minutes} min read)"


class ProjectResource(Resource):
    def __init__(self, title, minutes, repo_url, tags=None):
        super().__init__(title, minutes, tags)
        self.repo_url = repo_url

    def describe(self):
        return f"[Project] {self.title} ({self.minutes} min) -> {self.repo_url}"


def print_catalog(resources):
    print("Resource catalog:")
    for resource in resources:
        print(" -", resource.describe())


resources = [
    VideoResource("Decorators Explained", 30, "YouTube", tags=["functions"]),
    ArticleResource("Comprehensions 101", 15, "Sam", tags=["syntax"]),
    ProjectResource("CLI Habit Tracker", 90, "https://github.com/example/cli"),
]

print_catalog(resources)

for resource in resources:
    if isinstance(resource, SharableMixin):
        print(resource.share())
