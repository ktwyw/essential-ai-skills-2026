# Prompt library

Reusable prompts for the situations students meet most often. Each one is built from the four ingredients of module 1 (goal, context, constraints, format) and most add a *check* clause from module 4. Copy, fill in the brackets, and keep the ones that work for you in your own notes.

Two rules for all of them:

- **Replace every bracket.** A bracket left in is a guess the AI will make for you.
- **The output is a draft until you have checked it** (module 2). The prompts that ask the AI to show its sources, steps or tests exist so that checking is possible.

| File | Situations |
|------|-----------|
| [study.md](study.md) | Tutor mode: explanations at your level, hints not answers, quizzes, checking your own work |
| [writing.md](writing.md) | Emails, reports, abstracts, feedback on drafts, editing without rewriting |
| [coding.md](coding.md) | Functions with tests, explaining errors, code review, refactoring, scripts for chores |
| [data-analysis.md](data-analysis.md) | From a data profile to reproducible analysis code and figures |
| [literature.md](literature.md) | Understanding a paper you have, search terms, summarising your notes, checking claims |
| [engineering.md](engineering.md) | Derivations with unit checks, calculations as code, design calculations, safety |

## The anatomy of a good prompt, once more

```
Goal        I need to [decide / produce / understand] ... because ...
Context     Here is what you need to know: [audience, situation, data, examples, what I have tried]
Constraints [length, tone, what to avoid, what must be included, what you must not assume]
Format      [bullets / table / code block / Markdown with these headings]
Check       Show [sources / steps / tests / assumptions] so that I can verify the result.
```

Not every prompt needs every line. Every prompt needs the lines you would otherwise have left to chance.
