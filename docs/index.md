# Welcome to the SOLI Python Documentation

## Introduction

SOLI (Standard for Open Legal Information) is an open, CC-BY licensed standard designed to represent universal elements of legal data, improving communication and data interoperability across the legal industry.

The SOLI Python library provides an easy-to-use interface for working with the SOLI ontology, allowing users to load, parse, and query the SOLI knowledge graph.

For more information about SOLI, visit the [official SOLI website](https://openlegalstandard.org/).

## What is SOLI?

SOLI is a comprehensive ontology that includes over 18,000 standardized concepts covering a wide range of legal terms, including both common and specialized concepts. It combines the power of ontology and taxonomy to create a comprehensive way to describe legal information.

Key features of SOLI include:
- Unique identifiers for every concept
- Multilingual support
- Open development process

## Installation

You can install the SOLI Python library using `pip` from the following sources:


### GitHub (Development Version)

```bash
pip install --upgrade https://github.com/alea-institute/soli-python/archive/refs/heads/main.zip
```

### PyPI (Coming Soon)

```bash
pip install soli-python
```



## Getting Started

Loading the SOLI ontology is as simple as creating a new SOLI graph instance:

```python
from soli import SOLI

# Initialize the SOLI graph
# This will retrieve the OWL file from the default GitHub repository or
# re-use an existing, cached copy if available.

graph = SOLI()
```

Once you have initialized the graph, you can conveniently access the SOLI taxonomy or OWL classes.

```python
print(graph["R8g9E8c4U6pZQefIjUNRuDd"].to_json())
```

```json
{
  "iri": "https://soli.openlegalstandard.org/R8g9E8c4U6pZQefIjUNRuDd",
  "label": "Bankruptcy, Insolvency, and Restructuring Law",
  "sub_class_of": [
    "https://soli.openlegalstandard.org/RSYBzf149Mi5KE0YtmpUmr"
  ],
  "parent_class_of": [
    "https://soli.openlegalstandard.org/R8D2A8vpEW3oEpxLRVkaVDk",
    "https://soli.openlegalstandard.org/RBGaYz0rr5Dh0Sjxu0Z6DHx"
  ],
  "is_defined_by": null,
  "see_also": [],
  "comment": null,
  "deprecated": false,
  "preferred_label": null,
  "alternative_labels": [
    "Bankruptcy and Restructuring",
    "BKCY"
  ],
  "translations": {
    "en-gb": "Bankruptcy and Restructuring Law",
    "pt-br": "Direito de falência e reestruturação",
    "fr-fr": "Droit de la faillite et de la restructuration",
    "de-de": "Insolvenz- und Restrukturierungsrecht",
    "es-es": "Ley de Bancarrota y Reestructuración",
    "es-mx": "Ley de Quiebras y Reestructuración",
    "he-il": "חוקי פשיטת רגל והתארגנות כלכלית",
    "hi-in": "दिवालियापन और पुनर्गठन कानून",
    "zh-cn": "破产和重组法",
    "ja-jp": "破産および再生label"
    :
    "BKCY",
    "definition": "Laws relating to insolvent individuals and companies.",
    "examples": [],
    "notes": [
      "Added \"Insolvency\" to rdfs:label, per UK law (where \"insolvency\" differs from \"bankruptcy\"). In the UK, individuals and companies can be \"insolvent,\" but companies cannot file for \"bankruptcy.\""
    ],
    "history_note": null,
    "editorial_note": null,
    "in_scheme": null,
    "identifier": "BKCY",
    "description": null,
    "source": null,
    "country": null
}
```

### Listing taxonomies

For example, you can list all areas of law in the SOLI ontology:

```python
# Get all areas of law
areas_of_law = graph.get_areas_of_law()
print(areas_of_law[-1])

# Output: OWLClass(label=Antitrust and Competition Law, iri=https://soli.openlegalstandard.org/RDFwOzDi3E8DQ0OxTKb6UEJ)
````

It's also easy to limit the taxonomic depth:

```python
# Limit to top-level areas of law
areas_of_law = graph.get_areas_of_law()
top_areas_of_law = graph.get_areas_of_law(max_depth=1)
print(f"Count: {len(top_areas_of_law)} / {len(areas_of_law)}")

# Count: 31 / 174
````

Retrieving subgraphs in both directions, e.g., children and parents, is also straightforward:

```python
# Get parent classes for bankruptcy law
print("Parents:", graph.get_parents("R8g9E8c4U6pZQefIjUNRuDd"))

# Get child classes for bankruptcy law
print("Children", graph.get_children("R8g9E8c4U6pZQefIjUNRuDd"))
```

### IRIs
Note that you can use the SOLI IRIs, legacy IRIs, or short-hand identifiers to access classes:

```python
# Get a class by formal IRI
graph["https://soli.openlegalstandard.org/R8g9E8c4U6pZQefIjUNRuDd"] \
    == graph["R8g9E8c4U6pZQefIjUNRuDd"] \
    == graph["http://lmss.sali.org/R8g9E8c4U6pZQefIjUNRuDd"]

# True
```

### Converting classes

Classes can be converted to JSON, OWL, or Markdown in a single line:

 * `.to_json()`: Convert to JSON
 * `.to_owl_element()`: Convert to OWL lxml.etree element
 * `.to_owl_xml()`: Convert to OWL XML string
 * `.to_markdown()`: Convert to rich Markdown string


### Examples

More examples are available in the [examples](examples.md) section.



## Features

- Load the SOLI ontology from GitHub or a custom HTTP URL
- Search for classes by label or definition
- Get subclasses and parent classes
- Access detailed information about each class, including labels, definitions, and examples
- Convert classes to OWL XML or Markdown format

## API Reference

For detailed information about the SOLI Python library API, please refer to the API documentation (coming soon).

## Contributing

Contributions to the SOLI Python library are welcome! Please see our [contribution guidelines](contributing.md) for more information. You can also contribute to the SOLI standard itself through the [SOLI GitHub repository](https://github.com/alea-institute/soli-api).

## License

The SOLI Python library is released under the MIT License. See the [LICENSE](https://github.com/alea-institute/soli-python/blob/main/LICENSE) file for details.

The SOLI standard itself is available under the Creative Commons Attribution (CC-BY) License.

```{toctree}
:maxdepth: 2
:caption: Contents:

examples
soli/graph
soli/models
soli/config
soli/logger
contributing
```

## Indices and Tables

* {ref}`genindex`
* {ref}`modindex`
* {ref}`search`

## Learn More

To learn more about SOLI, its development, and how you can get involved, visit the [SOLI website](https://openlegalstandard.org/) or join the [SOLI community forum](https://openlegalstandard.org/forum/).
