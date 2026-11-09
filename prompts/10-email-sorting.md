# 10 · Sort emails into the right project folder

Task: [`tasks/README.md`](../tasks/README.md), task 10.

**Use made-up emails only, never real ones.** No real names, companies or projects.

## Chat prompt

```text
Make up 10 short emails for three fictional building projects, for example "Project A: school extension", "Project B: office building", "Project C: underground car park". Some are incoming, some outgoing, and some have attachments (just the file names). Make two of them ambiguous, so it's unclear which project they belong to. Use only made-up names and addresses.

Then assign each email to a project and build a table: date, sender, subject, project, attachment names. Explain your decision for the ambiguous emails.
```

## Agent prompt

```text
Build a small email sorting workflow in this folder, step by step. Use only made-up data.

1. Create a folder inbox/ with 10 made-up emails as .eml files for three fictional building projects. Some are incoming, some outgoing, some have small text attachments. Make two of them ambiguous.
2. Create one folder per project in projects/ (this simulates SharePoint).
3. Write a Python script sort_mail.py that reads the emails, decides which project each one belongs to, moves it into the project folder and saves its attachments there.
4. Put emails the script can't assign with confidence into projects/_unclear/, with a short reason.
5. Build an index index.csv: date, sender, subject, project, attachment names.

Run the script and show me the folder structure and the index.
```

## What to note in results.csv

Task `10`, the model and harness, how many emails landed in the right project, and in `notes` how the model handled the ambiguous emails.
