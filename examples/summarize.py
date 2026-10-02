"""
summarize.py: summarize a text file with the Claude API.

Usage:
    python examples/summarize.py path/to/file.md

Requires:
    pip install anthropic
    The ANTHROPIC_API_KEY environment variable set to your API key.

Optional:
    CLAUDE_MODEL environment variable to choose a model.
    See https://docs.claude.com/en/api/overview for current model names.
"""

import os
import sys

import anthropic

DEFAULT_MODEL = "claude-sonnet-5-5"


def read_file(path: str) -> str:
    """Return the contents of a text file, or exit with a clear message."""
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        sys.exit(f"File not found: {path}")


def summarize(text: str, model: str) -> str:
    """Send the text to Claude and return a short summary."""
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY automatically

    # A clear prompt: goal, audience, constraints, and format (see module 1).
    prompt = (
        "Summarize the document below for a busy student.\n"
        "Constraints: at most five bullet points, plain language, "
        "no information that is not in the document.\n"
        "Format: a one-line title, then the bullet points.\n\n"
        f"<document>\n{text}\n</document>"
    )

    response = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Usage: python examples/summarize.py path/to/file")

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Please set the ANTHROPIC_API_KEY environment variable first.")

    text = read_file(sys.argv[1])
    model = os.environ.get("CLAUDE_MODEL", DEFAULT_MODEL)
    print(summarize(text, model))

    # Module 2 reminder: check the summary against the original!


if __name__ == "__main__":
    main()
