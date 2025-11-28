"""Lesson 26 - Pandas DataFrames (Solution)

Study analytics dashboard implementation.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = Path(__file__).parent / "sessions.csv"
SUMMARY_PATH = Path(__file__).parent / "topic_summary.csv"
CHART_PATH = Path(__file__).parent / "topic_chart.png"

MOOD_SCORES = {"bad": 1, "neutral": 2, "good": 3}

def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["mood"] = df["mood"].fillna("neutral")
    df = df.dropna(subset=["minutes"])
    return df

def analyze(df: pd.DataFrame) -> None:
    print("Head:\n", df.head())
    print("\nMinutes stats:\n", df["minutes"].describe())

def topic_summary(df: pd.DataFrame) -> pd.DataFrame:
    df["mood_score"] = df["mood"].map(MOOD_SCORES)
    summary = df.groupby("topic").agg(
        total_minutes=("minutes", "sum"),
        session_count=("minutes", "count"),
        avg_mood=("mood_score", "mean"),
    )
    summary = summary.sort_values("total_minutes", ascending=False)
    summary.to_csv(SUMMARY_PATH)
    return summary

def plot_chart(summary: pd.DataFrame) -> None:
    summary["total_minutes"].plot(kind="bar", title="Minutes per Topic")
    plt.ylabel("Minutes")
    plt.tight_layout()
    plt.savefig(CHART_PATH)
    plt.close()

def top_sessions(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    print("\nTop sessions:\n", df.nlargest(n, "minutes"))
    return df.nlargest(n, "minutes")

def main() -> None:
    df = load_data(DATA_PATH)
    analyze(df)
    summary = topic_summary(df)
    plot_chart(summary)
    top_sessions(df)
    print("Summary saved to", SUMMARY_PATH)
    print("Chart saved to", CHART_PATH)

if __name__ == "__main__":
    main()
