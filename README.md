# SOLI Python Library

![SOLI Logo](https://openlegalstandard.org/assets/images/soli-intro-logo.png)

[![PyPI version](https://badge.fury.io/py/soli-python.svg)](https://badge.fury.io/py/soli-python)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/soli-python.svg)](https://pypi.org/project/soli-python/)

The SOLI Python Library provides a simple and efficient way to interact with the Standard for Open Legal Information (SOLI) ontology.

SOLI is an open, CC-BY licensed standard designed to represent universal elements of legal data, improving communication and data interoperability across the legal industry.

## Features

- Load the SOLI ontology from GitHub or a custom HTTP URL
- Search for classes by label or definition
- Get subclasses and parent classes
- Access detailed information about each class, including labels, definitions, and examples
- Convert classes to OWL XML or Markdown format

## Installation

You can install the SOLI Python library using pip:

```bash
pip install soli-python
```

For the latest development version, you can install directly from GitHub:

```bash
pip install --upgrade https://github.com/alea-institute/soli-python/archive/refs/heads/main.zip
```

## Quick Start

Here's a simple example to get you started with the SOLI Python library:

```python
from soli import SOLI

# Initialize the SOLI client
soli = SOLI()

# Search by prefix
results = soli.search_by_prefix("Mich")
for owl_class in results:
    print(f"Class: {owl_class.label}")

# Search for a class by label
results = soli.search_by_label("Mich")
for owl_class, score in results:
    print(f"Class: {owl_class.label}, Score: {score}")

# Get all areas of law
areas_of_law = soli.get_areas_of_law()
for area in areas_of_law:
    print(area.label)
```

## Documentation

For more detailed information about using the SOLI Python library, please refer to our [full documentation](https://soli-python.readthedocs.io/).

## Contributing

We welcome contributions to the SOLI Python library! If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and write tests if applicable
4. Run the test suite to ensure everything is working
5. Submit a pull request with a clear description of your changes

For more information, see our [contribution guidelines](CONTRIBUTING.md).

## SOLI API
A public, freely-accessible API is available for the SOLI ontology.

The API is hosted at [https://soli.openlegalstandard.org/](https://soli.openlegalstandard.org/).

The source code for the API is available on GitHub at [https://github.com/alea-institute/soli-api](https://github.com/alea-institute/soli-api).


## License

The SOLI Python library is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions about using the SOLI Python library, please [open an issue](https://github.com/alea-institute/soli-python/issues) on GitHub.

## Learn More

To learn more about SOLI, its development, and how you can get involved, visit the [SOLI website](https://openlegalstandard.org/) or join the [SOLI community forum](https://discourse.openlegalstandard.org/).
