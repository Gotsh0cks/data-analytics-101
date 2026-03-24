# Installing VS Code

## What Is VS Code?

VS Code (short for Visual Studio Code) is a **text editor designed for writing code**. Think of it like Microsoft Word, but instead of writing essays, you write programs. It is free, made by Microsoft, and used by millions of people — from beginners to professionals.

You could technically write code in Notepad, but VS Code makes your life much easier. It color-codes your code so it is easier to read, catches mistakes as you type, and has a built-in terminal (we will explain what that is shortly).

## VS Code Is Your Home Base

Throughout this course, **VS Code is where you will spend most of your time.** It is not just for Python — by adding extensions, VS Code becomes your single workspace for:

- **Reading lessons** — the `.md` lesson files open nicely in VS Code (right-click a `.md` file > "Open Preview")
- **Writing and running Python** — Modules 3, 5, 6, and 7
- **Writing and running SQL** — Module 4
- **Using the terminal** — installing packages, running scripts

The only times you will leave VS Code are for **Excel** (Module 2) and **Tableau** (Module 5 Part 2), which are point-and-click tools with their own windows. Everything else happens here.

---

## Step 1: Download VS Code

1. Open your web browser.
2. Go to **[https://code.visualstudio.com/](https://code.visualstudio.com/)**
3. Click the big blue **"Download for Windows"** button.
4. A file will download. It will be called something like `VSCodeUserSetup-x64-1.x.x.exe`.

---

## Step 2: Install VS Code

1. Open the downloaded file.
2. If Windows asks "Do you want to allow this app to make changes to your device?", click **Yes**.
3. Accept the license agreement and click **Next**.
4. Keep clicking **Next** through the options — the default settings are fine for our purposes.
5. On the "Select Additional Tasks" screen, it is helpful (but not required) to check:
   - **"Add 'Open with Code' action to Windows Explorer file context menu"** — this lets you right-click any folder and open it directly in VS Code, which is very handy.
   - **"Add 'Open with Code' action to Windows Explorer directory context menu"** — same idea but for when you right-click inside a folder.
6. Click **Install**.
7. Wait for the installation to finish, then click **Finish**.

VS Code should open automatically. If it does not, you can find it by pressing the Windows key and typing **"Visual Studio Code"**.

---

## Step 3: Install the Python Extension

VS Code on its own does not know anything about Python. We need to add a **Python extension** so VS Code can understand Python code and help you write it.

1. Open VS Code if it is not already open.
2. Look at the left sidebar. You will see a column of icons. Click the one that looks like **four small squares** (a puzzle piece icon). This is the **Extensions** panel.
   - If you are not sure which icon it is, you can also press **Ctrl+Shift+X** on your keyboard to open Extensions.
3. In the search box at the top of the Extensions panel, type: **Python**
4. The first result should be **"Python"** by **Microsoft** (it will have a blue checkmark and millions of downloads). Click on it.
5. Click the blue **Install** button.
6. Wait a few seconds for it to install. That is it.

This extension gives you:
- Color-coded Python code (so different parts of your code appear in different colors, making it easier to read)
- Error highlighting (red underlines when something is wrong)
- The ability to run Python files directly from VS Code
- Helpful suggestions as you type

---

## Step 3b: Install the SQL Server Extension

Later in this course (Module 4), you will write SQL queries to talk to databases. Instead of using a separate application for SQL, we will install an extension that lets you **write and run SQL directly in VS Code** — the same place you write Python.

1. Open the **Extensions** panel again (click the puzzle piece icon or press **Ctrl+Shift+X**).
2. In the search box, type: **SQL Server (mssql)**
3. Look for **"SQL Server (mssql)"** by **Microsoft**. Click on it.
4. Click the blue **Install** button.
5. Wait a few seconds for it to install.

You will not use this extension until Module 4, but installing it now means your setup is complete. When you get to Module 4, the [Install SQL Server](03_install_sql_server.md) guide will walk you through connecting VS Code to your database.

---

## Step 4: Learn How to Open a Folder

In VS Code, you work with **folders** rather than individual files. This is because real projects usually have many files that work together, and opening the whole folder lets VS Code understand the full picture.

Here is how to open a folder:

1. In VS Code, click **File** in the top menu bar.
2. Click **Open Folder...**
3. A file browser will appear. Navigate to the folder you want to open. For this course, you will navigate to and select the **data-analytics-101** folder.
4. Click **Select Folder**.
5. If VS Code asks "Do you trust the authors of the files in this folder?", click **"Yes, I trust the authors"**.

You should now see the folder's contents in the left sidebar under **Explorer** (the top icon that looks like two overlapping documents).

---

## Step 5: Learn How to Open the Built-In Terminal

The **terminal** is a way to talk to your computer by typing commands instead of clicking buttons. VS Code has a terminal built right in, so you do not have to switch between windows.

There are two ways to open it:

**Option A: Using the menu**
1. Click **Terminal** in the top menu bar.
2. Click **New Terminal**.

**Option B: Using a keyboard shortcut**
1. Press **Ctrl+`** (that is the backtick key — it is usually in the top-left of your keyboard, on the same key as the tilde ~, just below the Escape key).

A panel will appear at the bottom of the VS Code window. This is your terminal. You can type commands here just like you did in the Command Prompt earlier. In fact, it works the same way — but now it is conveniently inside your code editor.

You will use this terminal a lot throughout the course to run your Python scripts and other commands.

---

## Quick Reference

Here is a summary of the keyboard shortcuts you just learned:

| What It Does | Shortcut |
|-------------|----------|
| Open Extensions panel | Ctrl+Shift+X |
| Open / close the terminal | Ctrl+` |
| Open a folder | Ctrl+K, then Ctrl+O |
| Open Command Palette | Ctrl+Shift+P |
| Run a SQL query (Module 4) | Ctrl+Shift+E |
| Preview a Markdown file | Ctrl+Shift+V |

---

## What You Just Installed

VS Code is now set up with two extensions:

| Extension | What It Does | When You Use It |
|-----------|-------------|-----------------|
| **Python** | Write and run `.py` files | Modules 3, 5, 6, 7 |
| **SQL Server (mssql)** | Write and run `.sql` files | Module 4 |

You now have a proper code editor that handles both Python and SQL, and you know how to open folders and use the terminal. Time to put it to use.

Next up: [Running Your First Script](05_running_your_first_script.md)
