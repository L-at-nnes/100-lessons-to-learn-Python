"""Lesson 05 - Lists and Loops

Goal: store related values in lists, iterate with for/while loops, and practice list methods.
"""

# 1. Lists maintain order and can mix types, but keep data consistent when possible.
learning_plan = ["strings", "numbers", "conditionals", "lists"]
print("Initial plan:", learning_plan)

# 2. Indexing starts at 0. Negative indexes count from the end.
print("First topic:", learning_plan[0])
print("Last topic:", learning_plan[-1])

# 3. Update items by assignment.
learning_plan[1] = "math basics"
print("Updated plan:", learning_plan)

# 4. Append and insert add content.
learning_plan.append("loops")
learning_plan.insert(0, "setup")
print("Plan after append/insert:", learning_plan)

# 5. Remove items with pop/remove.
removed = learning_plan.pop()       # removes last item and returns it
print("Removed:", removed)
learning_plan.remove("setup")       # removes first matching value
print("Plan after removals:", learning_plan)

print()

# 6. Loop over values to generate friendly output.
print("Study order:")
for index, topic in enumerate(learning_plan, start=1):
    print(f"{index}. {topic.title()}")

# 7. List comprehensions build new lists succinctly.
upper_plan = [topic.upper() for topic in learning_plan]
print("Upper-case plan:", upper_plan)

# 8. While loops are useful when the loop length is not known ahead of time.
tasks_remaining = learning_plan.copy()
print("\nProcessing tasks with while loop:")
while tasks_remaining:
    current = tasks_remaining.pop(0)
    print(f"✅ Completed: {current}")
print("All tasks done!")

# 9. Combine loops with conditions to filter data.
long_topics = [topic for topic in learning_plan if len(topic) >= 6]
print("Topics with 6+ letters:", long_topics)

# 10. Summarize the progress.
print()
print(f"Today's lesson covered {len(learning_plan)} main topics and two loop patterns.")
