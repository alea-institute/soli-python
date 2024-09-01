# SOLI Configuration Module

This module contains the configuration utilities for the SOLI (Standard for Open Legal Information) Python library.

## Configuration Constants

- `DEFAULT_CONFIG_PATH`: Path to the default configuration file.
- `DEFAULT_GITHUB_API_URL`: Default GitHub API URL.
- `DEFAULT_GITHUB_OBJECT_URL`: Default GitHub raw content URL.
- `DEFAULT_SOURCE_TYPE`: Default source type for loading the ontology.
- `DEFAULT_HTTP_URL`: Default HTTP URL for the ontology.
- `DEFAULT_GITHUB_REPO_OWNER`: Default GitHub repository owner.
- `DEFAULT_GITHUB_REPO_NAME`: Default GitHub repository name.
- `DEFAULT_GITHUB_REPO_BRANCH`: Default GitHub repository branch.

## SOLI Configuration

A Pydantic model representing the configuration for the SOLI Python library.

### Attributes

- `source`: The source of the SOLI configuration. Must be either 'github' or 'http'.
- `url`: The URL of the SOLI configuration if source is 'http'.
- `repo_owner`: The owner of the GitHub repository if source is 'github'.
- `repo_name`: The name of the GitHub repository if source is 'github'.
- `branch`: The branch of the GitHub repository if source is 'github'.
- `path`: The path to the SOLI.owl file in the repository or URL.
- `use_cache`: Whether to use caching for the SOLI configuration.

### Methods

#### `load_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> SOLIConfiguration`

Load the configuration from a JSON file.

Args:
    config_path (str | Path): The path to the configuration file.

Returns:
    SOLIConfiguration: The loaded configuration object.

Raises:
    FileNotFoundError: If the configuration file is not found.

Example:

````python
config = SOLIConfiguration.load_config()
print(config.source)
print(config.repo_owner)
````


# Usage

To use the SOLI configuration in your project:

1. Create a JSON configuration file (default location: `~/.soli/config.json`) with the following structure:

````json
{
  "soli": {
    "source": "github",
    "repo_owner": "alea-institute",
    "repo_name": "soli",
    "branch": "1.0.0",
    "path": "SOLI.owl",
    "use_cache": true
  }
}
````

In your Python code, import and use the `SOLIConfiguration` class:

````python
from soli.config import SOLIConfiguration

# Load the configuration
config = SOLIConfiguration.load_config()

# Access configuration values
print(f"Source: {config.source}")
print(f"Repository: {config.repo_owner}/{config.repo_name}")
print(f"Branch: {config.branch}")
````

This module provides a flexible way to configure the SOLI Python library, allowing users to specify custom sources and paths for the SOLI ontology.



## Module Contents

```{eval-rst}
.. automodule:: soli.config
    :members:
```
