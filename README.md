# csvstat

A lightweight command-line CSV data profiling tool built with Python.

## Overview

`csvstat` is a command-line tool that analyzes CSV files and provides useful profiling information about the dataset, including column types, missing values, numerical statistics, and frequent values.

The project is also packaged as `csvstat-py` and published on PyPI, allowing users to install and use it directly with `pip`.

## Features

* Detects numeric, date, and text columns
* Counts missing values
* Calculates missing-value percentages
* Calculates minimum, mean, and maximum for numeric columns
* Displays the most frequent values in text columns
* Supports configurable top-N values
* Includes comprehensive `pytest` unit tests
* Packaged using `pyproject.toml`
* Published on PyPI

## Installation

### Install from PyPI

The easiest way to install `csvstat` is directly from PyPI:

```bash
python -m pip install csvstat-py
```

After installation, verify it:

```bash
csvstat --help
```

### Install from Source

Clone the repository:

```bash
git clone https://github.com/palak200526/csvStat.git
cd csvStat
```

Install the package locally:

```bash
python -m pip install -e .
```

## Usage

### Basic Usage

Run `csvstat` with a CSV file:

```bash
csvstat tests/data/sample.csv
```

### Top N Values

To display a different number of frequent values:

```bash
csvstat tests/data/sample.csv --top 3
```

## Example Output

```text
CSV file: tests/data/sample.csv

Rows: 10

Columns: 7

Age:
  Type: numeric
  Missing: 0
  Missing percentage: 0.00%
  Min: 22.0
  Mean: 28.20
  Max: 40.0

Salary:
  Type: numeric
  Missing: 0
  Missing percentage: 0.00%
  Min: 50000.0
  Mean: 67200.00
  Max: 95000.0
```

## Testing

The project uses `pytest` for unit testing.

Run the complete test suite:

```bash
pytest
```

Expected result:

```text
73 passed
```

## Project Structure

```text
csvStat/
├── src/
│   └── csvstat/
│       ├── __init__.py
│       ├── cli.py
│       └── profiler.py
├── tests/
│   ├── data/
│   │   └── sample.csv
│   ├── test_cli.py
│   └── test_profiler.py
├── pyproject.toml
├── README.md
├── PACKAGE.md
├── LICENSE
└── .gitignore
```

## Packaging

The project is configured as a Python package using `pyproject.toml`.

### Local Installation

Install the package locally with:

```bash
python -m pip install -e .
```

### PyPI Installation

The package is published on PyPI as:

* **Package:** `csvstat-py`
* **Version:** `0.1.4`

Install it using:

```bash
python -m pip install csvstat-py
```

After installation, the `csvstat` command can be used directly from the terminal:

```bash
csvstat tests/data/sample.csv
```

## PyPI

The package is available on PyPI:

https://pypi.org/project/csvstat-py/

## Source Code

The source code is available on GitHub:

https://github.com/palak200526/csvStat

## License

This project is licensed under the MIT License.
