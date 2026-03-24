"""
Lesson 4: Data Cleaning
========================
In this script, you'll learn how to find and fix common data
problems: missing values, duplicates, and wrong column types.
"""

import pandas as pd

# Load the sales data
df = pd.read_csv("../data/sales_data.csv")

print(f"Starting with {df.shape[0]} rows and {df.shape[1]} columns")
print()

# -----------------------------------------------
# Step 1: Check for missing values
# -----------------------------------------------
print("=== Missing Values Per Column ===")
print(df.isnull().sum())
print()

# Show rows where revenue is missing (if any)
missing_revenue = df[df["revenue"].isnull()]
if len(missing_revenue) > 0:
    print(f"Found {len(missing_revenue)} rows with missing revenue:")
    print(missing_revenue)
    print()
else:
    print("No missing revenue values found.")
    print()

# -----------------------------------------------
# Step 2: Handle missing values
# -----------------------------------------------

# Option A: Fill missing revenue with 0
df_filled = df.copy()
df_filled["revenue"] = df_filled["revenue"].fillna(0)
print("=== After filling missing revenue with 0 ===")
print(f"Missing revenue values: {df_filled['revenue'].isnull().sum()}")
print()

# Option B: Drop rows with any missing values
df_dropped = df.dropna()
print("=== After dropping rows with any missing value ===")
print(f"Rows remaining: {df_dropped.shape[0]} (started with {df.shape[0]})")
print()

# -----------------------------------------------
# Step 3: Find and remove duplicates
# -----------------------------------------------
num_duplicates = df.duplicated().sum()
print(f"=== Duplicate Rows: {num_duplicates} ===")

if num_duplicates > 0:
    print("Duplicate rows:")
    print(df[df.duplicated()])
    print()

# Remove duplicates
df_clean = df.drop_duplicates()
print(f"After removing duplicates: {df_clean.shape[0]} rows (was {df.shape[0]})")
print()

# -----------------------------------------------
# Step 4: Convert the date column to a proper date type
# -----------------------------------------------
print("=== Date Column Type ===")
print(f"Before conversion: {df_clean['date'].dtype}")

df_clean = df_clean.copy()  # Avoid SettingWithCopyWarning
df_clean["date"] = pd.to_datetime(df_clean["date"])

print(f"After conversion:  {df_clean['date'].dtype}")
print()

# Now we can do date-based operations
print("=== Date Range ===")
print(f"Earliest sale: {df_clean['date'].min()}")
print(f"Latest sale:   {df_clean['date'].max()}")
print()

# -----------------------------------------------
# Step 5: Save the cleaned data
# -----------------------------------------------
output_path = "../data/sales_data_cleaned.csv"
df_clean.to_csv(output_path, index=False)
print(f"Cleaned data saved to {output_path}")
print(f"Final dataset: {df_clean.shape[0]} rows, {df_clean.shape[1]} columns")
