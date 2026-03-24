# ============================================================
# Module 6: Prepare Data for Tableau
# ============================================================
# This script creates clean, Tableau-friendly CSV files from
# the course datasets. Tableau works best with data that has:
#   - Consistent column names (no spaces or special chars)
#   - Proper date formats (YYYY-MM-DD)
#   - No encoding issues
#
# Usage:
#   python lesson_05_prepare_data_for_tableau.py
#
# Output:
#   ../data/tableau_ready/
# ============================================================

import os
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data")
EXTERNAL_DIR = os.path.join(DATA_DIR, "external")
OUTPUT_DIR = os.path.join(DATA_DIR, "tableau_ready")


def clean_for_tableau(df, name):
    """Apply common cleaning steps for Tableau compatibility."""
    # Standardize column names: lowercase, underscores
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    print(f"  [OK] {name}: {len(df):,} rows, {len(df.columns)} columns")
    return df


def main():
    print("=" * 60)
    print("  Preparing Data for Tableau")
    print("=" * 60)
    print()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    files_created = 0

    # ---------------------------------------------------------
    # Course datasets
    # ---------------------------------------------------------
    print("Course datasets:")

    # Sales data
    path = os.path.join(DATA_DIR, "sales_data.csv")
    if os.path.exists(path):
        df = pd.read_csv(path)
        df = clean_for_tableau(df, "sales_data")
        # Ensure date column is properly formatted
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.strftime("%Y-%m-%d")
        df.to_csv(os.path.join(OUTPUT_DIR, "sales_data.csv"), index=False)
        files_created += 1

    # Employees
    path = os.path.join(DATA_DIR, "employees.csv")
    if os.path.exists(path):
        df = pd.read_csv(path)
        df = clean_for_tableau(df, "employees")
        if "hire_date" in df.columns:
            df["hire_date"] = pd.to_datetime(df["hire_date"], errors="coerce").dt.strftime("%Y-%m-%d")
        df.to_csv(os.path.join(OUTPUT_DIR, "employees.csv"), index=False)
        files_created += 1

    # Customers
    path = os.path.join(DATA_DIR, "customers.csv")
    if os.path.exists(path):
        df = pd.read_csv(path)
        df = clean_for_tableau(df, "customers")
        if "signup_date" in df.columns:
            df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce").dt.strftime("%Y-%m-%d")
        df.to_csv(os.path.join(OUTPUT_DIR, "customers.csv"), index=False)
        files_created += 1

    # ---------------------------------------------------------
    # External datasets
    # ---------------------------------------------------------
    if os.path.exists(EXTERNAL_DIR):
        print()
        print("External datasets:")

        for filename in sorted(os.listdir(EXTERNAL_DIR)):
            if filename.endswith(".csv"):
                filepath = os.path.join(EXTERNAL_DIR, filename)
                try:
                    df = pd.read_csv(filepath)
                    df = clean_for_tableau(df, filename)
                    df.to_csv(os.path.join(OUTPUT_DIR, filename), index=False)
                    files_created += 1
                except Exception as e:
                    print(f"  [ERROR] {filename}: {e}")

    print()
    print("=" * 60)
    print(f"  Done! {files_created} files saved to data/tableau_ready/")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Open Tableau Public")
    print("  2. Click 'Text file' on the left to connect to a CSV")
    print(f"  3. Navigate to: {os.path.abspath(OUTPUT_DIR)}")
    print("  4. Select a CSV file and start building!")


if __name__ == "__main__":
    main()
