# Module 2: Critical Evaluation

> AI output is fluent and confident whether it is right or wrong.

## Learning goals

By the end of this module you will be able to:

- Explain why polished AI output can still be wrong.
- Apply a simple verification routine to text, facts, and code.
- Decide how much checking a given task deserves.

## Key ideas

### Fluency is not accuracy

AI models produce text that sounds right. A polished paragraph can contain an invented statistic or a citation to a paper that does not exist. Working code can hide a bug that appears only on unusual inputs. Confidence of tone tells you nothing about correctness.

### A verification routine

| Output type | How to check it |
|-------------|-----------------|
| **Facts and figures** | Find the original source. If you cannot, treat it as unverified. |
| **Quotes and citations** | Open the source and confirm the words and the reference exist. |
| **Code** | Run it. Test normal cases, edge cases, and bad input. |
| **Reasoning** | Ask the AI to explain each step. Look for steps that do not follow. |
| **Calculations** | Recompute key numbers yourself or with a calculator or spreadsheet. |

### Match checking to stakes

A brainstorm for party themes needs little checking. A medical, legal, or financial claim needs a lot. Before you start, ask: *what happens if this is wrong?*

### Treat surprise as a signal

When an answer surprises you, that is exactly the moment to look closer. Sometimes the AI has found something new. Often it has made something up.

## Practice

1. **Source hunt.** Ask an AI for five statistics about a topic you care about, with sources. Try to verify every one. Record how many you could confirm, partly confirm, or not find.
2. **Bug hunt.** Ask an AI to write a function that calculates a student's average grade. Test it with an empty list, negative numbers, and text instead of numbers. What breaks?
3. **Explain yourself.** Ask an AI a multi-step reasoning question, such as a logic puzzle. Then ask it to explain each step. Find at least one step you would challenge.
4. **Two opinions.** Ask two different AI tools, or the same tool twice, the same factual question. Where do the answers differ? Which is right, and how do you know?

## Common mistakes

- **Checking the easy part.** Formatting, spelling and structure are where AI is strong; facts, references and edge cases are where it fails. Check the hard part first.
- **Asking the AI to verify itself in the same chat.** It will agree with what it just wrote (worked example 5). A fresh chat is weak evidence; an independent source is strong evidence.
- **Grading a reference from its title.** A DOI that resolves proves a paper exists, not that it says what the AI claimed (worked example 2).
- **"It runs" as proof.** A function that passes one example and fails on empty input is not finished (worked example 3).
- **Not deciding the stakes first.** Without "what happens if this is wrong?", checking is either skipped or done uniformly, and both waste time.

## See also

- Worked examples 2, 3 and 5: [fact-checking a summary](../examples/worked-examples/02-fact-checking-a-summary.md), [debugging AI code](../examples/worked-examples/03-debugging-ai-code.md), [checking a derivation](../examples/worked-examples/05-checking-a-derivation.md)
- Worked examples 10 and 12: [choosing a statistical test](../examples/worked-examples/10-choosing-a-statistical-test.md), [summarising a paper you have](../examples/worked-examples/12-summarising-a-paper-you-have.md)
- Scripts: [`check_citations.py`](../examples/python/check_citations.py), [`test_ai_function.py`](../examples/python/test_ai_function.py)
- Templates: [verification log](../templates/verification-log.md) · Exercises 2.1-2.6 · [Self-check quiz](../exercises/self-check-quizzes.md#module-2-critical-evaluation)

## Reflection

- What kinds of errors were hardest for you to spot?
- How did the verification exercise change how much you trust AI output?
- In your field, which mistakes would be most costly?

## Key takeaway

As generating content becomes cheap, the scarce skill is knowing which output is correct and which is good.

---

← Previous: [Module 1: Clear communication](01-clear-communication.md) · [Course home](../README.md) · Next: [Module 3: How AI behaves](03-how-ai-behaves.md) →
