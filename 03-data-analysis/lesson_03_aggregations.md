# Lesson 3: Aggregations

Aggregation means **combining many rows into a summary**. Instead of looking at every single sale, you might want to know the total revenue, the average order size, or the best-selling product. These are all aggregations.

If you've ever used SUM, AVERAGE, or COUNT formulas in Excel, you already understand the idea. pandas just makes it faster and more flexible.

## Basic Aggregations

pandas gives you simple methods to summarize a column:

```python
df["revenue"].sum()      # Total of all values
df["revenue"].mean()     # Average (mean) of all values
df["revenue"].min()      # Smallest value
df["revenue"].max()      # Largest value
df["revenue"].count()    # Number of non-missing values
df["revenue"].median()   # Middle value when sorted
```

Each of these takes an entire column and reduces it down to a single number. That's the core idea of aggregation: many values in, one value out.

## Group By: Summaries for Each Category

Here's where things get really useful. What if you don't just want the total revenue you want the **total revenue for each region**?

In Excel, you might use a Pivot Table for this. In pandas, you use `.groupby()`:

```python
df.groupby("region")["revenue"].sum()
```

Read this from left to right:

1. **`df.groupby("region")`** Split the data into groups, one for each region
2. **`["revenue"]`** Focus on the revenue column
3. **`.sum()`** Add up the values within each group

The result looks like this:

```
region
East     12500.00
North    15300.00
South    11200.00
West     13800.00
```

You can group by any column and use any aggregation:

```python
# Average revenue per product
df.groupby("product")["revenue"].mean()

# Total quantity sold per region
df.groupby("region")["quantity"].sum()
```

### Grouping by Multiple Columns

You can also group by more than one column to get more detailed summaries:

```python
# Average revenue by region AND product
df.groupby(["region", "product"])["revenue"].mean()
```

This gives you the average revenue for every combination of region and product.

## Multiple Aggregations at Once with `.agg()`

What if you want the total, average, and maximum revenue all at once? Use `.agg()`:

```python
df.groupby("region")["revenue"].agg(["sum", "mean", "max"])
```

This creates a table where each row is a region and each column is a different aggregation. It's like building a mini report in one line of code.

You can also apply different aggregations to different columns:

```python
df.groupby("region").agg(
    total_revenue=("revenue", "sum"),
    avg_quantity=("quantity", "mean"),
    num_sales=("revenue", "count")
)
```

This is very similar to what you'd build in an Excel Pivot Table, but you have full control over exactly what calculations to include.

## Quick Statistical Summary: `.describe()`

If you want a quick overview of a numeric column, use `.describe()`:

```python
df["revenue"].describe()
```

This gives you all the key statistics at once:

- **count** How many values
- **mean** The average
- **std** Standard deviation (how spread out the values are)
- **min** The smallest value
- **25%** The value at the 25th percentile
- **50%** The median (middle value)
- **75%** The value at the 75th percentile
- **max** The largest value

Don't worry if percentiles and standard deviation sound new. The important ones to start with are count, mean, min, and max.

## Try It Out

Run the script `lesson_03_aggregations.py` to see these examples:

```
python lesson_03_aggregations.py
```

## Key Takeaways

- **Aggregation** means summarizing many rows into fewer numbers (totals, averages, etc.).
- Use `.sum()`, `.mean()`, `.min()`, `.max()`, and `.count()` on any numeric column.
- Use `.groupby("column")` to get summaries **for each category**, like a Pivot Table.
- Use `.agg()` to calculate multiple summaries at once.
- Use `.describe()` for a quick statistical overview of a column.
