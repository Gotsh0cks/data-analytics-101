# Module 3 Exercise Expected Outputs

Your formatting may look slightly different, but your answers should match these values.

## Exercise 1: Load and Inspect

The employee dataset has:

```text
50 rows
9 columns
```

The first row should be employee `E001`, James Mitchell, in Engineering.

## Exercise 2: Employees Per Department

Expected department counts:

```text
Engineering    16
Sales          11
Marketing       8
Finance         8
HR              6
```

The missing department value is not counted by `value_counts()` unless you ask pandas to include missing values.

## Exercise 3: Average Salary by Department

Expected averages, rounded to 2 decimals:

```text
Engineering    114666.67
Sales           80181.82
Finance         72142.86
Marketing       62250.00
HR              60833.33
```

The department with the highest average salary is:

```text
Engineering
```

## Exercise 4: Filter by Hire Date

Employees hired after January 1, 2022:

```text
15
```

The filtered results should include employees such as Emily Rodriguez, Laura Anderson, Rachel White, and Lauren Collins.

## Exercise 5: Find Missing Data

Columns with missing values:

```text
department    1
salary        2
```

All other columns should show `0` missing values.

## Exercise 6: Top Customer State

Top 5 customer states:

```text
CA    10
TX     8
AZ     4
FL     4
OH     3
```

California has the most customers.
