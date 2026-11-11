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

## What to note in results.csv

Task `I1`, the model and harness, `data_location`, whether the counts match the script output, and in `notes` anything the model made up or got wrong.
