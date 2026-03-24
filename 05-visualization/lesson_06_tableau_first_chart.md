# Lesson 2: Your First Chart

## How Tableau Charts Work

Building a chart in Tableau follows a simple pattern:

1. **Drag a dimension** to the **Columns** or **Rows** shelf (this sets up your categories)
2. **Drag a measure** to the opposite shelf (this provides the numbers)
3. Tableau automatically creates the chart

That's it. Let's try it.

## Building a Bar Chart: Revenue by Category

Make sure you have `sales_data.csv` connected (from Lesson 1) and you're on a worksheet (Sheet 1).

### Step 1: Add the categories

- In the left sidebar, find **Category** under Dimensions
- **Drag it to the Columns shelf** (the bar at the top that says "Columns")
- You'll see the category names appear across the bottom of the canvas

### Step 2: Add the numbers

- Find **Revenue** under Measures
- **Drag it to the Rows shelf**
- A bar chart appears automatically, showing total revenue per category

Congratulations you just created your first Tableau chart.

### Step 3: Sort the bars

- Click the **sort descending** button in the toolbar (looks like a bar chart going from tall to short)
- The bars are now ordered from highest to lowest revenue

## Adding Labels

To show the actual numbers on each bar:

1. Find **Revenue** in Measures again
2. **Drag it onto the bars themselves** (or onto the **Label** box in the Marks card on the left)
3. Numbers appear on each bar

## Adding Color

To color the bars by category:

1. Find **Category** in Dimensions
2. **Drag it to the Color box** in the Marks card
3. Each bar gets a different color

## Changing Chart Types

Tableau picks a chart type automatically, but you can change it:

1. Click the **Show Me** button in the top right
2. A panel appears showing different chart types
3. Click on different options to see how they look
4. Click the chart type you want to keep

Common types you'll see:
- **Bar chart** comparing categories (what we just made)
- **Line chart** showing trends over time
- **Scatter plot** showing relationships between two numbers
- **Map** geographic data
- **Treemap** proportional comparison

## Building a Second Chart: Revenue Over Time

Let's add a second worksheet:

1. Click the **New Worksheet** icon at the bottom (looks like a sheet with a plus sign), or right-click any tab and select "New Worksheet"
2. On the new sheet:
   - Drag **Date** to the Columns shelf
   - Drag **Revenue** to the Rows shelf
3. Tableau creates a line chart showing revenue over time

### Adjusting the Date Level

By default, Tableau might show years. To see months:

1. Click the small **+** or **-** next to the date field on the Columns shelf
2. Or right-click the date field and choose the time period you want (Year, Quarter, Month, Day)

## Adding Filters

Filters let viewers focus on specific parts of the data:

1. Drag **Region** from Dimensions to the **Filters** shelf (on the left side)
2. A dialog box appears check which regions you want to show
3. Click **OK**

To make the filter visible to users:

1. Click the small dropdown arrow on the filter pill
2. Select **Show Filter**
3. A filter control appears on the right side of the canvas

## Renaming Your Sheet

Double-click the sheet tab at the bottom (where it says "Sheet 1") and type a descriptive name like "Revenue by Category" or "Sales Trend".

## Saving Your Work

- Press **Ctrl + S** to save
- Since this is Tableau Public, your work saves to the cloud
- You'll need to sign in with your Tableau Public account the first time

## What You've Learned

In this lesson you:
- Created a bar chart by dragging dimensions and measures
- Added labels and colors
- Changed chart types
- Created a line chart with time data
- Added interactive filters
- Created multiple worksheets

Next, we'll explore more chart types and learn to format them professionally.
