# Lesson 6: Python + SQL Server

## The Best of Both Worlds

So far you have used Python for data analysis (pandas) and SQL for database queries. But in real work, you often need **both at once** — run a SQL query, then analyze the results in Python.

This is one of the most common workflows for data analysts:

1. Query the database to get the data you need (SQL)
2. Load the results into a pandas DataFrame (Python)
3. Analyze, visualize, or export the results (Python)

## Connecting Python to SQL Server

To connect Python to SQL Server, you need the `pyodbc` library:

```bash
pip install pyodbc
```

### The Connection String

A connection string tells Python where the database is and how to connect:

```python
import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=DataAnalytics101;"
    "Trusted_Connection=yes;"
)
```

Let's break this down:
- **DRIVER** — the software that translates between Python and SQL Server (installed with SQL Server)
- **SERVER** — where the database is running (`localhost` means your own computer)
- **DATABASE** — which database to connect to
- **Trusted_Connection=yes** — use your Windows login (no separate username/password needed)

## The Magic Line: pd.read_sql()

Pandas has a built-in function that runs a SQL query and returns the results as a DataFrame:

```python
import pandas as pd

df = pd.read_sql("SELECT * FROM Sales", conn)
print(df.head())
```

One line to go from SQL to pandas. Column names, data types, and all the data come through automatically.

## Why Use pd.read_sql()?

You might wonder: "Why not just export to CSV and load it with pd.read_csv()?"

1. **Databases are faster.** A SQL query can filter millions of rows server-side and return only what you need.
2. **SQL handles the heavy lifting.** Let the database do joins, aggregations, and filtering. Then pandas handles visualization and final analysis.
3. **It is the real-world workflow.** Most company data lives in databases. You will query them daily.

## Practical Examples

### Query, then visualize

```python
import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=DataAnalytics101;"
    "Trusted_Connection=yes;"
)

# Let SQL do the aggregation
df = pd.read_sql("""
    SELECT category, SUM(revenue) as total_revenue
    FROM Sales
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

When filtering based on a variable, use **parameters** instead of string formatting. This prevents SQL injection — a serious security vulnerability.

```python
# GOOD: Use ? placeholders
department = "Engineering"
df = pd.read_sql(
    "SELECT * FROM Employees WHERE department = ?",
    conn,
    params=[department]
)

# BAD: Never do this (SQL injection risk)
# df = pd.read_sql(f"SELECT * FROM Employees WHERE department = '{department}'", conn)
```

### Combining SQL results with pandas analysis

```python
# Get data from SQL Server
employees = pd.read_sql("SELECT * FROM Employees", conn)

# Use pandas for analysis
salary_stats = employees.groupby("department")["salary"].agg(["mean", "min", "max"])
print(salary_stats)
```

## Writing DataFrames Back to a Database

You can save a pandas DataFrame as a new SQL Server table using `to_sql()`. This requires the `sqlalchemy` library:

```bash
pip install sqlalchemy
```

```python
from sqlalchemy import create_engine

engine = create_engine(
    "mssql+pyodbc://localhost/DataAnalytics101"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

# Save a DataFrame as a new table
summary = df.groupby("category")["revenue"].sum().reset_index()
summary.to_sql("revenue_summary", engine, if_exists="replace", index=False)
```

## Common Workflow Pattern

Here is a realistic analyst workflow:

```python
import pyodbc
import pandas as pd

# 1. Connect
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=DataAnalytics101;"
    "Trusted_Connection=yes;"
)

# 2. Query — let SQL filter the data
df = pd.read_sql("""
    SELECT e.first_name, e.last_name, e.department, e.salary
    FROM Employees e
    WHERE e.salary > 70000
    ORDER BY e.salary DESC
""", conn)

# 3. Analyze in pandas
print(f"High earners: {len(df)}")
print(f"Average salary: ${df['salary'].mean():,.0f}")
print(df.head(10))

# 4. Close
conn.close()
```

## Troubleshooting

**"ODBC Driver 17 for SQL Server not found"**
- Download and install the ODBC driver from Microsoft's website
- Search for "Microsoft ODBC Driver 17 for SQL Server download"

**"Login failed"**
- Make sure SQL Server is running (check Services on Windows)
- Make sure `Trusted_Connection=yes` is in your connection string
- Try `SERVER=localhost\\SQLEXPRESS` if you installed SQL Server Express

**"Database does not exist"**
- Run `00_setup_database.sql` in VS Code first (Ctrl+Shift+E) to create the DataAnalytics101 database

## Try It Yourself

Run `lesson_06_python_and_sql.py` to see these patterns in action. Then try writing your own queries that combine SQL's filtering power with pandas' analysis capabilities.
