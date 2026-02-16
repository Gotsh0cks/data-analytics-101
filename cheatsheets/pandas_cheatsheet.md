# Pandas Quick Reference

```python
import pandas as pd
```

## Core Operations

| What You Want To Do | Code |
|---|---|
| Load a CSV | `pd.read_csv("file.csv")` |
| See first N rows | `df.head(N)` |
| See last N rows | `df.tail(N)` |
| Number of rows and columns | `df.shape` |
| Column names | `df.columns` |
| Data types | `df.dtypes` |
| Quick summary | `df.info()` |
| Statistics | `df.describe()` |

## Selecting Data

| What You Want To Do | Code |
|---|---|
| Select one column | `df["column"]` |
| Select multiple columns | `df[["col1", "col2"]]` |
| Filter rows | `df[df["col"] > 100]` |
| Filter with multiple conditions | `df[(df["col1"] > 100) & (df["col2"] == "X")]` |

## Sorting

| What You Want To Do | Code |
|---|---|
| Sort ascending | `df.sort_values("col")` |
| Sort descending | `df.sort_values("col", ascending=False)` |

## Counting and Unique Values

| What You Want To Do | Code |
|---|---|
| Count unique values | `df["col"].value_counts()` |
| Unique values | `df["col"].unique()` |

## Grouping and Aggregation

| What You Want To Do | Code |
|---|---|
| Group and sum | `df.groupby("col")["value"].sum()` |
| Group and average | `df.groupby("col")["value"].mean()` |
| Group with multiple aggregations | `df.groupby("col")["value"].agg(["sum", "mean", "count"])` |

## Handling Missing Data

| What You Want To Do | Code |
|---|---|
| Check for missing values | `df.isnull().sum()` |
| Drop rows with missing values | `df.dropna()` |
| Fill missing values | `df.fillna(0)` |

## Cleaning and Converting

| What You Want To Do | Code |
|---|---|
| Remove duplicates | `df.drop_duplicates()` |
| Convert column type | `df["col"].astype(int)` |
| Convert to datetime | `pd.to_datetime(df["col"])` |

## Saving

| What You Want To Do | Code |
|---|---|
| Save to CSV | `df.to_csv("output.csv", index=False)` |
