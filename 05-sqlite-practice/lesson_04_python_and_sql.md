# Lesson 4: Python + SQL Together

## The Best of Both Worlds

So far you've used Python for data analysis (pandas) and SQL for database queries. But in real work, you often need **both at once** — run a SQL query, then analyze the results in Python.

This is one of the most common workflows for data analysts:

1. Query the database to get the data you need
2. Load the results into a pandas DataFrame
3. Analyze, visualize, or export the results

## The Magic Line: pd.read_sql()

Pandas has a built-in function that runs a SQL query and returns the results as a DataFrame:

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("../data/analytics.db")

df = pd.read_sql("SELECT * FROM sales_data", conn)
print(df.head())
```

That's it. One line to go from SQL to pandas. The column names, data types, and all the data come through automatically.

## Why Use pd.read_sql()?

You might wonder: "Why not just load the CSV directly with pd.read_csv()?"

Good question. Here's why `pd.read_sql()` matters:

1. **Databases are faster for large data.** A SQL query can filter millions of rows and return only what you need. Loading a huge CSV and filtering in pandas is slower.

2. **SQL can do the heavy lifting.** Let the database handle joins, aggregations, and filtering. Then pandas handles the final analysis and visualization.

3. **Real jobs use databases.** Most company data lives in databases, not CSV files. You'll query databases daily as an analyst.

## Practical Examples

### Query, then visualize

```python
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("../data/analytics.db")

# Let SQL do the aggregation
df = pd.read_sql("""
    SELECT category, SUM(revenue) as total_revenue
    FROM sales_data
    GROUP BY category
    ORDER BY total_revenue DESC
""", conn)

# Let matplotlib do the visualization
df.plot(kind="bar", x="category", y="total_revenue", legend=False)
plt.title("Revenue by Category")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("revenue_by_category.png")
plt.show()
```

### Parameterized queries (safe filtering)

When filtering based on a variable, use **parameters** instead of string formatting. This prevents SQL injection — a security vulnerability.

```python
# GOOD: Use ? placeholders
department = "Engineering"
df = pd.read_sql(
    "SELECT * FROM employees WHERE department = ?",
    conn,
    params=[department]
)

# BAD: Never do this (SQL injection risk)
# df = pd.read_sql(f"SELECT * FROM employees WHERE department = '{department}'", conn)
```

### Combining data from multiple queries

```python
# Get sales summary
sales = pd.read_sql("""
    SELECT category, SUM(revenue) as revenue
    FROM sales_data
    GROUP BY category
""", conn)

# Get employee count by department
headcount = pd.read_sql("""
    SELECT department, COUNT(*) as num_employees
    FROM employees
    GROUP BY department
""", conn)

# Now work with both DataFrames in pandas
print("Sales Summary:")
print(sales)
print("\nHeadcount:")
print(headcount)
```

## Writing DataFrames Back to the Database

You can also save a DataFrame as a new table:

```python
# Create a summary DataFrame
summary = pd.read_sql("""
    SELECT category, COUNT(*) as sales_count, SUM(revenue) as total
    FROM sales_data
    GROUP BY category
""", conn)

# Save it as a new table
summary.to_sql("sales_summary", conn, if_exists="replace", index=False)

# Verify it's there
check = pd.read_sql("SELECT * FROM sales_summary", conn)
print(check)
```

This is useful when you want to save analysis results back to the database for others to query.

## Common Workflow Pattern

Here's a realistic analyst workflow:

```python
import sqlite3
import pandas as pd

# 1. Connect
conn = sqlite3.connect("../data/analytics.db")

# 2. Query
df = pd.read_sql("SELECT * FROM titanic WHERE Age IS NOT NULL", conn)

# 3. Analyze
avg_age_by_class = df.groupby("Pclass")["Age"].mean()
print(avg_age_by_class)

# 4. Close
conn.close()
```

## Try It Yourself

Run `lesson_04_python_and_sql.py` to see these patterns in action. Then try writing your own queries against the external datasets.
