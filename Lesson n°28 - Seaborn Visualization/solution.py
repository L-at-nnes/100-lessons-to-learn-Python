"""Lesson 28 - Seaborn Visualization (Solution)

Topic performance dashboard implementation.
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

CSV_PATH = Path(__file__).parent / "topic_scores.csv"
OUT_PATH = Path(__file__).parent / "topic_dashboard.png"

def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.dropna(subset=["score", "minutes"])
    return df

def build_dashboard(df: pd.DataFrame, show: bool = False) -> None:
    sns.set_theme(style="darkgrid")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

    sns.boxplot(data=df, x="difficulty", y="score", palette="Spectral", ax=ax1)
    ax1.set_title("Score Distribution by Difficulty")

    sns.pointplot(
        data=df,
        x="topic",
        y="score",
        hue="difficulty",
        size=df["minutes"],
        palette="viridis",
        ax=ax2,
    )
    ax2.set_title("Average Score per Topic")
    ax2.set_ylabel("Score")
    ax2.set_xlabel("Topic")
    ax2.tick_params(axis="x", rotation=45)

    sorted_df = df.sort_values("score")
    lowest = sorted_df.iloc[0]
    highest = sorted_df.iloc[-1]
    ax2.annotate(
        "Lowest",
        (lowest["topic"], lowest["score"]),
        textcoords="offset points",
        xytext=(0, -10),
        ha="center",
        color="red",
    )
    ax2.annotate(
        "Highest",
        (highest["topic"], highest["score"]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        color="green",
    )

    plt.tight_layout()
    plt.savefig(OUT_PATH)
    if show:
        plt.show()
    plt.close(fig)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Topic performance dashboard")
    parser.add_argument("--show", action="store_true", help="Display the chart")
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    df = load_data(CSV_PATH)
    build_dashboard(df, show=args.show)
    print("Dashboard saved to", OUT_PATH)

if __name__ == "__main__":
    main()
