# ============================================================
# Module 5: Setup — Create the SQLite Database
# ============================================================
# This script creates a SQLite database file (analytics.db) and
# loads all available CSV datasets into it as tables.
#
# It loads:
#   - The 3 original course datasets (sales, employees, customers)
#   - Any external datasets from Module 4 (titanic, iris, tips, etc.)
#
# Usage:
#   python setup_database.py
#
# Output:
#   ../data/analytics.db
# ============================================================

import os
import sqlite3
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data")
EXTERNAL_DIR = os.path.join(DATA_DIR, "external")
DB_PATH = os.path.join(DATA_DIR, "analytics.db")


def clean_table_name(filename):
    """
    Convert a filename into a clean SQL table name.
    'sales_data.csv' -> 'sales_data'
    'world_happiness_2023.csv' -> 'world_happiness_2023'
    """
    name = os.path.splitext(filename)[0]
    # Replace any characters that aren't letters, digits, or underscores
    name = "".join(c if c.isalnum() or c == "_" else "_" for c in name)
    return name.lower()


def load_csv_to_table(conn, filepath, table_name):
    """Load a CSV file into a SQLite table."""
    try:
        df = pd.read_csv(filepath)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"  [OK] {table_name:30s} ({len(df):,} rows, {len(df.columns)} columns)")
        return True
    except Exception as e:
        print(f"  [ERROR] {table_name}: {e}")
        return False


def main():
    print("=" * 60)
    print("  Creating SQLite Database")
    print("=" * 60)
    print()
    print(f"Database location: {os.path.abspath(DB_PATH)}")
    print()

    # Remove old database if it exists (start fresh)
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("Removed existing database (starting fresh).")
        print()

    # Connect to SQLite (creates the file automatically)
    conn = sqlite3.connect(DB_PATH)

    success_count = 0
    fail_count = 0

    # ---------------------------------------------------------
    # Load original course datasets from data/
    # ---------------------------------------------------------
    print("Loading course datasets:")
    for filename in sorted(os.listdir(DATA_DIR)):
        if filename.endswith(".csv"):
            filepath = os.path.join(DATA_DIR, filename)
            table_name = clean_table_name(filename)
            if load_csv_to_table(conn, filepath, table_name):
                success_count += 1
            else:
                fail_count += 1

    # ---------------------------------------------------------
    # Load external datasets from data/external/
    # ---------------------------------------------------------
    if os.path.exists(EXTERNAL_DIR):
        print()
        print("Loading external datasets:")
        for filename in sorted(os.listdir(EXTERNAL_DIR)):
            if filename.endswith(".csv"):
                filepath = os.path.join(EXTERNAL_DIR, filename)
                table_name = clean_table_name(filename)
                if load_csv_to_table(conn, filepath, table_name):
                    success_count += 1
                else:
                    fail_count += 1
    else:
        print()
        print("No external datasets found. Run Module 4's download script first")
        print("for a richer database. (The course datasets are still loaded.)")

    conn.commit()

    # ---------------------------------------------------------
    # Show a summary of all tables
    # ---------------------------------------------------------
    print()
    print("-" * 60)
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    )
    tables = [row[0] for row in cursor.fetchall()]
    print(f"Database created with {len(tables)} table(s):")
    for table in tables:
        count = conn.execute(f"SELECT COUNT(*) FROM [{table}]").fetchone()[0]
        print(f"  - {table} ({count:,} rows)")

    conn.close()

    print()
    print("=" * 60)
    print(f"  Done! {success_count} tables loaded, {fail_count} failed.")
    print("=" * 60)
    print()
    print("You can now:")
    print("  1. Open analytics.db in DB Browser for SQLite")
    print("  2. Run lesson_01_sqlite_basics.py to start querying")
    print(f"  3. The database file is at: data/analytics.db")


if __name__ == "__main__":
    main()
