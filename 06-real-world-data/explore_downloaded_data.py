# ============================================================
# Module 4: Explore Downloaded Datasets
# ============================================================
# Run this after download_public_datasets.py to see what's
# inside each dataset. This uses the pandas skills you learned
# in Module 1.
#
# Usage:
#   python explore_downloaded_data.py
# ============================================================

import os
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data", "external")


def explore_csv(filepath):
    """Load a CSV file and print a summary of what's inside."""
    filename = os.path.basename(filepath)
    print(f"{'=' * 60}")
    print(f"  {filename}")
    print(f"{'=' * 60}")

    # Load the data
    df = pd.read_csv(filepath)

    # Basic shape
    print(f"\n  Rows: {len(df):,}    Columns: {len(df.columns)}")

    # Column names and types
    print(f"\n  Columns:")
    for col in df.columns:
        dtype = df[col].dtype
        missing = df[col].isnull().sum()
        missing_str = f"  ({missing} missing)" if missing > 0 else ""
        print(f"    - {col} ({dtype}){missing_str}")

    # First few rows
    print(f"\n  First 3 rows:")
    print(df.head(3).to_string(index=False, max_colwidth=30))

    # Quick stats for numeric columns
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if numeric_cols:
        print(f"\n  Numeric summary:")
        summary = df[numeric_cols].describe().loc[["mean", "min", "max"]]
        print(summary.to_string())

    print()


def main():
    print()
    print("  Exploring Downloaded Datasets")
    print()

    if not os.path.exists(DATA_DIR):
        print(f"Data directory not found: {DATA_DIR}")
        print("Run download_public_datasets.py first!")
        return

    # Find all CSV files in the external data directory
    csv_files = [
        f for f in os.listdir(DATA_DIR)
        if f.endswith(".csv")
    ]

    if not csv_files:
        print("No CSV files found in the external data directory.")
        print("Run download_public_datasets.py first!")
        return

    csv_files.sort()

    print(f"Found {len(csv_files)} dataset(s) in {os.path.abspath(DATA_DIR)}")
    print()

    for filename in csv_files:
        filepath = os.path.join(DATA_DIR, filename)
        try:
            explore_csv(filepath)
        except Exception as e:
            print(f"  [ERROR] Could not read {filename}: {e}")
            print()

    print("=" * 60)
    print("  Exploration complete!")
    print("=" * 60)
    print()
    print("Try loading any of these in your own script:")
    print(f'  import pandas as pd')
    print(f'  df = pd.read_csv("data/external/<filename>.csv")')


if __name__ == "__main__":
    main()
