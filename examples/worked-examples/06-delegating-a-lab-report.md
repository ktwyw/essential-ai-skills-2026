# Worked example 6: Delegating a lab report

**Modules:** 4, 5, 6 · **Time:** 30 minutes

## The task

A heat-exchanger lab report is due in a week. The group has the data and a rubric: introduction and theory (15 %), method (10 %), results with figures (30 %), discussion (30 %), conclusion and references (15 %). The course policy allows AI assistance if disclosed.

## Step 1: decompose

The group listed the work and decided, for each task, whether to delegate it, do it themselves, or share it:

| # | Task | Who | Why |
|---|------|-----|-----|
| 1 | Clean the data (remove warm-up readings, convert units) | **Me** | I know which readings are warm-up; the AI does not |
| 2 | Write the analysis code (log-mean temperature difference, U-value) | **Both** | AI drafts, I give test cases and check one value by hand |
| 3 | Make the figures | **AI**, then me | AI writes the matplotlib; I decide what the figures should show |
| 4 | Theory section (what LMTD is, assumptions) | **Both** | AI drafts from *my* bullet points; I check against the textbook |
| 5 | Discussion of why U was lower than the manufacturer's value | **Me** | This is the thinking the course is assessing |
| 6 | Proof-read and tighten the prose | **AI** | High-volume, low-risk, easy to check |
| 7 | Format references | **AI** | Mechanical, but every reference checked (worked example 2) |
| 8 | Final read and sign-off | **Me** | Accountability (module 6) |

Note what stayed with the students: anything requiring knowledge only they had (task 1), anything the course is assessing (task 5), and the final decision (task 8). The AI got volume and formatting.

## Step 2: write a delegation brief

The brief for task 3, using the three parts from module 4 (outcome, context, check):

> **Outcome:** two publication-quality matplotlib figures saved as PNG at 200 dpi: (a) hot and cold outlet temperatures vs flow rate, with error bars from the three repeats; (b) overall heat-transfer coefficient U vs Reynolds number on log-log axes with the manufacturer's value as a horizontal dashed line.
>
> **Context:** data in `results.csv` with columns [listed]; Re and U are already computed in columns `Re` and `U_W_m2K`; the manufacturer's value is 850 W/m²K; axis labels must include units; use a colour-blind-safe palette; figure width 160 mm for a two-column report.
>
> **Check:** I will open both PNGs and compare three plotted points with the CSV by eye; the code must run from a clean folder with only `results.csv` present.

Compare with the prompt most people write: "make me a graph of my data". The brief took five minutes and produced usable figures on the first try, except that the AI chose a log axis for figure (a) too - which the "check" caught in seconds.

## Step 3: plan before doing

For task 4 (theory section), the group asked the AI for an outline first:

> Before writing, give me a five-bullet outline of a 300-word theory section on LMTD for a counter-flow heat exchanger, based on these notes: [bullets]. Do not write the section yet.

The outline put the assumptions last. The group moved them first (the discussion depends on them) and only then asked for prose. Correcting an outline costs seconds; correcting a finished section costs a rewrite.

## Step 4: responsible-use decisions

- The raw data contained the names of the group members in a header row. They removed the row before sharing the file (module 6: personal data).
- They used the university-licensed assistant, as the course policy required.
- The disclosure statement in the report, from [`templates/ai-disclosure.md`](../../templates/ai-disclosure.md):

> AI assistance (university Claude account, October 2026) was used to draft the analysis code and figure scripts, to draft the theory section from our outline, and to proof-read. All code was tested against hand calculations; all references were verified; the discussion and conclusions were written by the group. Prompts and checks are listed in PROCESS.md.

## What to take from this

- **Decomposition made the AI policy easy to follow.** Once the tasks were listed, it was obvious which ones the course was assessing and which were chores.
- **The brief's "check" clause** is what turned AI output into something the group could sign.
- **Plan first** cost one extra prompt and saved a rewrite.
- **The students did the thinking** (tasks 1, 5, 8) and spent the saved time on the discussion - the 30 % of the mark that AI could not earn for them.

## Try it

Take your next assignment and build the task table before you open an AI tool. Mark each row AI / me / both, and write one delegation brief with all three parts.
