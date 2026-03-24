# ============================================================
# Lesson 6: Python + SQL Server
# ============================================================
# This script demonstrates how to connect Python to SQL Server
# and query data directly into pandas DataFrames.
#
# Prerequisites:
#   1. SQL Server running with the DataAnalytics101 database
#      (run 00_setup_database.sql in VS Code first — Ctrl+Shift+E)
#   2. pip install pyodbc pandas
#
# If SQL Server is not running, this script will show an error.
# That is expected — it requires a live database connection.
# ============================================================

import sys

try:
    import pyodbc
except ImportError:
    print("The 'pyodbc' package is not installed.")
    print("Install it by running:  pip install pyodbc")
    sys.exit(1)

import pandas as pd

# ============================================================
# Connection setup
# ============================================================
# Adjust the SERVER line if your SQL Server instance has a
# different name. Common values:
#   localhost           (default instance)
#   localhost\SQLEXPRESS (SQL Server Express)
#   .                   (shorthand for localhost)

CONNECTION_STRING = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=DataAnalytics101;"
    "Trusted_Connection=yes;"
)

print("Connecting to SQL Server...")
try:
    conn = pyodbc.connect(CONNECTION_STRING)
except pyodbc.Error as e:
    print(f"Could not connect to SQL Server: {e}")
    print()
    print("Troubleshooting:")
    print("  1. Make sure SQL Server is running (check Windows Services)")
    print("  2. Make sure you ran 00_setup_database.sql in VS Code (Ctrl+Shift+E)")
    print("  3. Try changing SERVER to localhost\\SQLEXPRESS")
    sys.exit(1)

print("Connected!")

# ============================================================
# 1. Basic pd.read_sql() -- SQL results as a DataFrame
# ============================================================
print("\n" + "=" * 60)
print("  1. Loading SQL results into a DataFrame")
print("=" * 60)

df = pd.read_sql("SELECT TOP 5 * FROM Sales", conn)
print(df)
print(f"\nType: {type(df)}")
print(f"Shape: {df.shape}")

# ============================================================
# 2. Let SQL aggregate, let pandas display
# ============================================================
print("\n" + "=" * 60)
print("  2. Revenue by category (SQL aggregation)")
print("=" * 60)

revenue = pd.read_sql("""
    SELECT
        category,
        COUNT(*) as num_sales,
        CAST(SUM(revenue) AS DECIMAL(10,2)) as total_revenue,
        CAST(AVG(revenue) AS DECIMAL(10,2)) as avg_revenue
    FROM Sales
    GROUP BY category
    ORDER BY total_revenue DESC
""", conn)

print(revenue.to_string(index=False))

# ============================================================
# 3. Parameterized queries (safe filtering)
# ============================================================
print("\n" + "=" * 60)
print("  3. Parameterized query -- Engineering employees")
print("=" * 60)

department = "Engineering"
engineers = pd.read_sql(
    "SELECT first_name, last_name, job_title, salary "
    "FROM Employees WHERE department = ?",
    conn,
    params=[department],
)
print(engineers.to_string(index=False))

# ============================================================
# 4. Combine SQL + pandas analysis
# ============================================================
print("\n" + "=" * 60)
print("  4. SQL query -> pandas analysis -> insight")
print("=" * 60)

employees = pd.read_sql("SELECT * FROM Employees", conn)

print("Department salary statistics:")
salary_stats = employees.groupby("department")["salary"].agg(["mean", "min", "max"])
salary_stats.columns = ["Average", "Minimum", "Maximum"]
salary_stats = salary_stats.round(0).astype(int)
print(salary_stats)

# ============================================================
# Clean up
# ============================================================
conn.close()

print("\n" + "=" * 60)
print("  Done! You have seen how Python and SQL Server work together.")
print("  Try combining your own queries with pandas analysis.")
print("=" * 60)
