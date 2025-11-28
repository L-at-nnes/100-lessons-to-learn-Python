# Exercise: Study Analytics Dashboard

Use Pandas to analyze a CSV of study sessions.

## Requirements

1. Load `sessions.csv` with columns: `date`, `topic`, `minutes`, `mood`.
2. Print the first 5 rows and summary statistics for minutes.
3. Group by topic to display total minutes and average mood (map moods to numeric scores before averaging).
4. Find the top 3 longest sessions.
5. Save a new CSV `topic_summary.csv` with columns `topic`, `total_minutes`, `session_count` sorted by total minutes.
6. Create a bar chart (using `matplotlib`) showing minutes per topic and save it as `topic_chart.png`.
7. Handle missing data: fill missing moods with `neutral` and drop rows with missing minutes.

## Stretch Ideas

- Add a command-line interface to specify the input CSV path.
- Compute streaks by counting consecutive days of study.
- Export summary statistics to JSON for further processing.

## Tips

- Use `pd.read_csv(path)` and `df.dropna(subset=['minutes'])`.
- Map moods to scores with a dictionary: `{'bad': 1, 'neutral': 2, 'good': 3}`.
- Use `df.nlargest(3, 'minutes')` to find the longest sessions.
