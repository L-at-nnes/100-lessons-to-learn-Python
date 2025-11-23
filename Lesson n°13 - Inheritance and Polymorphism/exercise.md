# Exercise: Resource Library

Model a learning resource library using inheritance and polymorphism.

## Requirements

1. Create a base class `Resource` with attributes `title`, `minutes`, and `tags` (list).
2. Add a method `describe()` returning a string with title + duration.
3. Create subclasses:
   - `VideoResource` with an extra attribute `platform`.
   - `ArticleResource` with `author`.
   - `ProjectResource` with `repo_url`.
4. Override `describe()` in each subclass to include their specific data.
5. Implement a function `print_catalog(resources)` that accepts a list of mixed resources and prints their descriptions (polymorphism in action).
6. Create a mixin `SharableMixin` that adds a `share()` method returning a formatted message. Combine it with at least one subclass.
7. Demonstrate the system by creating instances, printing the catalog, and calling `share()` on the sharable ones.

## Stretch Ideas

- Add an abstract base class requirement such as `play()` or `launch()`.
- Keep a counter of total resources using a class variable.
- Add a method to filter resources by tag using list comprehensions.

## Tips

- Use `super().__init__()` to avoid duplicating base initialization.
- Remember Python MRO: place mixins before base classes when inheriting.
- Polymorphism shines when functions operate on the base type but accept any subclass.
