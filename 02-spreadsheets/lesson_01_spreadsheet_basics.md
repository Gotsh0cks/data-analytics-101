# Lesson 1: Spreadsheet Basics

## What Is a Spreadsheet?

A spreadsheet is a grid of **rows** and **columns**. Each box in the grid is called a **cell**. That is it. Every spreadsheet you will ever see from a simple grocery list to a million-row financial dataset is built on this same grid.

- **Rows** go horizontally (left to right). They are numbered: 1, 2, 3, ...
- **Columns** go vertically (top to bottom). They are labeled with letters: A, B, C, ...
- **Cells** are identified by their column letter and row number. Cell **B3** is where column B meets row 3.

## Opening the Sample File

1. Make sure you have run `create_excel_samples.py` (see the Module README)
2. Open the file `data/excel/sales_data.xlsx` in Excel (or Google Sheets or LibreOffice Calc)
3. You should see a table of sales data with blue headers

## What You Are Looking At

The **Data** sheet contains sales transactions:

| Column | What It Contains | Example |
|--------|-----------------|---------|
| A: date | When the sale happened | 2024-01-05 |
| B: product | What was sold | Laptop |
| C: category | Product category | Electronics |
| D: region | Where it was sold | North |
| E: quantity | How many units | 2 |
| F: unit_price | Price per unit | 999.99 |
| G: revenue | Total sale amount | 1999.98 |

## Key Concepts

### The Formula Bar

At the top of the screen (just below the toolbar), you will see the **formula bar**. When you click on any cell, the formula bar shows what is *actually* in that cell either a value or a formula.

Try clicking on different cells to see their contents in the formula bar.

### The Name Box

To the left of the formula bar is the **Name Box**. It shows the address of the currently selected cell (like "A1" or "C5"). You can also type a cell address here and press Enter to jump directly to that cell.

### Sheets (Tabs)

At the bottom of the screen, you will see tabs labeled **Data** and **Summary**. These are different **sheets** within the same workbook. Click between them to switch views.

The Summary sheet contains some pre-built formulas you will learn how those work in the next lesson.

## Essential Navigation

| Action | How |
|--------|-----|
| Move one cell | Arrow keys |
| Jump to the beginning | Ctrl + Home |
| Jump to the last cell with data | Ctrl + End |
| Select a whole row | Click the row number on the left |
| Select a whole column | Click the column letter at the top |
| Select all data | Ctrl + A |

### Scrolling Through Data

If your data has many rows (this one has about 100), use:
- **Scroll wheel** to move up and down
- **Ctrl + Down Arrow** to jump to the last row of data in the current column
- **Ctrl + Up Arrow** to jump back to the top

Notice that the header row stays visible as you scroll that is because we froze the top row. This is a common practice so you always know which column you are looking at.

## What Is a "Range"?

A range is a group of cells. You describe a range by giving the top-left and bottom-right cells, separated by a colon:

- **A1:A10** cells A1 through A10 (a column of 10 cells)
- **A1:G1** cells A1 through G1 (the entire header row)
- **A1:G103** all of the data including headers

You will use ranges constantly when writing formulas.

## Try It Yourself

1. Open `data/excel/sales_data.xlsx`
2. Click on cell G2. What value do you see? What does the formula bar show?
3. Use Ctrl + End to find the last row of data. How many rows are there?
4. Click the "Summary" tab at the bottom. Click on cell B3 look at the formula bar to see the formula
5. Open `data/excel/employees.xlsx` and `data/excel/customers.xlsx` to see different datasets in the same format

---

Next up: [Formulas and Functions](lesson_02_formulas_and_functions.md) make Excel do math for you.
