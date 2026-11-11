# I1 · Read and analyze an IFC model

- **Date:** 2026-11-11
- **Who:** Narges
- **Model file:** "Einfamilienhaus" from the Bundesingenieurkammer, IFC2X3, exported from Autodesk Revit 2023 (83,183 entities)
- **Prompt:** chat prompt from `prompts/` for task I1, unchanged
- **Harness:** chat (all three)

## Summary

All three models agree on every count. Both say there are no rooms (`IfcSpace`), so the floor area can't be determined. They differ in the extra details: Claude and Qwen add useful observations, GPT sticks to the counts. None of them read the file "by eye": they ran Python in the provider's sandbox and answered from the script output. That is Way B inside a chat, but the data was processed on the provider's servers.

Not yet checked by an expert or a reference script.

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

## Open questions for Mr. Hanf

- Which counts are correct? (A reference script with IfcOpenShell would confirm them.)
- Are the storey elevation offsets that Claude found a real problem in practice?
- Which of the extra findings are useful for checking a model, and which are noise?
