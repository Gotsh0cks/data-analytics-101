# Installing SQL Server

## What Is a Database?

A database is an **organized filing cabinet for data that lives on your computer** (or on a server somewhere). Instead of storing data in a bunch of separate spreadsheets scattered across your desktop, a database keeps everything in one place, organized into tables, and makes it fast to search and retrieve exactly what you need.

Think of it this way: a spreadsheet is like a single sheet of paper with data on it. A database is like a whole filing cabinet with many labeled drawers, each containing neatly organized sheets that can reference each other.

---

## What Is SQL Server?

SQL Server is **Microsoft's database software**. It is one of the most widely used databases in the business world, especially in companies that use other Microsoft products like Windows, Excel, and Office 365.

SQL Server stores your data and lets you ask questions about it using a language called **SQL** (pronounced "sequel"). SQL stands for Structured Query Language, and it is the standard way to talk to databases. You will learn SQL later in this course.

We will install the **free** version called SQL Server Express. It has everything you need for learning and for many real-world uses.

---

## How Will You Write SQL?

You already installed VS Code for writing Python. The good news: **VS Code can also run SQL queries.** You installed the SQL Server (mssql) extension in the previous step ([Install VS Code](install_vscode.md)), which gives VS Code the ability to connect to SQL Server and run queries — all without leaving the editor.

This means VS Code is your **single workspace** for both Python and SQL throughout this course. No need to switch between different applications.

---

## Part 1: Install SQL Server 2022 Express

### Step 1: Download SQL Server Express

1. Open your web browser.
2. Go to **[https://www.microsoft.com/en-us/sql-server/sql-server-downloads](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)**
3. Scroll down the page. You will see different editions of SQL Server. Look for the section labeled **"Express"** — it will say "Free" underneath it.
   - **Do not** pick "Developer" or "Enterprise" — those are more complex to set up. Express is the right choice for learning.
4. Click the **"Download now"** button under Express.
5. A small file will download (called something like `SQL2022-SSEI-Expr.exe`). This is not the full installer — it is a downloader that will fetch the rest.

### Step 2: Run the Installer

1. Open the downloaded file.
2. If Windows asks "Do you want to allow this app to make changes to your device?", click **Yes**.
3. You will see three installation options. Click **"Basic"**.
   - Basic gives you a standard installation with sensible defaults. This is the easiest path and is perfect for learning.
4. Accept the license terms.
5. You can keep the default install location or change it. The default is fine — just click **Install**.
6. The installer will download and set up SQL Server. This can take **5 to 15 minutes** depending on your internet speed. You will see a progress bar.
7. When it finishes, you will see a summary screen showing your connection information. You will see something like:
   - **Instance name:** SQLEXPRESS
   - **Connection string:** (a long line of text — you do not need to worry about this right now)

**Important:** Make a note of the instance name. It is usually **SQLEXPRESS**. You will need it in a moment.

8. Click **Close**.

---

## Part 2: Connect VS Code to Your SQL Server

Now let's make sure everything is working by connecting VS Code to the SQL Server you just installed.

### Step 1: Open VS Code

If it is not already open, press the Windows key, type **Visual Studio Code**, and press Enter.

### Step 2: Create a Connection Profile

1. Press **Ctrl+Shift+P** to open the Command Palette (the search bar at the top of VS Code).
2. Type **sql connection** and select **"MS SQL: Add Connection"** from the list.
3. VS Code will ask you a series of questions at the top of the screen. Answer them one at a time:

| Prompt | What to Type |
|--------|-------------|
| **Server name** | `localhost\SQLEXPRESS` |
| **Database name** | Press **Enter** to skip (leave blank — this connects to the whole server) |
| **Authentication type** | Select **Windows Authentication** |
| **Profile name** | Type `Local SQL Server` (or any name you like) and press **Enter** |

**What does this mean?**
- **localhost** means "this computer" — the SQL Server is running right here on your machine, not on some remote server.
- **\SQLEXPRESS** is the name of the SQL Server instance you installed.
- **Windows Authentication** means SQL Server will verify your identity using your Windows login, so you do not need a separate username and password.

### Step 3: Verify It Worked

After you press Enter on the last prompt, VS Code will attempt to connect. You should see a confirmation in the bottom status bar showing your server name. If it connects successfully, you are all set.

To test it further:

1. Create a new file: press **Ctrl+N**, then save it as `test.sql` (press **Ctrl+S**).
2. Type this simple query:

```sql
SELECT @@VERSION;
```

3. Press **Ctrl+Shift+E** to run the query.
4. If VS Code asks you to choose a connection, select the **Local SQL Server** profile you just created.
5. You should see a results panel appear at the bottom showing the SQL Server version information.

If you see results, everything is working. You can delete `test.sql` — it was just for testing.

---

## Running SQL Files in VS Code — Quick Reference

You will use these steps throughout Module 4 when working with `.sql` files:

1. **Open** the `.sql` file in VS Code (double-click it in the Explorer sidebar, or use File > Open File)
2. **Connect** — if VS Code asks which connection to use, pick your **Local SQL Server** profile
3. **Run the whole file** — press **Ctrl+Shift+E**
4. **Run just a selection** — highlight the lines you want to run, then press **Ctrl+Shift+E**
5. **View results** — they appear in a panel at the bottom of VS Code

| Action | Shortcut |
|--------|----------|
| Run query / selection | Ctrl+Shift+E |
| Open Command Palette | Ctrl+Shift+P |
| Change SQL connection | Ctrl+Shift+P, then type "MS SQL: Connect" |

---

## Troubleshooting

**If the connection fails**, the most common reason is that the SQL Server service is not running. Here is how to check:

1. Press the **Windows key**, type **Services**, and press Enter.
2. A window will open showing a long list of services. Scroll down until you find **"SQL Server (SQLEXPRESS)"**.
3. Look at the "Status" column. It should say **"Running"**.
4. If it does not say "Running", right-click on it and click **Start**.
5. Go back to VS Code and try connecting again (Ctrl+Shift+P > "MS SQL: Connect").

If you are still stuck, check [common_errors.md](common_errors.md) for more help.

---

## You Are Done With This Step!

You now have SQL Server installed and connected to VS Code. Combined with the Python extension you installed earlier, VS Code is now your single workspace for:

- **Python** scripts (Modules 3, 5, 6, 7)
- **SQL** queries (Module 4)

That is everything you need. In the next step, we will install Tableau Public for interactive dashboards.

Before you move on, take a quick look at [common_errors.md](common_errors.md) so you know where to go if anything goes wrong later.

Next up: [Install Tableau Public](install_tableau_public.md)
