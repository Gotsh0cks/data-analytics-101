# Lesson 4: Data Cleaning

Real-world data is almost never perfect. You'll run into missing values, duplicate rows, and columns with the wrong data type. Cleaning your data is one of the most important (and time-consuming) parts of data analysis. Some say it takes up to 80% of the work.

In this lesson, you'll learn how to spot problems in your data and fix them.

## Why Data Is Messy

Here are some common problems you'll encounter:

- **Missing values** — Some cells are blank. Maybe a customer didn't fill in their email, or a sensor lost its connection for a moment.
- **Duplicate rows** — The same record appears more than once, perhaps because data was imported twice.
- **Wrong data types** — A date column is stored as plain text instead of an actual date, or a number column contains some text entries.

If you don't clean these up, your calculations could be wrong or your code could crash.

## Finding Missing Values

pandas uses `NaN` (which stands for "Not a Number") to represent missing values. You can spot them with `.isnull()`:

```python
# Check which cells are missing (True = missing)
df.isnull()

# Count missing values in each column
df.isnull().sum()
```

The `.isnull().sum()` pattern is one you'll use all the time. It gives you a quick count of how many missing values each column has.

To see the actual rows that have missing data in a specific column:

```python
# Show rows where revenue is missing
df[df["revenue"].isnull()]
```

## Handling Missing Values

You have two main options:

### Option 1: Remove rows with missing values — `.dropna()`

```python
# Drop any row that has at least one missing value
df_clean = df.dropna()

# Drop rows only if a specific column is missing
df_clean = df.dropna(subset=["revenue"])
```

Use this when you have plenty of data and the missing rows are a small fraction of the total.

### Option 2: Fill in missing values — `.fillna()`

```python
# Fill missing revenue with 0
df["revenue"] = df["revenue"].fillna(0)

# Fill missing values with the column's average
df["revenue"] = df["revenue"].fillna(df["revenue"].mean())
```

Use this when you don't want to lose rows. Filling with 0 makes sense for some situations (like "no sale happened"), while filling with the average makes sense for others (like estimating a missing measurement).

There is no single right answer — it depends on your data and what you're trying to learn from it.

## Finding Duplicates

Duplicate rows can inflate your counts and totals. To find them:

```python
# Check for duplicate rows (True = this row is a duplicate of an earlier one)
df.duplicated()

# Count how many duplicates there are
df.duplicated().sum()

# See the actual duplicate rows
df[df.duplicated()]
```

## Removing Duplicates

```python
# Remove duplicate rows, keeping the first occurrence
df_clean = df.drop_duplicates()

# Remove duplicates based on specific columns only
df_clean = df.drop_duplicates(subset=["date", "product", "region"])
```

The `subset` parameter is useful when you want to define what counts as a "duplicate." For example, two rows might have the same date, product, and region but different revenue — you decide whether that's a real duplicate or not.

## Changing Column Types

Sometimes pandas guesses the wrong type for a column. The most common issue is dates being stored as text.

### Convert a column to a different type: `.astype()`

```python
# Convert a column to integer
df["quantity"] = df["quantity"].astype(int)

# Convert a column to float (decimal numbers)
df["revenue"] = df["revenue"].astype(float)
```

### Convert text to a proper date: `pd.to_datetime()`

```python
# Convert the date column from text to a real date type
df["date"] = pd.to_datetime(df["date"])
```

Once a column is a proper date, you can do things like:

```python
# Extract the year
df["date"].dt.year

# Extract the month
df["date"].dt.month

# Filter for dates after a certain point
df[df["date"] > "2024-01-01"]
```

## Saving Cleaned Data

After cleaning, save your work to a new file so you don't overwrite the original:

```python
df.to_csv("../data/sales_data_cleaned.csv", index=False)
```

The `index=False` part prevents pandas from adding an extra column of row numbers to the file. You almost always want to include this.

## Try It Out

Run the script `lesson_04_data_cleaning.py` to walk through cleaning the sales data step by step:

```
python lesson_04_data_cleaning.py
```

## Key Takeaways

- Real data is messy. Always check for missing values, duplicates, and wrong types before doing analysis.
- Use `.isnull().sum()` to count missing values per column.
- Use `.dropna()` to remove rows with missing values, or `.fillna()` to fill them in.
- Use `.duplicated()` and `.drop_duplicates()` to find and remove duplicate rows.
- Use `.astype()` and `pd.to_datetime()` to fix column types.
- Save your cleaned data to a new CSV file with `.to_csv()`.

## What's Next?

Head to the [Exercises](lesson_05_exercises.md) to practice. Once you are done, move on to [Module 4: Databases & SQL](../04-databases-and-sql/).
