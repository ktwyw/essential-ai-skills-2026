"""
compare_answers.py: ask the same question several times in fresh conversations and compare the answers.

Usage:
    python examples/python/compare_answers.py "What is the boiling point of ethanol at 1 atm, in Celsius?" --runs 5
    python examples/python/compare_answers.py --file prompt.md --runs 3

Module 3 says answers vary; this script shows how much, for your question and your model. It prints each
answer, then a crude agreement measure (the fraction of word pairs shared between answers) and any
numbers that differ between runs - the ones to verify.

Requires: pip install anthropic   and the ANTHROPIC_API_KEY environment variable.
Each run is one API call; set a spending limit in the console before using this on long prompts.
"""

import argparse
import itertools
import os
import re
import sys

import anthropic

DEFAULT_MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5-5")


def ask(client, prompt: str, model: str, temperature: float) -> str:
    response = client.messages.create(
        model=model,
        max_tokens=600,
        temperature=temperature,
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(block.text for block in response.content if getattr(block, "type", "") == "text")


def words(text: str) -> set[str]:
    return set(re.findall(r"[a-z]{3,}", text.lower()))


def numbers(text: str) -> set[str]:
    return set(re.findall(r"-?\d+(?:\.\d+)?", text))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt", nargs="?", help="the question")
    ap.add_argument("--file", help="read the prompt from a file instead")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--temperature", type=float, default=1.0, help="0 makes answers more repeatable, not more correct")
    args = ap.parse_args()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Set the ANTHROPIC_API_KEY environment variable first.")
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            prompt = f.read()
    elif args.prompt:
        prompt = args.prompt
    else:
        sys.exit("Give a prompt or --file.")

    client = anthropic.Anthropic()
    answers = []
    for k in range(args.runs):
        text = ask(client, prompt, args.model, args.temperature)
        answers.append(text)
        print(f"\n===== run {k + 1} =====\n{text.strip()}")

    if len(answers) > 1:
        sims = [len(words(a) & words(b)) / max(1, len(words(a) | words(b))) for a, b in itertools.combinations(answers, 2)]
        print(f"\nMean word overlap between runs: {sum(sims) / len(sims):.2f} (1 = identical wording, 0 = nothing shared)")
        all_numbers = [numbers(a) for a in answers]
        common = set.intersection(*all_numbers)
        differing = set.union(*all_numbers) - common
        if differing:
            print("Numbers that appear in some runs but not all (verify these):", ", ".join(sorted(differing)))
        else:
            print("All numbers agree across runs. Agreement is not correctness: still verify the important ones.")


if __name__ == "__main__":
    main()
