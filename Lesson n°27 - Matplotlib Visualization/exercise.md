# Exercise: Study Progress Plots

Use Matplotlib to visualize study progress metrics.

## Requirements

1. Load `study_progress.csv` (columns: `day`, `minutes`, `mood`, `topics_completed`).
2. Create two plots:
   - Line chart for `minutes` over `day`.
   - Bar chart comparing `topics_completed` per day.
3. Use subplots (2 rows, 1 column) and share the X-axis.
4. Annotate the highest minutes value with text + arrow.
5. Use a colormap (`plt.cm.Blues`) for the bar chart based on `topics_completed` values.
6. Save the figure as `progress.png` and display it if run interactively.
7. Handle missing data by forward-filling minutes.

## Stretch Ideas

- Add a third subplot for mood scores using scatter plots.
- Add grid lines and custom font sizes for readability.
- Allow the CSV path to be passed as a CLI argument.

## Tips

- Use `plt.subplots(nrows=2, sharex=True)`.
- Use `ax.annotate` for the highlight arrow.
- Map mood strings to numbers if you build the scatter chart stretch goal.
