# Module 2: Spreadsheets & Excel

## What This Module Covers

Spreadsheets are the most common data tool in the world. If you work in an office, you will use spreadsheets. Excel (or Google Sheets) is often the first tool analysts reach for when they need to explore, summarize, or share data.

In this module, you will learn to:

- Navigate a spreadsheet and understand rows, columns, and cells
- Write formulas to calculate totals, averages, and more
- Sort and filter data to find what you need
- Build pivot tables to summarize data by category
- Create charts directly inside Excel

## Why Start with Excel?

Even though this course also teaches Python, SQL, and Tableau, we start with Excel for three reasons:

1. **You will use it every day.** Even analysts who primarily use Python still open Excel regularly.
2. **It builds intuition.** Seeing data in a grid helps you understand what filtering, sorting, and aggregating *mean* before you do them in code.
3. **Employers expect it.** Excel appears in 85%+ of data analyst job postings.

## Before You Start

You need a spreadsheet application. Any of these will work:

- **Microsoft Excel** (recommended) — If you have a Microsoft 365 subscription or a standalone copy
- **Google Sheets** (free) — Works in your browser at sheets.google.com. Almost identical to Excel for our purposes
- **LibreOffice Calc** (free) — A free desktop app. Download from libreoffice.org

If you are not sure which to use: if you have Excel, use Excel. If not, Google Sheets is the easiest free option.

## Generating Sample Files

Run `create_excel_samples.py` to generate .xlsx files from the course datasets:

```bash
python 02-spreadsheets/create_excel_samples.py
```

This creates ready-to-use Excel workbooks in `data/excel/` that you will open throughout the lessons.

## Lessons

| Lesson | Topic | What You Will Do |
|--------|-------|-----------------|
| 1 | [Spreadsheet Basics](lesson_01_spreadsheet_basics.md) | Open a file, navigate rows and columns, understand cells |
| 2 | [Formulas and Functions](lesson_02_formulas_and_functions.md) | SUM, AVERAGE, COUNT, MIN, MAX, IF, VLOOKUP |
| 3 | [Sorting and Filtering](lesson_03_sorting_filtering.md) | Sort by any column, filter rows, conditional formatting |
| 4 | [Pivot Tables](lesson_04_pivot_tables.md) | Summarize thousands of rows in seconds |
| 5 | [Excel Charts](lesson_05_excel_charts.md) | Bar, line, and pie charts — right inside Excel |

## Practice

After completing the lessons, test your skills with the [Exercises](exercises.md).

## Next Steps

Once you are comfortable with Excel, move on to [Module 3: Data Analysis with Python](../03-data-analysis/) — where you will learn to do the same things with code, unlocking the ability to work with bigger datasets and automate your work.
