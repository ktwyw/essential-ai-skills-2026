"""
quiz_from_notes.py: tutor mode (module 5): turn your own notes into a quiz, then grade yourself.

Usage:
    python examples/python/quiz_from_notes.py my-notes.md            # writes my-notes-quiz.md
    python examples/python/quiz_from_notes.py my-notes.md --n 8

The script asks the model for n questions of mixed difficulty, each with a model answer and the line of
your notes it was based on. Questions are written to a Markdown file with the answers hidden in collapsible
blocks. Before you use a question, check its answer against your notes: the model can misread them
(module 2), and a quiz with a wrong answer teaches the wrong thing.

Requires: pip install anthropic   and the ANTHROPIC_API_KEY environment variable.
"""

import argparse
import os
import sys
from pathlib import Path

import anthropic

DEFAULT_MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5-5")

PROMPT = """You are helping a student revise from their own notes. Write {n} quiz questions based ONLY on the notes below.
Mix recall, understanding and application questions. For each question give:
- the question
- a concise model answer
- the exact phrase from the notes it is based on, quoted

Use this Markdown format for every question and nothing else:

### Q{{k}}. <question>
<details><summary>Answer</summary>

<model answer>

*Based on:* "<quoted phrase>"
</details>

<notes>
{notes}
</notes>"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("notes")
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    args = ap.parse_args()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Set the ANTHROPIC_API_KEY environment variable first.")
    path = Path(args.notes)
    notes = path.read_text(encoding="utf-8")
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=args.model,
        max_tokens=2000,
        messages=[{"role": "user", "content": PROMPT.format(n=args.n, notes=notes)}],
    )
    quiz = "".join(b.text for b in response.content if getattr(b, "type", "") == "text")
    out = path.with_name(path.stem + "-quiz.md")
    out.write_text(f"# Quiz from {path.name}\n\nCheck each answer against your notes before trusting it.\n\n{quiz}\n", encoding="utf-8")
    print(f"Wrote {out} with {quiz.count('### Q')} questions. Open it, hide the answers, and try them.")


if __name__ == "__main__":
    main()
