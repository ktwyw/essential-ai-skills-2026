# Teaching Guide

Notes for instructors using this course. Adapt freely to your students' level and your institution's AI policy.

## Course design principles

- **Skills over tools.** Tools will change during the course itself. Emphasize communication, judgment, and responsibility.
- **Learning by doing.** Every module includes hands-on practice with a real AI assistant.
- **AI as tutor.** Encourage students to use AI to deepen understanding, not to skip it (see module 5).
- **Honesty and transparency.** Students should document how they use AI, and you should model the same.

## Suggested 8-week schedule

| Week | Topic | In class | Homework |
|------|-------|----------|----------|
| 1 | Module 1: Clear communication | Prompt makeover competition | Practice tasks 1 to 3; start a Markdown notes file |
| 2 | Module 2: Critical evaluation | Live fact-check of AI-generated statistics | Source hunt exercise |
| 3 | Module 3: How AI behaves | Find the edge: group experiments | Variability test; write an explanation of hallucination |
| 4 | Module 4: Decomposition and delegation | Plan a group project with AI | Delegation brief exercise |
| 5 | Modules 5 and 6: Expertise and responsible use | Debate: where is the line between help and dishonesty? | Traffic-light data exercise; disclosure statement |
| 6 | Module 7: Markdown, command line, Git | Lab: set up VS Code, fork and clone this repo | Push first notes to GitHub |
| 7 | Module 7: Python, APIs, SQL | Lab: run `summarize.py` and the SQL exercises | Capstone proposal |
| 8 | Capstone presentations | Presentations and peer review | Final reflection |

For a non-technical group, replace weeks 6 and 7 with Markdown only plus an extended non-technical capstone.

## A 12-week schedule for engineering and science students

Adds module 8, the worked examples, and more time for the technical toolkit. Each week pairs a module with one worked example (read before class) and one or two exercises from the [exercise bank](exercises/exercise-bank.md) (handed in).

| Week | Topic | Read before class | In class | Hand in |
|------|-------|-------------------|----------|---------|
| 1 | Module 1 | Worked example 1 | Prompt makeover in pairs on a real email | 1.2 Fabrication hunt |
| 2 | Module 2 | Worked example 2 | Live reference check with `check_citations.py` | 2.2 Reference check |
| 3 | Module 2 continued; Markdown | Worked examples 3 and 12 | Bug hunt: write the tests, then ask | 2.3 Bug hunt, in Markdown |
| 4 | Module 3 | Glossary | Find the edge; variability with `compare_answers.py` | 3.1 and 3.2 |
| 5 | Module 4 | Worked examples 6 and 11 | Decompose a current assignment; write briefs | 4.1 and 4.2 |
| 6 | Module 5 | Worked examples 13 and 14 | Tutor-mode problem session on the week's problem set | 5.2 (first half) |
| 7 | Module 6 | Worked example 7 | Injection demonstration; traffic lights; policy | 6.1 and 6.5 |
| 8 | Module 7: command line, Git | - | Lab: fork, clone, commit, push | 7.1 |
| 9 | Module 7: Python, data | Worked example 4 | Lab: profile and analyse `packed_bed.csv` | 7.3 and 8.3 |
| 10 | Module 8 | Worked examples 5, 8 and 9 | Dimensional detective on this week's derivations; compute vs recall | 8.1 and 8.2; capstone proposal |
| 11 | Capstone work | Sample PROCESS.md | Peer review of PROCESS drafts | 5.2 (second half) |
| 12 | Capstone presentations | - | Presentations, oral check-ins | Capstone and reflection |

## Grading

- **Weighting that has worked:** exercises 40 % (best eight of those set), capstone 40 %, oral check-in 10 %, participation in class experiments 10 %.
- **Grade the process, not the output.** The exercise bank's marking points and the capstone rubric reward specific verification, honest reporting of AI errors, and a defensible division of labour. A polished output with no evidence of checking is a *Developing*, not an *Excellent*.
- **Oral check-ins** (five minutes per student, "walk me through this prompt and what you checked") are the most reliable signal and take less time than reading a long report closely.
- **Use the instructor notes.** [exercises/instructor-notes.md](exercises/instructor-notes.md) lists what strong and weak answers look like for each exercise and the traps students fall into.

## Academic integrity in an AI-permitted course

The course position: AI use is permitted and must be disclosed; the student is accountable for the result; the thinking that the course assesses stays with the student. Practical measures that make this workable:

- State in the syllabus which uses are permitted for each assessment type, using the module 5 assistant/tutor distinction.
- Require the [disclosure statement](templates/ai-disclosure.md) on every submission, and a PROCESS.md on larger ones. Grade them.
- Prefer assessments with a process record and an oral component over detection tools, which are unreliable and adversarial.
- Model the practice: disclose your own AI use in preparing materials.

## Keeping the examples current

The worked examples reconstruct typical AI behaviour; tools improve and the specific errors shift. Each term, run the demonstrations yourself (the DOI check, the bug hunt, the derivation) and update the examples with what current tools do. Students enjoy finding that an example is out of date; that is critical evaluation in practice, and a pull request from a student is a good capstone component.

## Discussion prompts

- If AI can write an essay in seconds, what is the purpose of learning to write?
- Who is responsible when AI-assisted work contains an error?
- Which jobs will change most because of AI, and which skills will protect people in those jobs?
- Should students be required to disclose AI use? In which situations?
- How might AI affect learning differently for beginners and experts?

## Assessment ideas

- **Prompt portfolio:** students submit before-and-after versions of prompts with explanations.
- **Verification log:** students record AI errors they caught and how they confirmed them.
- **Capstone project:** see the rubric in [capstone/README.md](capstone/README.md).
- **Oral check-ins:** short conversations where students explain their work in their own words, a reliable way to confirm understanding.

## Practical setup

- Confirm which AI tools students may use under your institution's policy, and whether accounts are provided.
- Remind students not to share personal data about classmates or others with AI tools.
- For the Python API exercise, decide whether students use their own API keys or a shared class account with a spending limit. Never share keys in the repository.
- Ask students to **fork** this repository, so each has their own copy to commit to; the templates and exercise deliverables are designed to live there.
- The scripts in `examples/python/` that need no API key (`data_explore.py`, `check_citations.py`, `test_ai_function.py`) can be used in a lab with no accounts at all.

## Keeping the course current

AI changes quickly. Review the course each term: check that links work, that the examples run, and that the "strengths and weaknesses" table in module 3 still matches what students see. Invite students to submit improvements as pull requests; this is itself practice in Git and critical evaluation.
