# Exercise bank

Forty exercises, numbered by module. Each gives the task, the deliverable, and the marking points an instructor will look for. Difficulty: ★ 20-30 min · ★★ about an hour · ★★★ several hours.

## Module 1: Clear communication

**1.1 The anatomy ★** Take any three prompts you have written in the past month. For each, label which of goal, context, constraints and format were present. Rewrite the weakest one with all four. *Deliverable:* a table of the three prompts, the rewrite, and the before/after outputs. *Marking:* correct labelling; the rewrite removes identifiable guesses; the student names what the output changed.

**1.2 Fabrication hunt ★** Ask an AI to write a message for a real situation of yours with minimal context. List every statement in the output that you did not supply. *Deliverable:* the prompt, the output, the list, and a corrected prompt that prevents the fabrications. *Marking:* completeness of the list (students usually miss inferred dates and invented attachments).

**1.3 Audience shift ★** Rewrite one explanation of a concept from your course for three audiences (a 12-year-old, a classmate from another faculty, your professor). *Deliverable:* three prompts and outputs, plus 100 words on what changed and what the AI got wrong for the expert audience. *Marking:* the student noticed at least one error or oversimplification in the expert version.

**1.4 One example beats a paragraph ★★** Ask for a product or lab-safety notice in a specific style twice: once describing the style in words, once giving one short example. *Deliverable:* both prompts, both outputs, a judgement of which worked and why. *Marking:* a specific comparison, not "the second was better".

**1.5 The specification ★★** Write a prompt, using the [prompt library](../examples/prompts/README.md) template, for a task you will actually do this week. Run it. Then write the version you would give a human colleague. *Deliverable:* both versions and a paragraph on the differences. *Marking:* the student identifies what a human would know that the AI needed telling.

## Module 2: Critical evaluation

**2.1 Statistics audit ★★** Ask an AI (without web search) for five statistics about a topic in your field, with sources. Verify each. *Deliverable:* a [verification log](../templates/verification-log.md) with a status per statistic (confirmed / partly / not found / wrong) and the evidence. *Marking:* genuine source checking; the student distinguishes "not found" from "wrong".

**2.2 Reference check ★★** Ask for five references with DOIs on a topic you know. Run [`check_citations.py`](../examples/python/check_citations.py). Open every DOI that resolves and check that the paper supports the claim attached to it. *Deliverable:* the script output and a table: reference, resolves?, title matches?, supports claim?. *Marking:* the last column is filled from reading, not from the title.

**2.3 Bug hunt ★★** Ask for a function that converts a column of mixed temperature strings ("25 C", "77F", "298 K", "n/a") to Kelvin. Test it on ten inputs you write first. *Deliverable:* the test table, the first function, what failed, your corrected prompt, the second function. *Marking:* tests written before the code; failures diagnosed, not just listed.

**2.4 Challenge a step ★** Ask a multi-step reasoning question (a logic puzzle or a short proof). Ask the AI to explain each step. Find one step you would challenge and say why. *Deliverable:* the exchange and your challenge. *Marking:* the challenge is specific and reasoned, whether or not the AI was wrong.

**2.5 Two opinions ★** Ask two tools (or one tool twice in fresh chats) the same factual question with a numerical answer. *Deliverable:* both answers, which is right, and how you established it. *Marking:* the student used an independent source, not a third AI run.

**2.6 Stakes calibration ★** List ten AI uses from your week. For each, write what happens if the output is wrong and how much checking it therefore needs. *Deliverable:* the table. *Marking:* checking effort scales with stakes; at least two "high stakes" items identified.

## Module 3: How AI behaves

**3.1 Find the edge ★** Test an AI on: counting letters in a 30-letter word; multiplying two 6-digit numbers; summarising a paragraph; naming the capital of a small country; a question about last week's news. *Deliverable:* a table of task, answer, correct?, and whether a tool (code, search) was used. *Marking:* the student identified which failures a tool would fix.

**3.2 Variability measured ★★** Use [`compare_answers.py`](../examples/python/compare_answers.py) (or five fresh chats by hand) on a question with a numerical answer in your field. *Deliverable:* the five answers, the numbers that differed, and the verified value. *Marking:* the student explains why variability matters for how they use the tool.

**3.3 Context in, context out ★** Ask a question about a document without providing it; then with it. *Deliverable:* both outputs and a paragraph on what the first answer did instead of saying "I cannot know". *Marking:* the student recognises confident filling-in.

**3.4 Explain hallucination ★** Write a 150-word explanation of hallucination for a relative who has never used AI, using one example you observed yourself. *Deliverable:* the text. *Marking:* a real example; no claim that it can be fixed by "asking nicely".

**3.5 Tools or memory? ★** Ask about an event from this month three times: with web search on, with it off, and with "if you are not sure, say so" added. *Deliverable:* the three answers and what each tells you about where the answer came from. *Marking:* the student can tell a searched answer from a recalled one.

## Module 4: Decomposition and delegation

**4.1 Task table ★** Take your next assignment and build the AI / me / both table from [worked example 6](../examples/worked-examples/06-delegating-a-lab-report.md). *Deliverable:* the table with a reason per row. *Marking:* assessed thinking kept by the student; knowledge only the student has kept by the student.

**4.2 Delegation brief ★★** Write a brief with outcome, context and check for one task from 4.1, run it, and evaluate the output against your check. *Deliverable:* the [brief](../templates/delegation-brief.md), the output, the evaluation. *Marking:* the check is concrete enough to fail.

**4.3 Plan first ★★** For a multi-step task, ask for a plan, edit it, then let the AI proceed. Repeat the task in a fresh chat without the planning step. *Deliverable:* both outputs and a comparison. *Marking:* a specific improvement traced to the plan edit.

**4.4 The boundary ★** List three tasks in your studies you would never delegate, and three you always would. Justify each in one sentence. *Deliverable:* the list. *Marking:* reasons refer to accountability, learning, or unique knowledge, not just difficulty.

**4.5 Agent supervision ★★★** Give an AI agent (with code or file tools) a small multi-step task in a scratch folder, with checkpoints. *Deliverable:* the brief, the agent's plan, your interventions, the result, and what you would change in the brief. *Marking:* at least one intervention at a checkpoint; permissions limited to the scratch folder.

## Module 5: Domain expertise

**5.1 Expert eyes ★** Ask a question in your field; have a classmate from another field judge the answer; judge it yourself. *Deliverable:* the answer, both judgements, what the non-expert missed. *Marking:* at least one error or omission that only domain knowledge reveals.

**5.2 Hints-only problem set ★★** Solve three problems using only hint prompts ([study.md](../examples/prompts/study.md)). A week later, redo them without AI. *Deliverable:* the hint exchanges and the week-later attempt, honestly reported. *Marking:* honesty; reflection on what was retained.

**5.3 Find the error in the familiar ★** Ask an AI to explain a concept you know very well. *Deliverable:* the explanation with your annotations: wrong, oversimplified, or missing. *Marking:* at least one substantive annotation with a reference.

**5.4 Quiz yourself ★★** Run [`quiz_from_notes.py`](../examples/python/quiz_from_notes.py) (or the quiz prompt) on your notes for one topic. Check every answer against the notes before taking the quiz. *Deliverable:* the quiz, the corrections you made to it, your score. *Marking:* at least one answer checked and, if wrong, corrected.

**5.5 Skill inventory ★** List the five skills from your degree you most want to keep sharp. For each, state one thing you will keep doing without AI. *Deliverable:* the list. *Marking:* concrete practices, not resolutions.

## Module 6: Responsible use

**6.1 Traffic lights ★** Classify ten kinds of information you handle as green / yellow / red for sharing with AI tools, with reference to your institution's policy. *Deliverable:* the table and the policy clause for each red item. *Marking:* personal data about others is red; policy actually consulted.

**6.2 Policy summary ★** Summarise your institution's AI policy in five bullets, or draft one if none exists. *Deliverable:* the summary with a link or citation. *Marking:* accuracy against the source; if drafted, covers disclosure, data, and accountability.

**6.3 Injection in the wild ★★** Find a published prompt-injection incident. Explain the mechanism, the permissions that made it harmful, and the control that would have prevented it. *Deliverable:* 300 words with the source. *Marking:* mechanism correctly described; defence named is least privilege, human-in-the-loop, or input separation.

**6.4 The demonstration ★** Run the [classroom demonstration](../examples/worked-examples/07-prompt-injection.md) with [`injection_demo.txt`](../examples/python/injection_demo.txt) on two tools. *Deliverable:* what each did and a sentence on why this matters more for agents. *Marking:* correct connection between permissions and harm.

**6.5 Disclosure statement ★** Write the disclosure for one recent piece of AI-assisted work using the [template](../templates/ai-disclosure.md). *Deliverable:* the statement. *Marking:* specific tools and uses; states what was checked and what was the student's own.

**6.6 Permission audit ★** List every AI tool you use and the permissions it has. *Deliverable:* the table and the permissions you removed. *Marking:* at least one permission questioned.

## Module 7: The technical toolkit

**7.1 First repository ★★** Fork this repository, clone it, add a `notes/` folder with your module 1 notes in Markdown, commit with a meaningful message, push. *Deliverable:* the repository link. *Marking:* commit message explains why; Markdown renders correctly.

**7.2 Read AI code ★★** Ask for a 30-line script that does a chore for you. Annotate every line with a comment in your own words. *Deliverable:* the annotated script and two documentation links you opened. *Marking:* annotations show understanding; at least one library call verified against documentation.

**7.3 Data profile ★★** Run [`data_explore.py`](../examples/python/data_explore.py) on a dataset from one of your courses. *Deliverable:* the profile and three facts from it you would put in a prompt. *Marking:* the facts are the kind that change an analysis (missing values, units, groups).

**7.4 SQL with a check ★★** Ask an AI for three SQL queries on [`library.sql`](../examples/sql/library.sql). Run them. For one, compute the answer by hand from the table. *Deliverable:* queries, results, hand check. *Marking:* the hand check is real.

**7.5 The pipeline ★★★** A script that reads a CSV, computes something with pandas, writes a Markdown report with a figure, in a Git repository with a README. AI may write any of it; you must test all of it. *Deliverable:* the repository link and a PROCESS.md. *Marking:* runs from a clean clone; tests or hand checks present.

## Module 8: AI in science and engineering work

**8.1 Dimensional detective ★** Ask for a step-by-step derivation of a formula you know. Check the units of every line and one limiting case. *Deliverable:* the derivation with your marks. *Marking:* every line checked; the limiting case stated and evaluated.

**8.2 Compute, don't recall ★** Ask for a multi-step numerical answer from your field without a code tool, then as Python. *Deliverable:* both answers, the difference, your own hand check. *Marking:* the hand check decides, not the AI.

**8.3 The packed bed ★★** Repeat [worked example 4](../examples/worked-examples/04-ai-assisted-data-analysis.md) with [`packed_bed.csv`](../examples/data/packed_bed.csv): profile, prompt, code, one hand calculation. Then add a new question of your own (does flow depend on the repeat number?). *Deliverable:* the prompt log, code, figures, and a 100-word result statement. *Marking:* temperature correction done; hand check present; the result statement contains only what the code shows.

**8.4 Lab report with AI, disclosed ★★★** Produce one lab report using AI under your course policy, with a full PROCESS.md. *Deliverable:* the report and PROCESS.md. *Marking:* the capstone rubric's verification and responsible-use rows.

**8.5 Reference list from scratch ★★** Build a five-reference list on a topic using only prompts from [literature.md](../examples/prompts/literature.md) (search terms, then real search, then AI explanations of papers you have). *Deliverable:* the list with DOIs that resolve and one sentence per paper that you verified. *Marking:* every DOI resolves; sentences match the papers.

**8.6 Teach it ★** Write the "what catches it" row for one failure mode from your own experience, in the style of the module 8 table. *Deliverable:* the row and the story behind it. *Marking:* a real check that would have worked.
