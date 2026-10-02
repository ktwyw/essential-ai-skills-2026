# Module 3: How AI Behaves

> You don't need the mathematics. You need a working mental model.

## Learning goals

By the end of this module you will be able to:

- Explain hallucination, context windows, and variability in plain words.
- Predict which tasks AI will handle well and which it will struggle with.
- Use this model to choose better tasks and better prompts.

## Key ideas

### Language models generate plausible text

A large language model predicts likely continuations of text, based on patterns learned from enormous amounts of writing. This is why it is so good with language, and also why it can state false things smoothly. When it produces confident but untrue content, we call it **hallucination**.

### The context window

A model can only consider a limited amount of text at once, called its **context window**. What you include in the conversation (documents, examples, earlier messages) shapes the answer. What you leave out, it cannot know, unless it has tools such as search.

### Answers vary

The same prompt can give different answers on different runs. One good answer does not prove the model is reliable for that task. Test important uses several times.

### Strengths and weaknesses

| Usually strong | Less reliable without tools |
|----------------|-----------------------------|
| Drafting and rewriting | Precise facts and figures |
| Summarizing and explaining | Very recent events |
| Translating | Exact arithmetic and counting |
| Writing routine code | Niche or local knowledge |
| Brainstorming options | Anything it cannot see in its context |

Modern AI assistants often have **tools** such as web search, code execution, and file access. These cover many of the weaknesses: a model that runs code can calculate exactly, and one that searches can find recent information. Knowing whether a tool was used helps you judge the answer.

## Practice

1. **Find the edge.** Ask an AI to count the letters in a long word, multiply two large numbers, and summarize a paragraph. Which were reliable? If it has a code tool, ask it to use it and compare.
2. **Context matters.** Ask a question about a document without sharing it. Then share it and ask again. Describe the difference.
3. **Variability test.** Ask the same open question three times in fresh conversations. How consistent were the answers? What changed?
4. **Recent events.** Ask about something that happened this month. Did the AI search, say it didn't know, or answer from memory? How can you tell?

## Common mistakes

- **Treating one good answer as a guarantee.** The next run may differ; important uses should be tested several times ([`compare_answers.py`](../examples/python/compare_answers.py)).
- **Expecting the model to know what you did not give it.** It cannot see your file, your course or last week's news unless it has them in the context or a tool to fetch them - and it will answer anyway.
- **Confusing lower temperature with higher accuracy.** A repeatable wrong answer is still wrong.
- **Not noticing whether a tool was used.** An answer with a visible search or code step rests on different ground from one recalled from training.

## See also

- The [glossary](../glossary.md) for context window, token, temperature, tool use, hallucination
- Exercises 3.1-3.5 · [Self-check quiz](../exercises/self-check-quizzes.md#module-3-how-ai-behaves)

## Reflection

- Which result in the practice surprised you most?
- How would you explain hallucination to a friend who has never used AI?
- Given the strengths table, which of your own tasks are good candidates for AI?

## Key takeaway

With a working mental model, most AI failures become predictable, and predictable failures can be avoided.

---

← Previous: [Module 2: Critical evaluation](02-critical-evaluation.md) · [Course home](../README.md) · Next: [Module 4: Decomposition and delegation](04-decomposition-and-delegation.md) →
