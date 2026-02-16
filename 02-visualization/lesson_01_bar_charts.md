# Lesson 1: Bar Charts

## When Do You Use a Bar Chart?

Bar charts are your go-to chart when you want to **compare categories**. Any time you ask a question like:

- "Which region has the most sales?"
- "What product sells the most?"
- "How does this year compare to last year by department?"

...a bar chart is probably the right choice. Each bar represents a category, and the length (or height) of the bar tells you the value.

## How matplotlib Works

matplotlib is the most popular charting library in Python. Here is the basic recipe for creating any chart:

1. **Create a figure** -- this is your blank canvas
2. **Add your data** -- tell matplotlib what to draw
3. **Add labels** -- title, axis labels, etc.
4. **Show or save** -- display on screen or save to a file

Here is what that looks like in code:

```python
import matplotlib.pyplot as plt

# Step 1: Create a figure (the canvas)
plt.figure(figsize=(8, 5))

# Step 2: Add data (draw a bar chart)
plt.bar(["Apples", "Bananas", "Cherries"], [30, 50, 20])

# Step 3: Add labels
plt.title("Fruit Sales")
plt.xlabel("Fruit")
plt.ylabel("Number Sold")

# Step 4: Show it
plt.show()
```

That's it! Four steps and you have a chart.

## Figure and Axes: The Canvas Analogy

matplotlib has two key concepts you will see everywhere:

- **Figure** -- Think of this as the **canvas**. It is the entire image, including any white space around the edges.
- **Axes** -- Think of this as the **chart on the canvas**. It is where the actual bars, lines, or dots appear.

A figure can hold one chart or many charts (side by side, for example). For now, we will stick with one chart per figure. Just remember:

> **Figure = the canvas. Axes = the chart on the canvas.**

## Vertical vs. Horizontal Bar Charts

There are two flavors of bar chart:

- **Vertical bars** (`plt.bar`) -- Categories on the x-axis, values going up. This is the default and most common style.
- **Horizontal bars** (`plt.barh`) -- Categories on the y-axis, values going right. This is handy when your category names are long and would overlap on the x-axis.

Use vertical when your category names are short (like region names). Use horizontal when the names are longer (like product names or job titles).

## Key Parameters

Here are the most useful things you can customize:

| Parameter | What It Does | Example |
|-----------|-------------|---------|
| `color` | Changes the bar color | `color="steelblue"` |
| `figsize` | Sets the width and height of the canvas (in inches) | `figsize=(8, 5)` |
| `plt.title()` | Adds a title above the chart | `plt.title("Sales by Region")` |
| `plt.xlabel()` | Labels the x-axis | `plt.xlabel("Region")` |
| `plt.ylabel()` | Labels the y-axis | `plt.ylabel("Revenue ($)")` |
| `plt.tight_layout()` | Prevents labels from getting cut off | Just call it before saving |

## Try It Yourself

Run the script `lesson_01_bar_charts.py` in this folder. It will:

1. Load the sales data
2. Create a vertical bar chart showing total revenue by region
3. Create a horizontal bar chart showing the number of sales by product
4. Save both charts as PNG image files in this folder

After running the script, try changing:
- The `color` to something else (try `"seagreen"`, `"tomato"`, or `"#4C72B0"`)
- The `figsize` to make the chart wider or taller
- The title and axis labels

## What's Next?

In [Lesson 2](lesson_02_line_charts.md), you will learn how to show trends over time using line charts.
