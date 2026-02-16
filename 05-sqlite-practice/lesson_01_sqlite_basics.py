# ============================================================
# Lesson 1: SQLite Basics
# ============================================================
# This script demonstrates how to connect to a SQLite database,
# list tables, and run basic queries — all from Python.
#
# Before running this, make sure you've run setup_database.py!
# ============================================================

import os
import sqlite3

# Connect to the database
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "..", "data", "analytics.db")

print("Connecting to database...")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ============================================================
# 1. List all tables in the database
# ============================================================
print("\n" + "=" * 50)
print("  Tables in the database")
print("=" * 50)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    # Count rows in each table
    cursor.execute(f"SELECT COUNT(*) FROM [{table_name}]")
    count = cursor.fetchone()[0]
    print(f"  {table_name}: {count:,} rows")

# ============================================================
# 2. Run a simple SELECT query
# ============================================================
print("\n" + "=" * 50)
print("  First 5 rows from sales_data")
print("=" * 50)

cursor.execute("SELECT * FROM sales_data LIMIT 5")

# Get column names
columns = [desc[0] for desc in cursor.description]
print(f"\n  Columns: {', '.join(columns)}")

# Print each row
rows = cursor.fetchall()
print()
for row in rows:
    print(f"  {row}")

# ============================================================
# 3. Run a query with WHERE
# ============================================================
print("\n" + "=" * 50)
print("  Electronics products only")
print("=" * 50)

cursor.execute("""
    SELECT product, quantity, revenue
    FROM sales_data
    WHERE category = 'Electronics'
    ORDER BY revenue DESC
    LIMIT 5
""")

rows = cursor.fetchall()
print(f"\n  {'Product':<20} {'Qty':>5} {'Revenue':>10}")
print(f"  {'-'*20} {'-'*5} {'-'*10}")
for row in rows:
    print(f"  {row[0]:<20} {row[1]:>5} {row[2]:>10.2f}")

# ============================================================
# 4. Run an aggregation query
# ============================================================
print("\n" + "=" * 50)
print("  Total revenue by category")
print("=" * 50)

cursor.execute("""
    SELECT category, SUM(revenue) as total_revenue
    FROM sales_data
    GROUP BY category
    ORDER BY total_revenue DESC
""")

rows = cursor.fetchall()
print(f"\n  {'Category':<20} {'Total Revenue':>15}")
print(f"  {'-'*20} {'-'*15}")
for row in rows:
    print(f"  {row[0]:<20} ${row[1]:>13,.2f}")

# ============================================================
# Clean up
# ============================================================
conn.close()

print("\n" + "=" * 50)
print("  Done! Try modifying the queries above to explore more.")
print("=" * 50)
