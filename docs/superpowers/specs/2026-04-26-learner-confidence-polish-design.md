# Learner Confidence Polish Design

## Purpose

This polish pass is for internet-savvy friends and family who are comfortable with normal Windows PC basics but new to analytics, coding tools, SQL, and Tableau. The goal is not commercial polish. The goal is to make the first hour less intimidating, make errors easier to report or fix, and help learners know when they are ready to move on.

## Audience

Learners can use Windows Explorer, download files, unzip folders, and follow written instructions. They may not know what a terminal, package, script, working directory, SQL Server instance, or DataFrame is before this course.

## Approach

Add a small set of learner-facing docs and checklists that sit on top of the existing course:

- A first-session guide for the first 30 minutes.
- A richer rescue guide for common setup and path problems.
- End-of-module readiness checks and reflection prompts.
- A private helper guide for the course owner.
- A lightweight file/link validator for maintenance.

The course should keep its current simple folder structure. New files should be plain Markdown or small Python scripts using the standard library unless an existing dependency is already required.

## Scope

### In Scope

- Create `FIRST_30_MINUTES.md`.
- Expand `GET_HELP.md` with common beginner error patterns and fixes.
- Add `HELPING_A_LEARNER.md` for the course owner.
- Add module readiness checks and reflection prompts to module `README.md` files.
- Add a lightweight `check_course_files.py` validator for required learner-facing files and Markdown links.
- Update `START_HERE.md`, `progress_tracker.md`, `docs/ai/improvement_backlog.md`, and `docs/ai/course_quality_checklist.md` to reflect the new support layer.
- Fix obvious path-reference inconsistencies encountered in files touched by this pass.

### Out Of Scope

- Screenshots, videos, or GIFs.
- Website or LMS packaging.
- Public-branding polish.
- Large rewrites of lesson content.
- New analytics lessons or new datasets.
- Full external link checking.

## Learner Experience

The learner starts with `START_HERE.md`, which points to `FIRST_30_MINUTES.md`. The first-session guide helps them open the course, run the setup check when ready, and stop with a clear sense of progress. When something breaks, `GET_HELP.md` gives specific fixes before the learner asks for help.

Each module ends with a short readiness check and reflection prompt. This gives the learner permission to move on without mastering every detail and helps them name what they just learned.

## Owner Experience

`HELPING_A_LEARNER.md` gives the course owner a short playbook for helping without taking over. It emphasizes asking for the exact file, command, and error; checking folder location first; and pointing learners to hints and expected outputs in the right order.

## Maintenance

`check_course_files.py` should verify that key files exist and that local Markdown links in learner-facing docs resolve. It should avoid internet access and should not require SQL Server, Tableau, Excel, or third-party packages. It should be safe to run from the repo root.

## Success Criteria

- A learner can identify what to do in their first 30 minutes.
- A learner can self-diagnose the most common setup/path/package problems.
- Every module has a short readiness check and reflection prompt.
- The course owner has a lightweight helper guide.
- A maintainer can run one validator to catch missing key files or broken local Markdown links.
- Existing setup tests and solution scripts still pass.
