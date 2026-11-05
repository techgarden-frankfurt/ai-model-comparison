# Comparing AI Models · TechGarden Frankfurt

**Build. Code. Ship.**

What can current AI models really do? At the TechGarden meetups in Frankfurt we collect tests and results here: open and closed, European and non-European models, on real tasks.

## What this is about

There are plenty of claims about AI models. We try them ourselves and record what we see:

- **Quality:** Is the answer correct? Is it usable?
- **Speed:** How long does the answer take?
- **Cost:** What does a request cost?
- **Data:** Where does the model run, and where does the data go?

## The models

|  | Open (downloadable weights) | Closed (provider access only) |
|---|---|---|
| **European** | e.g. Mistral (open models) | e.g. Mistral (large models), Aleph Alpha |
| **Non-European** | e.g. Llama, Qwen, DeepSeek, GLM | e.g. GPT, Claude, Gemini |

This list is a starting point. Any model someone wants to test is welcome.

## How to contribute

1. Pick a task from [`tasks/`](tasks/) or bring your own.
2. Give the same task to two or more models.
3. Add your results to [`results/results.csv`](results/results.csv), one row per model and task.
4. Put longer answers, scripts or notes in their own file in `results/`, for example `results/2026-11-12_your-name_task-01.md`.
5. Open a pull request, and you're done.

You can try the models in a browser chat, through an API or locally, for example with [Ollama](https://ollama.com) or [LM Studio](https://lmstudio.ai).

## Ground rules

- **Public data only.** No confidential company data, no personal data.
- **No API keys or passwords** in the repository, not even in scripts.
- **Be precise:** Note the model name and version, date, access method (chat, API, local) and any important settings. Without these, results can't be compared.
- **Be honest:** Bad results and errors belong in the table too.
- Everyone is welcome, nobody has to be a pro.

## Folders

| Folder | Contents |
|---|---|
| `tasks/` | Test tasks to try out |
| `results/` | Results table and detailed results |
| `slides/` | Slides from the talks at the meetups |

## Meetups

TechGarden meetups take place every other Thursday from 6 to 9 pm in Frankfurt.

- **First meetup:** Thursday, 12 November 2026. Sign up: https://luma.com/ezi3o5tc
- Website: https://techgarden-frankfurt.de

## License

[MIT](LICENSE). Results and texts may be used freely, with a reference to this repository.
