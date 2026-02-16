"""
Lesson 2: Line Charts
======================
This script creates line charts from the sales data.
We'll make a monthly revenue trend and a multi-line chart
showing revenue by region over time.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../data/sales_data.csv")

# Convert the date column from text to actual dates
df["date"] = pd.to_datetime(df["date"])

# Create a "month" column so we can group by month
# to_period("M") turns a date like 2024-01-15 into 2024-01
df["month"] = df["date"].dt.to_period("M")

# ---------------------------------------------------------------------------
# Line chart 1: Monthly revenue trend
# ---------------------------------------------------------------------------
# Group by month and sum up the revenue
monthly_revenue = df.groupby("month")["revenue"].sum()

plt.figure(figsize=(10, 5))
plt.plot(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    color="steelblue",
    marker="o",
    linewidth=2,
)
plt.title("Monthly Revenue Trend (2024)")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("line_chart_monthly_revenue.png")
plt.show()
print("Chart saved as line_chart_monthly_revenue.png")

# ---------------------------------------------------------------------------
# Line chart 2: Revenue by region over time
# ---------------------------------------------------------------------------
# Group by both month and region, then sum revenue
monthly_region = df.groupby(["month", "region"])["revenue"].sum().reset_index()

plt.figure(figsize=(10, 5))

# Get the list of unique regions
regions = monthly_region["region"].unique()

# Plot one line for each region
for region in regions:
    region_data = monthly_region[monthly_region["region"] == region]
    plt.plot(
        region_data["month"].astype(str),
        region_data["revenue"],
        marker="o",
        linewidth=2,
        label=region,
    )

plt.title("Monthly Revenue by Region (2024)")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.legend()  # Shows the color-coded region names
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("line_chart_revenue_by_region.png")
plt.show()
print("Chart saved as line_chart_revenue_by_region.png")
