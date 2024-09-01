# Contributing to SOLI Python

Thank you for your interest in contributing to the SOLI Python project! We welcome contributions from the community and appreciate your help in making this project better.

## How to Contribute

### Reporting Bugs

If you find a bug in the project, please open an issue on our [GitHub Issues](https://github.com/alea-institute/soli-python/issues) page. When reporting a bug, please include:

- A clear and descriptive title
- A detailed description of the issue
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Any relevant logs or error messages

### Suggesting Enhancements

We welcome suggestions for improvements to the project. To suggest an enhancement, please open an issue on our [GitHub Issues](https://github.com/alea-institute/soli-python/issues) page with the label "enhancement". Please provide:

- A clear and descriptive title
- A detailed description of the proposed enhancement
- Any potential implementation ideas

### Pull Requests

We encourage you to contribute code to the project. To do so, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes
4. Write tests for your changes (if applicable)
5. Run the test suite to ensure all tests pass
6. Commit your changes with a clear and descriptive commit message
7. Push your branch to your fork
8. Open a pull request against the main repository

When submitting a pull request, please:

- Provide a clear and descriptive title
- Include a detailed description of the changes
- Reference any related issues
- Ensure your code follows the project's coding style and conventions
- Include tests for new functionality

## Development and Testing

To set up the project for development:

* Clone the repository
* Ensure that you have poetry installed:
  - You can install via the [official instructions](https://python-poetry.org/docs/main/#installing-with-the-official-installer).
  - Or you can install via [pipx](https://github.com/pypa/pipx): `pipx install poetry`
* Install the development dependencies: `poetry install`
* Make your changes.
* Test:
  - Run the test suite: `PYTHONPATH=. poetry run pytest tests/`
  - Test via docker: `bash docker/build.sh`

## Coding Style

We follow the PEP 8 style guide for Python code. Please ensure your code adheres to these guidelines.

You can use `ruff` or the `pre-commit run --all-files` command to check your code for style violations.

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## Discussion Forums

Additional discussions about the project can be found on the [SOLI Discourse community](https://discourse.openlegalstandard.org/).

## Questions

If you have any questions about contributing, please open an issue or contact the project maintainers.

Thank you for your contributions to the SOLI Python project!
