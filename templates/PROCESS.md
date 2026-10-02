# PROCESS.md: how this work was made

*Project:* [name] · *Author(s):* [names] · *Dates:* [start - end] · *AI tools:* [tool and version, e.g. "university Claude account, October 2026"; "GitHub Copilot in VS Code"]

## 1. Division of labour (module 4)

| Task | Who (AI / me / both) | Why |
|------|---------------------|-----|
| [e.g. clean the raw data] | me | only I know which runs were warm-up |
| [e.g. analysis code] | both | AI drafted, I supplied test cases and checked one value by hand |
| [e.g. discussion] | me | the assessed reasoning |
| [...] | | |

## 2. Prompts that produced something I kept (module 1)

Three or more, with the improvement they went through. Full prompt log in [prompt-log.md](prompt-log.md) if long.

**Prompt A** - purpose: [what for]
- First version: [text]
- Problem with the output: [what was missing, wrong, or guessed]
- Improved version: [text]
- What changed in the output: [specific]

**Prompt B** - ...

**Prompt C** - ...

## 3. Errors caught and how (module 2)

At least three. "None found" needs a description of what was checked.

| What the AI produced | What was wrong | How I found it | What I did |
|---------------------|----------------|----------------|------------|
| [e.g. reference 3 with DOI] | DOI did not resolve; paper exists in a different journal | check_citations.py, then search | replaced with the real citation after reading it |
| [e.g. daily_mean function] | crashed on empty input | my test table | gave the tests to the AI; second version passes |
| [e.g. derivation step 4] | sign dropped | limiting case (compression must heat) | corrected by hand |

## 4. Verification of the final result (module 8)

- [ ] Every number in the report comes from code or a cited source I opened.
- [ ] One result checked by hand: [which, and the two values].
- [ ] Units checked on [equations]. Limiting case checked: [which].
- [ ] All references resolve and were read.
- [ ] Code runs from a clean folder; tests: [how many, all pass?].

## 5. Privacy and security decisions (module 6)

- Data shared with AI tools: [what, and what was removed or anonymised first]
- Tools and accounts used: [and whether they comply with the course / institution policy]
- Permissions granted to any agent: [folders, services]

## 6. Disclosure statement

[Paste the statement from ai-disclosure.md that appears in the submitted work.]

## 7. Reflection (300-500 words for the capstone)

What I learned; what I would do differently; where AI helped most and least; what I kept doing myself and why.
