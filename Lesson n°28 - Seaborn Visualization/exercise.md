# Exercise: Topic Performance Dashboard

Build a Seaborn-based dashboard to compare topic performance.

## Requirements

1. Load `topic_scores.csv` containing columns `topic`, `difficulty`, `minutes`, `score`.
2. Create:
   - Boxplot showing score distribution grouped by `difficulty`.
   - Point plot showing average score per topic with `minutes` as size.
3. Apply a Seaborn theme and palette that reinforces difficulty levels.
4. Add annotations for the highest and lowest scoring topics.
5. Save the combined figure as `topic_dashboard.png`.
6. Provide a CLI option (`--show`) to display the plot interactively.
7. Handle missing data by dropping rows with null scores or minutes.

## Stretch Ideas

- Add violin plots for richer distributions.
- Export the computed averages to CSV or JSON.
- Use `sns.lmplot` to observe relationships between minutes and score.

## Tips

- Use `sns.set_theme(style='darkgrid')` or `sns.set_palette('Spectral')`.
- Convert the CLI option with `argparse` and call `plt.show()` when requested.
- Use `df.sort_values('score')` to find highest/lowest topics for annotation.
