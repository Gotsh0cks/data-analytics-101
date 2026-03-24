"""
Lesson 1: Loading Data
======================
In this script, you'll learn how to load a CSV file into pandas
and explore what's inside.
"""

import pandas as pd

# Load the sales data
df = pd.read_csv("../data/sales_data.csv")

# See the first 5 rows
print("=== First 5 rows ===")
print(df.head())
print()

# See the last 5 rows
print("=== Last 5 rows ===")
print(df.tail())
print()

# How many rows and columns?
print(f"This dataset has {df.shape[0]} rows and {df.shape[1]} columns")
print()

# What are the column names and types?
print("=== Column Info ===")
print(df.dtypes)
print()

# Quick summary
print("=== Summary ===")
df.info()
