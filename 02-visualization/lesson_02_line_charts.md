# Lesson 2: Line Charts

## When Do You Use a Line Chart?

Line charts are the best choice when you want to **show trends over time**. Any time you ask a question like:

- "Are sales going up or down?"
- "Which month had the highest revenue?"
- "How does this quarter compare to last quarter?"

...a line chart will give you the answer visually. The x-axis shows time (days, weeks, months, years) and the y-axis shows the value you are tracking.

**Rule of thumb:** If your x-axis is a date or time period, reach for a line chart first.

## How Dates Work in Charts

Dates can be tricky. When you load a CSV file with pandas, date columns come in as plain text (strings). You need to convert them to actual date objects so that:

- They sort in the correct order (January before February, not alphabetically)
- matplotlib can space them evenly on the x-axis
- You can group by month, quarter, or year

Here is how you convert a column to dates:

```python
df["date"] = pd.to_datetime(df["date"])
```

After converting, you can pull out just the month, year, or day:

```python
df["month"] = df["date"].dt.to_period("M")  # e.g., 2024-01, 2024-02
```

## Creating a Basic Line Chart

The function is `plt.plot()`. It works just like `plt.bar()` but draws a line instead of bars:

```python
plt.plot(x_values, y_values)
```

That is the simplest version. But you almost always want to add a few extras.

## Adding Multiple Lines to One Chart

One of the great strengths of line charts is showing **multiple trends on the same chart** so you can compare them. For example, you might show revenue for each region on the same chart with different colored lines.

The trick is simple: call `plt.plot()` multiple times before calling `plt.show()`. Each call adds another line to the same chart.

```python
plt.plot(months, north_revenue, label="North")
plt.plot(months, south_revenue, label="South")
plt.legend()  # This adds the color-coded labels
```

The `label` parameter names each line, and `plt.legend()` displays those names in a small box on the chart.

## Markers and Line Styles

You can customize how your lines look:

| Parameter | What It Does | Example |
|-----------|-------------|---------|
| `marker` | Adds dots at each data point | `marker="o"` (circles) |
| `linestyle` | Changes the line pattern | `linestyle="--"` (dashed) |
| `linewidth` | Changes line thickness | `linewidth=2` |
| `color` | Sets the line color | `color="steelblue"` |

Common markers: `"o"` (circle), `"s"` (square), `"^"` (triangle), `"D"` (diamond)

Common line styles: `"-"` (solid), `"--"` (dashed), `"-."` (dash-dot), `":"` (dotted)

## Formatting the X-Axis for Dates

When you have many dates on the x-axis, the labels can overlap and become unreadable. Two tricks help:

1. **Rotate the labels:** `plt.xticks(rotation=45)` tilts them at a 45-degree angle
2. **Use tight_layout:** `plt.tight_layout()` makes sure nothing gets cut off

## Try It Yourself

Run the script `lesson_02_line_charts.py` in this folder. It will:

1. Load the sales data and convert dates
2. Create a monthly revenue trend line chart
3. Create a multi-line chart showing revenue by region over time
4. Save both charts as PNG files

After running, try:
- Adding `marker="o"` to the plot calls to see data points
- Changing `linestyle` to `"--"` for dashed lines
- Changing the colors

## What's Next?

In [Lesson 3](lesson_03_pie_scatter.md), you will learn about pie charts and scatter plots.
