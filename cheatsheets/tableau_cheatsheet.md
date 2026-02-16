# Tableau Public Cheatsheet

Quick reference for Tableau Public. Print this out and keep it nearby.

---

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Save | Ctrl + S |
| Undo | Ctrl + Z |
| Redo | Ctrl + Y |
| New worksheet | Ctrl + M |
| Duplicate sheet | Ctrl + D |
| Select all | Ctrl + A |
| Fit to window | Ctrl + Shift + F |

---

## Building Charts

### The Basic Formula
1. Drag a **Dimension** (blue) to Columns or Rows
2. Drag a **Measure** (green) to the other shelf
3. Tableau auto-creates the chart

### Common Chart Recipes

**Bar chart:** Dimension on Columns, Measure on Rows

**Horizontal bar:** Dimension on Rows, Measure on Columns

**Line chart:** Date on Columns, Measure on Rows

**Scatter plot:** Measure on Columns, Measure on Rows

**Stacked bar:** Bar chart + drag a Dimension to Color

**Pie chart:** Click Show Me > select pie chart icon

**Treemap:** Click Show Me > select treemap icon

---

## The Marks Card

The Marks card (left side of the canvas) controls how data points look:

| Drop Zone | What It Does |
|-----------|-------------|
| **Color** | Colors data points by a field |
| **Size** | Makes points bigger/smaller by value |
| **Label** | Shows values on the chart |
| **Detail** | Adds granularity without visual change |
| **Tooltip** | Controls hover information |

---

## Filters

### Adding a filter
1. Drag a field to the **Filters** shelf
2. Choose values to include/exclude
3. Click OK

### Making a filter visible
- Click the dropdown arrow on the filter pill > **Show Filter**

### Filter types
- **Single value dropdown** — user picks one value
- **Multiple values list** — user checks multiple values
- **Slider** — for numeric ranges

### Apply filter to all sheets
- Right-click filter > **Apply to Worksheets** > **All Using This Data Source**

---

## Calculated Fields

Create new fields from existing data:

1. Right-click in the Data pane > **Create Calculated Field**
2. Name it and write the formula

### Common formulas

```
// Tip percentage
[Tip] / [Total Bill] * 100

// Full name
[First Name] + " " + [Last Name]

// Profit margin
([Revenue] - [Cost]) / [Revenue] * 100

// Year from date
YEAR([Date])

// IF statement
IF [Survived] = 1 THEN "Survived" ELSE "Did Not Survive" END
```

---

## Dashboards

### Creating a dashboard
1. Click the **New Dashboard** icon (bottom of screen)
2. Set the size (Automatic or fixed)
3. Drag worksheets from the left sidebar onto the canvas

### Making charts interactive
- Click a chart > click the **funnel icon** > now clicking that chart filters others

### Adding elements
- **Text:** Drag "Text" from Objects to add explanatory notes
- **Image:** Drag "Image" to add logos or images
- **Blank:** Drag "Blank" to add white space

---

## Formatting Essentials

### Chart title
- Double-click the title to edit

### Number format
- Right-click a measure > **Format** > **Numbers**
- Options: Currency, Percentage, Number

### Axis
- Right-click axis > **Edit Axis** (title, range)
- Right-click axis > **Format** (font, color)

### Colors
- Click **Color** in Marks card > **Edit Colors** > choose palette

### Remove clutter
- **Format** menu > **Lines** > turn off unnecessary gridlines
- **Format** menu > **Borders** > simplify borders

---

## Publishing

1. **File** > **Save to Tableau Public As...**
2. Sign in to your Tableau Public account
3. Name the workbook
4. Click **Save**
5. Dashboard is now live at: `public.tableau.com/views/YourWorkbook/...`

---

## Dimensions vs. Measures

| Dimensions (Blue) | Measures (Green) |
|-------------------|-----------------|
| Categories, names, dates | Numbers you calculate |
| Go on axes | Get aggregated (SUM, AVG) |
| Answer "what" or "which" | Answer "how many" or "how much" |
| Examples: Region, Product, Department | Examples: Revenue, Salary, Quantity |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Date shows as text (Abc) | Click the type icon > change to Date |
| Numbers show as text | Click the type icon > change to Number |
| Chart shows wrong aggregation | Right-click the measure > choose SUM, AVG, etc. |
| Too many marks | Add a filter or increase aggregation level |
| Dashboard looks different when published | Set a fixed dashboard size instead of Automatic |
