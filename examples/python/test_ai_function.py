"""
test_ai_function.py: a template for testing a function an AI wrote, before you trust it (worked example 3).

Usage:
    pip install pytest
    pytest examples/python/test_ai_function.py

The file contains the AI's first version (fails most tests) and the second version (passes). Replace
daily_mean with your own AI-written function and write the table of cases BEFORE you ask for the code:
the table is the specification, and giving it to the AI is what turns a vague request into a good answer.

No API key needed.
"""

import math

import pytest

# ----------------------------------------------------------------- the AI's first attempt


def daily_mean_v1(readings):
    """Return the mean of the valid readings in the list (AI's first version)."""
    valid = [r for r in readings if r is not None]
    return sum(valid) / len(valid)


# ----------------------------------------------------------------- the second attempt, after the tests were given

MISSING = {"", "N/A", "NA", "nan", "None"}
SENSOR_ERROR = -999.0


def to_reading(value):
    """Convert one raw CSV value to a float, or None if it is missing or invalid."""
    if value is None:
        return None
    if isinstance(value, str):
        value = value.strip()
        if value in MISSING:
            return None
        try:
            value = float(value)
        except ValueError:
            return None
    if isinstance(value, float) and math.isnan(value):
        return None
    if value == SENSOR_ERROR:
        return None
    return float(value)


def daily_mean(readings):
    """Mean of the valid readings; None if there are none."""
    valid = [v for v in (to_reading(r) for r in readings) if v is not None]
    if not valid:
        return None
    return sum(valid) / len(valid)


# ----------------------------------------------------------------- the test table, written before asking for code

CASES = [
    ("normal readings with one None", [20.1, 20.5, None, 21.0], pytest.approx(20.5333, abs=1e-3)),
    ("empty list", [], None),
    ("only missing", [None, None], None),
    ("text marker N/A", [20.1, "N/A", 21.0], pytest.approx(20.55)),
    ("sensor error code", [20.1, -999, 21.0], pytest.approx(20.55)),
    ("strings from CSV", ["20.1", "20.5"], pytest.approx(20.3)),
    ("empty string", ["", "20.0"], pytest.approx(20.0)),
    ("whitespace around numbers", [" 20.0 ", "21.0"], pytest.approx(20.5)),
]


@pytest.mark.parametrize("name, readings, expected", CASES, ids=[c[0] for c in CASES])
def test_daily_mean(name, readings, expected):
    assert daily_mean(readings) == expected


@pytest.mark.parametrize("name, readings, expected", CASES[1:], ids=[c[0] for c in CASES[1:]])
def test_first_version_fails_on_edge_cases(name, readings, expected):
    """Documents why the first version was not acceptable: it crashes or returns a wrong number."""
    try:
        result = daily_mean_v1(readings)
    except (ZeroDivisionError, TypeError):
        return  # a crash: the test passes because we expected the first version to be inadequate
    assert result != expected
