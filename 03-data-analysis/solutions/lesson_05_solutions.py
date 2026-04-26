"""
Module 3 Exercise Solutions
===========================
Run this after trying the exercises yourself:

    python 03-data-analysis/solutions/lesson_05_solutions.py

This script reads the course data and prints complete answers for
the Module 3 pandas exercises.
"""

from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"


def print_section(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main():
    employees = pd.read_csv(DATA_DIR / "employees.csv")
    customers = pd.read_csv(DATA_DIR / "customers.csv")

    print_section("Exercise 1: Load and Inspect")
    print(employees.head(10).to_string(index=False))
    print()
    print(f"Rows: {employees.shape[0]}")
    print(f"Columns: {employees.shape[1]}")

    print_section("Exercise 2: Employees Per Department")
    department_counts = employees["department"].value_counts()
    print(department_counts.to_string())

    print_section("Exercise 3: Average Salary by Department")
    average_salary = employees.groupby("department")["salary"].mean().sort_values(ascending=False)
    print(average_salary.round(2).to_string())
    print()
    print(f"Highest average salary department: {average_salary.idxmax()}")

    print_section("Exercise 4: Filter by Hire Date")
    employees["hire_date"] = pd.to_datetime(employees["hire_date"])
    recent_hires = employees[employees["hire_date"] > "2022-01-01"]
    print(recent_hires[["employee_id", "first_name", "last_name", "department", "hire_date"]].to_string(index=False))
    print()
    print(f"Employees hired after January 1, 2022: {len(recent_hires)}")

    print_section("Exercise 5: Find Missing Data")
    missing = employees.isnull().sum()
    print("All columns:")
    print(missing.to_string())
    print()
    print("Columns with missing values:")
    print(missing[missing > 0].to_string())

    print_section("Exercise 6: Top Customer State")
    top_states = customers["state"].value_counts().head(5)
    print(top_states.to_string())
    print()
    print(f"State with the most customers: {top_states.idxmax()}")


if __name__ == "__main__":
    main()
