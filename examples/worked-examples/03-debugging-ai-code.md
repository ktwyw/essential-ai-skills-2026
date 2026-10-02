# Worked example 3: Debugging AI-written code

**Modules:** 2, 7, 8 · **Time:** 30 minutes

## The task

Aigerim has a spreadsheet of hourly temperature readings from a reactor, exported as CSV. Some readings are missing (empty cells), some are recorded as `"N/A"`, and the sensor occasionally logs `-999` when it fails. She wants the daily mean temperature.

## The prompt

> Write a Python function that takes a list of hourly temperature readings for one day and returns the daily mean. Some readings may be missing.

## What came back

```python
def daily_mean(readings):
    """Return the mean of the valid readings in the list."""
    valid = [r for r in readings if r is not None]
    return sum(valid) / len(valid)

# Example
print(daily_mean([20.1, 20.5, None, 21.0]))   # 20.533...
```

> This function filters out missing values (`None`) and returns the average of the remaining readings.

The example runs and prints 20.533. Many people would stop here.

## The test routine

Module 2 says: test normal cases, edge cases, and bad input. Aigerim wrote the tests before fixing anything, so that she would know when she was done. The file [`examples/python/test_ai_function.py`](../python/test_ai_function.py) contains them.

| Input | Expected | What the AI's function did |
|-------|----------|---------------------------|
| `[20.1, 20.5, None, 21.0]` | 20.53 | 20.53 ✓ |
| `[]` | a clear error or `None`, not a crash | `ZeroDivisionError` ✗ |
| `[None, None]` | same as above | `ZeroDivisionError` ✗ |
| `[20.1, "N/A", 21.0]` | 20.55 (ignore the text) | `TypeError: unsupported operand` ✗ |
| `[20.1, -999, 21.0]` | 20.55 (sensor failure code) | −319.3 ✗ |
| `["20.1", "20.5"]` (strings from CSV) | 20.3 | `TypeError` ✗ |

One case passes out of six. The function solved the example, not the problem. The underlying reason: Aigerim's prompt said "may be missing" and the AI chose the narrowest meaning. She had not told it what missing looks like *in her data*.

## The second prompt

> The readings come from a CSV, so they may be strings. Missing values appear as an empty string, the string "N/A", or the number -999 (a sensor error code). Treat all of these as missing. If no valid readings remain, return None. Here are my test cases: [the table above as code]. Write the function so that all tests pass, and keep it readable.

## What came back

```python
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
    if value == SENSOR_ERROR:
        return None
    return float(value)


def daily_mean(readings):
    """Mean of the valid readings; None if there are none."""
    valid = [v for v in (to_reading(r) for r in readings) if v is not None]
    if not valid:
        return None
    return sum(valid) / len(valid)
```

All six tests pass. Aigerim read it line by line and asked about two things she did not understand (`isinstance`, and why `float(value)` is wrapped in `try`). She also noticed that the AI silently extended the set of missing markers (`"NA"`, `"nan"`, `"None"`) - reasonable, but a decision she should know about, since a real reading could never be the string `"None"` but a column of text could.

## One more check

A unit test proves the function does what the tests say. It does not prove the tests say the right thing. Aigerim ran the function on one real day of data and compared the result with the spreadsheet's `AVERAGE` of the same cells after removing the `-999` rows by hand: 21.84 in both. Now she trusted it for the other 364 days.

## What to take from this

- **"Works on the example" is the weakest possible evidence.** Edge cases are where AI code fails, and they are cheap to write down before you ask.
- **The AI chose the easy interpretation of a vague word.** "Missing" meant five different things in the data. Specifying them in the prompt was the real work.
- **Giving the tests to the AI turned a vague request into a specification.** The second answer was better mostly because the question was.
- **Read for silent decisions.** The expanded `MISSING` set was sensible, but unasked-for behaviour in code is how surprises get in.

## Try it

Ask an AI for a function that parses dates from a column of strings. Before running it, write six inputs: a normal date, two different formats, an empty string, a date with a typo, and a date in the future. Count how many it handles.
