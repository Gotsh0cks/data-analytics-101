# Module 2 Exercises: Basic Visualization

Test your charting skills with these practice problems. Each exercise asks you to create a chart from one of the datasets in the `../data/` folder. Save each chart as a PNG file and make sure it displays on screen.

Remember the basics for every chart:
- A clear, descriptive title
- Labeled axes
- `plt.tight_layout()` before saving
- `plt.savefig("filename.png")` to save
- `plt.show()` to display

---

## Exercise 1: Average Salary by Department (Bar Chart)

Using `../data/employees.csv`, create a **vertical bar chart** that shows the **average salary** for each department.

Your chart should have:
- A title like "Average Salary by Department"
- Labeled x-axis ("Department") and y-axis ("Average Salary ($)")
- A color of your choice

Save it as `exercise_01_salary_by_dept.png`.

---

## Exercise 2: Employees per Department (Pie Chart)

Using `../data/employees.csv`, create a **pie chart** showing how many employees are in each department.

Your chart should have:
- Labels for each department
- Percentages displayed on each slice (use `autopct`)
- A title like "Employee Distribution by Department"

Save it as `exercise_02_employees_pie.png`.

---

## Exercise 3: Customer Signups per Month (Line Chart)

Using `../data/customers.csv`, create a **line chart** showing how many new customers signed up each month.

Steps to get you started:
- Load the data and convert `signup_date` to a datetime column
- Create a month column using `.dt.to_period("M")`
- Count the number of customers per month
- Plot the result as a line chart

Your chart should have:
- Markers at each data point
- A title like "New Customer Signups per Month"
- Rotated x-axis labels so the dates are readable

Save it as `exercise_03_signups_per_month.png`.

---

## Exercise 4: Salary vs. Years Since Hire (Scatter Plot)

Using `../data/employees.csv`, create a **scatter plot** showing the relationship between an employee's salary and how many years they have been at the company.

Steps to get you started:
- Load the data and convert `hire_date` to a datetime column
- Calculate years since hire: subtract `hire_date` from today's date and convert to years
- Plot salary on the y-axis and years on the x-axis

Your chart should have:
- Semi-transparent dots (`alpha=0.6`)
- A title like "Salary vs. Years at Company"
- Properly labeled axes

Save it as `exercise_04_salary_vs_tenure.png`.

---

## Exercise 5: Presentation-Ready Chart

Take **any chart** from the exercises above (or from the lessons) and make it "presentation-ready" using seaborn styling.

Your chart should include:
- A seaborn style (`sns.set_style("whitegrid")` or another style)
- A color from a seaborn palette
- A bold title with a larger font size
- Labeled axes with appropriate font sizes
- Grid lines
- `dpi=150` in your `savefig()` call for higher quality

Save it as `exercise_05_polished_chart.png`.

---

## Exercise 6 (BONUS): Combining Data from Two Files

Create a single chart that uses data from **two different CSV files**. Here are some ideas:

- A bar chart comparing the number of records in each dataset (how many sales vs. how many customers vs. how many employees)
- A scatter plot that merges customer spending data with another dataset
- Any creative combination you can think of

The goal is to practice loading multiple files and putting the information together in one visualization.

Save it as `exercise_06_combined_chart.png`.

---

## Hints

If you get stuck, here are some pointers:

**Exercise 1:**
```python
avg_salary = df.groupby("department")["salary"].mean()
```
Remember that some salary values might be missing. `mean()` will skip them automatically.

**Exercise 2:**
```python
dept_counts = df["department"].value_counts()
plt.pie(dept_counts.values, labels=dept_counts.index, autopct="%1.1f%%")
```
Note: some employees might have a missing department. You can drop those rows first with `df.dropna(subset=["department"])`.

**Exercise 3:**
```python
customers["signup_date"] = pd.to_datetime(customers["signup_date"])
customers["month"] = customers["signup_date"].dt.to_period("M")
signups_per_month = customers.groupby("month").size()
```

**Exercise 4:**
```python
from datetime import datetime

df["hire_date"] = pd.to_datetime(df["hire_date"])
df["years_at_company"] = (datetime.now() - df["hire_date"]).dt.days / 365.25
```
Remember to drop rows where salary is missing before plotting.

**Exercise 5:**
```python
import seaborn as sns
sns.set_style("whitegrid")
plt.title("My Title", fontsize=14, fontweight="bold")
plt.savefig("exercise_05_polished_chart.png", dpi=150)
```

**Exercise 6:**
```python
sales = pd.read_csv("../data/sales_data.csv")
employees = pd.read_csv("../data/employees.csv")
# Now combine or compare the data in a single chart
```
