"""Lesson 28 - Seaborn Visualization

Goal: use Seaborn to build richer charts with themes and annotations.
"""

from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style="whitegrid")

data = pd.DataFrame({
    "lesson": [21, 22, 23, 24, 25],
    "minutes": [40, 55, 60, 45, 50],
    "mood": ["good", "good", "neutral", "neutral", "bad"],
})

plt.figure(figsize=(6, 4))
sns.barplot(data=data, x="lesson", y="minutes", hue="mood", palette="viridis")
plt.title("Minutes and Mood per Lesson")
plt.tight_layout()
plt.savefig(Path(__file__).parent / "seaborn_bar.png")
plt.close()

plt.figure(figsize=(6, 4))
sns.scatterplot(data=data, x="lesson", y="minutes", hue="mood", s=120)
sns.lineplot(data=data, x="lesson", y="minutes", color="gray", alpha=0.5)
plt.title("Lesson Minutes Trend")
plt.tight_layout()
plt.savefig(Path(__file__).parent / "seaborn_scatter.png")
plt.close()

print("Saved seaborn_bar.png and seaborn_scatter.png")
