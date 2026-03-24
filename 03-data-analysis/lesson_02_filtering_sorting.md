# Lesson 2: Filtering and Sorting

Now that you know how to load data and look at it, let's learn how to **find specific information** in your data. This is like using the filter and sort features in Excel, but with a lot more power.

## Selecting Specific Columns

Sometimes your dataset has many columns but you only care about a few. In Excel, you might hide the columns you don't need. In pandas, you select just the ones you want:

```python
# Select a single column
df["product"]

# Select multiple columns (note the double brackets)
df[["product", "revenue"]]
```

When you select multiple columns, you pass a **list** of column names inside the brackets. That's why there are two sets of brackets — the outer ones are for pandas, the inner ones create the list.

## Filtering Rows by a Condition

Filtering means keeping only the rows that match some condition. It's like clicking the filter dropdown in Excel and choosing specific values.

In pandas, you write the condition inside brackets:

```python
# Keep only rows where region is "North"
df[df["region"] == "North"]
```

Here's what's happening step by step:

1. `df["region"] == "North"` checks every row and returns `True` or `False`
2. Putting that inside `df[...]` keeps only the rows where the result is `True`

You can use these comparison operators:

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equals | `df["region"] == "North"` |
| `!=` | Not equal to | `df["region"] != "North"` |
| `>` | Greater than | `df["revenue"] > 500` |
| `<` | Less than | `df["quantity"] < 10` |
| `>=` | Greater than or equal to | `df["revenue"] >= 500` |
| `<=` | Less than or equal to | `df["quantity"] <= 5` |

## Combining Multiple Conditions

What if you want rows that match **more than one** condition? Use `&` for "and" and `|` for "or". Make sure to wrap each condition in parentheses:

```python
# North region AND revenue over 500
df[(df["region"] == "North") & (df["revenue"] > 500)]

# North region OR South region
df[(df["region"] == "North") | (df["region"] == "South")]
```

- **`&` (and):** Both conditions must be true.
- **`|` (or):** At least one condition must be true.

The parentheses around each condition are required. Without them, Python gets confused about the order of operations.

## Sorting Data

Sorting rearranges your rows in order. Use `.sort_values()`:

```python
# Sort by revenue, lowest to highest (ascending — the default)
df.sort_values("revenue")

# Sort by revenue, highest to lowest (descending)
df.sort_values("revenue", ascending=False)

# Sort by multiple columns
df.sort_values(["region", "revenue"], ascending=[True, False])
```

That last example sorts by region A-Z first, and then within each region, sorts by revenue from highest to lowest.

## Counting Values: `.value_counts()`

A very common question is "how many times does each value appear?" The `.value_counts()` method answers this instantly:

```python
# How many sales in each region?
df["region"].value_counts()

# How many sales of each product?
df["product"].value_counts()
```

This is like creating a quick tally or frequency table. The results are sorted from most common to least common by default.

## Try It Out

Run the script `lesson_02_filtering_sorting.py` to see these examples in action:

```
python lesson_02_filtering_sorting.py
```

## Key Takeaways

- Use `df["column_name"]` to select one column, or `df[["col1", "col2"]]` for multiple.
- Filter rows by putting a condition inside brackets: `df[df["column"] > value]`.
- Combine conditions with `&` (and) or `|` (or), wrapping each condition in parentheses.
- Sort with `.sort_values("column")` and use `ascending=False` for descending order.
- Use `.value_counts()` to quickly count how often each value appears.
