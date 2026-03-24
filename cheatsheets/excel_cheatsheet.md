# Excel Cheatsheet

Quick reference for Excel formulas, shortcuts, and features. Print this out and keep it nearby.

---

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Save | Ctrl + S |
| Undo | Ctrl + Z |
| Redo | Ctrl + Y |
| Copy | Ctrl + C |
| Paste | Ctrl + V |
| Find | Ctrl + F |
| Replace | Ctrl + H |
| Select all | Ctrl + A |
| Jump to last cell | Ctrl + End |
| Jump to first cell | Ctrl + Home |
| Insert new row | Select row, Ctrl + Shift + + |
| Delete row | Select row, Ctrl + - |
| Toggle filters | Ctrl + Shift + L |
| AutoSum | Alt + = |

---

## Essential Formulas

### Math
```
=SUM(A2:A100)           Add up a range
=AVERAGE(A2:A100)       Calculate the mean
=MIN(A2:A100)           Smallest value
=MAX(A2:A100)           Largest value
=COUNT(A2:A100)         Count cells with numbers
=COUNTA(A2:A100)        Count non-empty cells
=ROUND(A2, 2)           Round to 2 decimal places
```

### Conditional
```
=IF(A2>100, "High", "Low")              If/then/else
=COUNTIF(B2:B100, "Electronics")        Count matching cells
=SUMIF(B2:B100, "North", C2:C100)       Sum where condition met
=AVERAGEIF(B2:B100, "Sales", C2:C100)   Average where condition met
```

### Lookup
```
=VLOOKUP("Laptop", A2:F100, 6, FALSE)   Find value in a table
=INDEX(C2:C100, MATCH("Laptop", A2:A100, 0))   More flexible lookup
```

### Text
```
=LEN(A2)                   Length of text
=UPPER(A2)                 Convert to uppercase
=LOWER(A2)                 Convert to lowercase
=TRIM(A2)                  Remove extra spaces
=LEFT(A2, 3)               First 3 characters
=RIGHT(A2, 3)              Last 3 characters
=CONCATENATE(A2, " ", B2)  Join text (or use &)
```

### Date
```
=TODAY()                   Today's date
=YEAR(A2)                  Extract year
=MONTH(A2)                 Extract month
=DAY(A2)                   Extract day
=DATEDIF(A2, B2, "D")     Days between two dates
```

---

## Pivot Tables Quick Steps

1. Select your data (Ctrl + A)
2. Insert > PivotTable > New Worksheet > OK
3. Drag fields:
   - **Rows** = categories to group by
   - **Values** = numbers to calculate (Sum, Average, Count)
   - **Columns** = second grouping dimension (optional)
   - **Filters** = dropdown filter (optional)
4. To change Sum to Average: click dropdown on value > Value Field Settings

---

## Charts Quick Steps

1. Select data (including headers)
2. Insert > choose chart type
3. Click chart > + button > add Title, Labels, Legend
4. Right-click elements to format

### Chart Type Guide

| Question | Chart |
|----------|-------|
| Compare categories | Bar / Column |
| Show trend over time | Line |
| Show proportions | Pie (max 5 slices) |
| Show relationships | Scatter |

---

## Data Validation Tips

- **Numbers stored as text:** Select column > Data > Text to Columns > Finish
- **Dates not recognized:** Select column > Format Cells > Date
- **Remove duplicates:** Data > Remove Duplicates
- **Sort:** Data > Sort (one or multiple levels)
- **Filter:** Data > Filter (or Ctrl + Shift + L)

---

## Conditional Formatting

1. Select range
2. Home > Conditional Formatting
3. Options:
   - **Highlight Cells Rules** > Greater Than, Less Than, Equal To
   - **Color Scales** > Green-Yellow-Red gradient
   - **Data Bars** > In-cell bar charts

---

## Google Sheets Differences

| Excel | Google Sheets |
|-------|--------------|
| Ctrl + Shift + L (filter) | Data > Create a filter |
| Insert > PivotTable | Insert > Pivot table |
| VLOOKUP | Same syntax |
| Conditional Formatting | Format > Conditional formatting |
| .xlsx files | .gsheet (auto-saves to cloud) |
