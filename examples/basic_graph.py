from soli import SOLI

if __name__ == "__main__":
    # Initialize the SOLI client with default settings
    soli = SOLI()

    # Get the number of classes in the ontology
    print(f"Number of classes: {len(soli)}")

    # Get ontology title and description
    print(f"Title: {soli.title}")
    print(f"Description: {soli.description}")

    # Access a class by IRI
    contract_class = soli["https://soli.openlegalstandard.org/R602916B1A80fDD28d392d3f"]
    print(f"Class: {contract_class.label}")
    print(f"Definition: {contract_class.definition}")

    # Access a class by short IRI
    edmi_class = soli["R602916B1A80fDD28d392d3f"]
    print(f"Class: {edmi_class.label}")

    # Get class by index
    first_class = soli[0]
    print(f"First class: {first_class.label}")
