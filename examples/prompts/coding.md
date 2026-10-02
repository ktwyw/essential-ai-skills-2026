# Prompts for coding

The theme of every prompt here: get something you can **test**, and understand what you keep (module 7, module 8, worked example 3).

## A function with tests

```
Write a Python function `[name](...)` that [what it does].
Inputs: [types, ranges, how missing or invalid values look]. Output: [type, and what to return when there is no valid answer].
Here are test cases it must pass: [table or asserts, including edge cases: empty input, zero, negative, wrong type].
Return: the function with a docstring, then the tests as pytest functions. Use only the standard library and [allowed packages]. Keep it readable over clever.
```

*Why:* writing the test cases first is the real specification. Template: [`test_ai_function.py`](../python/test_ai_function.py).

## Explain this error

```
This code [paste] produced this error [paste full traceback]. Explain what the error means and which line causes it, and what concept I should understand to avoid it. Do not fix the code; I will.
```

## Review my code

```
Review this code for [correctness / readability / performance], in that order: [paste]. It is meant to [purpose] and is run [how often, on what size of data].
List issues with line numbers and severity (bug / risk / style). For bugs, give an input that triggers them. Do not rewrite the whole thing.
```

## Script for a chore

```
Write a Python script that [task, e.g. renames every .JPG file in a folder to lowercase .jpg and reports what it renamed]. It must: do a dry run by default and only act with a --apply flag; never overwrite an existing file; print what it would do. Folder path comes from the command line.
```

*Why the dry run:* an AI-written script that acts immediately on your files is a script you cannot test safely.

## Explain code line by line

```
Explain this code to me line by line, assuming I know basic Python but not [library]: [paste]. For each library call, say what it does and link the documentation page.
```

*Check:* open two of the documentation links. Fabricated functions are common.

## Refactor without changing behaviour

```
Refactor this function to be clearer without changing what it returns for any input: [paste]. Keep the same name and signature. Then write three tests that would fail if the behaviour had changed.
```

## From pseudocode to code

```
Here is my algorithm in pseudocode: [paste]. Implement it in Python exactly as written, without "improving" it. If a step is ambiguous, ask me before guessing. Add a comment on each line that maps to a pseudocode step.
```

## When the AI uses a function you do not recognise

Ask: "Is `library.function_name` a real function in version [x]? Link the documentation." If it cannot link it, assume it does not exist.
