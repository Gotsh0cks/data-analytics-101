# Module 5: Visualizing & Presenting Data

## What This Module Covers

Data analysis means nothing if you cannot communicate what you found. Visualization is how you turn numbers into stories that people understand and act on.

This module teaches **two complementary approaches**:

- **Part 1: Code-Based Visualization** — Python with matplotlib and seaborn. Precise, reproducible, scriptable.
- **Part 2: Interactive Dashboards** — Tableau Public. Drag-and-drop, interactive, ready to share.

## When to Use Which

| Situation | Use Code (matplotlib) | Use Tableau |
|-----------|----------------------|-------------|
| Quick exploration for yourself | Yes | |
| Automated reports (run weekly) | Yes | |
| Precise control over every pixel | Yes | |
| Presenting to stakeholders | | Yes |
| Viewers need to click and explore | | Yes |
| Building a public portfolio | | Yes |
| Static charts for a report/paper | Yes | |

Most analysts use both. Code for analysis, Tableau for presentation.

## Lessons

### Part 1: Code-Based Visualization (matplotlib / seaborn)

| Lesson | Topic | Files |
|--------|-------|-------|
| 1 | [Bar Charts](lesson_01_bar_charts.md) | `.md` / `.py` |
| 2 | [Line Charts](lesson_02_line_charts.md) | `.md` / `.py` |
| 3 | [Pie & Scatter Charts](lesson_03_pie_scatter.md) | `.md` / `.py` |
| 4 | [Styling and Polish](lesson_04_styling.md) | `.md` / `.py` |

### Part 2: Interactive Dashboards (Tableau Public)

| Lesson | Topic | File |
|--------|-------|------|
| 5 | [Connecting to Data](lesson_05_tableau_connect_data.md) | `.md` |
| 6 | [Your First Chart](lesson_06_tableau_first_chart.md) | `.md` |
| 7 | [Chart Types & Formatting](lesson_07_tableau_charts_formatting.md) | `.md` |
| 8 | [Interactive Dashboards](lesson_08_tableau_dashboards.md) | `.md` |
| 9 | [Publishing & Sharing](lesson_09_tableau_publish.md) | `.md` |

## Preparing Data for Tableau

Run `prepare_data_for_tableau.py` to generate clean CSV files optimized for Tableau:

```bash
python 05-visualization/prepare_data_for_tableau.py
```

## Practice

After completing all lessons, head to [Exercises](exercises.md) for practice problems covering both matplotlib and Tableau.

## Prerequisites

- Completed Modules 2-3 (you need to understand the data and basic pandas)
- Python libraries installed: `pip install matplotlib seaborn pandas`
- Tableau Public installed (from Module 1)

## A Quick Note

Charts are one of the most powerful tools in data analytics. When you hand someone a table with 100 rows of numbers, their eyes glaze over. When you hand them a clean bar chart, they immediately see the story. This module teaches you how to tell that story — with both code and drag-and-drop tools.
