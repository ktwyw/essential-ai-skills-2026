# Module 8: AI in Science and Engineering Work

> In technical work, the question is never "did the AI answer?" but "can I show the answer is right?"

## Learning goals

By the end of this module you will be able to:

- Use AI for derivations, problem sets, code, data analysis, lab reports, and literature work without being misled by it.
- Choose, for each kind of task, the check that catches the typical AI failure.
- Keep your own understanding growing while using AI in a technical course.
- Document AI use in a way that makes your work reproducible and honest.

## Key ideas

### The failure modes are different in technical work

In everyday writing, a wrong AI answer usually looks slightly off. In technical work it often looks *exactly* like a right one. The common failures are:

| Task | Typical AI failure | What catches it |
|------|-------------------|-----------------|
| Derivation | A sign, factor of 2, or unit dropped mid-way; a step that "follows" but does not | Check units and limiting cases; redo the suspect step by hand |
| Problem set | Correct method, wrong arithmetic; or a plausible method that does not apply | Recompute numbers with code; ask "what assumption does this method need?" |
| Code | Runs on the example, fails on edge cases; uses a library function that does not exist | Run it on edge cases; read the documentation for every unfamiliar call |
| Data analysis | Confident conclusions from a plot the AI never saw; silent dropping of missing data | Look at the raw data yourself first; ask for the exact steps and rerun them |
| Literature | Papers that do not exist, or exist but say something else | Resolve every DOI; open every source; never cite what you have not read |
| Explanations | Smooth but subtly wrong statements of a concept | Compare with the textbook; ask for the edge case where the explanation breaks |

### Units and limits: the two cheapest checks

Two habits catch most derivation and calculation errors in seconds:

1. **Dimensional check.** Every term in an equation must have the same units. An AI that writes `v = a·t²` has made an error you can see without redoing anything.
2. **Limiting cases.** Set a parameter to zero, infinity, or a value where you know the answer. A drag formula must give zero force at zero velocity; a solution for a heated rod must give a uniform temperature when the heating stops.

Ask the AI to do both checks itself, then redo them yourself. Agreement between the two is weak evidence; disagreement is strong evidence of an error.

### Make the AI compute, not recall

Language models are unreliable at arithmetic from memory but reliable when they run code. For any numerical answer that matters:

- Ask the AI to write and run the calculation (most assistants have a code tool), or
- Paste the calculation into Python yourself.

A number that was *recalled* ("the density of ethanol is about 0.79 g/cm³") is a claim to verify; a number that was *computed* from stated inputs is a calculation to check.

### Code: trust tests, not confidence

AI writes routine code quickly and well. It also, with the same confidence, calls functions that do not exist, mishandles empty inputs, and changes behaviour between runs. The discipline is the same as for human code:

- Ask for the function *and* a few test cases, including edge cases (empty input, zero, negative values, wrong type).
- Run the tests. A function with no tests is a draft.
- For anything scientific, check one output by hand or against a known case before trusting a thousand.

The worked example [Debugging AI-written code](../examples/worked-examples/03-debugging-ai-code.md) shows the whole routine; [`examples/python/test_ai_function.py`](../examples/python/test_ai_function.py) is a template.

### Data: look before you ask

AI cannot see your data unless you give it, and even then it sees a text copy of a slice. Before asking an AI to analyse a dataset:

1. Open the file. Count the rows and columns. Note missing values, units, and anything odd (a column of zeros, a date in the wrong century).
2. Give the AI the *schema and a sample*, not the whole file, plus the facts you noticed.
3. Ask for the analysis as code you can run, not as conclusions. Conclusions that you cannot reproduce are not results.

[`examples/python/data_explore.py`](../examples/python/data_explore.py) produces a one-page profile of a CSV to paste into a prompt.

### Literature: every reference is unverified until opened

Fabricated references remain one of the most common AI errors. They look perfect: real journal, plausible authors, correct formatting, a DOI with the right shape. The only check that works is to resolve the DOI or search the title and *open the paper*. [`examples/python/check_citations.py`](../examples/python/check_citations.py) checks a list of DOIs against the Crossref database in seconds; it tells you whether a DOI exists and what title it belongs to, not whether the paper says what the AI claims. That part is reading.

Good uses of AI in literature work:

- Explaining a paper you have (paste it, or share the file).
- Suggesting search terms and related concepts.
- Summarising *your* notes across several papers.

Poor uses: asking for "the key papers on X" without tools, or for a reference list.

### Learning versus producing

In a course, the output is rarely the point; the understanding is. The tutor-mode habits from module 5 matter most here:

- For a problem set, ask for a hint or a check of *your* solution, not the solution.
- For a derivation, ask the AI to review your steps and point to the first one that is wrong, without correcting it.
- For code, ask it to explain the error message and the concept, then fix the code yourself.
- After any AI-assisted problem, close the chat and redo the problem on paper. If you cannot, you have not learned it yet.

### Reproducibility and disclosure

Technical work is only as good as its reproducibility. When AI was involved, record:

- Which tool and version, and the date.
- The prompts that produced anything you kept (code, derivations, text).
- What you checked and how.

A short PROCESS section or file (template in [`templates/PROCESS.md`](../templates/PROCESS.md)) does this in ten minutes and is what a supervisor, reviewer, or future you needs.

## Worked examples for this module

[Units and property values](../examples/worked-examples/08-units-and-property-values.md) · [A correlation used outside its range](../examples/worked-examples/09-correlation-out-of-range.md) · [Choosing a statistical test](../examples/worked-examples/10-choosing-a-statistical-test.md) · [Summarising a paper you have](../examples/worked-examples/12-summarising-a-paper-you-have.md) · [An exam explanation that is subtly wrong](../examples/worked-examples/14-an-exam-explanation-that-is-subtly-wrong.md) · and, from earlier modules, [debugging AI code](../examples/worked-examples/03-debugging-ai-code.md), [AI-assisted data analysis](../examples/worked-examples/04-ai-assisted-data-analysis.md) and [checking a derivation](../examples/worked-examples/05-checking-a-derivation.md).

## Practice

1. **Dimensional detective.** Ask an AI to derive the period of a simple pendulum, the drag force on a sphere, or the time constant of an RC circuit, step by step. Check the units of every line. Then ask for the same derivation again in a fresh chat and compare.
2. **Compute, don't recall.** Ask an AI (without a code tool) for the result of a multi-step calculation from your field, such as the pressure drop in a pipe or the final temperature after mixing two liquids. Then ask it to write Python for the same calculation and run it. Compare the two answers.
3. **Edge cases.** Ask an AI for a function that converts a temperature reading between Celsius, Fahrenheit and Kelvin. Test it on 0 K, −300 °C, the string `"25"`, and a list. Write down what broke and fix it yourself.
4. **Reference check.** Ask an AI for five references on a topic in your field, with DOIs. Run `check_citations.py` on them. Open the ones that exist and check whether they support the claims the AI attached to them.
5. **Tutor-mode problem.** Solve one problem from your current course using only hints from the AI. Then ask it to grade your solution and point to the weakest step.

## Reflection

- Which check in the table above would have caught your most recent AI-related mistake?
- When the AI and you disagree about a calculation, how do you decide who is right?
- What would your instructor need to see to trust a result you produced with AI?

## Key takeaway

In technical work, AI is a fast but unreliable colleague: let it draft, compute, and explain, then apply the checks your field already has - units, limits, tests, sources - before you believe anything.

---

← Previous: [Module 7: The technical toolkit](07-technical-toolkit/README.md) · [Course home](../README.md) · Next: [Capstone project](../capstone/README.md) →
