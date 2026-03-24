# ============================================================
# Capstone Project Template
# ============================================================
# Fill in each section below to complete your capstone project.
# Replace the placeholder comments with your own code.
#
# Usage:
#   python project_template.py
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# STEP 1: Load your dataset
# ============================================================
# Replace the path with your chosen dataset

# df = pd.read_csv("../data/external/titanic.csv")
# print(f"Loaded {len(df)} rows and {len(df.columns)} columns")

# ============================================================
# STEP 2: Explore the data
# ============================================================
# Uncomment and run these to understand your data

# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())

# ============================================================
# STEP 3: Clean the data
# ============================================================
# Handle missing values, fix data types, remove duplicates

# Example:
# df["Age"].fillna(df["Age"].median(), inplace=True)
# df.drop_duplicates(inplace=True)

# ============================================================
# STEP 4: Analyze — Answer your questions
# ============================================================
# Write code to answer 3-5 questions about your data.

# Question 1: _______________________________________________
# Your code here


# Question 2: _______________________________________________
# Your code here


# Question 3: _______________________________________________
# Your code here


# ============================================================
# STEP 5: Visualize — Create at least 3 charts
# ============================================================
sns.set_style("whitegrid")

# Chart 1: ________________________________________________
# Your code here
# plt.savefig("chart_01.png", dpi=150)
# plt.show()

# Chart 2: ________________________________________________
# Your code here
# plt.savefig("chart_02.png", dpi=150)
# plt.show()

# Chart 3: ________________________________________________
# Your code here
# plt.savefig("chart_03.png", dpi=150)
# plt.show()

# ============================================================
# STEP 6: Summarize your findings
# ============================================================
# Print a brief summary of what you found

# print("=" * 60)
# print("  Summary of Findings")
# print("=" * 60)
# print("1. Finding one...")
# print("2. Finding two...")
# print("3. Finding three...")
