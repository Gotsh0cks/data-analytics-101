# Installing SQL Server and Azure Data Studio

## What Is a Database?

A database is an **organized filing cabinet for data that lives on your computer** (or on a server somewhere). Instead of storing data in a bunch of separate spreadsheets scattered across your desktop, a database keeps everything in one place, organized into tables, and makes it fast to search and retrieve exactly what you need.

Think of it this way: a spreadsheet is like a single sheet of paper with data on it. A database is like a whole filing cabinet with many labeled drawers, each containing neatly organized sheets that can reference each other.

---

## What Is SQL Server?

SQL Server is **Microsoft's database software**. It is one of the most widely used databases in the business world, especially in companies that use other Microsoft products like Windows, Excel, and Office 365.

SQL Server stores your data and lets you ask questions about it using a language called **SQL** (pronounced "sequel"). SQL stands for Structured Query Language, and it is the standard way to talk to databases. You will learn SQL later in this course.

We will install the **free** version called SQL Server Express. It has everything you need for learning and for many real-world uses.

---

## What Is Azure Data Studio?

Azure Data Studio is a **tool for writing and running SQL queries**. Think of it the same way you think about VS Code: VS Code is where you write Python code, and Azure Data Studio is where you write SQL code to interact with your database.

It is free, made by Microsoft, and designed to be beginner-friendly.

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

## Part 2: Install Azure Data Studio

### Step 1: Download Azure Data Studio

1. Open your web browser.
2. Go to **[https://learn.microsoft.com/en-us/azure-data-studio/download-azure-data-studio](https://learn.microsoft.com/en-us/azure-data-studio/download-azure-data-studio)**
3. Under the Windows section, click the download link for the **User Installer** (the `.exe` file).
4. Wait for the download to finish.

### Step 2: Install Azure Data Studio

1. Open the downloaded file.
2. If Windows asks "Do you want to allow this app to make changes to your device?", click **Yes**.
3. Accept the license agreement and click **Next**.
4. Keep clicking **Next** through the options — the defaults are fine.
5. Click **Install**.
6. When it finishes, leave "Launch Azure Data Studio" checked and click **Finish**.

---

## Part 3: Connect to Your Local SQL Server

Now let's make sure everything is working by connecting Azure Data Studio to the SQL Server you just installed.

### Step 1: Open Azure Data Studio

If it did not open automatically, press the Windows key, type **Azure Data Studio**, and press Enter.

### Step 2: Create a Connection

1. When Azure Data Studio opens, you should see a **Welcome** tab. Look for a **"New Connection"** button, or click the **"Connections"** icon in the left sidebar (it looks like a small server or plug).
2. A connection form will appear. Fill it in as follows:

| Field | What to Enter |
|-------|--------------|
| **Connection type** | Microsoft SQL Server |
| **Server** | `localhost\SQLEXPRESS` |
| **Authentication type** | Windows Authentication |
| **Database** | (leave as default) |

**What does this mean?**
- **localhost** means "this computer" — the SQL Server is running right here on your machine, not on some remote server.
- **\SQLEXPRESS** is the name of the SQL Server instance you installed.
- **Windows Authentication** means SQL Server will verify your identity using your Windows login, so you do not need a separate username and password.

3. Click **Connect**.

### Step 3: Verify It Worked

If everything is set up correctly, you will see your server appear in the left sidebar under "Connections." You can click the little arrow next to it to expand it and see the system databases that SQL Server created automatically (like `master`, `model`, `msdb`, and `tempdb`).

You do not need to know what those databases are yet — we will cover that later. For now, the important thing is that you are connected.

---

## Troubleshooting

**If the connection fails**, the most common reason is that the SQL Server service is not running. Here is how to check:

1. Press the **Windows key**, type **Services**, and press Enter.
2. A window will open showing a long list of services. Scroll down until you find **"SQL Server (SQLEXPRESS)"**.
3. Look at the "Status" column. It should say **"Running"**.
4. If it does not say "Running", right-click on it and click **Start**.
5. Go back to Azure Data Studio and try connecting again.

If you are still stuck, check [common_errors.md](common_errors.md) for more help.

---

## You Are Done With This Step!

You now have a complete data analytics setup on your computer:

- **Python** for writing analysis code
- **VS Code** for editing your code
- **SQL Server** for storing data in databases
- **Azure Data Studio** for writing SQL queries

That is everything you need. In the next module, we will start actually working with data.

Before you move on, take a quick look at [common_errors.md](common_errors.md) so you know where to go if anything goes wrong later.
