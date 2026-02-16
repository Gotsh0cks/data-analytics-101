# Lesson 3: Pie Charts and Scatter Plots

## Part 1: Pie Charts

### When Do You Use a Pie Chart?

Pie charts are used to show **parts of a whole**. They answer questions like:

- "What percentage of our revenue comes from each category?"
- "How is our budget split across departments?"
- "What share of the market does each product have?"

A pie chart takes a total (the whole pie) and slices it up to show how much each category contributes.

### A Word of Warning About Pie Charts

Pie charts get a bad reputation in data analytics, and for good reason. They have some real limitations:

- **Hard to compare similar slices.** If two slices are 23% and 26%, it is nearly impossible to tell the difference just by looking at the pie. A bar chart would make that difference obvious.
- **Too many slices = a mess.** If you have more than 5 or 6 categories, the pie becomes cluttered and unreadable.
- **No trend over time.** Pie charts show a snapshot. If you need to compare across months or years, use a bar or line chart instead.

**Best practice:** Limit your pie chart to **5 or 6 slices maximum**. If you have more categories, group the smaller ones into an "Other" slice, or just use a bar chart instead.

### How to Create a Pie Chart

```python
plt.pie(values, labels=labels, autopct="%1.1f%%")
```

The key parameters:

| Parameter | What It Does | Example |
|-----------|-------------|---------|
| `labels` | Names for each slice | `labels=["Electronics", "Furniture"]` |
| `autopct` | Shows percentages on each slice | `autopct="%1.1f%%"` (one decimal place) |
| `startangle` | Rotates the pie (in degrees) | `startangle=90` (starts at the top) |
| `colors` | Sets custom colors for slices | `colors=["steelblue", "coral"]` |

The `autopct` format string looks weird, but here is what it means: `%1.1f%%` says "show one decimal place, then a literal percent sign." So 0.2345 becomes "23.5%".

---

## Part 2: Scatter Plots

### When Do You Use a Scatter Plot?

Scatter plots show the **relationship between two numbers**. Each dot represents one row of data, with one number on the x-axis and another on the y-axis. They answer questions like:

- "Do customers who order more also spend more?"
- "Is there a relationship between salary and years of experience?"
- "Does advertising spend correlate with revenue?"

### What Correlation Looks Like

When you look at a scatter plot, you are looking for patterns:

- **Positive correlation** -- The dots trend upward from left to right. As one number goes up, the other goes up too. Example: more orders usually means more money spent.
- **Negative correlation** -- The dots trend downward. As one number goes up, the other goes down. Example: as product price goes up, quantity sold may go down.
- **No correlation** -- The dots are scattered randomly with no clear pattern. The two numbers are not related.

Here is a simple way to think about it:

```
Positive:    No correlation:    Negative:
     .  .         .   .              .  .
   .  .         .     .            .  .
  .  .       .    .     .         .  .
 .  .          .    .           .  .
.  .         .       .        .  .
```

### How to Create a Scatter Plot

```python
plt.scatter(x_values, y_values)
```

Useful parameters:

| Parameter | What It Does | Example |
|-----------|-------------|---------|
| `color` or `c` | Dot color | `color="steelblue"` |
| `s` | Dot size | `s=50` |
| `alpha` | Transparency (0=invisible, 1=solid) | `alpha=0.6` |
| `edgecolors` | Border color around dots | `edgecolors="white"` |

The `alpha` parameter is especially useful when you have many dots that overlap. Setting it to 0.5 or 0.6 makes overlapping dots darker, so you can see where the data clusters.

## Try It Yourself

Run the script `lesson_03_pie_scatter.py` in this folder. It will:

1. Create a pie chart showing revenue share by product category
2. Create a scatter plot showing the relationship between customer orders and spending
3. Save both charts as PNG files

After running, try:
- Adding `explode` to the pie chart to pull a slice out: `explode=(0.05, 0, 0)` (one value per slice)
- Changing the `alpha` on the scatter plot to see the effect of transparency
- Changing `s` to make the dots bigger or smaller

## What's Next?

In [Lesson 4](lesson_04_styling.md), you will learn how to make all of these charts look polished and professional.
