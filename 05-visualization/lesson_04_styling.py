"""
Lesson 4: Styling and Polish
==============================
This script shows how to make charts look professional using
seaborn styles, color palettes, and proper labeling.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the seaborn style -- this improves ALL charts, even plain matplotlib ones
sns.set_style("whitegrid")

# Load the data
df = pd.read_csv("../data/sales_data.csv")
customers = pd.read_csv("../data/customers.csv")

# ===========================================================================
# Chart 1: Polished grouped bar chart with seaborn
# ===========================================================================
# We want to show total revenue by region, broken down by category.
# seaborn makes this easy with the "hue" parameter.

plt.figure(figsize=(10, 6))
sns.barplot(
    data=df,
    x="region",
    y="revenue",
    hue="category",
    estimator="sum",          # Sum up the revenue (not average)
    palette="Set2",           # A pleasant color palette
    edgecolor="white",        # White border around each bar
)
plt.title("Total Revenue by Region and Category", fontsize=14, fontweight="bold")
plt.xlabel("Region", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.legend(title="Category", fontsize=10, title_fontsize=11)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("styled_bar_chart.png", dpi=150)
plt.show()
print("Chart saved as styled_bar_chart.png")

# ===========================================================================
# Chart 2: Styled scatter plot with seaborn
# ===========================================================================
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=customers,
    x="total_orders",
    y="total_spent",
    s=100,                    # Larger dots
    color="steelblue",
    alpha=0.7,
    edgecolor="white",
)

# Add a trend line to make the relationship clearer
sns.regplot(
    data=customers,
    x="total_orders",
    y="total_spent",
    scatter=False,            # Don't draw dots again, just the line
    color="coral",
    line_kws={"linewidth": 2, "linestyle": "--"},
)

plt.title("Customer Orders vs. Total Spent", fontsize=14, fontweight="bold")
plt.xlabel("Number of Orders", fontsize=12)
plt.ylabel("Total Amount Spent ($)", fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("styled_scatter_plot.png", dpi=150)
plt.show()
print("Chart saved as styled_scatter_plot.png")

# ===========================================================================
# Chart 3: Demonstrating color palettes
# ===========================================================================
# Let's recreate the revenue-by-region bar chart with a custom palette
# to show how much difference styling makes

revenue_by_region = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
colors = sns.color_palette("coolwarm", len(revenue_by_region))

plt.figure(figsize=(10, 6))
bars = plt.bar(
    revenue_by_region.index,
    revenue_by_region.values,
    color=colors,
    edgecolor="white",
    linewidth=1.5,
)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2.0,
        height + 200,
        f"${height:,.0f}",
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold",
    )

plt.title("Total Revenue by Region", fontsize=14, fontweight="bold")
plt.xlabel("Region", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("styled_revenue_by_region.png", dpi=150)
plt.show()
print("Chart saved as styled_revenue_by_region.png")
