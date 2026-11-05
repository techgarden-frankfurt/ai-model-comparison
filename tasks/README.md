# Tasks

A few starter tasks. Give each task to several models as literally as possible, so the answers can be compared. Feel free to add your own tasks as new files.

## 01 · Summarize a German technical text
Take a public German technical text (e.g. a data sheet, a summary of a standard, a Wikipedia article) and ask the model for a five-sentence summary.
**What to look for:** Are the facts right? Is anything important missing? Is anything made up?

## 02 · Read a table from a PDF
Give the model a public PDF page containing a table and ask for a specific value.
**What to look for:** Does it find the right row and column? Also for tables spanning two pages?

## 03 · Question with a source
Ask something that is covered in the text you provide, and require the passage as evidence.
**What to look for:** Does it cite a real passage or make one up?

## 04 · "I don't know"
Ask something that is **not** covered in the text you provide.
**What to look for:** Does the model honestly say it can't find the answer, or does it guess?

## 05 · Write code
Have it write a small function, e.g. in Python or Rust: read a CSV file and calculate the average of a column.
**What to look for:** Does the code run on the first try? Are error cases handled?

## 06 · Translate
Translate a short German technical paragraph into English and back.
**What to look for:** Do technical terms stay correct? Is any meaning lost?

## 07 · Sensitive topics
Ask models from different countries the same factual question about a politically or historically sensitive topic.
**What to look for:** Does the model answer factually, dodge the question or refuse?

## 08 · Read and analyze a BIM file
Take a public IFC model (e.g. a sample file from buildingSMART or the IfcOpenShell test files) and ask the model to analyze it: Which storeys, rooms and components are there? How many doors and windows? What is the total floor area? Let the model write and run a small script if needed (e.g. with IfcOpenShell in Python).
**What to look for:** Are the counts and areas correct? Does it understand the structure of the model, or does it make things up?
**Sample models:** The German Federal Chamber of Engineers (Bundesingenieurkammer) offers real IFC models from five projects for download, from a single-family house to a high-rise: [BIM project examples](https://bingk.de/projektbeispiele-bim/). You can view them in a browser at [ifcviewer.de](https://www.ifcviewer.de/). Please link to the models instead of adding them to this repository.

## 09 · Sort emails into the right project folder
Create a handful of made-up incoming and outgoing emails for three or four fictional projects, some with attachments. Ask the model to assign each email to the right project folder, store the attachments there and build a simple index (date, sender, subject, project, attachment names). A local folder structure is enough to simulate SharePoint.
**What to look for:** Does every email land in the right project? What does the model do with ambiguous emails? Is the index complete and searchable?
**Important:** Use made-up emails only, never real ones.
