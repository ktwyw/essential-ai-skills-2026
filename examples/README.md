# Examples

Starter code, data and worked examples for modules 7 and 8. Read every line of code before you run it.

## Worked examples (no setup needed)

Fourteen annotated case studies in [`worked-examples/`](worked-examples/README.md), from a prompt makeover and a summary with fabricated references to a coding agent that weakens tests, a statistical test chosen for the wrong design, and a bilingual glossary. Each shows the AI's output with its errors left in, and the routine that found them.

## Prompt library (no setup needed)

Reusable prompts in [`prompts/`](prompts/README.md), one file per situation: studying, writing, coding, data analysis, literature, and engineering problem solving. Each prompt is annotated with what it asks for and why.

## Scripts

Set up once:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r examples/requirements.txt
```

The first three scripts need no API key.

| Script | What it does | Needs |
|--------|-------------|-------|
| [`python/data_explore.py`](python/data_explore.py) | One-page profile of a CSV to paste into a prompt instead of the raw data (worked example 4) | pandas |
| [`python/check_citations.py`](python/check_citations.py) | Resolves DOIs through Crossref: FOUND with title and journal, or NOT FOUND (worked example 2) | requests, internet |
| [`python/test_ai_function.py`](python/test_ai_function.py) | Template for testing an AI-written function on edge cases before trusting it (worked example 3) | pytest |
| [`summarize.py`](summarize.py) | Your first AI API call: summarise a text file | anthropic, API key |
| [`python/compare_answers.py`](python/compare_answers.py) | Asks the same question in several fresh conversations and reports how the answers differ (module 3) | anthropic, API key |
| [`python/quiz_from_notes.py`](python/quiz_from_notes.py) | Tutor mode: turns your notes into a quiz with hidden answers (module 5) | anthropic, API key |

```bash
python examples/python/data_explore.py examples/data/packed_bed.csv
python examples/python/check_citations.py 10.1016/j.jpowsour.2005.01.006 10.1000/xyz123
pytest examples/python/test_ai_function.py
```

For the API scripts, set your key first and never put it in a file that is committed:

```bash
export ANTHROPIC_API_KEY="your-key-here"     # Windows PowerShell: $env:ANTHROPIC_API_KEY="your-key-here"
python examples/summarize.py my-notes.md
python examples/python/compare_answers.py "Which is denser at 20 C, ethanol or acetone?" --runs 5
python examples/python/quiz_from_notes.py my-notes.md --n 8
```

You need an API key from the Claude Console. API usage is paid, so set a spending limit. Check the [API documentation](https://docs.claude.com/en/api/overview) for current model names and pricing; the scripts read the model name from the `CLAUDE_MODEL` environment variable if you want to change it.

## Data

| File | Description | Used in |
|------|-------------|---------|
| [`data/packed_bed.csv`](data/packed_bed.csv) | Flow through a packed bed at four pressure drops on two days; one missing value, a temperature difference between days | worked example 4, module 8 exercises |
| [`python/injection_demo.txt`](python/injection_demo.txt) | Meeting notes with a hidden instruction, for the classroom demonstration of prompt injection | worked example 7 |

## `sql/library.sql`: a practice database

A small library database for the SQL exercises.

```bash
sqlite3 library.db < examples/sql/library.sql
sqlite3 library.db "SELECT title, year FROM books ORDER BY year;"
```
