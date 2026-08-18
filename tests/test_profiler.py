import pytest

from src.csvstat.profiler import (
    is_numeric,
    is_date,
    infer_type,
    numeric_stats,
)



@pytest.mark.parametrize(
    "value, expected",
    [
        ("25", True),
        ("25.5", True),
        ("-25", True),
        ("-25.5", True),
        ("0", True),
        ("0.0", True),
        ("1e3", True),
        ("+25", True),
        (" 25 ", True),
        ("hello", False),
        ("", False),
        ("   ", False),
        ("25abc", False),
        ("1,000", False),
    ],
)
def test_is_numeric(value, expected):
    assert is_numeric(value) is expected


def test_is_numeric_invalid_object():
    with pytest.raises(TypeError):
        is_numeric(None)



@pytest.mark.parametrize(
    "value, expected",
    [
        ("2026-08-18", True),
        ("18-08-2026", True),
        ("2026/08/18", True),
        ("2026-02-30", False),
        ("2026-13-01", False),
        ("18/08/2026", False),
        ("hello", False),
        ("", False),
        ("   ", False),
        ("2024-02-29", True),
        ("2025-02-29", False),
    ],
)
def test_is_date(value, expected):
    assert is_date(value) is expected


def test_is_date_invalid_object():
    with pytest.raises(TypeError):
        is_date(None)




@pytest.mark.parametrize(
    "values, expected",
    [
        (["10", "20", "30"], "numeric"),
        (["10.5", "20.2", "30.8"], "numeric"),
        (["-10", "-20", "-30"], "numeric"),
        (
            ["2026-01-01", "2026-02-01", "2026-03-01"],
            "date",
        ),
        (["IT", "HR", "Finance"], "text"),
        (["IT", "25", "HR"], "text"),
        (["10", "", "20", "30"], "numeric"),
        (
            ["2026-01-01", "", "2026-03-01"],
            "date",
        ),
        (["IT", "", "HR"], "text"),
        (["", "", ""], "text"),
        (["  ", " ", ""], "text"),
        ([" 10 ", " 20 ", " 30 "], "numeric"),
        (
            ["2026-01-01", "100", "2026-03-01"],
            "text",
        ),
        (["100"], "numeric"),
        (["Alice"], "text"),
        (["2026-08-18"], "date"),
    ],
)
def test_infer_type(values, expected):
    assert infer_type(values) == expected


def test_infer_type_empty_list():
    assert infer_type([]) == "text"


def test_infer_type_none_values():
    with pytest.raises(AttributeError):
        infer_type([None, "10", "20"])




@pytest.mark.parametrize(
    "values, expected_min, expected_mean, expected_max",
    [
        (["10", "20", "30"], 10, 20, 30),
        (["10.5", "20.5", "30.5"], 10.5, 20.5, 30.5),
        (["-10", "-20", "-30"], -30, -20, -10),
        (["0", "10", "20"], 0, 10, 20),
        (["10", "", "20", "30"], 10, 20, 30),
        ([" 10 ", " 20 ", " 30 "], 10, 20, 30),
        (["50"], 50, 50, 50),
        (["10", "10", "10"], 10, 10, 10),
        (
            ["10", "20", "25"],
            10,
            pytest.approx(18.333333),
            25,
        ),
        (["1e2", "2e2", "3e2"], 100, 200, 300),
    ],
)
def test_numeric_stats(
    values,
    expected_min,
    expected_mean,
    expected_max,
):
    minimum, mean, maximum = numeric_stats(values)

    assert minimum == expected_min
    assert mean == expected_mean
    assert maximum == expected_max


@pytest.mark.parametrize(
    "values",
    [
        ["", "", ""],
        [],
    ],
)
def test_numeric_stats_invalid_input(values):
    with pytest.raises(ValueError):
        numeric_stats(values)