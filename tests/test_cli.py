import sys

from src.csvstat.cli import main


def test_csv_loading_and_row_count(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            "tests/data/sample.csv"
        ]
    )

    main()

    output = capsys.readouterr().out

    assert "Rows: 10" in output


def test_column_count(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            "tests/data/sample.csv"
        ]
    )

    main()

    output = capsys.readouterr().out

    assert "Columns: 7" in output



def test_numeric_column_detection(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            "tests/data/sample.csv"
        ]
    )

    main()

    output = capsys.readouterr().out

    assert "Age:" in output
    assert "Type: numeric" in output


def test_text_column_detection(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            "tests/data/sample.csv"
        ]
    )

    main()

    output = capsys.readouterr().out

    assert "Department:" in output
    assert "Type: text" in output


def test_numeric_statistics(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            "tests/data/sample.csv"
        ]
    )

    main()

    output = capsys.readouterr().out

    assert "Min: 22.0" in output
    assert "Mean: 28.20" in output
    assert "Max: 40.0" in output


def test_salary_statistics(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            "tests/data/sample.csv"
        ]
    )

    main()

    output = capsys.readouterr().out

    assert "Min: 50000.0" in output
    assert "Mean: 67200.00" in output
    assert "Max: 95000.0" in output




def test_categorical_statistics(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            "tests/data/sample.csv"
        ]
    )

    main()

    output = capsys.readouterr().out

    assert "Top 5 values:" in output
    assert "IT: 4" in output
    assert "HR: 3" in output
    assert "Finance: 3" in output


def test_top_argument(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            "tests/data/sample.csv",
            "--top",
            "1"
        ]
    )

    main()

    output = capsys.readouterr().out

    assert "Top 1 values:" in output
    assert "IT: 4" in output



def test_invalid_file(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            "does_not_exist.csv"
        ]
    )

    main()

    output = capsys.readouterr().out

    assert "was not found" in output



def test_top_zero(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            "tests/data/sample.csv",
            "--top",
            "0"
        ]
    )

    try:
        main()
    except SystemExit as error:
        assert error.code == 2


def test_top_negative(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            "tests/data/sample.csv",
            "--top",
            "-1"
        ]
    )

    try:
        main()
    except SystemExit as error:
        assert error.code == 2


def test_top_non_integer(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            "tests/data/sample.csv",
            "--top",
            "abc"
        ]
    )

    try:
        main()
    except SystemExit as error:
        assert error.code == 2



def test_empty_csv(tmp_path, monkeypatch, capsys):
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("")

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            str(empty_file)
        ]
    )

    main()

    output = capsys.readouterr().out

    assert "CSV file:" in output




def test_header_only_csv(tmp_path, monkeypatch, capsys):
    csv_file = tmp_path / "header_only.csv"

    csv_file.write_text(
        "Name,Age,Salary,Department\n"
    )

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            str(csv_file)
        ]
    )

    main()

    output = capsys.readouterr().out

    assert "Rows: 0" in output
    assert "Columns: 4" in output



def test_missing_values(tmp_path, monkeypatch, capsys):
    csv_file = tmp_path / "missing.csv"

    csv_file.write_text(
        "Name,Age,Salary\n"
        "Alice,22,50000\n"
        "Bob,,60000\n"
        "Charlie,23,\n"
    )

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            str(csv_file)
        ]
    )

    main()

    output = capsys.readouterr().out

    assert "Missing: 1" in output



def test_whitespace_values(tmp_path, monkeypatch, capsys):
    csv_file = tmp_path / "whitespace.csv"

    csv_file.write_text(
        "Name,Age\n"
        "Alice, 22 \n"
        "Bob, 25 \n"
    )

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            str(csv_file)
        ]
    )

    main()

    output = capsys.readouterr().out

    assert "Type: numeric" in output
    assert "Min: 22.0" in output
    assert "Max: 25.0" in output