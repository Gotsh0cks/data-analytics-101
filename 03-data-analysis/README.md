# Module 3: Data Analysis with Python

## What This Module Covers

In Module 2, you learned to analyze data in Excel — formulas, sorting, filtering, pivot tables, and charts. Excel is great, but it has limits. When your dataset grows to hundreds of thousands of rows, when you need to repeat the same analysis every week, or when you want to document exactly what you did so someone else can verify it — you need code.

In this module, you will learn **pandas** — a Python library that gives you Excel-like power through code. If Excel is a Swiss Army knife, pandas is a full workshop.

## Excel vs. pandas — A Quick Comparison

| Task | In Excel | In pandas |
|------|----------|-----------|
| Open a file | File > Open | `pd.read_csv("file.csv")` |
| View first rows | Scroll to top | `df.head()` |
| Sort by column | Data > Sort | `df.sort_values("column")` |
| Filter rows | Data > Filter | `df[df["column"] > 100]` |
| Pivot table | Insert > PivotTable | `df.groupby("column").sum()` |
| Count rows | COUNTA formula | `len(df)` |

The syntax is different, but the *concepts* are the same. You already know what filtering and sorting mean — now you will learn to express those ideas in code.

## Why Code Instead of Clicking?

1. **Scale.** Excel struggles past ~1 million rows. Pandas handles millions easily.
2. **Reproducibility.** A script documents every step. You can re-run it anytime and get the same result.
3. **Automation.** Need to run the same analysis every Monday? A script does it in one click.
4. **Collaboration.** Code can be reviewed, version-controlled (Git), and shared precisely.

## Lessons

| Lesson | Topic | What You Will Do |
|--------|-------|-----------------|
| 1 | [Loading Data](lesson_01_loading_data.md) | Open a CSV file and explore what is inside |
| 2 | [Filtering and Sorting](lesson_02_filtering_sorting.md) | Find specific rows and put them in order |
| 3 | [Aggregations](lesson_03_aggregations.md) | Calculate totals, averages, and summaries (the code version of pivot tables) |
| 4 | [Data Cleaning](lesson_04_data_cleaning.md) | Fix missing values, duplicates, and bad data |

Each lesson has a `.md` explanation and a `.py` script you can run.

## Practice

After completing the lessons, test your skills with the [Exercises](exercises.md).

## Datasets Used

- `../data/sales_data.csv` — The same sales data you explored in Excel
- `../data/employees.csv` — Employee records (used in exercises)
- `../data/customers.csv` — Customer information (used in exercises)

## Prerequisites

- Completed Module 2 (so you understand what filtering, sorting, and aggregating mean)
- Python 3 installed (from Module 1)
- pandas installed: `pip install pandas`

---

> **Tip from Module 2:** Remember how pivot tables let you summarize data by category in seconds? In Lesson 3, you will learn `groupby()` — the pandas equivalent. Same concept, different tool.
