# Module 6 Exercise Hints

Try each exercise on your own before reading the hint. If a hint gives you enough to keep going, return to your own code and keep working before checking the expected outputs.

## Exercise 1: Explore the Titanic Dataset

Load the file with `pd.read_csv()`. If you are running your script from the repo root, the path will look like `data/external/titanic.csv`.

Start with the basic inspection tools:

```python
print(titanic.shape)
print(titanic.head())
titanic.info()
```

The `Survived` column uses `0` for did not survive and `1` for survived. Because of that, the mean of the column gives the survival rate as a decimal. Multiply by `100` to turn it into a percentage.

For missing values, use:

```python
missing = titanic.isnull().sum()
print(missing[missing > 0])
```

## Exercise 2: Tipping Patterns

After loading `tips.csv`, inspect it first so you know the column names:

```python
print(tips.head())
print(tips["day"].value_counts())
print(tips["time"].value_counts())
```

Use the `tip` column for average tip amount.

For average tip by day, group by the `day` column:

```python
tips.groupby("day")["tip"].mean()
```

For lunch compared with dinner, group by the `time` column instead. After you get the two averages, write one plain-English sentence saying which meal has the higher average tip.

## Exercise 3: Iris Species Comparison

Load `iris.csv`, then confirm the species names and columns:

```python
print(iris.head())
print(iris["species"].value_counts())
```

To compare flower species, use `groupby("species")`.

For average petal length:

```python
iris.groupby("species")["petal_length"].mean()
```

For widest sepals, use the `sepal_width` column. Once you have the average sepal width for each species, look for the largest value.

## Exercise 4: Find Your Own Dataset

Use the same first-pass checklist on any dataset you find:

1. Load the dataset with `pd.read_csv()` or the loading function that matches the file type.
2. Print `df.shape` to see rows and columns.
3. Print `df.head()` to inspect the first few records.
4. Print `df.info()` or `df.dtypes` to understand column types.
5. Use `df.isnull().sum()` to check missing values.
6. Use `.value_counts()` on category columns to see common values.
7. Write three questions that match the columns you actually have.

Good questions are specific and answerable. For example, instead of "What is interesting?", aim for a question shaped like "Which category has the highest average value?" or "How does this number change by group?"
