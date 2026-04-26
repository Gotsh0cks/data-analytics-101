"""
Module 6 Exercise Solutions
===========================
Run this after trying the exercises yourself:

    python 06-real-world-data/solutions/05_solutions.py

This script reads the downloaded public datasets and prints complete
answers for the Module 6 real-world data exercises.
"""

from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data" / "external"


def format_number(value):
    return f"{value:.2f}"


def format_percent(value):
    return f"{value:.2f}%"


def print_section(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main():
    titanic = pd.read_csv(DATA_DIR / "titanic.csv")
    tips = pd.read_csv(DATA_DIR / "tips.csv")
    iris = pd.read_csv(DATA_DIR / "iris.csv")

    print_section("Exercise 1: Explore the Titanic Dataset")
    print(f"Shape: {titanic.shape[0]} rows x {titanic.shape[1]} columns")
    print(f"Rows: {titanic.shape[0]}")
    print(f"Columns: {titanic.shape[1]}")
    print(f"Survival percentage: {format_percent(titanic['Survived'].mean() * 100)}")
    print(f"Average age: {format_number(titanic['Age'].mean())}")
    print()

    missing = titanic.isnull().sum()
    missing_columns = missing[missing > 0]
    print(f"Columns with missing values: {len(missing_columns)}")
    for column, count in missing_columns.items():
        print(f"{column}: {count} missing")

    print()
    print("Plain-English interpretation:")
    print("Fewer than half of passengers survived, and the average age was about 30.")
    print("The Cabin column has many missing values, so use it carefully.")

    print_section("Exercise 2: Tipping Patterns")
    average_tip = tips["tip"].mean()
    average_tip_by_day = tips.groupby("day")["tip"].mean()
    highest_tip_day = average_tip_by_day.idxmax()
    average_tip_by_time = tips.groupby("time")["tip"].mean()

    print(f"Average tip: {format_number(average_tip)}")
    print(
        "Highest average tip day: "
        f"{highest_tip_day}, {format_number(average_tip_by_day[highest_tip_day])}"
    )
    print(f"Dinner average tip: {format_number(average_tip_by_time['Dinner'])}")
    print(f"Lunch average tip: {format_number(average_tip_by_time['Lunch'])}")
    print()
    print("Plain-English interpretation:")
    print("Dinner parties tipped more than lunch parties on average in this dataset.")

    print_section("Exercise 3: Iris Species Comparison")
    average_petal_length = iris.groupby("species")["petal_length"].mean()
    average_sepal_width = iris.groupby("species")["sepal_width"].mean()
    widest_sepal_species = average_sepal_width.idxmax()

    print("Average petal length by species:")
    for species, value in average_petal_length.items():
        print(f"{species}: {format_number(value)}")
    print()
    print(f"Widest average sepal width species: {widest_sepal_species}")
    print(f"Widest average sepal width: {format_number(average_sepal_width[widest_sepal_species])}")
    print()
    print("Plain-English interpretation:")
    print("Setosa has much shorter petals than the other species.")
    print("Setosa also has the widest sepals on average.")

    print_section("Exercise 4: Find Your Own Dataset")
    print("Use this checklist with the dataset you chose:")
    print("[ ] Shape printed")
    print("[ ] Column names printed")
    print("[ ] Data types printed")
    print("[ ] Missing values checked")
    print("[ ] Three answerable questions written down")
    print()
    print("Example question shapes:")
    print("- Which group has the highest average value?")
    print("- Which category appears most often?")
    print("- Are there missing values that would affect the analysis?")


if __name__ == "__main__":
    main()
