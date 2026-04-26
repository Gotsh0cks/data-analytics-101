# Get Help

Getting stuck is normal. Most beginner problems come from one small detail: a folder, command, package, file name, or setup step.

Before you ask for help, try to capture exactly what happened. That makes the fix much faster.

## Try These First

1. Make sure you opened the main `data-analytics-101` folder, not one of the numbered module folders.
2. If you are in VS Code, open the terminal with **Terminal > New Terminal**.
3. Run this from the main course folder if Python is already installed:

```bash
python check_setup.py
```

4. Copy the exact command you ran and the exact error message you saw.
5. If copying is hard, send a screenshot.

You do not need to solve the problem before asking. The goal is to share enough context that someone can help you quickly.

## Help Request Template

```text
I need help with Data Analytics 101.

Module:
Lesson or file:

What I was trying to do:

The command I ran or step I tried:

What happened:

What I expected to happen:

Error message, if there was one:

Did I run python check_setup.py?

What did check_setup.py print?
```

## If Python Is Not Recognized

You may see something like:

```text
'python' is not recognized as an internal or external command
```

Try this:

1. Close and reopen VS Code or your terminal.
2. Run:

```bash
python --version
```

3. If that fails, try:

```bash
py --version
```

4. If `py` works but `python` does not, use `py` for now:

```bash
py check_setup.py
```

5. If neither works, go back to `01-setting-up/01_install_python.md` and reinstall Python. Make sure to check **Add python.exe to PATH** during installation.

## If You See File Not Found

You may see something like:

```text
FileNotFoundError: [Errno 2] No such file or directory
```

This usually means one of three things:

- You are running the command from the wrong folder.
- The file path was typed differently from the lesson.
- The data file was not downloaded or created yet.

Try this:

1. In VS Code, choose **File > Open Folder**.
2. Open the main `data-analytics-101` folder.
3. Open a new terminal.
4. Run:

```bash
python check_setup.py
```

If the setup checker says a data file is missing, follow the module instructions that create or download that file.

## If The Terminal Is In The Wrong Folder

Commands in this course usually expect you to be in the main course folder.

In the terminal, run:

```bash
dir
```

You should see files like:

```text
START_HERE.md
README.md
check_setup.py
data
00-what-is-data-analytics
01-setting-up
```

If you do not see those, open the correct folder in VS Code:

1. Choose **File > Open Folder**.
2. Select the main `data-analytics-101` folder.
3. Open a new terminal.

## If Package Install Fails

You may see an error while installing packages like `pandas`, `matplotlib`, or `openpyxl`.

First, try:

```bash
python -m pip install --upgrade pip
python -m pip install pandas matplotlib seaborn openpyxl requests
```

If that fails, copy the full error message. Package errors can come from internet connection issues, Python install issues, or a missing permission.

If the command says `pip` is not recognized, use:

```bash
python -m pip --version
```

If that also fails, Python may not be installed correctly.

## If VS Code Feels Confusing

VS Code is a text editor with a built-in terminal. You do not need to know every button.

For this course, focus on four actions:

1. **Open a folder:** File > Open Folder.
2. **Open a file:** click it in the Explorer panel on the left.
3. **Preview Markdown:** open a `.md` file and press `Ctrl+Shift+V`.
4. **Open the terminal:** Terminal > New Terminal.

If the terminal looks stuck, close it with the trash can icon and open a new one.

## If SQL Server Will Not Connect

SQL Server setup can be fussy the first time.

Check these in order:

1. Did you install SQL Server Express?
2. Did you install the VS Code SQL Server extension?
3. Did you run `04-databases-and-sql/00_setup_database.sql`?
4. Is SQL Server running?
5. Did you try one of these server names?

```text
localhost
localhost\SQLEXPRESS
.
```

If Python cannot connect to SQL Server, the rest of the Python course may still work. SQL Server is mainly needed for Module 4 and the Python + SQL lesson.

## If Tableau Cannot Find A CSV

Tableau needs you to choose a CSV file from the course folder.

For Module 5, first run:

```bash
python 05-visualization/lesson_05_prepare_data_for_tableau.py
```

Then look in:

```text
data/tableau_ready/
```

You should see CSV files like:

```text
sales_data.csv
employees.csv
customers.csv
titanic.csv
```

If the folder is missing, run the preparation script again from the main course folder.

## Tips For Copying Error Messages

- Copy the exact error text if you can.
- If copying is hard, send a screenshot.
- Include the command you ran right before the error appeared.
- Mention whether you are using GitHub, VS Code, Notepad, SQL Server, or Tableau.

## Common Quick Checks

- Make sure you opened the main `data-analytics-101` folder in VS Code.
- Make sure you extracted the ZIP file before running scripts.
- Make sure the terminal is open inside VS Code.
- Make sure Python installed correctly by running `python --version`.
- Make sure core packages installed by running `python -m pip install pandas matplotlib seaborn openpyxl requests`.
