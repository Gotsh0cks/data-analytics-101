# Lesson 1: Connecting to Your Data

## The Start Page

When you open Tableau Public, you see the **Start** page. The left side has a "Connect" section this is where you tell Tableau where your data is.

For our purposes, you'll use:
- **Text file** for CSV files (this is what we'll use most)
- **Microsoft Excel** for .xlsx files

## Connecting to a CSV File

1. Open Tableau Public
2. On the left side, click **Text file**
3. Navigate to your project's `data/tableau_ready/` folder
4. Select `sales_data.csv`
5. Click **Open**

Tableau will load the file and show you a preview of the data.

## The Data Source Page

After connecting, you'll see the **Data Source** page. This shows:

- **Top left:** Your connected file(s)
- **Bottom:** A preview of the data (first 1,000 rows)
- **Column headers** with data type icons

### Data Type Icons

Tableau automatically detects what type each column is:

| Icon | Type | Example |
|------|------|---------|
| **Abc** | Text (string) | Product names, regions |
| **#** | Number | Quantity, revenue |
| **Calendar** | Date | Sale date, hire date |
| **T\|F** | Boolean | True/False values |

If Tableau guesses wrong (e.g., treats a date as text), click the icon above the column name and select the correct type.

## Dimensions vs. Measures

Tableau sorts your columns into two categories:

- **Dimensions** (blue) Categorical data you group by: product name, region, department
- **Measures** (green) Numeric data you calculate with: revenue, salary, quantity

This is important because it affects how Tableau builds charts. Dimensions go on the "axes" (categories), and measures get aggregated (summed, averaged, etc.).

## Connecting Multiple Files

To work with more than one CSV:

1. After connecting your first file, look at the top-left area
2. Click **Add** next to "Connections"
3. Select **Text file** again
4. Choose another CSV (e.g., `employees.csv`)

Tableau will try to automatically join the tables. If the tables aren't related, you can drag each one independently.

## Going to the Worksheet

Once your data looks correct in the preview:

1. Click the **Sheet 1** tab at the bottom of the screen
2. This takes you to the worksheet where you build charts

You'll see:
- **Left sidebar:** Your columns, split into Dimensions and Measures
- **Top area:** Empty "Columns" and "Rows" shelves
- **Center:** A blank canvas your future chart

## Quick Check

Before moving on, make sure:
- Your data loaded correctly (check the preview for obvious issues)
- Date columns show the calendar icon (not Abc)
- Number columns show the # icon (not Abc)
- You can see your columns listed in the left sidebar on Sheet 1

## Next Steps

In the next lesson, you'll drag your first columns onto the canvas and create your first chart. It's easier than you think.
