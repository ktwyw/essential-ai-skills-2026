# Self-check quizzes

Five questions per module. Answer before opening the answer. These are for revision, not assessment; the point is to notice which ideas have not stuck.

## Module 1: Clear communication

**1.** Name the four ingredients of a good prompt.
<details><summary>Answer</summary>Goal, context, constraints, format. (And, for delegated work, a check: module 4.)</details>

**2.** Why is "tell me about X" a weak prompt even when X is clear?
<details><summary>Answer</summary>It leaves the audience, purpose, length and format to be guessed, so the answer is generic - correct for nobody in particular.</details>

**3.** When is one example better than a description of the style you want?
<details><summary>Answer</summary>Almost always for tone and layout: an example shows what adjectives can only gesture at. Describe the goal; show the style.</details>

**4.** The AI's draft email mentions "the attached report". You have no attachment. What went wrong and how do you prevent it?
<details><summary>Answer</summary>The model filled a gap with a plausible detail (fabrication). Add "do not invent details; mark anything missing as [BRACKET]" and read every sentence as if you were signing it.</details>

**5.** An answer disappoints you. What should you do before clicking "retry"?
<details><summary>Answer</summary>Diagnose what the prompt left unsaid and rewrite it so a capable stranger could not misread it. Retry only changes the dice.</details>

## Module 2: Critical evaluation

**1.** Why does a confident tone tell you nothing about correctness?
<details><summary>Answer</summary>The model generates fluent text whether or not the content is true; fluency and accuracy are produced by the same mechanism and are not linked.</details>

**2.** What is the only check that establishes whether an AI-supplied reference is real?
<details><summary>Answer</summary>Resolving the DOI or searching the title and opening the paper. Formatting, plausibility and a DOI-shaped string prove nothing.</details>

**3.** A function passes the example in the AI's reply. What have you learned?
<details><summary>Answer</summary>Very little. Edge cases (empty input, zero, wrong type) are where AI code fails; "works on the example" is the weakest evidence.</details>

**4.** You ask "is this correct?" in the same chat and the AI says yes. How much is that worth?
<details><summary>Answer</summary>Almost nothing: it tends to agree with its own output. A fresh chat is weak evidence; an independent check (source, limiting case, computation) is strong evidence.</details>

**5.** How should the amount of checking be decided?
<details><summary>Answer</summary>By the stakes: ask "what happens if this is wrong?" A party theme needs none; a dosage or a load calculation needs full verification.</details>

## Module 3: How AI behaves

**1.** Define hallucination in one sentence.
<details><summary>Answer</summary>Confident output that is false or unsupported, produced because the model generates plausible text rather than retrieving verified facts.</details>

**2.** What is a context window and why does it matter for your prompts?
<details><summary>Answer</summary>The amount of text the model can consider at once. What you include shapes the answer; what you leave out, it cannot know (unless it has tools).</details>

**3.** Why does one good answer not prove a tool is reliable for a task?
<details><summary>Answer</summary>Answers vary between runs; a single success may be luck. Important uses should be tested several times.</details>

**4.** Which of these is a model usually weak at without tools: translating, exact arithmetic, drafting, summarising?
<details><summary>Answer</summary>Exact arithmetic (and counting, recent events, precise figures). With a code tool, arithmetic becomes reliable.</details>

**5.** How can you tell whether an answer about recent events came from search or from memory?
<details><summary>Answer</summary>Look for cited sources or a visible search step; ask the tool directly; and compare with a run where search is off. Recalled answers about recent events are unreliable.</details>

## Module 4: Decomposition and delegation

**1.** What three parts does every delegated task need?
<details><summary>Answer</summary>A clear outcome (what "done" looks like), enough context, and a way to check.</details>

**2.** Give two kinds of task you should keep rather than delegate.
<details><summary>Answer</summary>Final decisions and accountability; sensitive judgement calls; anything requiring knowledge only you have; relationships; choosing the goal itself.</details>

**3.** Why ask an agent for its plan before it starts?
<details><summary>Answer</summary>Correcting direction early is far cheaper than redoing finished work; the plan reveals misunderstandings while they cost nothing.</details>

**4.** What makes a "check" clause good?
<details><summary>Answer</summary>It is concrete enough to fail: a specific comparison, test, or condition, not "make sure it is correct".</details>

**5.** What changes about your role as AI becomes more capable of acting on its own?
<details><summary>Answer</summary>It shifts from doing to planning and supervising: specifying outcomes, supplying context, checking at milestones, and keeping decisions.</details>

## Module 5: Domain expertise

**1.** Why does an expert get more value from the same AI tool than a novice?
<details><summary>Answer</summary>The expert knows what good looks like: they ask better questions, spot plausible errors, and know what to delegate.</details>

**2.** What is the erosion risk and who is most exposed to it?
<details><summary>Answer</summary>Skills fade or never form if AI does the hard thinking; students and early-career people, who have not yet built the expertise that makes AI safe to rely on.</details>

**3.** Turn "solve this problem" into a tutor-mode prompt.
<details><summary>Answer</summary>"Give me one hint, not the answer" or "check my solution and point to the first wrong step without correcting it".</details>

**4.** After an AI-assisted problem, what simple test shows whether you learned it?
<details><summary>Answer</summary>Close the chat and redo it on paper. If you cannot, you have not learned it yet.</details>

**5.** When is assistant mode (just produce it) the right choice?
<details><summary>Answer</summary>When the goal is the output, not learning: chores, formatting, drafts in areas you already command.</details>

## Module 6: Responsible use

**1.** Name three kinds of information that should not be pasted into an AI tool without checking policy.
<details><summary>Answer</summary>Personal data about other people, confidential work or client information, credentials (passwords, API keys).</details>

**2.** What is prompt injection, in one sentence?
<details><summary>Answer</summary>Hidden instructions inside content an AI reads (a web page, email, document) that the AI then follows as if they came from the user.</details>

**3.** Why does injection become more dangerous as AI gains the ability to act?
<details><summary>Answer</summary>A misled summariser only misleads you; a misled agent with email, file or payment access can leak data, delete work or spend money.</details>

**4.** What does "least privilege" mean for an AI agent?
<details><summary>Answer</summary>Give it only the access the current task needs - a scratch folder, not your whole drive; browsing, not email - and no more.</details>

**5.** Who is responsible for an error in AI-assisted work?
<details><summary>Answer</summary>You are. The work is still your work; disclosure describes how it was made but does not transfer accountability.</details>

## Module 7: The technical toolkit

**1.** Why are plain-text, open formats the natural tools for working with AI?
<details><summary>Answer</summary>They are what models read and write most fluently, and they can be diffed, versioned and reviewed - including an agent's changes.</details>

**2.** What does Git give you when an AI agent edits your files?
<details><summary>Answer</summary>A reviewable, reversible history: you can see exactly what changed and undo it.</details>

**3.** What should you do with every unfamiliar library call in AI-written code?
<details><summary>Answer</summary>Open its documentation. Fabricated functions are common and look exactly like real ones.</details>

**4.** Why run a script with a dry-run flag first?
<details><summary>Answer</summary>A script that acts on your files immediately cannot be tested safely; a dry run shows what it would do.</details>

**5.** Why keep API keys out of the repository?
<details><summary>Answer</summary>Anything committed is hard to remove and may be public; a leaked key lets others spend your money. Use environment variables and .gitignore.</details>

## Module 8: AI in science and engineering work

**1.** Which two cheap checks catch most derivation errors, and which kind of error does each catch?
<details><summary>Answer</summary>Units (catch dropped factors and wrong quantities) and limiting cases (catch dropped signs and wrong physics).</details>

**2.** What is the difference between a recalled number and a computed one?
<details><summary>Answer</summary>A recalled value (from the model's memory) is a claim to verify; a computed one (from stated inputs via code) is a calculation you can read and check.</details>

**3.** Why profile a dataset before asking an AI about it?
<details><summary>Answer</summary>The AI sees only a text copy of a slice; missing values, units and group differences change the analysis and must be told to it.</details>

**4.** What does a resolving DOI prove, and what does it not prove?
<details><summary>Answer</summary>That a work with that identifier exists; not that it says what the AI claimed. That requires reading it.</details>

**5.** What belongs in a PROCESS record of AI-assisted technical work?
<details><summary>Answer</summary>Tool and date, the prompts that produced anything kept, what was checked and how, and what the student did themselves.</details>
