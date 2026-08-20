# csvstat-py

A lightweight command-line **CSV** data profiling tool built with Python.

`csvstat-py` is a simple command-line tool for quickly analyzing **CSV** files and understanding the structure and basic statistics of a dataset.

## Features

* Detects numeric, date, and text columns
* Counts missing values
* Calculates missing-value percentages
* Calculates minimum, mean, and maximum for numeric columns
* Displays the most frequent values in text columns
* Supports configurable top-N values
* Simple command-line interface
* Unit tested using pytest

## Installation

Install `csvstat-py` directly from PyPI:

```bash
pip install csvstat-py
```

## Usage

Run `csvstat` with a **CSV** file:

```bash
csvstat sample.csv
```

### Top N Values

Display a specific number of frequent values:

```bash
csvstat sample.csv --top 3
```

### Command Options

```text
usage: csvstat [-h] [--top TOP] file
```

* `file` — Path to the **CSV** file
* `--top TOP` — Number of frequent values to display
* `-h, --help` — Show help information

## Requirements

* Python 3.10 or higher

## Testing

The project uses `pytest` for unit testing.

Run:

```bash
pytest
```

## Package Information

* **Package:** `csvstat-py`
* **Command:** `csvstat`
* **Version:** `0.1.4`
* **License:** MIT

## PyPI

https://pypi.org/project/csvstat-py/

## Source Code

https://github.com/palak200526/csvStat

## License

This project is licensed under the **MIT** License.
