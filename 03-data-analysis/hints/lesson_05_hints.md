# Module 3 Exercise Hints

Try each exercise on your own before reading the hint. If the hint is enough to get you moving, go back to your own file and keep working.

## Exercise 1: Load and Inspect

Use `pd.read_csv()` to load `../data/employees.csv`.

Use `.head(10)` to see the first 10 rows.

Use `.shape` to get the number of rows and columns.

## Exercise 2: Employees Per Department

Select the `department` column.

Use `.value_counts()` to count each department. It sorts from most to least by default.

## Exercise 3: Average Salary by Department

Use `.groupby("department")["salary"].mean()`.

To see the highest average first, add `.sort_values(ascending=False)`.

To get only the department name with the highest average, use `.idxmax()`.

## Exercise 4: Filter by Hire Date

First convert the `hire_date` column:

```python
employees["hire_date"] = pd.to_datetime(employees["hire_date"])
```

Then filter rows where the date is after `"2022-01-01"`.

Use `len()` to count the filtered rows.

## Exercise 5: Find Missing Data

Use `.isnull().sum()` to count missing values in each column.

To show only columns with missing data:

```python
missing = employees.isnull().sum()
print(missing[missing > 0])
```

## Exercise 6: Top Customer State

Load `../data/customers.csv`.

Select the `state` column and use `.value_counts()`.

Use `.head(5)` to show only the top five states.
