# I1 · Read and analyze a BIM file

Task: [`tasks/README.md`](../tasks/README.md), task I1. Sample model: "Einfamilienhaus" from the [Bundesingenieurkammer](https://bingk.de/projektbeispiele-bim/). Download it yourself and don't add it to this repository.

## Chat prompt

Attach the IFC file (or the ZIP file, if your chat accepts it) and paste:

```text
This is an IFC model of a single-family house. Please tell me:
1. Which storeys are there?
2. How many doors and how many windows are there?
3. Which other kinds of building elements are there, and how many of each?
4. Are there rooms (IfcSpace)? If yes, what is the total floor area?

Only use what is in the file. If something can't be determined from the file, say so instead of guessing.
```

If the file is too large for your chat, use the agent prompt instead.

## Agent prompt

```text
In this folder there is an IFC file (Einfamilienhaus.ifc). Build a small Python script, step by step, that analyzes it with IfcOpenShell (pip install ifcopenshell).

1. Open the file and print the IFC schema version.
2. List all storeys.
3. Count doors, windows and all other building elements by type.
4. Count the rooms (IfcSpace). If there are rooms, calculate the total floor area and explain where the area comes from.
5. Print the results as a short table.

Run the script after each step and show me the output. Don't guess: if the model doesn't contain something, say so.
```

## Agent prompt: compare harnesses

```text
Please solve task I1 from tasks/README.md as software (Way B).

0. First find out who you are: which tool are you running in (Claude Code, Codex or Qwen Code), and which model and version are you using? Use the short name claude-code, codex or qwen-code. Tell me briefly what you found before you continue.
1. Make sure you are on the latest main branch (git pull), then create a new branch i1-<shortname>.
2. Write a Python script results/<date>_<your-name>_task-I1/<shortname>.py. It uses only ifcopenshell and the standard library, takes the path to the IFC file as an argument and prints: storeys, doors, windows, all other building elements by type, and rooms (IfcSpace) with floor area if available. Short comments in English.
3. Run it on the IFC file and show me the output. If you don't know where the file is, ask me for the path.
4. Never copy or commit the IFC file into the repository.
5. Append one row to results/results.csv: date, who, task I1, your model, your version, harness = your short name, origin = where your model comes from, data_location = where your model's provider runs (the script runs locally, but your work on it ran at the provider), quality empty, and in notes whether the script ran on the first try and how many storeys, doors and windows it found.
6. One commit, push, and open a pull request titled "I1 · <shortname>".
```

Run the tools one after another, not at the same time, to avoid conflicts in results.csv. Compare the pull requests: did the script run on the first try, and do the counts match?

## What to note in results.csv

Task `I1`, the model and harness, `data_location`, whether the counts match the script output, and in `notes` anything the model made up or got wrong.
