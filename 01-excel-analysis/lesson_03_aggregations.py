"""
Lesson 3: Aggregations
=======================
In this script, you'll learn how to summarize data with totals,
averages, group-by operations, and more.
"""

import pandas as pd

# Load the sales data
df = pd.read_csv("../data/sales_data.csv")

# -----------------------------------------------
# Basic aggregations
# -----------------------------------------------
print("=== Basic Aggregations ===")
print(f"Total revenue:   ${df['revenue'].sum():,.2f}")
print(f"Average revenue: ${df['revenue'].mean():,.2f}")
print(f"Min revenue:     ${df['revenue'].min():,.2f}")
print(f"Max revenue:     ${df['revenue'].max():,.2f}")
print(f"Number of sales: {df['revenue'].count()}")
print()

# Average quantity per order
print(f"Average quantity per order: {df['quantity'].mean():.1f}")
print()

# -----------------------------------------------
# Group By: Revenue by region
# -----------------------------------------------
print("=== Total Revenue by Region ===")
revenue_by_region = df.groupby("region")["revenue"].sum()
print(revenue_by_region)
print()

# -----------------------------------------------
# Group By: Revenue by product
# -----------------------------------------------
print("=== Total Revenue by Product ===")
revenue_by_product = df.groupby("product")["revenue"].sum()
print(revenue_by_product)
print()

# -----------------------------------------------
# Group By: Average revenue by region and product
# -----------------------------------------------
print("=== Average Revenue by Region and Product ===")
avg_by_region_product = df.groupby(["region", "product"])["revenue"].mean()
print(avg_by_region_product)
print()

# -----------------------------------------------
# Multiple aggregations with .agg()
# -----------------------------------------------
print("=== Multiple Aggregations by Region ===")
region_summary = df.groupby("region").agg(
    total_revenue=("revenue", "sum"),
    avg_revenue=("revenue", "mean"),
    max_revenue=("revenue", "max"),
    num_sales=("revenue", "count")
)
print(region_summary)
print()

# -----------------------------------------------
# Describe the revenue column
# -----------------------------------------------
print("=== Revenue Statistics (.describe()) ===")
print(df["revenue"].describe())
print()

# -----------------------------------------------
# Count of sales per category
# -----------------------------------------------
print("=== Sales Count per Category ===")
if "category" in df.columns:
    print(df["category"].value_counts())
else:
    # If there's no category column, use product instead
    print("(No 'category' column found — showing product counts instead)")
    print(df["product"].value_counts())
