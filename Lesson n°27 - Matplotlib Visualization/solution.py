"""Lesson 27 - Matplotlib Visualization (Solution)

Study progress plots implementation.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

CSV_PATH = Path(__file__).parent / "study_progress.csv"
OUT_PATH = Path(__file__).parent / "progress.png"

def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["minutes"] = df["minutes"].fillna(method="ffill")
    return df

def plot_progress(df: pd.DataFrame) -> None:
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))
    ax1.plot(df["day"], df["minutes"], marker="o", color="tab:blue")
    ax1.set_title("Minutes per Day")
    ax1.set_ylabel("Minutes")

    max_idx = df["minutes"].idxmax()
    ax1.annotate(
        "Peak",
        (df.loc[max_idx, "day"], df.loc[max_idx, "minutes"]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        arrowprops={"arrowstyle": "->"},
    )

    colors = plt.cm.Blues(df["topics_completed"] / df["topics_completed"].max())
    ax2.bar(df["day"], df["topics_completed"], color=colors)
    ax2.set_title("Topics Completed")
    ax2.set_xlabel("Day")
    ax2.set_ylabel("Topics")

    plt.tight_layout()
    plt.savefig(OUT_PATH)
    plt.close(fig)

def main() -> None:
    df = load_data(CSV_PATH)
    print("Head:\n", df.head())
    plot_progress(df)
    print("Plot saved to", OUT_PATH)

if __name__ == "__main__":
    main()
