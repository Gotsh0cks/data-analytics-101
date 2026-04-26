"""
Module 5 Matplotlib Exercise Solutions
======================================
Run this after trying the exercises yourself:

    python 05-visualization/solutions/lesson_10_matplotlib_solutions.py

This script reads the course CSV files and saves completed charts to:

    05-visualization/exercise_outputs/
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"
OUTPUT_DIR = ROOT_DIR / "05-visualization" / "exercise_outputs"


def currency(value, _position):
    """Format chart axis values as whole-dollar amounts."""
    return f"${value:,.0f}"


def save_chart(filename, dpi=150):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / filename
    plt.tight_layout()
    plt.savefig(output_path, dpi=dpi, bbox_inches="tight")
    plt.close()
    print(f"Saved {output_path.relative_to(ROOT_DIR)}")


def load_data():
    employees = pd.read_csv(DATA_DIR / "employees.csv")
    customers = pd.read_csv(DATA_DIR / "customers.csv")
    return employees, customers


def exercise_01_salary_by_department(employees):
    salary_by_department = (
        employees.groupby("department")["salary"]
        .mean()
        .sort_values(ascending=False)
    )

    colors = sns.color_palette("Set2", len(salary_by_department))
    plt.figure(figsize=(9, 5))
    bars = plt.bar(
        salary_by_department.index,
        salary_by_department.values,
        color=colors,
        edgecolor="white",
    )

    plt.title("Average Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Average Salary ($)")
    plt.ylim(0, salary_by_department.max() * 1.15)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(currency))

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 1500,
            f"${height:,.0f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    save_chart("exercise_01_salary_by_dept.png")


def exercise_02_employees_pie(employees):
    department_counts = employees["department"].value_counts()

    colors = sns.color_palette("pastel", len(department_counts))
    plt.figure(figsize=(7, 7))
    plt.pie(
        department_counts.values,
        labels=department_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        counterclock=False,
        colors=colors,
        wedgeprops={"edgecolor": "white", "linewidth": 1},
    )
    plt.title("Employees per Department")
    plt.axis("equal")

    save_chart("exercise_02_employees_pie.png")


def exercise_03_signups_per_month(customers):
    customers = customers.copy()
    customers["signup_date"] = pd.to_datetime(customers["signup_date"])
    monthly_signups = (
        customers.groupby(customers["signup_date"].dt.to_period("M"))
        .size()
        .sort_index()
    )

    labels = monthly_signups.index.astype(str)
    x_positions = range(len(labels))

    plt.figure(figsize=(12, 5))
    plt.plot(
        x_positions,
        monthly_signups.values,
        color="steelblue",
        marker="o",
        linewidth=2,
    )
    plt.title("Customer Signups per Month")
    plt.xlabel("Signup Month")
    plt.ylabel("New Customer Signups")
    plt.xticks(
        ticks=list(x_positions)[::3],
        labels=labels[::3],
        rotation=45,
        ha="right",
    )
    plt.ylim(bottom=0)
    plt.grid(axis="y", alpha=0.3)

    save_chart("exercise_03_signups_per_month.png")


def exercise_04_salary_vs_tenure(employees):
    employees = employees.copy()
    employees["hire_date"] = pd.to_datetime(employees["hire_date"])
    reference_date = pd.Timestamp.today().normalize()
    employees["years_since_hire"] = (
        (reference_date - employees["hire_date"]).dt.days / 365.25
    )

    scatter_data = employees.dropna(subset=["salary", "years_since_hire"])

    plt.figure(figsize=(9, 5))
    plt.scatter(
        scatter_data["years_since_hire"],
        scatter_data["salary"],
        color="steelblue",
        alpha=0.6,
        s=70,
        edgecolors="white",
    )
    plt.title("Salary vs. Years Since Hire")
    plt.xlabel("Years Since Hire")
    plt.ylabel("Salary ($)")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(currency))
    plt.grid(True, alpha=0.25)

    save_chart("exercise_04_salary_vs_tenure.png")


def exercise_05_presentation_ready(employees):
    sns.set_style("whitegrid")

    salary_by_department = (
        employees.groupby("department")["salary"]
        .mean()
        .sort_values(ascending=False)
    )

    colors = sns.color_palette("deep", len(salary_by_department))
    plt.figure(figsize=(10, 6))
    bars = plt.barh(
        salary_by_department.index,
        salary_by_department.values,
        color=colors,
        edgecolor="white",
    )
    plt.gca().invert_yaxis()
    plt.title(
        "Average Salary by Department",
        fontsize=16,
        fontweight="bold",
        pad=12,
    )
    plt.xlabel("Average Salary ($)", fontsize=12)
    plt.ylabel("Department", fontsize=12)
    plt.xlim(0, salary_by_department.max() * 1.2)
    plt.gca().xaxis.set_major_formatter(FuncFormatter(currency))
    plt.grid(axis="x", alpha=0.3)

    for bar in bars:
        width = bar.get_width()
        plt.text(
            width + 1500,
            bar.get_y() + bar.get_height() / 2,
            f"${width:,.0f}",
            va="center",
            fontsize=10,
            fontweight="bold",
        )

    save_chart("exercise_05_presentation_ready.png", dpi=150)


def main():
    employees, customers = load_data()

    exercise_01_salary_by_department(employees)
    exercise_02_employees_pie(employees)
    exercise_03_signups_per_month(customers)
    exercise_04_salary_vs_tenure(employees)
    exercise_05_presentation_ready(employees)

    print()
    print(f"All charts saved in {OUTPUT_DIR.relative_to(ROOT_DIR)}")


if __name__ == "__main__":
    main()
