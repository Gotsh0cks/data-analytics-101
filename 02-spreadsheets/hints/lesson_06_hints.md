# Module 2 Exercise Hints

Try each exercise on your own before reading the hint. If a hint gives you enough to continue, go back to Excel and finish the step yourself.

## Exercise 1: Formulas Practice

Start by finding the columns you need in `employees.xlsx`. The salary values are in the `salary` column, and department names are in the `department` column.

Useful formula patterns:

```text
=SUM(range)
=AVERAGE(range)
=COUNTA(range)
=COUNTIF(range, "text to count")
=SUMIF(criteria_range, "text to match", sum_range)
```

For the employee count, count a column that should have a value on every employee row, such as `employee_id`. Avoid counting the header row.

For the Sales and Engineering questions, the department column is the criteria range. The salary column is the sum range for the salary-spend question.

## Exercise 2: Sorting Challenge

Before sorting, click anywhere inside the data table. If Excel asks whether to expand the selection, choose the option that keeps the full rows together.

For one-column sorts:

- `hire_date`: sort oldest to newest.
- `salary`: sort largest to smallest.

For the HR question, use **Data > Sort**, then add levels:

1. Sort by `department` from A to Z.
2. Then sort by `salary` from largest to smallest.

After sorting, look at the first HR row you see.

## Exercise 3: Filtering Drill

Turn on filters with **Data > Filter** or **Ctrl + Shift + L**.

For row counts after filtering, you can:

- Look at the bottom-left of Excel, where it may show how many rows are found.
- Select the visible cells in the filtered column and read the Count on the status bar.
- Use `SUBTOTAL` so filtered-out rows are ignored.

Helpful `SUBTOTAL` patterns:

```text
=SUBTOTAL(103, range_to_count_visible_nonblank_cells)
=SUBTOTAL(109, range_to_sum_visible_numbers)
```

Clear filters between questions so one filter does not accidentally affect the next answer.

For the Electronics North revenue question, apply both filters first, then sum the visible `revenue` values.

## Exercise 4: Pivot Table Challenges

Create each pivot table from the `Data` sheet. Click inside the data, then use **Insert > PivotTable > New Worksheet**.

For the sales-data pivots:

- Total revenue by region: put `region` in **Rows** and `revenue` in **Values**. Make sure Values uses **Sum**.
- Average sale amount by product: put `product` in **Rows** and `revenue` in **Values**. Change Values from **Sum** to **Average**.
- Category by region counts: put `category` in **Rows**, `region` in **Columns**, and a non-empty field such as `product` or `date` in **Values**. Change Values to **Count** if needed.

For the customer-data pivots:

- Total spending by state: put `state` in **Rows** and `total_spent` in **Values**. Use **Sum**.
- Average orders by state: put `state` in **Rows** and `total_orders` in **Values**. Use **Average**.

Sort the pivot values from largest to smallest when the question asks which group is highest.

## Exercise 5: Chart Building

Make a small pivot summary first, then build the chart from that summary. This keeps the chart clean and easier to read.

Suggested chart setup:

- Revenue by region column chart: pivot with `region` in **Rows** and `revenue` in **Values** as **Sum**. Sort the totals highest to lowest before charting.
- Revenue trend line chart: pivot with `date` in **Rows** and `revenue` in **Values** as **Sum**. Group the dates by month before charting.
- Revenue share pie chart: pivot with `category` in **Rows** and `revenue` in **Values** as **Sum**.

For every chart, check that the title says what the chart shows, the labels are readable, and extra legends or gridlines are removed when they do not add useful information.
