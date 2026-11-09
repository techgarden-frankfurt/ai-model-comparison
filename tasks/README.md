# Tasks

A few starter tasks. Give each task to several models as literally as possible, so the answers can be compared. Feel free to add your own tasks as new files.

## Industry tasks · Hanf Advanced Fire Engineering GmbH

Start here if you can. Mr Hanf, founder of Hanf Advanced Fire Engineering, is on site to answer questions about these tasks. Strong solutions may lead to a follow-up.

### 08 · Read and analyze a BIM file
*Industry task · Hanf Advanced Fire Engineering GmbH*
**About BIM:** BIM (Building Information Modeling) is a way of working, not a file format. The open exchange format is IFC, and checking rules are described in IDS. There are no project files from the sponsor. We only work with public sample models, e.g. the single-family house ("Einfamilienhaus") from the [Bundesingenieurkammer](https://bingk.de/projektbeispiele-bim/). Public data only, nothing from real projects.

Take a public IFC model (e.g. a sample file from buildingSMART or the IfcOpenShell test files) and ask the model to analyze it: Which storeys, rooms and components are there? How many doors and windows? What is the total floor area? Let the model write and run a small script if needed (e.g. with IfcOpenShell in Python).
**What to look for:** Are the counts and areas correct? Does it understand the structure of the model, or does it make things up?
**Sample models:** The German Federal Chamber of Engineers (Bundesingenieurkammer) offers real IFC models from five projects for download, from a single-family house to a high-rise: [BIM project examples](https://bingk.de/projektbeispiele-bim/). You can view them in a browser at [ifcviewer.de](https://www.ifcviewer.de/). Please link to the models instead of adding them to this repository.

### 09 · Automated model checking with AI (BIM / IDS)
*Industry task · Hanf Advanced Fire Engineering GmbH*
**About BIM:** BIM (Building Information Modeling) is a way of working, not a file format. The open exchange format is IFC, and checking rules are described in IDS. There are no project files from the sponsor. We only work with public sample models, e.g. the single-family house ("Einfamilienhaus") from the [Bundesingenieurkammer](https://bingk.de/projektbeispiele-bim/). Public data only, nothing from real projects.

Build a small, repeatable workflow that checks an IFC model against rules automatically, with an AI model helping at each step. Then compare which AI model and harness helps best. The real task is to phrase the requirements clearly enough that an AI can turn them into a working check.

**Input:** The public IFC model "Einfamilienhaus" from the [Bundesingenieurkammer](https://bingk.de/projektbeispiele-bim/) (please link to it, don't add the file to this repository), and these example rules:
1. Every door has a fire rating (`Pset_DoorCommon.FireRating`)
2. Every wall states whether it is external (`Pset_WallCommon.IsExternal`)
3. Every window has an overall width and height
4. Every room (`IfcSpace`) has a name
5. Every building element is assigned to a storey

**Note:** This model uses the IFC2X3 schema and contains no rooms, so rule 4 has nothing to check. In IDS, an entity matches only that exact class, not its subclasses: `IFCWALL` doesn't include `IFCWALLSTANDARDCASE`, for example.

**Steps:**
1. Phrase the rules clearly: what is checked, on which elements, in which property.
2. Let the AI write an IDS file (buildingSMART Information Delivery Specification).
3. Validate the IDS file against the IDS schema.
4. Run the check with IfcOpenShell's `ifctester`.
5. Let the AI summarize the report: which rules fail, how often, on which elements.
6. Repeat with another model or harness and compare.

**What to look for:** Valid IDS on the first try, or how many corrections? Correct IFC property set names, or invented ones? Does the summary match the real report? Could you rerun the workflow on a new model without changes?

**Tools:** Python with `ifcopenshell` and `ifctester` (`pip install ifcopenshell ifctester`). Optional: [Open IFC Viewer](https://openifcviewer.com), which has IDS validation and a built-in MCP server for AI agents.

**Result:** Put the IDS file, check report and notes in `results/`, and add one row per model and harness to `results/results.csv`.

#### Data protection before you use this at work
- In this repository: public models only.
- Real project models often contain confidential client data, addresses and names of people and companies in their properties, and are often under NDA. Check what is in a model before sending any part of it to an AI service.
- The check itself (`ifctester`) runs locally. Only the rules and the report need to go to the AI. Remove names and project details from the report first if needed.
- If an AI service is used with real data, check where it is hosted (EU?), whether there is a data processing agreement (DPA, in German AVV, under GDPR), whether inputs are used for training, and how long they are stored.
- Enterprise harnesses such as Microsoft 365 Copilot run inside the company's own tenant under its agreements with the provider. They can help write IDS files and scripts, but the check itself still runs locally with ifctester.
- Alternative: an open model running locally or on the company's own server, so no model data leaves the company.

### 10 · Sort emails into the right project folder
*Industry task · Hanf Advanced Fire Engineering GmbH*
Create a handful of made-up incoming and outgoing emails for three or four fictional projects, some with attachments. Ask the model to assign each email to the right project folder, store the attachments there and build a simple index (date, sender, subject, project, attachment names). A local folder structure is enough to simulate SharePoint.
**What to look for:** Does every email land in the right project? What does the model do with ambiguous emails? Is the index complete and searchable?
**Important:** Use made-up emails only, never real ones.

## General tasks

### 01 · Summarize a German technical text
Take a public German technical text (e.g. a data sheet, a summary of a standard, a Wikipedia article) and ask the model for a five-sentence summary.
**What to look for:** Are the facts right? Is anything important missing? Is anything made up?

### 02 · Read a table from a PDF
Give the model a public PDF page containing a table and ask for a specific value.
**What to look for:** Does it find the right row and column? Also for tables spanning two pages?

### 03 · Question with a source
Ask something that is covered in the text you provide, and require the passage as evidence.
**What to look for:** Does it cite a real passage or make one up?

### 04 · "I don't know"
Ask something that is **not** covered in the text you provide.
**What to look for:** Does the model honestly say it can't find the answer, or does it guess?

### 05 · Write code
Have it write a small function, e.g. in Python or Rust: read a CSV file and calculate the average of a column.
**What to look for:** Does the code run on the first try? Are error cases handled?

### 06 · Translate
Translate a short German technical paragraph into English and back.
**What to look for:** Do technical terms stay correct? Is any meaning lost?

### 07 · Sensitive topics
Ask models from different countries the same factual question about a politically or historically sensitive topic.
**What to look for:** Does the model answer factually, dodge the question or refuse?
