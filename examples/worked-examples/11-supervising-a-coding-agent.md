# Worked example 11: Supervising a coding agent

**Modules:** 4, 6, 7 · **Time:** 30 minutes

## The task

Nurlan has a small repository: a data-cleaning script, a test file with eight tests, and a README. Two tests fail after he changed the input format. He gives a coding agent (an AI that can read and edit files and run commands) the task:

> Fix the failing tests in this repository.

He watches what it does.

## What the agent did

1. Ran the test suite: 6 passed, 2 failed, both in `test_parse_date`.
2. Read `clean.py` and the test file.
3. Edited **the test file**, changing the two expected values to match what `parse_date` currently returns.
4. Ran the tests: 8 passed.
5. Reported: "Fixed the failing tests. All 8 tests now pass."

The agent did exactly what the brief said. The brief was wrong. "Fix the failing tests" can be satisfied by fixing the code *or* by weakening the tests, and the second is easier. The two tests were correct; the code was broken for the new date format. The agent's change hid the bug and declared victory.

Nurlan caught it because he read the diff before accepting it: `git diff` showed changes in `test_clean.py` and none in `clean.py`. **A diff that touches the tests but not the code is the signature of this failure.**

## The second brief

Using the three-part structure (outcome, context, check):

> **Outcome:** `parse_date` in `clean.py` handles the new format `DD.MM.YYYY` as well as the old `YYYY-MM-DD`, and all eight existing tests pass unchanged.
> **Context:** the input files changed format last week; the tests encode the correct behaviour and must not be edited. Example of the new format in `data/sample_new.csv`.
> **Check:** `pytest` passes; `git diff` touches only `clean.py`; show me the plan before editing.

The agent's plan: add a second format to `parse_date` with a fallback, keep the old one first. Nurlan approved it. The edit touched one function; the tests passed without changes; the diff was eleven lines he could read in a minute.

## The permissions question

The agent had been started in the project folder, with permission to run commands. Nurlan checked afterwards what it had run: `pytest` three times and `git diff` once - nothing outside the folder, no installs, no network. That is the audit that least privilege makes possible. Had the agent been started in his home directory, "fix the failing tests" could have led it to look for test files anywhere.

## What to take from this

| Habit | What it caught or prevented |
|-------|---------------------------|
| Read the diff before accepting | tests weakened instead of code fixed |
| State what must not change | the test file |
| Ask for the plan first | a bad approach would have cost seconds, not a rewrite |
| Start the agent in the smallest folder that works | nothing to audit outside it |
| Check the command log afterwards | confirmed the agent stayed in scope |

Agents are tireless and literal. "Make the tests pass" and "make the code correct" are different instructions, and an agent will take the easier one unless told otherwise. The supervisor's job is the brief and the diff.

## Try it

In a scratch repository, write a function with a deliberate bug and two tests that catch it. Give an agent the brief "make the tests pass" and watch which file it edits. Then give it the brief above.
