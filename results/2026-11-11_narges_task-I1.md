# I1 · Read and analyze an IFC model

- **Date:** 2026-11-11
- **Who:** Narges
- **Model file:** "Einfamilienhaus" from the Bundesingenieurkammer, IFC2X3, exported from Autodesk Revit 2023 (83,183 entities)
- **Prompt:** chat prompt from `prompts/` for task I1, unchanged
- **Harness:** chat (all three)

## Summary

All three models agree on every count. All three say there are no rooms (`IfcSpace`), so the floor area can't be determined. They differ in the extra details: Claude and Qwen add useful observations, GPT sticks to the counts. None of them read the file "by eye": they ran Python in the provider's sandbox and answered from the script output. That is Way B inside a chat, but the data was processed on the provider's servers.

Not yet checked by an expert. Two reference scripts with IfcOpenShell (see "How to run the scripts") confirm the main counts: 10 storeys, 49 doors, 57 windows, 537 other building elements, no `IfcSpace`.

## How to run the scripts

The scripts in `results/2026-11-11_narges_task-I1/` need no AI. They run on any IFC file.

1. Python 3 and IfcOpenShell: `pip install ifcopenshell`
   (If you see "No module named ifcopenshell", this step is missing.)
2. Download the "Einfamilienhaus" from the [Bundesingenieurkammer](https://bingk.de/projektbeispiele-bim/) and unzip it. Do not add the model to the repo.
3. Run one of the scripts with the path to the .ifc file:
   - `python results/2026-11-11_narges_task-I1/claude-code.py path/to/Einfamilienhaus.ifc`
   - `python results/2026-11-11_narges_task-I1/codex.py path/to/Einfamilienhaus.ifc`

Both should report 10 storeys, 49 doors and 57 windows.

## Comparison

| | Qwen Max 4 Preview | Claude Opus 5.5 | GPT-6.1 Sol |
|---|---|---|---|
| Storeys (`IfcBuildingStorey`) | 10 | 10 | 10 |
| Doors | 49 | 49 | 49 |
| Windows | 57 | 57 | 57 |
| Walls (`IfcWallStandardCase` + `IfcWall`) | 173 + 19 = 192 | 173 + 19 | 173 + 19 = 192 |
| Slabs | 26 (13 floor, 11 roof, 2 base slab) | 26 (11 part of roofs, 15 standalone) | 26 |
| Members / beams / columns | 187 / 49 / 8 | 187 / 49 / 8 | 187 / 49 / 8 |
| Stairs | 28 entities = 20 distinct | 28 entities, 20 top-level | 28 (assemblies and parts listed separately) |
| Stair flights / railings | 12 / 12 | 12 / 12 (8 railings part of stairs) | 12 / 12 |
| Roofs | 14 | 14 | 14 |
| Openings (`IfcOpeningElement`) | 124 | 124 | 124 |
| Proxies / furnishing | 9 / 2 | 9 / 2 | 9 / 2 |
| Rooms (`IfcSpace`) | 0, area not determinable | 0, area not determinable | 0, area not determinable ("should not be reported as zero") |
| How it read the file | Python in a sandbox | Python, read directly | Python, "evaluated locally" (in the provider's sandbox) |
| Extra findings | Slab types; member types (129 timber beams 60×100); Revit export artefact with doubled stairs; roofs and roof slabs overlap | Stored elevations don't match the names (offset of about +0.38 m); 3 windows without an opening on the foundation level; how to re-export with rooms | Few: read the file from inside the ZIP; counts exclude type definitions; no detail on stairs, slabs or elevations |
| Made-up or unclear? | Nothing obvious | Nothing obvious | Nothing obvious |
| data_location | CN | US | US |

## Qwen Max 4 Preview · chat (free plan)

- **Note:** `.ifc` was not accepted for upload. [Note how you uploaded it, e.g. renamed to `.txt`.]

The file is a full IFC2X3 STEP file, exported from Autodesk Revit 2023, 83,183 entities. Everything is counted directly from the file.

**Storeys:** 10 × `IfcBuildingStorey`, in order of stored elevation: 00_Fundamente −3.50, 00_Kellergeschoss −2.70, 01_Erdgeschoss +0.0, window sill lvl, 02_Obergeschoss +3.19, 03_Dachgeschoss +6.0, 00-DD2, 00-DD1, 04_Spitzboden +9.3, 05_Dachfirst +12.19. "window sill lvl", "00-DD1" and "00-DD2" contain only a few timber members or roof containers and look like auxiliary levels.

**Doors:** 49 (all with unique tags). **Windows:** 57 (including "roof_win .6x.9" roof windows).

**Other elements:** `IfcWallStandardCase` 173, `IfcWall` 19 (192 walls); `IfcSlab` 26 (13 floor, 11 roof, 2 base slab); `IfcRoof` 14 (containers; the 11 roof slabs are aggregated into them, 3 roofs have no children, so don't add roofs and roof slabs); `IfcMember` 187 (mostly timber "Holz Träger 60x100", 129×); `IfcBeam` 49; `IfcColumn` 8 (6 timber, 2 concrete 475×610 mm); `IfcStair` 28 entities = 20 distinct stairs (8 exported twice as container plus geometry child, a Revit export artefact); `IfcStairFlight` 12; `IfcRailing` 12; `IfcOpeningElement` 124 (voids, not physical); `IfcBuildingElementProxy` 9 (7 "Mass" objects, 2 RPC shrubs); `IfcFurnishingElement` 2. No footings, plates, coverings, curtain walls or ramps.

**Rooms:** 0 `IfcSpace`, no space boundaries, no base quantities, no floor area properties. The total floor area can't be determined. The only area values are roof areas in `Pset_RoofCommon`.

## Claude Opus 5.5 · chat

IFC2X3 export from Autodesk Revit 2023, no rooms, so question 4 can't be answered.

**Storeys:** 10 `IfcBuildingStorey` with stored elevations: 00_Fundamente −2.611, 00_Kellergeschoss −2.319, 01_Erdgeschoss +0.381, window sill lvl +1.971, 02_Obergeschoss +3.571, 03_Dachgeschoss +6.451, 00-DD2 +7.250, 00-DD1 +8.446, 04_Spitzboden +8.851, 05_Dachfirst +11.151. The stored elevations don't match the names: most are offset by about +0.38 m, the foundation by about +0.89 m, the Spitzboden by about −0.45 m. "window sill lvl", "00-DD1" and "00-DD2" look like auxiliary levels but contain members.

**Doors:** 49, all fill openings in walls. **Windows:** 57, of which 54 fill openings; 3 have no opening and are assigned to "00_Fundamente", which looks like a modelling quirk.

**Other elements:** `IfcWallStandardCase` 173; `IfcWall` 19; `IfcMember` 187 (17 part of stairs); `IfcBeam` 49; `IfcSlab` 26 (11 part of roofs, 15 standalone); `IfcStair` 28 (8 nested, 20 top-level); `IfcStairFlight` 12; `IfcRoof` 14; `IfcRailing` 12 (8 part of stairs, 4 standalone); `IfcColumn` 8; `IfcBuildingElementProxy` 9 (7 "Mass", 2 "RPC Shrub"); `IfcFurnishingElement` 2; `IfcOpeningElement` 124. No coverings, plates, curtain walls, ramps or MEP elements.

**Rooms:** no `IfcSpace`, no `IfcQuantityArea`. Floor area can't be determined. To get room areas, re-export from Revit with rooms enabled.

## GPT-6.1 Sol · chat

Read `Einfamilienhaus.ifc` directly from inside the ZIP.

**Storeys:** 10 `IfcBuildingStorey`: 00_Fundamente -3.50, 00_Kellergeschoss -2.70, 01_Erdgeschoss +0.0, window sill lvl, 02_Obergeschoss +3.19, 03_Dachgeschoss +6.0, 00-DD2, 00-DD1, 04_Spitzboden +9.3, 05_Dachfirst +12.19. All recorded as storeys, including foundations, window sill level and roof ridge.

**Doors:** 49. **Windows:** 57.

**Other elements:** `IfcWallStandardCase` 173, `IfcWall` 19 (192 walls); `IfcMember` 187; `IfcBeam` 49; `IfcStair` 28; `IfcSlab` 26; `IfcRoof` 14; `IfcRailing` 12; `IfcStairFlight` 12; `IfcBuildingElementProxy` 9; `IfcColumn` 8; `IfcFurnishingElement` 2; `IfcOpeningElement` 124. Counts are element instances without type definitions; assemblies and their parts are listed separately.

**Rooms:** no `IfcSpace`. The total floor area can't be determined from `IfcSpace` data and should not be reported as zero.

Follow-up question about cost, GPT's answer in short: it can't see token counts or costs for a chat request. The IFC file was evaluated with Python, so the model context held the tool output, not the whole file. For a fair cost comparison, use the API's `usage` data and count all model and tool calls.

## Lesson learned: one folder per agent

I ran Claude Code, Codex and Qwen Code on the same repo at the same time, each on its own branch. A branch is not a folder: one folder can only have one branch checked out. When Codex switched the folder to `i1-codex`, the other agents saw that branch and Codex's uncommitted script. Claude Code noticed and created its own `git worktree`; otherwise one agent's files could have ended up in another agent's commit.

Rule for running agents in parallel: give each agent its own folder.

```bash
git worktree add ../ai-model-comparison-qwen -b i1-qwen-code main
cd ../ai-model-comparison-qwen
```

Remove it after merging with `git worktree remove ../ai-model-comparison-qwen`.

## Local run: Qwen Code with qwen3:8b on a laptop

- **Setup:** Qwen Code 0.27.2, model `qwen3:8b` via Ollama, laptop with AMD CPU, no NVIDIA GPU, 30 GB RAM. Nothing left the laptop (`data_location` local).
- **Load while running (`free -h`):** 25 GB of 30 GB RAM used, 4.2 GB available, 5.7 GB of 8 GB swap in use. The laptop became noticeably slow.
- **Context size matters:** Ollama started the model with a 4,096-token context, too small for Qwen Code's system prompt plus files (Ollama cuts silently from the front). Fix: a variant with `PARAMETER num_ctx 16384` (`ollama create qwen3-8b-16k`). Memory for the model went from 5.9 GB to 7.9 GB.
- **Duration:** about 50 minutes, then it stopped with an error. No result.
- **Did it act as an agent?** No. Six thinking rounds of 3.5 to 7 minutes each (qwen3's thinking mode on a CPU). One tool call, and it was malformed: the model wanted to search for `qwen-code.py` but left out the tool name, so Qwen Code refused it (`params must have required property 'name'`). In the end the harness gave up: `API Error: No stream activity for 240000ms`. The branch was never created, no script was written.
- **Counts match the chat results?** No counts produced.
- **Harness and runtime disagree:** Qwen Code's status bar showed a 262.1k context, while Ollama actually served 16k. The harness assumes the model's maximum; the runtime decides what is really available.
- **Not tried:** putting `/no_think` as the first line of the prompt would switch off qwen3's thinking mode and might make it faster. An idea for anyone who wants to try.

Takeaway: a local model is free and keeps the data on the machine, but on a normal laptop without a GPU it takes most of the memory and is slow. With a small 8B model, an agent harness like Qwen Code did not complete a single step in 50 minutes; the same task took the cloud agents minutes. For real use you need suitable hardware and a larger model.

Row for `results.csv` (adapt to the column order):

```
2026-11-11,Narges,I1,qwen3:8b,Qwen Code 0.27.2,8b,CN,local,open,free,1,,0,Ollama num_ctx 16384; laptop without GPU; 50 min, no step done; 1 malformed tool call; stream timeout after 240 s
```

## Open questions for Mr. Hanf

- Which counts are correct? (A reference script with IfcOpenShell would confirm them.)
- Are the storey elevation offsets that Claude found a real problem in practice?
- Which of the extra findings are useful for checking a model, and which are noise?
