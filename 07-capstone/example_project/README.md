# Titanic Example Project

This is one possible capstone project, not the only correct answer. Use it to see what a complete beginner-sized project can look like.

## Question

Which passenger groups had higher or lower survival rates on the Titanic?

This example looks at survival by:

- Passenger class
- Sex
- Age group

## Files

- `titanic_example.py` loads, cleans, analyzes, and visualizes the data.
- `07-capstone/example_project/outputs/` is created when you run the script. This folder is ignored by git because it contains generated files.

The script saves:

- `outputs/survival_by_class.png`
- `outputs/survival_by_sex.png`
- `outputs/survival_by_age_group.png`
- `outputs/titanic_summary.csv`

## How to Run It

From the repository root, run:

```bash
python 07-capstone/example_project/titanic_example.py
```

The script does not open chart windows. It saves the charts as PNG files and prints a short summary in the terminal.

If you see a file-not-found error, make sure `data/external/titanic.csv` exists. If it is missing, go back to Module 6 and run the public dataset download script.

## What "Good Enough" Looks Like Here

This example is good enough because it:

1. Asks a focused question.
2. Loads the dataset with a path that works from the repo.
3. Handles missing ages before making age groups.
4. Calculates survival rates by meaningful groups.
5. Saves charts and a summary table.
6. Prints a short interpretation without claiming more than the data proves.

Your project can use a different dataset, different questions, and different charts. The goal is to make your thinking easy to follow.
