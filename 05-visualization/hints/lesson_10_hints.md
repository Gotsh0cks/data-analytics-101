# Module 5 Exercise Hints

Try each exercise on your own first. If you get stuck, read only the section for the exercise you are working on, then go back to your own chart or dashboard.

## Exercise 1: Average Salary by Department

A bar chart is the right choice because you are comparing categories.

Load `../data/employees.csv` if your practice script is inside `05-visualization`, then group by `department` and calculate the mean of `salary`. Sorting the result from highest to lowest makes the chart easier to scan.

Use a vertical bar chart, a title that says exactly what the chart shows, and a y-axis label that includes dollars. If you add value labels above the bars, round them so the labels stay readable.

## Exercise 2: Employees per Department

This is a "parts of a whole" question, so a pie chart is reasonable because there are only a few departments.

Start with the `department` column and use a count method. The missing department value should not become its own unlabeled slice unless you intentionally choose to show missing values.

Use department names as labels and `autopct` to show percentages. A square figure size usually keeps a pie chart from looking stretched.

## Exercise 3: Customer Signups per Month

A line chart is the right chart type because signup dates happen over time.

Convert `signup_date` to a real datetime column first. Then group by month, count the rows in each month, and sort the months before plotting.

Use markers so each month is visible. If the x-axis labels feel crowded, rotate the labels or show every few month labels instead of every single one.

## Exercise 4: Salary vs. Tenure

A scatter plot works because you are comparing two numbers: years since hire and salary.

Convert `hire_date` to datetime, then subtract it from today's date to estimate years since hire. Drop rows with missing salary before plotting so matplotlib does not silently skip points in a confusing way.

Put years since hire on the x-axis and salary on the y-axis. Use `alpha=0.6` so overlapping dots are easier to see.

## Exercise 5: Presentation-Ready Chart

Pick one chart that already works before you polish it. A good choice is the salary-by-department bar chart because it has clear categories and room for labels.

Set a seaborn style near the top of your script with `sns.set_style("whitegrid")`. Then improve the title, axis labels, colors, and figure size.

For presentation polish, look for small readability wins: sorted bars, subtle grid lines, readable value labels, and a higher-resolution save with `dpi=150`.

## Exercise 6: Sales Performance Dashboard

Run `lesson_05_prepare_data_for_tableau.py` first, then connect Tableau Public to `data/tableau_ready/sales_data.csv`.

Build one worksheet at a time:

1. Product revenue: use `product` and `SUM(revenue)`, then sort descending.
2. Revenue over time: use `date` by month and `SUM(revenue)`.
3. Region and category: use `region`, `SUM(revenue)`, and put `category` on Color.

After the worksheets work, create the dashboard. Add a Region filter and apply it to all worksheets that use the sales data source.

## Exercise 7: Employee Overview Dashboard

Connect Tableau to `data/tableau_ready/employees.csv`.

For employee counts, use `department` with a count of employee records. For average salary, change the `salary` aggregation from `SUM` to `AVG`.

For the scatter plot, put `hire_date` on one axis and `salary` on the other. Put `employee_id` on Detail so Tableau keeps one mark per employee. Add `department` to Color if it helps, but keep the chart readable. Add a `department` filter and apply it to all employee worksheets.

## Exercise 8: Portfolio Project

Start with the question before choosing charts. A strong dashboard answers one question clearly instead of showing every field in the dataset.

Choose three chart types that each add something different: for example, one comparison chart, one trend chart, and one relationship or detail chart.

Before publishing, check that your title, subtitle, filters, chart names, labels, and tooltips all help someone understand the dashboard without you standing beside them.
