# SOLI Python Examples

This document provides examples of how to use the SOLI (Standard for Open Legal Information) Python library. We'll start with basic usage and progress to more complex examples.

## Installation

You can install the latest version of the SOLI Python library from GitHub using `pip`:

```bash
pip install --upgrade https://github.com/alea-institute/soli-python/archive/refs/heads/main.zip
```

## Initializing the SOLI Graph

```python
from soli import SOLI

# Initialize the SOLI graph with default settings
soli = SOLI()

# Initialize with custom settings
soli_custom = SOLI(
    source_type="github",
    github_repo_owner="alea-institute",
    github_repo_name="SOLI",
    github_repo_branch="1.0.0",
    use_cache=True
)

# Initialize from a custom HTTP URL
soli_http = SOLI(
    source_type="http",
    http_url="https://github.com/alea-institute/SOLI/raw/main/SOLI.owl"
)
```

## Basic Operations

```python
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
```

## Searching for Classes

### Search by Label

```python
# Search for classes with "SDNY" in the label
results = soli.search_by_label("SDNY", limit=3)
for owl_class, score in results:
    print(f"Class: {owl_class.label}, Score: {score}")
```

### Search by Definition

```python
# Search for classes with "waterways" in the definition
results = soli.search_by_definition("waterways", limit=3)
print("** Definitions **")
for owl_class, score in results:
    print(f"Class: {owl_class.label}, Definition: {owl_class.definition[:50]}..., Score: {score}")
```

## Working with SOLI Taxonomic Types

```python
from soli import SOLITypes

# Get all areas of law
areas_of_law = soli.get_areas_of_law()
print("Areas of Law:")
for area in areas_of_law:
    print(f"- {area.label}")

# Get all legal entities
legal_entities = soli.get_legal_entities()
print("\nLegal Entities:")
for entity in legal_entities:
    print(f"- {entity.label}")

# Get all industries
industries = soli.get_industries()
print("\nIndustries:")
for industry in industries:
    print(f"- {industry.label}")
```

## Traversing the Ontology

```python
# Get parent classes
bankruptcy_law = soli.search_by_label("Personal Bankruptcy Law")[0][0]
parent_classes = soli.get_parents(bankruptcy_law.iri)
print("Parent classes of Personal Bankruptcy Law:")
for parent in parent_classes:
    print(f"- {parent.label}")

# Get child classes
area_of_law_iri = soli["https://soli.openlegalstandard.org/RSYBzf149Mi5KE0YtmpUmr"].iri
child_classes = soli.get_children(area_of_law_iri, max_depth=1)
print("\nDirect child classes of Area of Law:")
for child in child_classes:
    print(f"- {child.label}")

# Get entire subgraph
subgraph = soli.get_subgraph(area_of_law_iri, max_depth=2)
print(f"\nNumber of classes in Area of Law subgraph (depth 2): {len(subgraph)}")
```

## Working with Triples

```python
# Get triples by predicate
is_defined_by_triples = soli.get_triples_by_predicate("rdfs:isDefinedBy")
print(f"Number of rdfs:isDefinedBy triples: {len(is_defined_by_triples)}")

# Get triples by subject
subject_iri = "https://soli.openlegalstandard.org/RBGPkZ1oRgcP05LWQBGLEne"
subject_triples = soli.get_triples_by_subject(subject_iri)
print(f"\nTriples for subject {subject_iri}:")
for triple in subject_triples:
    print(f"- {triple[1]} {triple[2]}")

# Get triples by object
object_iri = "https://soli.openlegalstandard.org/R9sbuHkJC9aqDlHAgw58VSB"
object_triples = soli.get_triples_by_object(object_iri)
print(f"\nTriples with object {object_iri}:")
for triple in object_triples:
    print(f"- {triple[0]} {triple[1]}")
```

## Advanced Usage

### Refreshing the Ontology

```python
# Refresh the ontology to get the latest version
soli.refresh()
print(f"Ontology refreshed. New class count: {len(soli)}")
```

### Generating New IRIs

```python
# Generate a new IRI for a custom class
new_iri = soli.generate_iri()
print(f"Generated IRI: {new_iri}")
```

### Working with Multiple Branches

```python
# List available branches
branches = SOLI.list_branches()
print("Available branches:")
for branch in branches:
    print(f"- {branch}")

# Load a specific branch
soli_1_0_0 = SOLI(github_repo_branch="1.0.0")
print(f"Loaded SOLI version 1.0.0. Class count: {len(soli_1_0_0)}")
```

These examples demonstrate the basic and advanced usage of the SOLI Python library. You can explore more functionality by referring to the API documentation and the source code of the `SOLI` class in the `soli/graph.py` file.
