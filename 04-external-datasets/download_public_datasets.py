# ============================================================
# Module 4: Download Public Datasets
# ============================================================
# This script downloads free, publicly available datasets
# that you'll use throughout the rest of this course.
#
# No accounts or API keys needed — just run this script!
#
# Usage:
#   python download_public_datasets.py
#
# Files are saved to: ../data/external/
# ============================================================

import os
import urllib.request
import sys

# Where to save downloaded files (relative to this script)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data", "external")

# Datasets to download
# Each entry: (filename, url, description)
DATASETS = [
    (
        "titanic.csv",
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
        "Titanic passenger data — survival, class, age, fare, etc.",
    ),
    (
        "iris.csv",
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv",
        "Iris flower measurements — a classic beginner dataset.",
    ),
    (
        "world_happiness.csv",
        "https://raw.githubusercontent.com/Escavine/World-Happiness/main/World-happiness-report-2024.csv",
        "World Happiness Report — country happiness scores and factors.",
    ),
    (
        "tips.csv",
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv",
        "Restaurant tipping data — bill amount, tip, day, time, party size.",
    ),
]


def download_file(url, filepath, description):
    """Download a single file from a URL."""
    filename = os.path.basename(filepath)

    if os.path.exists(filepath):
        print(f"  [SKIP] {filename} already exists")
        return True

    print(f"  Downloading {filename}...")
    print(f"    {description}")

    try:
        urllib.request.urlretrieve(url, filepath)
        # Show file size
        size = os.path.getsize(filepath)
        if size > 1024 * 1024:
            size_str = f"{size / (1024 * 1024):.1f} MB"
        else:
            size_str = f"{size / 1024:.1f} KB"
        print(f"    Saved ({size_str})")
        return True

    except Exception as e:
        print(f"    [ERROR] Failed to download: {e}")
        return False


def main():
    print("=" * 60)
    print("  Downloading Public Datasets")
    print("=" * 60)
    print()

    # Create the output directory if it doesn't exist
    os.makedirs(DATA_DIR, exist_ok=True)
    print(f"Saving files to: {os.path.abspath(DATA_DIR)}")
    print()

    success_count = 0
    fail_count = 0

    for filename, url, description in DATASETS:
        filepath = os.path.join(DATA_DIR, filename)
        if download_file(url, filepath, description):
            success_count += 1
        else:
            fail_count += 1
        print()

    # Summary
    print("=" * 60)
    print(f"  Done! {success_count} downloaded, {fail_count} failed.")
    print("=" * 60)

    if fail_count > 0:
        print()
        print("Some downloads failed. Check your internet connection and try again.")
        print("You can safely re-run this script — it will skip files that")
        print("already exist.")
        sys.exit(1)

    print()
    print("Next steps:")
    print("  1. Run explore_downloaded_data.py to see what's in each file")
    print("  2. Continue to Module 5 to load these into a SQL database")


if __name__ == "__main__":
    main()
