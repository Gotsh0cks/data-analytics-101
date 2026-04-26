# Module 5 Exercise Expected Outputs

Your charts do not need to match anyone else's colors or exact layout. Use this file to check the data, chart choice, and readability.

## Exercise 1: Average Salary by Department

Expected averages, rounded to 2 decimals:

```text
Engineering    114666.67
Sales           80181.82
Finance         72142.86
Marketing       62250.00
HR              60833.33
```

Your chart should have five bars, one for each department with non-missing department data. Engineering should be the highest bar.

Quality check:

- The title is "Average Salary by Department" or very close.
- The y-axis is labeled as salary or average salary.
- The chart is saved as `exercise_01_salary_by_dept.png`.

## Exercise 2: Employees per Department

Expected department counts:

```text
Engineering    16
Sales          11
Marketing       8
Finance         8
HR              6
```

These counts add up to 49 because one employee row has a missing department.

Approximate pie chart percentages:

```text
Engineering    32.7%
Sales          22.4%
Marketing      16.3%
Finance        16.3%
HR             12.2%
```

Quality check:

- Each slice has a department label.
- Percentages are visible.
- The chart is saved as `exercise_02_employees_pie.png`.

## Exercise 3: Customer Signups per Month

Your line chart should show monthly signup counts from January 2020 through December 2023.

Reasonable expectations:

- The y-values should be small counts, mostly between 1 and 3 signups per month.
- Several months have 3 signups, including June 2020, July 2020, August 2020, September 2020, and January 2021.
- The x-axis should be in date order, not alphabetical order.
- Markers should appear at the monthly data points.

Quality check:

- The title clearly mentions customer signups by month.
- The x-axis is labeled as month or signup month.
- The y-axis is labeled as number of signups or customer signups.
- The chart is saved as `exercise_03_signups_per_month.png`.

## Exercise 4: Salary vs. Tenure

Your scatter plot should show salary compared with years since hire.

Reasonable expectations:

- The chart should plot one point for each employee with both a hire date and a salary.
- Because two employee rows have missing salary values, you should see 48 plotted points if you drop missing salaries.
- The x-axis values will change slightly over time because "years since hire" depends on the day you run the script.
- The y-axis should use salary values from the employee dataset.

Quality check:

- Dots are semi-transparent, using something like `alpha=0.6`.
- The x-axis is labeled as years since hire or tenure.
- The y-axis is labeled as salary.
- The chart is saved as `exercise_04_salary_vs_tenure.png`.

## Exercise 5: Presentation-Ready Chart

Your polished chart may be based on any earlier exercise.

Quality check:

- `sns.set_style("whitegrid")` or a similar seaborn style is used.
- The title is larger and bold.
- Axis labels are clear and readable.
- Colors are intentional and not distracting.
- The file is saved with `dpi=150`.
- If you follow the solution script, the file is `exercise_05_presentation_ready.png`.

## Exercise 6: Sales Performance Dashboard

The Tableau dashboard should use `data/tableau_ready/sales_data.csv`.

Expected worksheet checks:

- Product revenue chart: products are sorted by total revenue. Laptop should be the top product, with total revenue around `$30,999.69`.
- Revenue over time chart: the timeline runs from January 2024 through December 2024.
- Region/category stacked bar chart: the view includes four regions and three categories.

Dashboard quality check:

- The dashboard has a descriptive title.
- The Region filter controls all three charts.
- Worksheet names are meaningful; avoid names like "Sheet 1".
- Currency fields are formatted as dollars where appropriate.

## Exercise 7: Employee Overview Dashboard

The Tableau dashboard should use `data/tableau_ready/employees.csv`.

Expected data checks:

- Department counts match Exercise 2.
- Average salary by department matches Exercise 1.
- The scatter plot uses hire date and salary, with salary as a numeric measure.

Dashboard quality check:

- The Department filter controls all employee charts.
- Bar charts show data labels.
- Salary is formatted as currency or a clearly labeled number.
- Missing department or missing salary values are handled intentionally.

## Exercise 8: Portfolio Project

Because this exercise is open-ended, there is no single correct answer.

Your finished dashboard should have:

- At least 3 different chart types.
- At least 1 interactive filter.
- A clear title and subtitle.
- A specific question the dashboard answers.
- Clean sheet names, labels, and formatting.
- A published Tableau Public version if you are building a portfolio.

Before calling it done, open the published dashboard and test the filters yourself.
