from soli import SOLI

if __name__ == "__main__":
    # Initialize the SOLI client with default settings
    soli = SOLI()

    # Get parent classes
    bankruptcy_law = soli.search_by_label("Personal Bankruptcy Law")[0][0]
    parent_classes = soli.get_parents(bankruptcy_law.iri)
    print("Parent classes of Personal Bankruptcy Law:")
    for parent in parent_classes:
        print(f"- {parent.label}")

    # Get child classes
    area_of_law_iri = soli[
        "https://soli.openlegalstandard.org/RSYBzf149Mi5KE0YtmpUmr"
    ].iri
    child_classes = soli.get_children(area_of_law_iri, max_depth=1)
    print("\nDirect child classes of Area of Law:")
    for child in child_classes:
        print(f"- {child.label}")

    # Get entire subgraph
    subgraph = soli.get_subgraph(area_of_law_iri, max_depth=2)
    print(f"\nNumber of classes in Area of Law subgraph (depth 2): {len(subgraph)}")
