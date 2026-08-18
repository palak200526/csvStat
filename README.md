# csvstat

A lightweight command-line CSV data profiling tool built with Python.

## Overview

`csvstat` is a command-line tool that analyzes CSV files and provides useful profiling information about the dataset, including column types, missing values, numerical statistics, and frequent values.

## Features

* Detects numeric, date, and text columns
* Counts missing values
* Calculates missing-value percentages
* Calculates minimum, mean, and maximum for numeric columns
* Displays the most frequent values in text columns
* Supports configurable top-N values
* Includes comprehensive `pytest` unit tests
* Packaged using `pyproject.toml`

## Installation

Clone the repository:

```bash
git clone https://github.com/palak200526/csvStat.git
cd csvStat
```

Install the package:

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
├── LICENSE
└── .gitignore
```

## Packaging

The project is configured as a Python package using `pyproject.toml`.

Install the package locally with:

```bash
python -m pip install -e .
```

After installation, the `csvstat` command can be used directly from the terminal:

```bash
csvstat tests/data/sample.csv
```

## License

This project is licensed under the MIT License.
