#!/usr/bin/env python3
"""Analyze an IFC locally. Usage: python codex.py path/to/model.ifc"""

import argparse
from collections import Counter
import math
from pathlib import Path
import sys

import ifcopenshell
import ifcopenshell.util.unit


def area_scale(unit):
    """Convert an explicit IFC area unit to square metres."""
    if unit.is_a("IfcSIUnit") and unit.Name == "SQUARE_METRE":
        return ifcopenshell.util.unit.get_prefix_multiplier(unit.Prefix) ** 2
    if unit.is_a("IfcConversionBasedUnit"):
        factor = unit.ConversionFactor
        return float(factor.ValueComponent.wrappedValue) * area_scale(factor.UnitComponent)
    raise ValueError(f"Unsupported area unit: {unit}")


def room_areas(space, default_scale):
    """Read declared net and gross floor quantities without double counting."""
    found = {}
    for relation in space.IsDefinedBy:
        if not relation.is_a("IfcRelDefinesByProperties"):
            continue
        definition = relation.RelatingPropertyDefinition
        if not definition.is_a("IfcElementQuantity"):
            continue
        for quantity in definition.Quantities:
            if not quantity.is_a("IfcQuantityArea"):
                continue
            kind = {"NetFloorArea": "net", "GrossFloorArea": "gross"}.get(quantity.Name)
            if kind is None:
                continue
            scale = area_scale(quantity.Unit) if quantity.Unit else default_scale
            value = float(quantity.AreaValue) * scale
            if math.isfinite(value) and value >= 0:
                found.setdefault(kind, []).append(value)
    # Conflicting quantities are ambiguous, so do not silently choose one.
    return {
        kind: values[0]
        for kind, values in found.items()
        if all(math.isclose(values[0], value) for value in values)
    }


def label(entity):
    return f"#{entity.id()} {entity.Name or '(unnamed)'!r}"


def analyze(model):
    print(f"IFC schema: {model.schema}")
    units = ifcopenshell.util.unit
    length_scale = units.calculate_unit_scale(model)
    area_unit = units.get_project_unit(model, "AREAUNIT")
    default_area_scale = area_scale(area_unit) if area_unit else length_scale ** 2

    storeys = sorted(
        model.by_type("IfcBuildingStorey"),
        key=lambda item: (item.Elevation is None, item.Elevation or 0, item.id()),
    )
    print(f"Storeys: {len(storeys)}")
    for storey in storeys:
        elevation = (
            f"{storey.Elevation * length_scale:.3f} m"
            if storey.Elevation is not None else "unavailable"
        )
        print(f"  {label(storey)}; elevation: {elevation}")

    # by_type includes subclasses; group other elements by their exact IFC class.
    print(f"Doors: {len(model.by_type('IfcDoor'))}")
    print(f"Windows: {len(model.by_type('IfcWindow'))}")
    others = Counter(
        element.is_a()
        for element in model.by_type("IfcBuildingElement")
        if not element.is_a("IfcDoor") and not element.is_a("IfcWindow")
    )
    print(f"Other building elements: {sum(others.values())}")
    for name, count in sorted(others.items()):
        print(f"  {name}: {count}")

    spaces = sorted(model.by_type("IfcSpace"), key=lambda item: item.id())
    print(f"Rooms (IfcSpace): {len(spaces)}")
    totals = {"net": [], "gross": []}
    for space in spaces:
        areas = room_areas(space, default_area_scale)
        description = "; ".join(
            f"{kind} floor area: {areas[kind]:.3f} m²"
            for kind in ("net", "gross") if kind in areas
        )
        print(f"  {label(space)}; {description or 'floor area: unavailable'}")
        for kind, value in areas.items():
            totals[kind].append(value)

    # Keep net and gross separate and make incomplete coverage explicit.
    for kind, values in totals.items():
        if values:
            print(
                f"Total {kind} room floor area: {sum(values):.3f} m² "
                f"({len(values)}/{len(spaces)} rooms with declared quantities)"
            )
        else:
            print(f"Total {kind} room floor area: unavailable")
    print("Areas use declared NetFloorArea/GrossFloorArea quantities; no geometry estimate.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ifc_path", type=Path, help="Path to a local IFC file")
    args = parser.parse_args()
    path = args.ifc_path.expanduser()
    if not path.is_file():
        parser.error(f"IFC file not found: {path}")
    try:
        analyze(ifcopenshell.open(str(path)))
    except (OSError, RuntimeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
