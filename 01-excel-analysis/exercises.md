# Module 1 Exercises

Time to practice what you've learned. These exercises use the `employees.csv` and `customers.csv` datasets in the `../data/` folder. Try to solve each one on your own before looking at the hints at the bottom.

You can write your solutions in a new Python file (for example, `exercises.py`) in this folder, or try them out in an interactive Python session.

---

## Exercise 1: Load and Inspect

Load `../data/employees.csv` into a DataFrame and print the first 10 rows. How many rows and columns does the dataset have?

```python
# Your code here
```

---

## Exercise 2: Employees Per Department

How many employees are in each department? Display the counts from most to least.

```python
# Your code here
```

---

## Exercise 3: Average Salary by Department

What is the average salary for each department? Which department has the highest average salary?

```python
# Your code here
```

---

## Exercise 4: Filter by Hire Date

Find all employees who were hired after January 1, 2022. How many are there?

```python
# Your code here
```

---

## Exercise 5: Find Missing Data

Check the employees dataset for missing values. Which columns have missing data, and how many values are missing in each?

```python
# Your code here
```

---

## Exercise 6: Top Customer State

Load `../data/customers.csv`. Which state has the most customers? Show the top 5 states by customer count.

```python
# Your code here
```

---

## Hints

Try to solve each exercise on your own first. If you get stuck, these hints will point you in the right direction.

**Exercise 1:**
Use `pd.read_csv()` to load the file. Use `.head(10)` to see the first 10 rows (instead of the default 5). Use `.shape` to find the number of rows and columns.

**Exercise 2:**
Select the department column and use `.value_counts()`. It sorts from most to least by default.

**Exercise 3:**
Use `.groupby("department")["salary"].mean()`. To find the highest, you can add `.sort_values(ascending=False)` and look at the first row, or use `.idxmax()` to get the department name directly.

**Exercise 4:**
First, convert the hire date column to a datetime type using `pd.to_datetime()`. Then filter with a comparison: `df[df["hire_date"] > "2022-01-01"]`. Use `len()` to count the rows.

**Exercise 5:**
Use `df.isnull().sum()` to count missing values per column. To see only the columns that have missing data, you can add a filter: `missing = df.isnull().sum()` then `missing[missing > 0]`.

**Exercise 6:**
Load the file with `pd.read_csv()`. Use the state column's `.value_counts()` method, then use `.head(5)` to see only the top 5.
