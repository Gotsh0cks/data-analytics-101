"""
Module 4 Python + SQL Exercise Solution
=======================================
Run this after trying Exercise 9 yourself:

    python 04-databases-and-sql/solutions/lesson_07_python_sql_solution.py

This script connects to SQL Server, runs the Exercise 9 revenue-by-category
query, prints the pandas DataFrame, and saves the matching bar chart.
"""

import sys
from pathlib import Path


# Edit this connection string if your SQL Server instance has a different name.
# Common SERVER values:
#   localhost
#   localhost\\SQLEXPRESS
#   .
CONNECTION_STRING = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=DataAnalytics101;"
    "Trusted_Connection=yes;"
)


CATEGORY_REVENUE_QUERY = """
SELECT
    category,
    CAST(SUM(revenue) AS DECIMAL(10,2)) AS total_revenue
FROM Sales
GROUP BY category
ORDER BY total_revenue DESC
"""


def print_section(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def load_dependencies():
    try:
        import pyodbc
    except ImportError:
        print("The 'pyodbc' package is not installed.")
        print("Install it by running:  pip install pyodbc")
        return None

    try:
        import pandas as pd
    except ImportError:
        print("The 'pandas' package is not installed.")
        print("Install it by running:  pip install pandas")
        return None

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("The 'matplotlib' package is not installed.")
        print("Install it by running:  pip install matplotlib")
        return None

    return pyodbc, pd, plt


def run_query(pd, conn, title, query):
    print_section(title)
    df = pd.read_sql(query, conn)
    print(df.to_string(index=False))
    return df


def main():
    dependencies = load_dependencies()
    if dependencies is None:
        return 1

    pyodbc, pd, plt = dependencies

    print("Connecting to SQL Server...")
    conn = None

    try:
        conn = pyodbc.connect(CONNECTION_STRING)
    except pyodbc.Error as error:
        print(f"Could not connect to SQL Server: {error}")
        print()
        print("Troubleshooting:")
        print("  1. Make sure SQL Server is running.")
        print("  2. Run 04-databases-and-sql/00_setup_database.sql first.")
        print("  3. Try changing SERVER to localhost\\SQLEXPRESS.")
        return 1

    try:
        print("Connected!")

        category_revenue = run_query(
            pd,
            conn,
            "Exercise 9: Revenue by Category",
            CATEGORY_REVENUE_QUERY,
        )

        category_revenue["total_revenue"] = pd.to_numeric(category_revenue["total_revenue"])

        category_revenue.plot(
            kind="bar",
            x="category",
            y="total_revenue",
            legend=False,
            title="Revenue by Category",
        )
        plt.ylabel("Revenue ($)")
        plt.xlabel("Category")
        plt.tight_layout()
        output_path = Path(__file__).resolve().parent / "python_sql_revenue_by_category.png"
        plt.savefig(output_path, dpi=150, bbox_inches="tight")
        plt.close()
        print(f"Saved chart to {output_path}")

    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
