### Hexlet tests and linter status:
[![Actions Status](https://github.com/NikolyKa/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/NikolyKa/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/ca7b3feebf184ee01fa0/maintainability)](https://codeclimate.com/github/NikolyKa/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ca7b3feebf184ee01fa0/test_coverage)](https://codeclimate.com/github/NikolyKa/python-project-lvl2/test_coverage)
[![linter-check](https://github.com/NikolyKa/python-project-lvl2/actions/workflows/linter-check.yml/badge.svg)](https://github.com/NikolyKa/python-project-lvl2/actions/workflows/linter-check.yml)
[![tests](https://github.com/NikolyKa/python-project-lvl2/actions/workflows/tests.yml/badge.svg)](https://github.com/NikolyKa/python-project-lvl2/actions/workflows/tests.yml)

## Generate diff.

### This program find differences between two configuration files.

### Supported formats: 
- **YAML**,
- **YML**,
- **JSON**.

## Installation:
```$ git clone https://github.com/NikolyKa/python-project-lvl2.git```

## Usage:

`$ gendiff -h`

```
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        Available formats : stylish, plain, json
```
## Format examples:
### Flat File (JSON)

[![asciicast](https://asciinema.org/a/yknJyMf791U077fr62A7SPilj.svg)](https://asciinema.org/a/yknJyMf791U077fr62A7SPilj)
### Nested File (JSON)


[![asciicast](https://asciinema.org/a/3DgfpkMtEeCA6shz4cRct0oMF.svg)](https://asciinema.org/a/3DgfpkMtEeCA6shz4cRct0oMF)
### Plain File (JSON)

[![asciicast](https://asciinema.org/a/65uPdNTUp0jS9zKBmqUjRBwMR.svg)](https://asciinema.org/a/65uPdNTUp0jS9zKBmqUjRBwMR)
### Json File

[![asciicast](https://asciinema.org/a/GCajRsxAxaIIPuXHmDmzKpUwi.svg)](https://asciinema.org/a/GCajRsxAxaIIPuXHmDmzKpUwi)