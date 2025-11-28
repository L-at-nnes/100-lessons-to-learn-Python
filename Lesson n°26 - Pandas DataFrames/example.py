"""Lesson 26 - Pandas DataFrames

Goal: load CSV data, transform with Pandas, and export summaries.
"""

from pathlib import Path
import pandas as pd

data = {
    "lesson": [21, 22, 23, 24],
    "topic": ["Venv", "Packaging", "HTTP", "Async"],
    "minutes": [40, 55, 60, 45],
    "status": ["done", "done", "done", "review"],
}

df = pd.DataFrame(data)
print("DataFrame head:\n", df.head())

print("\nStats:\n", df.describe())

completed = df[df["status"] == "done"]
print("\nCompleted lessons:\n", completed)

avg_minutes = df.groupby("status")["minutes"].mean()
print("\nAvg minutes per status:\n", avg_minutes)

output = Path(__file__).parent / "summary.csv"
completed.to_csv(output, index=False)
print("Saved summary to", output)
