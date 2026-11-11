# I2 · Automated model checking with AI (BIM / IDS)

Task: [`tasks/README.md`](../tasks/README.md), task I2. Sample model: "Einfamilienhaus" from the [Bundesingenieurkammer](https://bingk.de/projektbeispiele-bim/). Download it yourself and don't add it to this repository.

## Chat prompt

```text
I want to check an IFC model (schema IFC2X3) automatically. Please write an IDS file (buildingSMART Information Delivery Specification) for these rules:
1. Every door has a fire rating (Pset_DoorCommon.FireRating)
2. Every wall states whether it is external (Pset_WallCommon.IsExternal)
3. Every window has an overall width and height
4. Every room (IfcSpace) has a name
5. Every building element is assigned to a storey

For each rule, explain which IFC classes, property sets and properties you used and why.
```

Then check the IDS file in a validator, for example [Open IFC Viewer](https://openifcviewer.com) or `ifctester`.

## Agent prompt

```text
In this folder there is an IFC file (Einfamilienhaus.ifc). I want a small, repeatable check of this model. Use Python with ifcopenshell and ifctester (pip install ifcopenshell ifctester).

1. Find out which IFC schema the model uses.
2. Write an IDS file rules.ids for these rules:
   1. Every door has a fire rating (Pset_DoorCommon.FireRating)
   2. Every wall states whether it is external (Pset_WallCommon.IsExternal)
   3. Every window has an overall width and height
   4. Every room (IfcSpace) has a name
   5. Every building element is assigned to a storey
3. Validate rules.ids against the IDS schema and fix it until it is valid.
4. Run the check with ifctester and save the report.
5. Summarize the report: which rules fail, how often, on which elements.
6. Write a script check.py that does steps 3 to 5 for any IFC file, so I can rerun it on a new model.

Show me the output after each step. Check how many elements each rule actually applies to, and tell me if a rule applies to no elements at all.
```

## What to note in results.csv

Task `I2`, the model and harness, `data_location`, whether the IDS was valid on the first try (or how many corrections it took), and in `notes` any invented property set names or differences between the summary and the real report.
