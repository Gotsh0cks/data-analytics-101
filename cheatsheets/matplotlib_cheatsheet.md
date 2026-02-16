# Matplotlib & Seaborn Quick Reference

## Basic Setup

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

## Chart Types

### Bar Chart (Vertical)

```python
plt.bar(df["category"], df["value"])
plt.show()
```

### Bar Chart (Horizontal)

```python
plt.barh(df["category"], df["value"])
plt.show()
```

### Line Chart

```python
plt.plot(df["x"], df["y"])
plt.show()
```

### Pie Chart

```python
plt.pie(df["value"], labels=df["category"], autopct="%1.1f%%")
plt.show()
```

### Scatter Plot

```python
plt.scatter(df["x"], df["y"])
plt.show()
```

### Seaborn Bar Plot

```python
sns.barplot(data=df, x="category", y="value")
plt.show()
```

### Seaborn Scatter Plot

```python
sns.scatterplot(data=df, x="col1", y="col2", hue="category")
plt.show()
```

## Styling

| What You Want To Do | Code |
|---|---|
| Set figure size | `plt.figure(figsize=(10, 6))` |
| Add title | `plt.title("My Chart")` |
| Add x-axis label | `plt.xlabel("X Axis")` |
| Add y-axis label | `plt.ylabel("Y Axis")` |
| Add legend | `plt.legend()` |
| Add grid | `plt.grid(True)` |
| Change colors | `plt.bar(x, y, color="skyblue")` |
| Set seaborn style | `sns.set_style("whitegrid")` |
| Save chart to file | `plt.savefig("chart.png", dpi=150, bbox_inches="tight")` |
| Rotate x-axis labels | `plt.xticks(rotation=45)` |
| Tight layout | `plt.tight_layout()` |
