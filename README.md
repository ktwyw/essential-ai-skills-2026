# Essential Skills for AI Proficiency in 2026

A practical, open course on the skills that matter most for working well with AI, for students, educators, and professionals.

> **Core idea:** AI proficiency is less about which tools you know and more about how you work with AI. Tools change every year. The ability to specify clearly, delegate wisely, and judge critically does not.

## Who this is for

This course is for anyone who wants to use AI effectively and responsibly. Modules 1 to 6 need no technical background. Module 7 introduces the technical toolkit for students who want to build things with AI, and module 8 applies the whole course to technical study and research - problem sets, lab reports, code, data and literature - where AI's mistakes look exactly like correct answers and the checks that catch them are the ones your field already has.

## Course map

| # | Module | Focus | Technical? |
|---|--------|-------|------------|
| 1 | [Clear communication](modules/01-clear-communication.md) | Prompting as precise specification | No |
| 2 | [Critical evaluation](modules/02-critical-evaluation.md) | Judging whether AI output is correct and good | No |
| 3 | [How AI behaves](modules/03-how-ai-behaves.md) | A practical mental model of strengths and limits | No |
| 4 | [Decomposition and delegation](modules/04-decomposition-and-delegation.md) | Breaking work into tasks AI can carry out | No |
| 5 | [Domain expertise](modules/05-domain-expertise.md) | Why knowing your field makes AI more useful | No |
| 6 | [Responsible use](modules/06-responsible-use.md) | Privacy, security, and accountability | No |
| 7 | [The technical toolkit](modules/07-technical-toolkit/README.md) | Python, command line, Git, Markdown, SQL, APIs, LaTeX | Yes |
| 8 | [AI in science and engineering work](modules/08-ai-for-study-and-research.md) | Derivations, calculations, code, data, literature - and the checks that catch AI's mistakes in each | Partly |
| ★ | [Capstone project](capstone/README.md) | Bring everything together in one real project | Mixed |

## Beyond the modules

| Resource | What it is |
|----------|-----------|
| [Worked examples](examples/worked-examples/README.md) | Fourteen annotated case studies: a prompt makeover, a summary with fabricated references, AI code that fails on real inputs, a data analysis done wrong and then right, a derivation with a sign error, delegating a lab report, a prompt injection, stale property values, a correlation out of its range, the wrong statistical test, a coding agent that weakens the tests, a paper summary with transposed numbers, a bilingual glossary, and an exam explanation that is subtly wrong. The AI's errors are left in; the routines that found them are shown. |
| [Prompt library](examples/prompts/README.md) | Reusable, annotated prompts for studying, writing, coding, data analysis, literature and engineering problem solving |
| [Exercise bank](exercises/exercise-bank.md) | Forty graded exercises with deliverables and marking points, plus [self-check quizzes](exercises/self-check-quizzes.md) and [instructor notes](exercises/instructor-notes.md) |
| [Templates](templates/README.md) | PROCESS.md, AI disclosure statement, prompt log, verification log, delegation brief |
| [Scripts and data](examples/README.md) | A CSV profiler, a DOI checker, a test template for AI-written code, a variability measurement, a quiz generator, and a lab dataset with the faults real data have |
| [Glossary](glossary.md) · [FAQ](faq.md) | Plain-language definitions; the questions students ask in week one |
| [Capstone ideas](capstone/project-ideas.md) · [Sample PROCESS.md](capstone/examples/sample-PROCESS.md) | Thirty projects by field, and a complete example of the process record |

## How to use this course

**Students:** work through the modules in order. Each one has learning goals, key ideas, hands-on practice, common mistakes, and reflection questions. Read the worked example linked from each module before the practice, do the practice with a real AI assistant, check yourself with the quiz, and keep your notes in Markdown using the templates.

**Instructors:** see the [Teaching Guide](TEACHING-GUIDE.md) for a suggested 8-week schedule, discussion prompts, and assessment ideas.

**Everyone:** a curated list of learning links is in [resources.md](resources.md).

## Suggested learning path

1. Start with **clear communication** and **Markdown**. Both pay off immediately and need no setup.
2. Work through modules **2 to 6** to build judgment and good habits.
3. Learn **Python** and the **command line** together, then add **Git and GitHub**.
4. Add **SQL**, **APIs**, and **data formats** when you start building projects.
5. Learn **LaTeX or Typst** only if your field calls for it.
6. If you are in a technical degree, work through **module 8** alongside your current courses: its exercises use your own problem sets and lab data.
7. Finish with the **capstone project**.

## Repository structure

```
essential-ai-skills-2026/
├── README.md                  ← you are here
├── TEACHING-GUIDE.md          ← for instructors: schedules, grading, integrity
├── glossary.md · faq.md       ← definitions; first-week questions
├── resources.md               ← curated links
├── modules/                   ← the six core skills, the toolkit, AI in technical work
│   └── 07-technical-toolkit/  ← one guide per tool
├── examples/
│   ├── worked-examples/       ← fourteen annotated case studies
│   ├── prompts/               ← the prompt library
│   ├── python/                ← scripts (profiler, DOI checker, test template, ...)
│   ├── data/                  ← a lab dataset with realistic faults
│   └── sql/                   ← the practice database
├── exercises/                 ← exercise bank, self-check quizzes, instructor notes
├── templates/                 ← PROCESS.md, disclosure, logs, delegation brief
└── capstone/                  ← brief, rubric, thirty ideas, a sample process record
```

## Contributing

Corrections, new exercises, and translations are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Version

Version 1.1, October 2026 (see [CHANGELOG.md](CHANGELOG.md)). AI tools change quickly; see the [Teaching Guide](TEACHING-GUIDE.md) for how to keep the course current.

## License

Course text is shared under [CC BY 4.0](LICENSE.md); example code under the MIT License. You may reuse and adapt it with attribution.
