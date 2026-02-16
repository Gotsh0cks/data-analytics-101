# ============================================================
# Module 4: Download a Kaggle Dataset (Optional)
# ============================================================
# This script shows how to download datasets from Kaggle using
# their API. This requires a free Kaggle account and API key.
#
# SETUP (one-time):
#   1. Go to kaggle.com and create a free account
#   2. Go to kaggle.com/settings (or click your profile icon > Settings)
#   3. Scroll to "API" section and click "Create New Token"
#   4. This downloads a file called kaggle.json
#   5. Move kaggle.json to: C:\Users\<YourName>\.kaggle\kaggle.json
#   6. Install the kaggle package: pip install kaggle
#
# Usage:
#   python download_kaggle_dataset.py
# ============================================================

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data", "external")


def check_kaggle_setup():
    """Verify that the Kaggle API is ready to use."""
    # Check if kaggle package is installed
    try:
        import kaggle  # noqa: F401
    except ImportError:
        print("The 'kaggle' package is not installed.")
        print("Install it by running:  pip install kaggle")
        print()
        return False

    # Check if API key exists
    kaggle_dir = os.path.join(os.path.expanduser("~"), ".kaggle")
    kaggle_json = os.path.join(kaggle_dir, "kaggle.json")

    if not os.path.exists(kaggle_json):
        print(f"Kaggle API key not found at: {kaggle_json}")
        print()
        print("To set up your Kaggle API key:")
        print("  1. Go to kaggle.com/settings")
        print("  2. Click 'Create New Token' under the API section")
        print("  3. Move the downloaded kaggle.json file to:")
        print(f"     {kaggle_json}")
        print()
        return False

    return True


def download_dataset(dataset_slug, target_dir):
    """
    Download a Kaggle dataset.

    Parameters:
        dataset_slug: The Kaggle dataset identifier (e.g., "uciml/iris")
        target_dir: Where to save the files
    """
    from kaggle.api.kaggle_api_extended import KaggleApi

    api = KaggleApi()
    api.authenticate()

    print(f"Downloading: {dataset_slug}")
    print(f"Saving to:   {os.path.abspath(target_dir)}")
    print()

    os.makedirs(target_dir, exist_ok=True)
    api.dataset_download_files(dataset_slug, path=target_dir, unzip=True)

    # Show what was downloaded
    print("Downloaded files:")
    for f in os.listdir(target_dir):
        filepath = os.path.join(target_dir, f)
        if os.path.isfile(filepath):
            size = os.path.getsize(filepath)
            print(f"  {f} ({size / 1024:.1f} KB)")


def main():
    print("=" * 60)
    print("  Kaggle Dataset Downloader")
    print("=" * 60)
    print()

    if not check_kaggle_setup():
        sys.exit(1)

    # ---------------------------------------------------------
    # Change this to any Kaggle dataset you want to download!
    # Find the slug on the dataset's Kaggle page — it's in the URL.
    # Example: kaggle.com/datasets/uciml/iris  ->  slug = "uciml/iris"
    # ---------------------------------------------------------
    DATASET_SLUG = "uciml/iris"

    # Save to a subfolder named after the dataset
    dataset_name = DATASET_SLUG.split("/")[-1]
    target_dir = os.path.join(DATA_DIR, f"kaggle_{dataset_name}")

    download_dataset(DATASET_SLUG, target_dir)

    print()
    print("Done! You can now load these files with pandas:")
    print(f'  df = pd.read_csv("{target_dir}/<filename>.csv")')


if __name__ == "__main__":
    main()
