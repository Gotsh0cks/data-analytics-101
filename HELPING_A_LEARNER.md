# Helping A Learner

This guide is for the person supporting a friend or family member through Data Analytics 101.

The goal is not to rescue them from every hard moment. The goal is to help them stay oriented, reduce setup panic, and build enough confidence to keep trying.

## First Response When They Are Stuck

Ask for four things:

1. What file or lesson are you on?
2. What folder is open in VS Code?
3. What command or step did you try?
4. What exact error message did you see?

If they can send a screenshot, ask for one screenshot that includes the command and the error.

## Troubleshooting Order

Check these in order before guessing:

1. Are they in the main `data-analytics-101` folder?
2. Did they extract the ZIP file?
3. Are they running the command from the VS Code terminal?
4. Does `python --version` or `py --version` work?
5. Does `python check_setup.py` run?
6. Does the file path in the lesson match where the file actually is?
7. Is the needed package installed?
8. Is this a later-module tool issue, such as SQL Server or Tableau?

Most beginner issues are in the first three items.

## Help Without Taking Over

Try to avoid grabbing the keyboard right away.

Better prompts:

- "Can you read me the command you typed?"
- "What folder does the terminal show?"
- "What does the error say after the word `FileNotFoundError`?"
- "Can you find that file in Windows Explorer?"
- "Which support step are you on: hint, expected output, or solution?"

Less helpful patterns:

- Silently fixing the file yourself.
- Rewriting their code before they understand the problem.
- Saying "this is easy."
- Explaining five future topics when they only need the next step.

## When To Use Hints, Outputs, And Solutions

For exercise modules, use this order:

1. Ask them to try the exercise first.
2. If they are stuck, point them to the hint for that exercise.
3. If they have an answer, point them to the expected output.
4. If they tried and compared, let them read the solution.

The solution is not cheating after they have tried. It is part of the learning loop.

## Common Confidence Dips

**"I broke it."**

Usually they did not. Ask what changed, then rerun the smallest check.

**"I am bad at this."**

Name the specific skill they are practicing: paths, commands, formulas, syntax, or reading errors. Most frustration comes from a tiny tool detail, not lack of ability.

**"My output looks different."**

Check whether the value matches, not whether formatting is identical.

**"I do not know what to do next."**

Point them back to `progress_tracker.md` or the module `README.md`.

## Good First-Hour Support

In the first sitting, success can be small:

- They found the course folder.
- They opened `START_HERE.md`.
- They opened `progress_tracker.md`.
- They started Module 0.
- They know where `GET_HELP.md` is.

Do not rush them into SQL, Tableau, or the capstone.

## When To Step In Directly

It is reasonable to take over briefly when:

- an installer is broken or confusing
- Windows PATH needs to be fixed
- SQL Server services are not running
- a file is genuinely missing
- the learner is too frustrated to keep reading

When you do step in, narrate what you are checking:

"I am checking the folder first because most file errors come from running the command in the wrong place."

That turns the fix into a lesson instead of magic.
