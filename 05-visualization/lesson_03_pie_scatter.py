"""
Lesson 3: Pie Charts and Scatter Plots
=======================================
This script creates a pie chart from sales data (revenue share by category)
and a scatter plot from customer data (total orders vs total spent).
"""

import pandas as pd
import matplotlib.pyplot as plt

# ===========================================================================
# Pie chart: Revenue share by category
# ===========================================================================
df = pd.read_csv("../data/sales_data.csv")

# Group by category and sum the revenue
revenue_by_category = df.groupby("category")["revenue"].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    revenue_by_category.values,
    labels=revenue_by_category.index,
    autopct="%1.1f%%",        # Show percentages with one decimal place
    startangle=90,             # Start the first slice at the top
    colors=["steelblue", "coral", "mediumseagreen"],
)
plt.title("Revenue Share by Category")
plt.tight_layout()
plt.savefig("pie_chart_revenue_by_category.png")
plt.show()
print("Chart saved as pie_chart_revenue_by_category.png")

# ===========================================================================
# Scatter plot: Total orders vs total spent (from customers.csv)
# ===========================================================================
customers = pd.read_csv("../data/customers.csv")

plt.figure(figsize=(8, 5))
plt.scatter(
    customers["total_orders"],
    customers["total_spent"],
    color="steelblue",
    alpha=0.6,                 # Slightly transparent so overlapping dots are visible
    s=60,                      # Dot size
    edgecolors="white",        # White border around each dot
)
plt.title("Customer Orders vs. Total Spent")
plt.xlabel("Total Orders")
plt.ylabel("Total Spent ($)")
plt.tight_layout()
plt.savefig("scatter_orders_vs_spent.png")
plt.show()
print("Chart saved as scatter_orders_vs_spent.png")
