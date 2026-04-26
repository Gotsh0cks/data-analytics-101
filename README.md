# Data Analytics 101

A beginner-friendly, hands-on guide to data analytics. No prior technical experience required.

This course teaches you to think critically about data and use the same tools that professional data analysts use every day:

1. **Understanding data** what analytics is, how to think about data problems
2. **Spreadsheets** hands-on Excel for formulas, pivot tables, and charts
3. **Python** pandas for loading, cleaning, and analyzing data at scale
4. **SQL** querying databases with T-SQL and SQL Server
5. **Visualization** matplotlib for code-based charts, Tableau for interactive dashboards
6. **Real-world data** finding, downloading, and evaluating external datasets

## Who Is This For?

This guide is for **complete beginners**. You do not need:

- A computer science degree
- Any programming experience
- Any math beyond basic arithmetic

All you need is a computer running Windows and a willingness to learn.

## How to Get This on Your Computer

If someone sent you a link and you ended up on a page that looks confusing that is **GitHub**. GitHub is a website where people store and share code. You do not need to understand GitHub to take this course. You just need to download the files once. Here is how:

### Step 1: Download the files

1. You should see a green button near the top of this page that says **"<> Code"**. Click it.
2. In the dropdown that appears, click **"Download ZIP"** (it is at the bottom of the dropdown).
3. Your browser will download a file called something like `data-analytics-101-main.zip`.

### Step 2: Extract the ZIP

A `.zip` file is like a compressed folder. You need to **extract** (unpack) it before you can use the files inside.

1. Open your **Downloads** folder (or wherever your browser saves files).
2. Find the file `data-analytics-101-main.zip`.
3. **Right-click** on it and select **"Extract All..."**
4. Choose a location you will remember your **Desktop** or **Documents** folder works well.
5. Click **Extract**.

You will now have a folder called `data-analytics-101-main`. You can rename it to just `data-analytics-101` if you like.

### Step 3: Start the course

Open the folder you just extracted. Inside you will see numbered folders (`00-what-is-data-analytics`, `01-setting-up`, etc.) and this README file. You are ready to go.

**Start reading at Module 0** (scroll down to the module table below, and click the link). Module 0 is just reading no software to install yet. Module 1 will walk you through installing everything you need.

### How to read the lesson files

The lessons are written in `.md` files (Markdown). You have a few options for reading them:

- **On GitHub** (easiest to start) Just browse the folders and click any `.md` file. GitHub will display it nicely formatted with headings, tables, and links.
- **In VS Code** (after Module 1) Once VS Code is installed, open any `.md` file and press **Ctrl+Shift+V** to see a nicely formatted preview. This is how you will read lessons for the rest of the course.
- **In Notepad** You can open `.md` files in Notepad. They are just text, so they are readable even without formatting.

You do not need to pick one use GitHub for Module 0, then switch to VS Code once it is installed in Module 1.

## How to Navigate This Course

This course is organized into **8 modules** (numbered 0 through 7). Each module is a folder. Inside each folder, there is a **README.md** file that tells you what the module covers, what order to do the lessons in, and where to go next.

**The path is simple: start at Module 0, finish it, move to Module 1, finish it, and so on.**

Every README links to the next module at the bottom, so you always know where to go. Click the folder links in the table below to begin.

| Module | What You Will Learn | Time Estimate |
|--------|-------------------|---------------|
| [Module 0: What Is Data Analytics](00-what-is-data-analytics/) | Concepts, tools overview, career paths | 30-45 min |
| [Module 1: Setting Up](01-setting-up/) | Install Python, VS Code, SQL Server, Tableau | 1-2 hours |
| [Module 2: Spreadsheets](02-spreadsheets/) | Excel: formulas, sorting, pivot tables, charts | 2-3 hours |
| [Module 3: Data Analysis](03-data-analysis/) | Python + pandas: load, filter, aggregate, clean | 3-4 hours |
| [Module 4: Databases & SQL](04-databases-and-sql/) | T-SQL: queries, joins, aggregations, Python+SQL | 4-5 hours |
| [Module 5: Visualization](05-visualization/) | matplotlib + Tableau: charts and dashboards | 4-5 hours |
| [Module 6: Real-World Data](06-real-world-data/) | Find and download external datasets | 1-2 hours |
| [Module 7: Capstone Project](07-capstone/) | End-to-end project using all your skills | 3-5 hours |

There are also [cheatsheets](cheatsheets/) you can print out and keep nearby as quick references.

## Where You Will Work

After Module 1, you will have a few tools installed. Here is when you use each one:

| Tool | What It Is | When You Use It |
|------|-----------|-----------------|
| **VS Code** | Code editor (your home base) | Python scripts, SQL queries, reading lessons, terminal |
| **Excel** | Spreadsheet application | Module 2 (spreadsheets) |
| **Tableau Public** | Dashboard builder | Module 5 Part 2 (interactive dashboards) |

**VS Code is where you spend most of your time.** You write Python there, you write SQL there, and you can even read the lesson files there. The only times you leave VS Code are for Excel and Tableau, which are point-and-click tools with their own windows.

## Getting Started

**First time here?** Start with [START_HERE.md](START_HERE.md). It explains how to use this course, how to check your setup, and how to ask for help if you get stuck.

After that, begin with [Module 0 - What Is Data Analytics](00-what-is-data-analytics/).

Module 0 is just reading no installing or coding. It explains what data analytics is, what tools you will learn, and what kind of career it can lead to. Then Module 1 walks you through installing everything.

## Sample Data

All lessons use the same three datasets located in the [data/](data/) folder:

- **sales_data.csv** - Sales transactions for a small company
- **employees.csv** - Employee records with departments and salaries
- **customers.csv** - Customer information and spending history

Module 6 also teaches you to download external datasets (Titanic, Iris, Tips, World Happiness) into `data/external/`.

Using the same data across all modules helps you see how the same questions can be answered with different tools.

## Prerequisites

- A computer running Windows 10 or 11
- An internet connection (for downloading tools)
- About 3 GB of free disk space

Everything else is covered in Modules 0 and 1.

## Quick Links

| Resource | What It Is |
|----------|-----------|
| [Start Here](START_HERE.md) | Friendly first stop for self-paced learners |
| [Progress Tracker](progress_tracker.md) | Checklist for tracking your course progress |
| [Get Help](GET_HELP.md) | Template for asking for help when you are stuck |
| [Cheatsheets](cheatsheets/) | Printable quick-reference sheets for Excel, pandas, SQL, matplotlib, Tableau |
| [Sample Data](data/) | The CSV files used throughout the course |
| [Module 0](00-what-is-data-analytics/) | First course module |
