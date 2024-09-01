from soli import SOLI

if __name__ == "__main__":
    # Initialize the SOLI client with default settings
    soli = SOLI()

    # Get all areas of law
    areas_of_law = soli.get_areas_of_law()
    print("** Areas of Law:**")
    for area in areas_of_law:
        print(f"- {area.label}")
    print()

    # Only top level
    areas_of_law = soli.get_areas_of_law(max_depth=1)
    print("** Top Level Areas of Law:**")
    for area in areas_of_law:
        print(f"- {area.label}")
    print()

    # Get all legal entities
    legal_entities = soli.get_legal_entities()
    print("\nLegal Entities:")
    for entity in legal_entities:
        print(f"- {entity.label}")
    print()
