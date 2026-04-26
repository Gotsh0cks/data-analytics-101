"""
Titanic capstone example project.

Run from the repository root:

    python 07-capstone/example_project/titanic_example.py

The script saves charts and a summary CSV in:

    07-capstone/example_project/outputs/
"""

from pathlib import Path

import matplotlib
import pandas as pd


matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT_DIR / "data" / "external" / "titanic.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


def print_section(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def survival_summary(df, group_column, category_name):
    summary = (
        df.groupby(group_column, observed=False)
        .agg(
            passengers=("Survived", "size"),
            survived=("Survived", "sum"),
            survival_rate_pct=("Survived", lambda values: values.mean() * 100),
        )
        .reset_index()
        .rename(columns={group_column: "group"})
    )
    summary.insert(0, "category", category_name)
    summary["survival_rate_pct"] = summary["survival_rate_pct"].round(1)
    return summary


def save_survival_chart(summary, title, output_path, colors):
    groups = summary["group"].astype(str)
    rates = summary["survival_rate_pct"]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(groups, rates, color=colors)
    plt.title(title)
    plt.xlabel("")
    plt.ylabel("Survival rate (%)")
    plt.ylim(0, 100)

    for bar, rate in zip(bars, rates):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 2,
            f"{rate:.1f}%",
            ha="center",
            va="bottom",
        )

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Could not find {DATA_PATH}. "
            "Make sure the Module 6 public datasets have been downloaded."
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    titanic = pd.read_csv(DATA_PATH)
    missing_age_count = titanic["Age"].isna().sum()
    median_age = titanic["Age"].median()

    # Fill missing ages only for age-group analysis. Keep the original Age column unchanged.
    titanic["Age_for_group"] = titanic["Age"].fillna(median_age)
    titanic["Age Group"] = pd.cut(
        titanic["Age_for_group"],
        bins=[0, 12, 18, 35, 60, 100],
        labels=["Child", "Teen", "Young adult", "Adult", "Older adult"],
        include_lowest=True,
    )

    class_summary = survival_summary(titanic, "Pclass", "Passenger class")
    class_summary["group"] = class_summary["group"].map(
        {1: "1st class", 2: "2nd class", 3: "3rd class"}
    )

    sex_summary = survival_summary(titanic, "Sex", "Sex")
    sex_summary["group"] = sex_summary["group"].str.title()

    age_summary = survival_summary(titanic, "Age Group", "Age group")

    combined_summary = pd.concat(
        [class_summary, sex_summary, age_summary],
        ignore_index=True,
    )
    combined_summary.to_csv(OUTPUT_DIR / "titanic_summary.csv", index=False)

    save_survival_chart(
        class_summary,
        "Titanic Survival Rate by Passenger Class",
        OUTPUT_DIR / "survival_by_class.png",
        ["#4E79A7", "#59A14F", "#F28E2B"],
    )
    save_survival_chart(
        sex_summary,
        "Titanic Survival Rate by Sex",
        OUTPUT_DIR / "survival_by_sex.png",
        ["#E15759", "#76B7B2"],
    )
    save_survival_chart(
        age_summary,
        "Titanic Survival Rate by Age Group",
        OUTPUT_DIR / "survival_by_age_group.png",
        ["#4E79A7", "#59A14F", "#F28E2B", "#E15759", "#B07AA1"],
    )

    overall_survival_rate = titanic["Survived"].mean() * 100

    print_section("Titanic Capstone Example")
    print(f"Rows loaded: {len(titanic)}")
    print(f"Overall survival rate: {overall_survival_rate:.1f}%")
    print(f"Missing ages filled for age groups: {missing_age_count}")
    print(f"Median age used for filling: {median_age:.1f}")

    print_section("Survival by Passenger Class")
    print(class_summary.to_string(index=False))

    print_section("Survival by Sex")
    print(sex_summary.to_string(index=False))

    print_section("Survival by Age Group")
    print(age_summary.to_string(index=False))

    print_section("Short Interpretation")
    print(
        "Survival was highest for 1st class passengers and for women. "
        "Children also had a higher survival rate than most older groups. "
        "This shows clear survival differences by class, sex, and age group, "
        "but it does not prove why any individual passenger survived."
    )
    print()
    print(f"Saved charts and summary table to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
