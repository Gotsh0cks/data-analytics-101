"""
Lesson 2: Filtering and Sorting
================================
In this script, you'll learn how to select columns, filter rows,
sort data, and count values.
"""

import pandas as pd

# Load the sales data
df = pd.read_csv("../data/sales_data.csv")

# -----------------------------------------------
# Selecting specific columns
# -----------------------------------------------
print("=== Product and Revenue columns only ===")
print(df[["product", "revenue"]].head())
print()

# -----------------------------------------------
# Filtering rows
# -----------------------------------------------

# Filter for only the "North" region
north_sales = df[df["region"] == "North"]
print("=== Sales in the North region ===")
print(north_sales.head())
print(f"({len(north_sales)} rows total)")
print()

# Filter for revenue greater than 500
high_revenue = df[df["revenue"] > 500]
print("=== Sales with revenue > 500 ===")
print(high_revenue.head())
print(f"({len(high_revenue)} rows total)")
print()

# Combine conditions: North region AND revenue > 500
north_high = df[(df["region"] == "North") & (df["revenue"] > 500)]
print("=== North region AND revenue > 500 ===")
print(north_high.head())
print(f"({len(north_high)} rows total)")
print()

# -----------------------------------------------
# Sorting data
# -----------------------------------------------

# Sort by revenue, lowest to highest
print("=== Sorted by revenue (ascending) ===")
print(df.sort_values("revenue").head())
print()

# Sort by revenue, highest to lowest
print("=== Sorted by revenue (descending) ===")
print(df.sort_values("revenue", ascending=False).head())
print()

# -----------------------------------------------
# Counting values
# -----------------------------------------------

# How many sales per product?
print("=== Sales count per product ===")
print(df["product"].value_counts())
print()

# How many sales per region?
print("=== Sales count per region ===")
print(df["region"].value_counts())
