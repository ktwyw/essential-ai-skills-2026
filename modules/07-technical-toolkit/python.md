# Python

## Why it matters

Python is the main language of AI, data science, and automation. You do not need to become a software engineer. The goal is to read, run, and debug code well enough to understand and judge what AI writes for you.

## Learn first

1. Variables, data types, and printing output
2. Lists and dictionaries
3. `if` statements and `for` loops
4. Functions
5. Reading and writing files
6. Installing and importing packages (`pip install`)
7. Then: `pandas` for data and `requests` for web services

## Tips for becoming proficient

- **Automate one real chore**, such as renaming files or cleaning a spreadsheet, rather than following only abstract exercises.
- **Read AI-written code line by line.** Ask the AI to explain anything you don't understand.
- **Type code yourself at first** instead of pasting. The friction builds memory.
- **Learn to read error messages.** Read the last line first, then find the line number. Debugging is where real understanding forms.
- **Use virtual environments** (`python -m venv .venv`) to keep each project's packages separate.

## Practice

1. Write a script that asks for your name and age and prints how old you will be in 2030.
2. Write a function that takes a list of grades and returns the average, highest, and lowest. Handle an empty list without crashing.
3. Use `pandas` to load a CSV file, then print the average of one column.
4. Ask an AI to write a script for a task, then deliberately break it and fix it yourself.

## Resources

- Official tutorial: https://docs.python.org/3/tutorial/
- Examples in this repo: [`examples/summarize.py`](../../examples/summarize.py) (an API call), [`examples/python/data_explore.py`](../../examples/python/data_explore.py) (pandas), [`examples/python/test_ai_function.py`](../../examples/python/test_ai_function.py) (pytest), [`examples/python/check_citations.py`](../../examples/python/check_citations.py) (requests)
- Worked example 3: [Debugging AI-written code](../../examples/worked-examples/03-debugging-ai-code.md)
