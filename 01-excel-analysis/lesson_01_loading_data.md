# Lesson 1: Loading Data

## What is a CSV File?

CSV stands for **Comma-Separated Values**. It's the simplest way to store spreadsheet data as plain text. Instead of a fancy Excel file with formatting, colors, and formulas, a CSV file just stores the raw data with commas between each value.

Here's what a CSV file looks like if you open it in a text editor:

```
name,age,city
Alice,30,New York
Bob,25,Chicago
Carol,35,Denver
```

The first line is the **header row** — it tells you the name of each column. Every line after that is a row of data. Each value is separated by a comma, which is where the name comes from.

Almost every data tool can read and write CSV files, which is why they are so popular. If you have an Excel file, you can save it as a CSV by choosing "Save As" and selecting "CSV" as the format.

## What is pandas?

**pandas** is a Python library that makes it easy to work with data in tables (rows and columns). If you've used Excel or Google Sheets before, pandas will feel familiar — except instead of clicking around a spreadsheet, you write short commands.

Why use pandas instead of Excel?

- It can handle millions of rows without slowing down
- You can automate repetitive tasks by writing scripts
- It's free and works on any computer
- It connects easily to databases, websites, and other data sources

## Loading a CSV File

To use pandas, you first need to **import** it. By convention, everyone gives it the short nickname `pd`:

```python
import pandas as pd
```

Then you load a CSV file using `pd.read_csv()`:

```python
df = pd.read_csv("../data/sales_data.csv")
```

This reads the file and stores the data in a variable called `df`. The `df` stands for **DataFrame**, which is the pandas name for a table of data. Think of a DataFrame as a spreadsheet living inside Python.

## Exploring Your Data

Once you've loaded your data, you'll want to take a look at it. Here are the most useful commands:

### See the first few rows: `.head()`

```python
df.head()
```

This shows you the first 5 rows of your data. It's a great way to quickly see what your data looks like. You can also pass a number to see more or fewer rows, like `df.head(10)` for the first 10 rows.

### See the last few rows: `.tail()`

```python
df.tail()
```

This shows the last 5 rows. Useful for checking if your data loaded completely.

### Check the size: `.shape`

```python
df.shape
```

This tells you how many rows and columns your data has, as a pair of numbers like `(1000, 6)` — meaning 1,000 rows and 6 columns. Notice there are no parentheses after `shape` — it's a property, not a function.

### See column names and types: `.dtypes`

```python
df.dtypes
```

This shows each column name and its **data type**. Common types include:

| Type | What It Means | Example |
|------|--------------|---------|
| `int64` | Whole numbers | 1, 42, -7 |
| `float64` | Decimal numbers | 3.14, 99.99 |
| `object` | Text (strings) | "North", "Widget" |
| `datetime64` | Dates and times | 2024-01-15 |

### Get a full summary: `.info()`

```python
df.info()
```

This gives you a complete overview: the number of rows, each column's name and type, and how many non-missing values each column has. It's like a health check for your data.

## Putting It All Together

Run the script `lesson_01_loading_data.py` to see all of these commands in action with the sales data. Open a terminal, navigate to this folder, and type:

```
python lesson_01_loading_data.py
```

## Key Takeaways

- A **CSV file** is spreadsheet data saved as plain text with commas between values.
- **pandas** is a Python library for working with tables of data.
- Use `pd.read_csv()` to load a CSV file into a **DataFrame**.
- Use `.head()`, `.tail()`, `.shape`, `.dtypes`, and `.info()` to explore your data.
- Always look at your data after loading it to make sure everything looks right.
