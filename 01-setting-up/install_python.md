# Installing Python

## What Is Python?

Python is a programming language — a way to give instructions to your computer by typing them out. Think of it like learning a new language, except instead of talking to a person, you are talking to your machine. You type instructions, and the computer follows them.

Python is one of the most popular languages for data analytics because it is relatively easy to read (it looks a lot like plain English) and it has a huge collection of free tools built by other people that make working with data much easier.

---

## Step 1: Download Python

1. Open your web browser (Edge, Chrome, Firefox — whichever you use).
2. Go to **[https://www.python.org/downloads/](https://www.python.org/downloads/)**
3. You will see a big yellow button that says something like **"Download Python 3.x.x"** (the numbers will vary — that is fine, just make sure it starts with 3). Click that button.
4. A file will download. It will be called something like `python-3.x.x-amd64.exe`. Wait for the download to finish.

---

## Step 2: Run the Installer

1. Open the downloaded file. You can usually find it in your **Downloads** folder, or click the download notification at the bottom of your browser.
2. An installer window will appear.

### THIS IS THE MOST IMPORTANT STEP:

At the bottom of the installer window, you will see a checkbox that says:

> **"Add python.exe to PATH"**

**CHECK THIS BOX.** Put a checkmark in it before you do anything else.

#### What does "Add to PATH" mean?

Your computer has a list of places it looks when you type a command. This list is called the PATH. If Python is not on that list, your computer will not know where to find it when you type `python`, and you will get an error. Checking this box puts Python on that list automatically. If you skip this step, things will break later and it is annoying to fix.

3. Now click **"Install Now"** (the top option). You do not need to customize anything.
4. Wait for the installation to finish. You will see a progress bar. This usually takes a minute or two.
5. When it says "Setup was successful", click **Close**.

---

## Step 3: Verify Python Is Installed

Let's make sure everything worked.

1. Press the **Windows key** on your keyboard (the key with the Windows logo, usually near the bottom-left).
2. Type **cmd** and press Enter. This opens a program called **Command Prompt** — it is a window where you can type commands to your computer. It will look like a black or dark window with white text.
3. In the Command Prompt, type the following and then press Enter:

```
python --version
```

4. You should see something like:

```
Python 3.12.4
```

The exact numbers may differ, and that is perfectly fine. What matters is that you see a version number starting with 3.

**If you see an error instead**, like "python is not recognized", check the [common_errors.md](common_errors.md) troubleshooting guide.

---

## Step 4: Install Data Analytics Packages

Python by itself is a general-purpose language. To make it great for data analytics, we need to install some additional tools called **packages**. A package is a collection of code that someone else wrote and shared for free, so you do not have to build everything from scratch.

We will install these packages using a tool called **pip**. Think of pip as an **app store for Python tools** — you tell it what you want, and it downloads and installs it for you. Pip was installed automatically when you installed Python.

In your Command Prompt (the same window from Step 3), type the following command and press Enter:

```
pip install pandas matplotlib seaborn openpyxl
```

Wait for it to finish. You will see a lot of text scrolling by — that is normal. It is downloading and setting up each package. This may take a few minutes depending on your internet speed.

Here is what each package does:

| Package | What It Does |
|---------|-------------|
| **pandas** | The main tool for working with data in Python. Think of it as a super-powered spreadsheet inside your code. |
| **matplotlib** | Creates charts and graphs from your data. |
| **seaborn** | Makes those charts look nicer with less effort. Built on top of matplotlib. |
| **openpyxl** | Lets Python read and write Excel files (.xlsx). |

### Alternative: Install from a requirements file

As you work through this course, you may see a file called `requirements.txt` in some folders. This is a file that lists all the packages needed for that section. Instead of typing each package name, you can install everything at once with:

```
pip install -r requirements.txt
```

This tells pip: "read the file called requirements.txt and install everything listed in it." You will see this approach used frequently in real-world projects.

---

## Step 5: Verify the Packages Installed Correctly

Still in the Command Prompt, type:

```
python -c "import pandas; print(pandas.__version__)"
```

If you see a version number (like `2.2.1`), everything is working. If you see an error that says "No module named pandas", check the [common_errors.md](common_errors.md) troubleshooting guide.

---

## You Are Done With This Step!

Python is installed, and you have got the key data analytics packages ready to go. Next, we will install the app where you will actually write your code.

Next up: [install_vscode.md](install_vscode.md)
