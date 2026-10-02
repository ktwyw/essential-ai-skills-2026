# Prompts for studying (tutor mode)

The goal in a course is understanding, so these prompts ask the AI to help you think, not to think for you (module 5). Close the chat afterwards and redo the work on paper.

## Explain at my level

```
Explain [concept] to a [second-year chemical engineering] student who already knows [prerequisites] but has never met [concept].
Use one concrete example from [my field]. Then give one edge case where the simple explanation breaks down.
Keep it under 250 words. Do not use the words [jargon you want avoided].
```

*Why it works:* stating what you already know stops the AI from re-explaining basics; asking for the edge case exposes oversimplification (worked example 2 shows why that matters).

## Hint, not answer

```
I am working on this problem: [problem statement]. Here is where I am: [your work so far].
Give me ONE hint that moves me forward, without revealing the next step or the answer.
If my work so far contains an error, tell me which line it is in but not what the error is.
```

*Why it works:* the AI can see your reasoning and point at the failure; you still do the correcting. Ask for a second hint only after you have tried.

## Check my solution

```
Here is a problem and my full solution: [both]. Do not solve it yourself.
List each step of my solution and mark it correct, doubtful, or wrong. For doubtful or wrong steps, say what principle I may have misapplied, not the correct version.
Finally, name the single step you would check first and why.
```

## Quiz me

```
Quiz me on [topic / these notes: paste]. Ask one question at a time and wait for my answer.
Mix recall, understanding, and application. After each answer, say whether I was right, explain briefly, and quote the part of the notes it came from.
After 8 questions, list the concepts I got wrong.
```

*Check:* the quoted note is how you catch a question built on a misreading. See also [`quiz_from_notes.py`](../python/quiz_from_notes.py).

## Reconstruct from memory

```
I am going to explain [concept] from memory in my own words. Then I want you to: (1) point out anything wrong or missing, (2) ask me one question that tests whether I really understand it, (3) stop. Here is my explanation: [...]
```

## Make a study plan

```
I have an exam on [topics] on [date]. I have [hours] per day. My weakest areas are [list]. Past papers use these question types: [list].
Make a day-by-day plan in a table with: topic, activity (practice problems / notes / self-test), minutes, and how I will check I learned it. Spend most time on weak areas. Leave the last day for a full past paper.
```

## Compare explanations

```
Here are two explanations of [concept], one from my lecture notes and one from the textbook: [paste both]. Where do they differ in emphasis or assumptions? Is either incomplete? Which one should I use for [exam / design work], and why?
```

## What NOT to ask (in a course)

- "Solve this problem set." You will not be able to do it in the exam.
- "Write my lab report discussion." That is the part being assessed.
- "Is this right?" in the same chat where the AI wrote it. It will say yes (worked example 5). Ask in a fresh chat, or better, check a limiting case.
