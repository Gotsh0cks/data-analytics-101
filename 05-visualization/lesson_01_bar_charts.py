"""
Lesson 1: Bar Charts
=====================
This script creates bar charts from the sales data.
We'll make a vertical bar chart (revenue by region) and
a horizontal bar chart (sales count by product).
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../data/sales_data.csv")

# ---------------------------------------------------------------------------
# Bar chart 1: Total revenue by region
# ---------------------------------------------------------------------------
# Group the data by region and add up all the revenue in each region
revenue_by_region = df.groupby("region")["revenue"].sum()

plt.figure(figsize=(8, 5))
plt.bar(revenue_by_region.index, revenue_by_region.values, color="steelblue")
plt.title("Total Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("bar_chart_revenue_by_region.png")
plt.show()
print("Chart saved as bar_chart_revenue_by_region.png")

# ---------------------------------------------------------------------------
# Bar chart 2: Number of sales by product (horizontal)
# ---------------------------------------------------------------------------
# value_counts() counts how many times each product appears in the data
sales_by_product = df["product"].value_counts()

plt.figure(figsize=(8, 5))
plt.barh(sales_by_product.index, sales_by_product.values, color="coral")
plt.title("Number of Sales by Product")
plt.xlabel("Number of Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("bar_chart_sales_by_product.png")
plt.show()
print("Chart saved as bar_chart_sales_by_product.png")
