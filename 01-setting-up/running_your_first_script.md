# Running Your First Script

## What Is a "Script"?

A script is a **text file with instructions for the computer**. That is all it is. When you "run" a script, you are telling the computer: "Read this file and do what it says."

A Python script is a text file that ends with `.py` (that is its **file extension** — the letters after the dot in a file name that tell the computer what kind of file it is, like how `.docx` means a Word document and `.jpg` means a photo).

We have already created a tiny script for you called `hello.py`. Let's run it together.

---

## Step 1: Open VS Code

If VS Code is not already open, press the **Windows key**, type **Visual Studio Code**, and press Enter.

---

## Step 2: Open the Course Folder

1. Click **File** in the top menu bar.
2. Click **Open Folder...**
3. Navigate to the **data-analytics-101** folder. This is where all the course files live.
4. Click **Select Folder**.
5. If VS Code asks whether you trust the authors, click **Yes, I trust the authors**.

You should see the folder structure in the left sidebar. If you click the little arrow next to **00-getting-started**, it will expand and show you the files inside, including `hello.py`.

---

## Step 3: Open the Terminal

The terminal is a way to talk to your computer by typing commands instead of clicking. Instead of double-clicking icons and using menus, you type a command and press Enter. It feels unfamiliar at first, but you will get used to it quickly.

Open the terminal inside VS Code:

1. Click **Terminal** in the top menu bar.
2. Click **New Terminal**.

A panel will appear at the bottom of the VS Code window. You will see some text and a blinking cursor. This is where you will type commands.

---

## Step 4: Navigate to the Right Folder

The terminal needs to know which folder you want to work in. Right now, it is probably in the `data-analytics-101` folder (you can see the current folder name in the terminal prompt — it is the text before the blinking cursor).

Type the following command and press Enter:

```
cd 00-getting-started
```

**What does `cd` mean?** It stands for "change directory." A directory is just another word for a folder. So `cd 00-getting-started` means "go into the folder called 00-getting-started."

You should see the terminal prompt change to show that you are now inside the `00-getting-started` folder.

---

## Step 5: Run the Script

Now for the exciting part. Type the following command and press Enter:

```
python hello.py
```

**What does this command mean?** You are telling the computer: "Use Python to read the file called hello.py and follow its instructions."

---

## Step 6: See the Result

You should see this appear in the terminal:

```
Hello, Data World!
```

---

## Congratulations! You just ran your first program!

That might seem simple, but take a moment to appreciate what just happened. You:

1. Opened a code editor
2. Used the terminal to navigate to a folder
3. Told Python to execute a script
4. And it worked!

Every complex program, every data analysis, every app on your phone — they all started just like this: someone wrote instructions in a file and told a computer to run them.

---

## What Just Happened, Step by Step

If you are curious about what went on behind the scenes:

1. You typed `python hello.py` and pressed Enter.
2. Your computer found the Python program you installed earlier (this is why the PATH setting was so important).
3. Python opened the file `hello.py` and read its contents.
4. The file contains one instruction: `print("Hello, Data World!")`
5. `print()` is a Python command that means "display this text on the screen."
6. Python followed that instruction and displayed the text in your terminal.

That is it. No magic — just a computer reading instructions from a file and following them, one step at a time.

---

## Bonus: Try Changing It

If you want to experiment, click on `hello.py` in the left sidebar of VS Code to open it. You will see:

```python
print("Hello, Data World!")
```

Try changing the text inside the quotes to something else, like:

```python
print("My name is Camille and I am learning data analytics!")
```

Save the file (Ctrl+S), then go back to the terminal and run `python hello.py` again. You should see your new message.

Changing code and re-running it to see what happens is how programmers learn. Do not be afraid to experiment.

---

## Next Steps

You have now confirmed that Python works on your computer and you know how to run a script. Next, we will install the database tools you will need later in the course.

Next up: [install_sql_server.md](install_sql_server.md)
