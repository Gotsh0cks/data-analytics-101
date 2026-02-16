# ============================================================
# Lesson 4: Python + SQL Together
# ============================================================
# This script shows how to combine SQL queries with pandas
# for a realistic data analysis workflow.
#
# Before running this, make sure you've run setup_database.py!
# ============================================================

import os
import sqlite3
import pandas as pd

# Connect to the database
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "..", "data", "analytics.db")
conn = sqlite3.connect(DB_PATH)

# ============================================================
# 1. Basic pd.read_sql() — SQL results as a DataFrame
# ============================================================
print("=" * 60)
print("  1. Loading SQL results into a DataFrame")
print("=" * 60)

df = pd.read_sql("SELECT * FROM sales_data LIMIT 5", conn)
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
        ROUND(SUM(revenue), 2) as total_revenue,
        ROUND(AVG(revenue), 2) as avg_revenue
    FROM sales_data
    GROUP BY category
    ORDER BY total_revenue DESC
""", conn)

print(revenue.to_string(index=False))

# ============================================================
# 3. Parameterized queries (safe filtering)
# ============================================================
print("\n" + "=" * 60)
print("  3. Parameterized query — Engineering employees")
print("=" * 60)

department = "Engineering"
engineers = pd.read_sql(
    "SELECT first_name, last_name, job_title, salary FROM employees WHERE department = ?",
    conn,
    params=[department],
)
print(engineers.to_string(index=False))

# ============================================================
# 4. Query external data — Titanic survival analysis
# ============================================================
print("\n" + "=" * 60)
print("  4. Titanic survival by class (external dataset)")
print("=" * 60)

try:
    titanic_summary = pd.read_sql("""
        SELECT
            Pclass as class,
            COUNT(*) as passengers,
            SUM(Survived) as survived,
            ROUND(100.0 * SUM(Survived) / COUNT(*), 1) as survival_pct
        FROM titanic
        GROUP BY Pclass
        ORDER BY Pclass
    """, conn)
    print(titanic_summary.to_string(index=False))
except Exception:
    print("Titanic table not found. Run Module 4's download script")
    print("and then re-run setup_database.py to load external datasets.")

# ============================================================
# 5. Combine SQL + pandas analysis
# ============================================================
print("\n" + "=" * 60)
print("  5. SQL query -> pandas analysis -> insight")
print("=" * 60)

employees = pd.read_sql("SELECT * FROM employees", conn)

# pandas analysis on the query results
print("Department salary statistics:")
salary_stats = employees.groupby("department")["salary"].agg(["mean", "min", "max"])
salary_stats.columns = ["Average", "Minimum", "Maximum"]
salary_stats = salary_stats.round(0).astype(int)
print(salary_stats)

# ============================================================
# 6. Save analysis results back to the database
# ============================================================
print("\n" + "=" * 60)
print("  6. Saving results back to the database")
print("=" * 60)

# Create a summary and save it as a new table
summary = pd.read_sql("""
    SELECT category, SUM(revenue) as total_revenue
    FROM sales_data
    GROUP BY category
""", conn)

summary.to_sql("revenue_summary", conn, if_exists="replace", index=False)
print("Created table: revenue_summary")

# Verify by reading it back
check = pd.read_sql("SELECT * FROM revenue_summary", conn)
print(check.to_string(index=False))

# ============================================================
# Clean up
# ============================================================
conn.close()

print("\n" + "=" * 60)
print("  Done! You've seen how Python and SQL work together.")
print("  Try combining your own queries with pandas analysis.")
print("=" * 60)
