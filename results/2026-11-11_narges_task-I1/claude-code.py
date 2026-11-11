"""Task I1: analyze an IFC model with IfcOpenShell.

Usage: python claude-code.py path/to/model.ifc

Prints storeys, doors, windows, all other building elements by type,
and rooms (IfcSpace) with their floor area if the file contains one.
Only reports what is in the file; nothing is estimated from geometry.
"""

import sys
from collections import Counter

import ifcopenshell
import ifcopenshell.util.element
import ifcopenshell.util.unit

# Area names to look for on IfcSpace, in order of preference.
# Base quantities first, then common property names.
AREA_KEYS = ["NetFloorArea", "GrossFloorArea", "Area", "NetArea", "GrossArea"]


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python claude-code.py path/to/model.ifc")

    model = ifcopenshell.open(sys.argv[1])
    print(f"File:   {sys.argv[1]}")
    print(f"Schema: {model.schema}")

    # Scale factor from project length unit to metres
    length_scale = ifcopenshell.util.unit.calculate_unit_scale(model)

    # 1. Storeys, sorted by stored elevation
    storeys = sorted(
        model.by_type("IfcBuildingStorey"),
        key=lambda s: s.Elevation if s.Elevation is not None else 0.0,
    )
    print(f"\nStoreys: {len(storeys)}")
    for s in storeys:
        if s.Elevation is None:
            elev = "no elevation"
        else:
            elev = f"{s.Elevation * length_scale:+.3f} m"
        print(f"  {s.Name or '(no name)':<30} {elev}")

    # 2. Doors and windows, also split by storey
    doors = model.by_type("IfcDoor")
    windows = model.by_type("IfcWindow")
    print(f"\nDoors:   {len(doors)}")
    print(f"Windows: {len(windows)}")
    print_per_storey("Doors per storey", doors)
    print_per_storey("Windows per storey", windows)

    # 3. All other building elements by type (subtypes of IfcBuildingElement)
    others = Counter(
        e.is_a()
        for e in model.by_type("IfcBuildingElement")
        if not e.is_a("IfcDoor") and not e.is_a("IfcWindow")
    )
    print(f"\nOther building elements: {sum(others.values())}")
    for ifc_type, n in others.most_common():
        print(f"  {ifc_type:<28} {n}")

    # Elements that are not building elements (e.g. openings, furniture)
    non_building = Counter(
        e.is_a()
        for e in model.by_type("IfcElement")
        if not e.is_a("IfcBuildingElement")
    )
    if non_building:
        print("\nOther elements (not building elements, not counted above):")
        for ifc_type, n in non_building.most_common():
            print(f"  {ifc_type:<28} {n}")

    # Note parts that belong to a larger element (e.g. stair flights in a stair)
    parts = Counter()
    for rel in model.by_type("IfcRelAggregates"):
        if rel.RelatingObject.is_a("IfcElement"):
            for part in rel.RelatedObjects:
                parts[f"{part.is_a()} in {rel.RelatingObject.is_a()}"] += 1
    if parts:
        print("\nOf these, parts of a larger element (counted above as well):")
        for key, n in parts.most_common():
            print(f"  {key:<40} {n}")

    # 4. Rooms and floor area
    spaces = model.by_type("IfcSpace")
    print(f"\nRooms (IfcSpace): {len(spaces)}")
    if not spaces:
        print("  No IfcSpace in the file: total floor area can't be determined.")
        return

    total = 0.0
    missing = 0
    sources = Counter()
    for space in spaces:
        area, source = find_area(space)
        name = " ".join(x for x in (space.Name, space.LongName) if x)
        if area is None:
            missing += 1
            print(f"  {name or '(no name)':<30} no area in file")
        else:
            total += area
            sources[source] += 1
            print(f"  {name or '(no name)':<30} {area:8.2f} m²  ({source})")
    print(f"\nTotal floor area: {total:.2f} m² from {len(spaces) - missing} rooms")
    if missing:
        print(f"  {missing} rooms have no area value and are not included.")
    for source, n in sources.items():
        print(f"  Source: {source} ({n} rooms)")


def print_per_storey(title, elements):
    """Print how many elements each storey contains."""
    counts = Counter()
    for e in elements:
        container = ifcopenshell.util.element.get_container(e)
        counts[container.Name if container else "(not assigned)"] += 1
    print(f"  {title}:")
    for name, n in counts.items():
        print(f"    {name:<28} {n}")


def find_area(space):
    """Return (area, source) for a space from its quantities or properties."""
    # get_psets returns property sets and quantity sets
    for set_name, values in ifcopenshell.util.element.get_psets(space).items():
        for key in AREA_KEYS:
            value = values.get(key)
            if isinstance(value, (int, float)) and value > 0:
                return float(value), f"{set_name}.{key}"
    return None, None


if __name__ == "__main__":
    main()
