# Module 5 Tableau Exercise Solution Guide

Use this after you have tried the Tableau exercises yourself. Tableau workbooks are created inside Tableau Public, so this guide gives the exact build steps instead of creating `.twbx` files for you.

## Before You Start

From the repo root, prepare the Tableau-ready CSV files:

```bash
python 05-visualization/lesson_05_prepare_data_for_tableau.py
```

Then open Tableau Public and connect to the CSV named in each exercise.

## Exercise 6: Sales Performance Dashboard

Connect to `data/tableau_ready/sales_data.csv`.

### Worksheet 1: Total Revenue by Product

1. Create a new worksheet named `Revenue by Product`.
2. Drag `product` to Rows.
3. Drag `revenue` to Columns.
4. Make sure `revenue` is aggregated as `SUM(revenue)`.
5. Click the sort descending icon so the highest-revenue product appears first.
6. On the Marks card, choose Bar.
7. Drag `SUM(revenue)` to Label.
8. Format `revenue` as currency.

### Worksheet 2: Revenue Over Time

1. Create a new worksheet named `Monthly Revenue`.
2. Drag `date` to Columns.
3. Choose month-level dates.
4. Drag `revenue` to Rows.
5. Make sure `revenue` is aggregated as `SUM(revenue)`.
6. On the Marks card, choose Line.
7. Edit the title to `Monthly Revenue`.
8. Format the revenue axis as currency.

### Worksheet 3: Revenue by Region and Category

1. Create a new worksheet named `Revenue by Region and Category`.
2. Drag `region` to Rows.
3. Drag `revenue` to Columns.
4. Make sure `revenue` is aggregated as `SUM(revenue)`.
5. Drag `category` to Color on the Marks card.
6. Keep the Marks type as Bar.
7. Format revenue as currency.

### Dashboard

1. Create a new dashboard named `Sales Performance Dashboard`.
2. Turn on the dashboard title and use a clear title such as `Sales Performance Dashboard`.
3. Drag the three worksheets onto the dashboard.
4. Add a `region` filter from one sales worksheet.
5. Right-click the `region` filter and choose **Apply to Worksheets** > **All Using This Data Source**.
6. Test the filter by selecting one region and confirming all three charts update.
7. Rename any leftover default sheet names before saving or publishing.

## Exercise 7: Employee Overview Dashboard

Connect to `data/tableau_ready/employees.csv`.

### Worksheet 1: Employees per Department

1. Create a new worksheet named `Employees per Department`.
2. Drag `department` to Rows.
3. Drag `employee_id` to Columns.
4. Change the aggregation to Count if Tableau does not do that automatically.
5. Sort descending.
6. Drag the count measure to Label.
7. If a Null department appears, either filter it out or rename it intentionally as missing data.

### Worksheet 2: Average Salary by Department

1. Create a new worksheet named `Average Salary by Department`.
2. Drag `department` to Rows.
3. Drag `salary` to Columns.
4. Change `SUM(salary)` to `AVG(salary)`.
5. Sort descending.
6. Drag `AVG(salary)` to Label.
7. Format `salary` as currency.

### Worksheet 3: Hire Date vs. Salary

1. Create a new worksheet named `Hire Date vs Salary`.
2. Drag `hire_date` to Columns and use the exact date or a continuous date field.
3. Drag `salary` to Rows.
4. Drag `employee_id` to Detail on the Marks card so Tableau keeps one mark per employee instead of aggregating everyone together.
5. Use the Marks card to choose Circle if Tableau does not create a scatter-style view automatically.
6. Drag `department` to Color if it makes the view easier to read.
7. Format `salary` as currency.

### Dashboard

1. Create a new dashboard named `Employee Overview Dashboard`.
2. Add the three employee worksheets.
3. Turn on the dashboard title and write a title that explains the dashboard.
4. Add a `department` filter.
5. Apply the `department` filter to all worksheets using the employee data source.
6. Confirm that the bar chart labels are visible.
7. Test the filter and make sure the scatter plot updates with the bar charts.

## Exercise 8: Portfolio Project

Choose a dataset and write the main question before building charts.

1. Connect to your chosen dataset.
2. Create at least three worksheets with different chart types.
3. Give every worksheet a descriptive name.
4. Build a dashboard with a title and subtitle.
5. Add at least one filter and apply it to the relevant worksheets.
6. Check that all labels, axes, colors, and tooltips are readable.
7. Save to Tableau Public with a clear workbook name.
8. Open the published dashboard in a browser and test the filters again.

Portfolio check: someone should be able to open the published dashboard and understand the question, the important charts, and the main takeaway without asking you what the dashboard means.
