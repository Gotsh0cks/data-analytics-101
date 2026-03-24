# Common Errors and How to Fix Them

Getting error messages is a completely normal part of working with computers. Every programmer — even those with decades of experience — runs into errors regularly. An error does not mean you did something stupid. It means the computer needs you to fix something specific before it can continue.

This page covers the most common errors you will encounter in Module 0 and how to solve them.

---

## "python is not recognized as an internal or external command"

**When does this happen?** When you type `python --version` or `python hello.py` in the Command Prompt or terminal.

**What it means:** Your computer does not know where to find Python. This is a **PATH issue**. Remember the "Add python.exe to PATH" checkbox during installation? If that was not checked, Python is installed on your computer, but the system does not know where to look for it.

**How to fix it:**

### Option A: Reinstall Python (easiest)

1. Go to **[https://www.python.org/downloads/](https://www.python.org/downloads/)** and download Python again.
2. Run the installer. This time, make absolutely sure you check **"Add python.exe to PATH"** at the bottom of the first screen.
3. Click **"Install Now"**.
4. Close any open Command Prompt or terminal windows (the fix will not apply to windows that were already open).
5. Open a new Command Prompt and try `python --version` again.

### Option B: Add Python to PATH manually

1. Press the **Windows key** and type **"environment variables"**.
2. Click **"Edit the system environment variables"**.
3. In the window that appears, click the **"Environment Variables..."** button at the bottom.
4. In the top section ("User variables"), find the variable called **Path** and double-click it.
5. Click **"New"** and add the path where Python was installed. This is usually:
   - `C:\Users\YourUsername\AppData\Local\Programs\Python\Python312\`
   - `C:\Users\YourUsername\AppData\Local\Programs\Python\Python312\Scripts\`
   (Replace "YourUsername" with your actual Windows username, and "Python312" with your actual Python version folder.)
6. Click **OK** on all the windows to save.
7. Close any open Command Prompt or terminal windows and open a new one.
8. Try `python --version` again.

### Option C: Try `py` instead of `python`

On some Windows installations, Python registers itself as `py` instead of `python`. Try typing:

```
py --version
```

If that works, use `py` wherever this course says `python`. For example: `py hello.py` instead of `python hello.py`.

---

## "pip is not recognized as an internal or external command"

**When does this happen?** When you try to install packages with `pip install pandas`.

**What it means:** Same idea as the Python error above — the system cannot find pip.

**How to fix it:**

### Option A: Use `python -m pip` instead

Instead of typing `pip install pandas`, type:

```
python -m pip install pandas
```

This tells Python to run pip directly, bypassing the PATH issue. You can use this pattern any time `pip` is not recognized:

```
python -m pip install pandas matplotlib seaborn openpyxl
```

### Option B: Fix the PATH

Follow the same PATH fix described in the Python section above. The `Scripts` folder (which contains pip) needs to be in your PATH. If you reinstall Python with the "Add to PATH" checkbox checked, pip should work automatically.

---

## "Permission denied" or "Access is denied"

**When does this happen?** When installing Python, running pip, or installing SQL Server.

**What it means:** Windows is blocking the action because it requires administrator privileges.

**How to fix it:**

1. Close the Command Prompt or terminal.
2. Press the **Windows key** and type **cmd**.
3. **Right-click** on "Command Prompt" in the search results.
4. Click **"Run as administrator"**.
5. If Windows asks "Do you want to allow this app to make changes to your device?", click **Yes**.
6. Try your command again in this new window.

For pip specifically, you can also try adding `--user` to the end of the command:

```
pip install pandas --user
```

This installs the package just for your user account, which does not require administrator access.

---

## "No module named pandas" (or matplotlib, seaborn, etc.)

**When does this happen?** When you try to use pandas (or another package) in a Python script and get an error like:

```
ModuleNotFoundError: No module named 'pandas'
```

**What it means:** The package is not installed yet. Python does not come with data analytics packages built in — you need to install them separately.

**How to fix it:**

Open a Command Prompt or terminal and run:

```
pip install pandas
```

Replace `pandas` with whichever package is missing. Or install all the ones you need at once:

```
pip install pandas matplotlib seaborn openpyxl
```

If pip is not recognized, use:

```
python -m pip install pandas matplotlib seaborn openpyxl
```

---

## "Cannot connect to SQL Server" or Connection Errors in VS Code

**When does this happen?** When you try to connect to your local SQL Server from VS Code (using the mssql extension) and it fails.

**What it means:** Usually, the SQL Server service is not running on your computer.

**How to fix it:**

### Step 1: Check if SQL Server is running

1. Press the **Windows key** and type **Services**.
2. Click on **"Services"** (the one with the gear icon).
3. A long list of services will appear. Scroll down to find **"SQL Server (SQLEXPRESS)"**.
4. Look at the **Status** column:
   - If it says **"Running"**, the service is fine and the problem is something else (see Step 2).
   - If it is **blank** or says **"Stopped"**, right-click on it and click **"Start"**.
5. Try connecting again in VS Code (Ctrl+Shift+P > "MS SQL: Connect").

### Step 2: Double-check your connection settings

Make sure your connection in VS Code is set to:

| Field | Value |
|-------|-------|
| Server | `localhost\SQLEXPRESS` |
| Authentication type | Windows Authentication |

Common mistakes:
- Typing just `localhost` without `\SQLEXPRESS`.
- Typing `SQLEXPRESS` without `localhost\` before it.
- Choosing "SQL Login" instead of "Windows Authentication" (you did not set up a SQL login, so this will not work).

### Step 3: Enable TCP/IP (if the above did not help)

1. Press the **Windows key** and type **"SQL Server Configuration Manager"**. If you cannot find it, look in your Start Menu under "Microsoft SQL Server 2022" folder.
2. In the left panel, expand **"SQL Server Network Configuration"**.
3. Click on **"Protocols for SQLEXPRESS"**.
4. In the right panel, check if **TCP/IP** is **Disabled**. If it is, right-click on it and click **Enable**.
5. You will need to restart the SQL Server service. Go back to Services (Windows key > type "Services") and right-click **"SQL Server (SQLEXPRESS)"** > click **Restart**.
6. Try connecting again.

---

## General Troubleshooting Advice

When you encounter an error that is not listed here, follow these steps:

### 1. Read the error message carefully

Error messages are written by programmers to help you figure out what went wrong. They may look intimidating at first, but they usually contain the answer — or at least a strong hint. Look for the last line of the error, which is usually the most specific and helpful.

### 2. Copy the exact error message and search for it

Select the error text, copy it (Ctrl+C), open your web browser, and paste it into Google. Add "Windows" to your search if the results are not relevant. For example:

```
"pip is not recognized as an internal or external command" Windows
```

Thousands of other people have had the same error before you. Sites like Stack Overflow will often have step-by-step solutions.

### 3. Do not panic

An error message is not a failure — it is information. It is the computer telling you exactly what it needs. Think of it as a conversation: the computer said "I cannot do this because of X." Your job is to fix X.

### 4. Close and reopen

Sometimes, especially after installing something new or changing settings, you need to close your Command Prompt, terminal, or VS Code and reopen it for the changes to take effect. This is one of the most common reasons a fix "does not work" — you just need a fresh window.

### 5. Restart your computer

If all else fails, restart. It sounds like a cliche, but many installation steps only fully take effect after a restart. It takes two minutes and solves more problems than you would expect.

---

## You Are Ready

If you have made it through Module 0 and everything is installed and working, give yourself some credit. Setting up a development environment is honestly one of the most frustrating parts of learning to code, and you just finished it. The fun part — actually working with data — starts now.
