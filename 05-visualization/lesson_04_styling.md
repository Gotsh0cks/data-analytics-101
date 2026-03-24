# Lesson 4: Styling and Polish

## Why Presentation Matters

You have learned how to make bar charts, line charts, pie charts, and scatter plots. But right now, they probably look a bit plain -- default colors, small text, no grid lines. That is fine for exploring data on your own, but when you share a chart with your boss, your team, or in a report, it needs to look professional.

Your boss doesn't want to see default gray charts. A polished chart shows that you care about the details and makes your analysis easier to understand.

Good news: it does not take much effort to go from "rough draft" to "presentation-ready."

## The Basics: Titles, Labels, and Legends

Every chart you share should have these three things at minimum:

1. **A clear title** -- What is this chart showing? Make it specific. "Revenue" is vague. "Monthly Revenue by Region (2024)" is clear.
2. **Axis labels** -- What do the x-axis and y-axis represent? Include units when relevant (e.g., "Revenue ($)" not just "Revenue").
3. **A legend** -- If your chart has multiple colors or lines, the reader needs to know what each one represents.

```python
plt.title("Monthly Revenue by Region (2024)", fontsize=14, fontweight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.legend(fontsize=10)
```

## Changing Colors

### Individual Colors

You can set colors using:
- **Named colors:** `"steelblue"`, `"coral"`, `"seagreen"`, `"tomato"`, `"slategray"`
- **Hex codes:** `"#4C72B0"`, `"#DD8452"`, `"#55A868"`
- **RGB tuples:** `(0.3, 0.5, 0.7)`

### Color Palettes

Instead of picking individual colors, you can use a **palette** -- a pre-made set of colors that look good together. seaborn comes with many built-in palettes:

```python
import seaborn as sns

colors = sns.color_palette("Set2", 4)   # Get 4 colors from the "Set2" palette
colors = sns.color_palette("pastel")     # Soft, pastel colors
colors = sns.color_palette("deep")       # Bold, saturated colors
```

## Adding Grid Lines

Grid lines help readers estimate values more accurately:

```python
plt.grid(axis="y", alpha=0.3)        # Horizontal grid lines only, very subtle
plt.grid(True, alpha=0.3)            # Both directions
```

The `alpha` parameter controls transparency. A value around 0.3 gives you subtle grid lines that help without being distracting.

## Adjusting Figure Size

The `figsize` parameter controls how big your chart is, measured in inches (width, height):

```python
plt.figure(figsize=(10, 6))  # 10 inches wide, 6 inches tall
```

General guidelines:
- **Bar charts:** `(8, 5)` or `(10, 6)` -- slightly wider than tall
- **Pie charts:** `(7, 7)` -- square looks best
- **Line charts:** `(10, 5)` -- wider to give the trend room to breathe
- **Presentations:** Go bigger, like `(12, 6)`

## Introduction to seaborn

**seaborn** is a library built on top of matplotlib. It does two things:

1. **Better defaults** -- Just importing seaborn and setting a style makes all your charts look nicer, even if you use plain matplotlib commands.
2. **Easier syntax** -- seaborn has its own chart functions that can create complex charts with less code.

### Setting a Style

The easiest win is to set a seaborn style at the top of your script:

```python
import seaborn as sns

sns.set_style("whitegrid")  # Clean white background with grid lines
```

Available styles:
- `"whitegrid"` -- White background with gray grid lines (most popular)
- `"darkgrid"` -- Gray background with white grid lines
- `"white"` -- Clean white background, no grid
- `"dark"` -- Gray background, no grid
- `"ticks"` -- White background with tick marks on axes

### seaborn Bar Plots

seaborn can create bar charts directly from a DataFrame, which saves you the groupby step:

```python
sns.barplot(data=df, x="region", y="revenue", estimator="sum")
```

This one line replaces the groupby + plt.bar combo. seaborn figures out the grouping automatically.

### seaborn Scatter Plots

seaborn scatter plots can add extra information through color and size:

```python
sns.scatterplot(data=df, x="total_orders", y="total_spent", hue="state", s=80)
```

The `hue` parameter colors dots by a category (like state or region), so you can see groups within your data.

## Putting It All Together

A "presentation-ready" chart checklist:

- [ ] Clear, specific title
- [ ] Labeled axes with units
- [ ] Legend (if multiple groups)
- [ ] Appropriate colors (not the defaults)
- [ ] Grid lines for readability
- [ ] Right size for the context
- [ ] `tight_layout()` to prevent cutoff

## Try It Yourself

Run the script `lesson_04_styling.py` in this folder. It will:

1. Create a polished grouped bar chart using seaborn
2. Create a styled scatter plot with seaborn
3. Demonstrate color palettes, proper labels, grids, and legends
4. Save all charts as PNG files

After running, try:
- Switching between seaborn styles (`"darkgrid"`, `"white"`, etc.)
- Using different color palettes (`"Set1"`, `"muted"`, `"bright"`)
- Changing `fontsize` on the title and labels

## What's Next?

Head over to the [Exercises](exercises.md) to practice everything you have learned in this module!
