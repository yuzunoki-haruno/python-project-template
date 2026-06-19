# Python Project Template

**Release**: 1.1.0  
**Date**: 2026-06-20

## Overview

This repository provides a template for a standard project directory.  
Instructions for use are provided in [Usage](#usage).  
A project directory will be created by a Python script.

## Features

- Provide a consistent starting point for new projects
- Reduce manual setup effort
- Improve maintainability and onboarding experience

## Usage

Run the script and configure the project name, description, author, and other details.  
If you leave a field blank and press Enter, the default value will be used.

```shell
$ curl https://raw.githubusercontent.com/yuzunoki-haruno/python-project-template/refs/heads/main/build_project.py -o build_project.py
$ python3 build_project.py 
> project name [my-project]: sample-project
> description [Python project]: This is sample project
> author [Example Author]: Haruno Yuzunoki
> email [exsample.com]: haruno.yusuznoki@example.com
> version [0.1.0]: 1.0.0
> date [2026-06-13]:
Cloning into 'python-project-template'...
```

After the script runs, a project directory with the following structure will be created in the current directory.

```text
sample-project/
├── LICENSE                    # Project license file
├── LICENSES/                  # Directory containing multiple license texts
│   ├── Beerware.txt           # Full text of the Beerware License
│   └── MIT.txt                # Full text of the MIT License
├── README.md                  # Project overview, installation, and usage instructions
├── docs/                      # Project documentation
│   ├── assets/                # Images and other static assets used in the documentation
│   ├── changelog.md           # Release notes and change history
│   ├── index.md               # Documentation landing page
│   ├── reference.md           # API and technical reference documentation
│   └── usage.md               # Usage guide and examples
├── pyproject.toml             # Project metadata, build configuration, and dependencies
├── src/                       # Source code
│   ├── examples/              # Example scripts demonstrating library usage
│   └── sample-project/        # Main Python package
│       ├── __init__.py        # Package initialization module
│       └── py.typed           # Marker indicating support for type hints (PEP 561)
└── tests/                     # Test suite
    └── __init__.py            # Test package initialization module
```

## License

This project is available under multiple licenses.
You can choose either of the following licenses:

- MIT License ([LICENSE-MIT](./LICENSES/MIT.txt))
- Beerware License ([LICENSE-BEERWARE](./LICENSES/Beerware.txt))
