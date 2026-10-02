# Frequently asked questions

Questions students ask in the first weeks, with the course's answers and where to read more.

**Which AI tool should I use?**
Whichever your institution permits and provides; the skills in this course transfer between tools. If you have a choice, prefer one with tools (code execution, search, file reading), because those cover the common weaknesses (module 3). Check the policy before pasting anything you did not write yourself (module 6).

**Is it cheating to use AI for my assignment?**
It depends on the course, and the course policy is the answer - find it (exercise 6.2). Where AI is permitted, two rules keep you safe: disclose how you used it ([template](templates/ai-disclosure.md)), and do the assessed thinking yourself (worked example 6). Where it is not permitted, do not use it.

**The AI gave me an answer. How do I know it is right?**
You do not, until you check it by a method the AI did not control: a source, a test, a hand calculation, a limiting case (modules 2 and 8). Asking the AI "are you sure?" is not a check (worked example 5).

**Why did it make up a reference?**
Because it generates plausible text, and a plausible reference is text (glossary: hallucination). Resolve every DOI with [`check_citations.py`](examples/python/check_citations.py), then open the paper. Use AI to *explain* papers you have, not to *find* papers you do not (prompt library: [literature](examples/prompts/literature.md)).

**It wrote the code and it runs. Can I use it?**
Running on one example is the weakest evidence there is. Write six test cases, including edge cases, before you trust it; and read every line, opening the documentation for any function you do not recognise (worked example 3).

**Why do I get different answers each time?**
Models sample from many possible continuations; the same prompt gives different text and sometimes different facts (module 3). For anything important, ask more than once in fresh chats and verify what differs ([`compare_answers.py`](examples/python/compare_answers.py)).

**Can I paste my lab group's data into the chat?**
Remove names and anything personal first; then check the course policy on the tool. For analysis, paste a profile ([`data_explore.py`](examples/python/data_explore.py)) rather than the whole file, and ask for code you can run yourself (worked example 4).

**Does using AI make me learn less?**
It can (module 5). Use tutor-mode prompts ([study.md](examples/prompts/study.md)): hints, checks of your work, quizzes. After any AI-assisted problem, close the chat and redo it on paper. If you cannot, you have not learned it.

**Should I learn Python if AI can write it?**
Yes - to read it. Someone must judge whether the code does what the task needs, and that someone is you (module 7). The bar is reading and testing, not writing from scratch.

**What is the difference between a chatbot and an agent?**
A chatbot answers; an agent acts - browses, edits files, runs code, sends messages. Agents need delegation briefs (module 4) and limited permissions (module 6), because a misled agent can do damage a misled chatbot cannot (worked example 7).

**How do I cite an AI tool?**
Follow your course or journal's rule. Most now ask for a disclosure statement rather than a citation ([template](templates/ai-disclosure.md)). Where a citation is required, name the tool, the provider, the version or date, and what it was used for.

**The course says to document everything. Isn't that a lot of work?**
About ten minutes per assignment with the [templates](templates/README.md), and it saves far more when a supervisor asks "where did this number come from?" It is also the habit that makes technical work reproducible, with or without AI.

**Can I translate this course?**
Yes; the text is CC BY 4.0. See [CONTRIBUTING.md](CONTRIBUTING.md) for the translations folder convention.
