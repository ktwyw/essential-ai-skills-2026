# Module 1: Clear Communication

> The quality of an AI's answer rarely exceeds the quality of the request.

## Learning goals

By the end of this module you will be able to:

- Explain why a prompt is a specification, not a search query.
- Write prompts that state the goal, context, constraints, and output format.
- Improve a weak prompt by diagnosing what it left unsaid.

## Key ideas

### A prompt is a brief

Think of an AI assistant as a capable colleague who knows nothing about your situation. Everything it needs must be in the request. "Write a summary" gets something generic. "Summarize this report in five sentences for a finance director deciding whether to renew the contract" gets something useful.

### The four ingredients of a good prompt

| Ingredient | Question it answers | Example |
|------------|--------------------|---------|
| **Goal** | What do you want and why? | "I need to decide whether to renew this contract." |
| **Context** | What does the AI need to know? | "We are a 40-person school; budget is tight this year." |
| **Constraints** | What are the limits? | "Under 150 words. Avoid jargon." |
| **Format** | What should the result look like? | "Three bullet points, then a one-line recommendation." |

### Show, don't only tell

One good example of the output you want often works better than a paragraph of description. If you can, include a sample, or a bad example labeled as one.

### Iterate deliberately

When an answer disappoints you, don't just click "retry". Ask yourself what you left unsaid, then rewrite the prompt so that a capable stranger could not misread it.

## Practice

1. **Before and after.** Take this weak prompt: *"Tell me about climate change."* Rewrite it three times for three audiences: a 12-year-old, a city council member, and a climate scientist. Compare the answers.
2. **The four ingredients.** Pick a real task you need to do this week. Write a prompt that includes all four ingredients from the table. Save the prompt and the answer in a Markdown file.
3. **Diagnose the gap.** Ask an AI to plan a one-day trip with no other details. Then list everything it had to guess. Rewrite the prompt to remove every guess.
4. **Example power.** Ask for a product description twice: once with a description of the style you want, once with a short example of that style. Which worked better?

## Common mistakes

- **Asking a question when you need a specification.** "Tell me about X" returns an encyclopaedia entry; "I need X in order to Y, for Z, under these limits, in this form" returns something you can use.
- **Leaving the AI to invent what you did not say.** Dates, names, attachments, relationships: anything not supplied will be guessed, and guesses read exactly like facts (worked example 1).
- **Describing style instead of showing it.** One example beats three adjectives.
- **Retrying instead of rewriting.** A new roll of the dice with the same prompt gives the same gaps.

## See also

- Worked example 1: [A prompt makeover](../examples/worked-examples/01-prompt-makeover.md)
- The [prompt library](../examples/prompts/README.md), one file per situation
- Templates: [prompt log](../templates/prompt-log.md) · Exercises 1.1-1.5 in the [exercise bank](../exercises/exercise-bank.md) · [Self-check quiz](../exercises/self-check-quizzes.md#module-1-clear-communication)

## Reflection

- Which of the four ingredients do you most often forget?
- How is writing a prompt similar to giving instructions to a person? How is it different?
- When was the last time a misunderstanding came from something you assumed was obvious?

## Key takeaway

Clear writing is the most important AI skill, and it is the same skill that makes you a better communicator with people.

---

[Course home](../README.md) · Next: [Module 2: Critical evaluation](02-critical-evaluation.md) →
