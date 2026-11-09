# Prompts

Starter prompts: copy, run, then refine together on site.

There is one file per industry task from [`tasks/`](../tasks/README.md). Each file has:

- a **chat prompt** to get started in a browser chat, no coding tools needed
- an **agent prompt** for Claude Code, Qwen Code or a similar tool, which builds a small script step by step
- a line on **what to note in results.csv**

| Task | Prompts |
|---|---|
| 08 · Read and analyze a BIM file | [`08-bim-analysis.md`](08-bim-analysis.md) |
| 09 · Automated model checking with AI (BIM / IDS) | [`09-ids-model-checking.md`](09-ids-model-checking.md) |
| 10 · Sort emails into the right project folder | [`10-email-sorting.md`](10-email-sorting.md) |

Run agent prompts in a separate working folder, not inside this repository, and don't commit model files. Public data only.

These prompts are a starting point. If you find a better version, add it here with a pull request.
