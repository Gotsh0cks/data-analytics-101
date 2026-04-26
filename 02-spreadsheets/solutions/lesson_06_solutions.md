# Module 2 Exercise Solutions

Use this after trying the exercises, then checking the hints and expected outputs. If your numbers are close but not exact, check for an active filter, a missing row, or a range that accidentally includes the header.

## Exercise 1: Formulas Practice

Open `data/excel/employees.xlsx` and use the `Data` sheet. The employee rows run from row 2 through row 51.

```text
Total payroll: =SUM(F2:F51)
Average salary: =AVERAGE(F2:F51)
Employee count: =COUNTA(A2:A51)
Sales employees: =COUNTIF(D2:D51, "Sales")
Engineering salary spend: =SUMIF(D2:D51, "Engineering", F2:F51)
```

Column `A` has employee IDs, column `D` has departments, and column `F` has salaries. `AVERAGE` ignores blank salary cells, which is what you want here.

## Exercise 2: Sorting Challenge

Open `data/excel/employees.xlsx`, click inside the table, and use **Data > Sort**.

1. Sort `hire_date` from oldest to newest. The first person listed is Mark Hernandez.
2. Sort `salary` from largest to smallest. The first person listed is Monica Cook.
3. Use a multi-level sort: `department` A to Z, then `salary` largest to smallest. In the HR group, the highest-paid person is Michelle Thomas.

If Excel asks whether to expand the selection, choose the option that keeps the full rows together.

## Exercise 3: Filtering Drill

Open `data/excel/sales_data.xlsx`, then turn on filters with **Data > Filter**.

1. Filter `category` to Furniture. Count the visible rows, or use `=SUBTOTAL(103, C2:C104)`. The count is 24.
2. Clear the filter, then filter `revenue` with **Number Filters > Greater Than** and enter `1000`. Count the visible revenue cells with `=SUBTOTAL(103, G2:G104)`. The count is 20.
3. Clear filters again, then filter `category` to Electronics and `region` to North. Sum visible revenue with the status bar or `=SUBTOTAL(109, G2:G104)`. The total is 16,269.68.
4. Use **Data > Clear** or turn filters off when you are done.

`SUBTOTAL` is helpful because it ignores rows hidden by filters.

## Exercise 4: Pivot Table Challenges

For each pivot, click inside the `Data` sheet and choose **Insert > PivotTable > New Worksheet**.

Using `data/excel/sales_data.xlsx`:

1. Total revenue for each region: put `region` in **Rows** and `revenue` in **Values**. Keep Values set to **Sum** and sort largest to smallest.
2. Average sale amount for each product: put `product` in **Rows** and `revenue` in **Values**. Open **Value Field Settings** and choose **Average**.
3. Sales count by category and region: put `category` in **Rows**, `region` in **Columns**, and `product` or `date` in **Values**. Set Values to **Count**.

Using `data/excel/customers.xlsx`:

4. Highest total spending state: put `state` in **Rows** and `total_spent` in **Values** as **Sum**. Sort largest to smallest. TX is highest at 24,328.74.
5. Highest average orders per state: put `state` in **Rows** and `total_orders` in **Values** as **Average**. Sort largest to smallest. MN is highest at 43.00.

## Exercise 5: Chart Building

Build each chart from a pivot summary instead of the raw table.

1. Column chart: create a pivot with `region` in **Rows** and `revenue` in **Values** as **Sum**. Sort highest to lowest, select the pivot summary, then choose **Insert > Column Chart**. A good title is `Total Revenue by Region`.
2. Line chart: create a pivot with `date` in **Rows** and `revenue` in **Values** as **Sum**. Right-click a date in the pivot, choose **Group**, and group by months. Insert a line chart and title it `Monthly Revenue Trend`.
3. Pie chart: create a pivot with `category` in **Rows** and `revenue` in **Values** as **Sum**. Insert a pie chart and title it `Revenue Share by Category`.

Before calling a chart finished, add readable data labels, remove legends that repeat the title, and keep the number formatting easy to scan.
