"""Lesson 27 - Matplotlib Visualization

Goal: build line/bar charts with Matplotlib and customize styling.
"""

import matplotlib.pyplot as plt

lessons = [1, 2, 3, 4]
minutes = [30, 45, 60, 40]

plt.figure(figsize=(6, 4))
plt.plot(lessons, minutes, marker="o", label="Minutes")
plt.title("Minutes per Lesson")
plt.xlabel("Lesson")
plt.ylabel("Minutes")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("minutes_line.png")
plt.close()

plt.figure(figsize=(6, 4))
plt.bar(lessons, minutes, color="skyblue")
plt.title("Minutes per Lesson (Bar)")
plt.xlabel("Lesson")
plt.ylabel("Minutes")
plt.tight_layout()
plt.savefig("minutes_bar.png")
plt.close()

print("Charts saved: minutes_line.png, minutes_bar.png")
