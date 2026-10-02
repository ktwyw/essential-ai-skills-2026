# Examples

Starter code for module 7. Read every line before you run it.

## `summarize.py`: your first AI API call

Summarizes a text file using the Claude API.

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install the dependency
pip install -r examples/requirements.txt

# 3. Set your API key (never put it in the code or commit it)
export ANTHROPIC_API_KEY="your-key-here"     # Windows PowerShell: $env:ANTHROPIC_API_KEY="your-key-here"

# 4. Run it
python examples/summarize.py my-notes.md
```

You need an API key from the Claude Console. API usage is paid, so set a spending limit. Check the [API documentation](https://docs.claude.com/en/api/overview) for current model names and pricing.

## `sql/library.sql`: a practice database

A small library database for the SQL exercises.

```bash
sqlite3 library.db < examples/sql/library.sql
sqlite3 library.db "SELECT title, year FROM books ORDER BY year;"
```
