# AGENTS.md

Guidance for Codex and other AI coding agents working in this repository.

## Repository Purpose

`data-analytics-101` is a private, self-paced beginner course for friends and family who are learning data analytics from scratch. The course should feel calm, practical, and encouraging. It teaches the path from basic analytics concepts through Excel, Python/pandas, SQL Server, visualization, real-world datasets, and a capstone project.

The primary measure of success is not technical sophistication. It is whether a non-technical learner can open the repo, follow the path, recover from mistakes, and finish with a small portfolio project they understand.

## Audience

- Complete beginners, often with no programming or command-line experience.
- Windows users by default.
- Learners working independently, without a live instructor beside them.
- Friends and family, so tone should be warm, direct, and confidence-building.

## Agent Workflow

Before making changes:

1. Run `git status --short` and preserve user changes.
2. Read the relevant module README and nearby lesson files before editing.
3. Check `docs/ai/repo_overview.md`, `docs/ai/course_quality_checklist.md`, and `docs/ai/improvement_backlog.md` for context.
4. Keep changes small and easy to review.

For creative course changes, feature additions, or broad refactors, use the Superpowers brainstorming/planning workflow when it is available in the Codex environment. Do not jump straight into large edits without a design or user approval.

## Editing Principles

- Preserve the beginner-friendly voice. Prefer plain English over technical shorthand.
- Explain jargon the first time it appears in a lesson.
- Favor concrete examples over abstract descriptions.
- Keep the numbered course path stable: Module 0 through Module 7.
- Avoid unrelated refactors while changing course content.
- Do not remove learning scaffolding just because it feels repetitive to an expert.
- Do not add a course platform, website, notebook system, or automation framework unless the user asks for it.
- Prefer small Markdown and script improvements over large restructures.

## Code and Data Rules

- Python lesson scripts should work from the documented learner workflow.
- When practical, make file paths relative to the script location instead of the current terminal directory.
- Avoid hidden internet requirements in core lessons. If a script downloads data, document that clearly.
- Do not change sample datasets without updating affected lessons, expected outputs, and exercises.
- Do not commit generated cache files such as `__pycache__/`.
- Keep large binary assets out of the repo unless they are necessary learner materials.

## Course Quality Expectations

Each lesson should ideally include:

- A clear purpose.
- Beginner-friendly explanation.
- Runnable example or concrete action.
- Expected output or a way to check progress.
- Practice prompt or reflection question.
- Next step.

Exercises should ideally include hints and, when appropriate, separate solutions.

Capstone material should help learners finish. Rubrics, examples, templates, and "good enough" guidance are more valuable than open-ended perfection.

## Verification

Use the lightest verification that fits the change:

- For Markdown-only changes: check links and read rendered structure mentally.
- For Python lesson scripts: run `python -m compileall -q .` and run representative scripts when safe.
- For SQL lessons: inspect syntax and preserve SQL Server/T-SQL assumptions.
- For Tableau or Excel instructions: verify file names and learner workflow references.

If verification cannot be run locally, say so in the final summary.

## Important Files

- `README.md`: main learner entry point.
- `00-what-is-data-analytics/` through `07-capstone/`: course modules.
- `data/`: sample datasets used throughout the course.
- `cheatsheets/`: quick reference materials.
- `docs/ai/repo_overview.md`: persistent repo context for AI agents.
- `docs/ai/course_quality_checklist.md`: review checklist for polish work.
- `docs/ai/improvement_backlog.md`: prioritized future improvements.

