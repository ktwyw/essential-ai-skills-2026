# PROCESS.md: lab-data pipeline for CHME 302

*Project:* packed-bed permeability pipeline · *Author:* Zhanel A. · *Dates:* 6-27 October 2026 · *AI tools:* university Claude account (October 2026); GitHub Copilot in VS Code

This is a sample of what a complete process record looks like. It accompanies a small project: a script that reads the packed-bed data, corrects for viscosity, fits Darcy's law per day, and writes a report with figures.

## 1. Division of labour

| Task | Who | Why |
|------|-----|-----|
| Identify which readings were warm-up and which day was warmer | me | knowledge from being in the lab |
| Data profile | me (script) | `data_explore.py`, 30 seconds |
| Analysis code | both | AI drafted from my specification; I wrote the hand check and the tests |
| Figures | AI, then me | AI wrote matplotlib; I rejected a log axis it chose for figure 1 |
| Report text | both | I wrote the results and discussion; AI drafted the method section from my bullets and proof-read |
| README and requirements | AI, checked by me | mechanical |
| Final sign-off | me | accountability |

## 2. Prompts that produced something I kept

**Prompt A** - analysis code.
- First version: "Analyse this data and tell me the permeability" with the CSV pasted. Output: a paragraph with a number (0.0412 L/min/kPa) and no code; it had invented the bed dimensions and used one regression for both days.
- Improved version: profile pasted, bed dimensions and viscosity values given with sources, "write code, do not interpret", per-day fits requested.
- What changed: runnable code, two slopes (0.0392 and 0.0479), viscosities stated, and a note that one row was missing.

**Prompt B** - figure specification. First version "plot the data" gave a single unlabelled scatter. The delegation-brief version (axes, units, markers per day, 160 mm width, 200 dpi) gave a usable figure except for a log axis I had not asked for; I added "linear axes" to the brief.

**Prompt C** - method section. Outline first (five bullets), reordered to put assumptions before the equation, then prose. The draft said "the data were fitted by least squares"; I changed it to "fitted through the origin by least squares, separately for each day", which is what the code does.

## 3. Errors caught and how

| What the AI produced | What was wrong | How I found it | What I did |
|---------------------|----------------|----------------|------------|
| First answer: "clear linear relationship… permeability 2.3 × 10⁻¹¹ m²" | one regression across two temperatures; bed dimensions invented | `data_explore.py` showed temperature differed by day; no dimensions in the file | re-prompted with the physics and the constants |
| Viscosity of water at 28 °C given as 0.89 mPa s | too high for 28 °C (that is roughly 25 °C) | checked against a property table | corrected to 0.83 mPa s; asked the AI to cite its source next time |
| Figure 1 on log axes | not what the brief asked (and hides the linearity) | opened the PNG | added "linear axes" to the brief |
| Method draft: "fitted by least squares" | incomplete description of what the code does | read the code and the text together | corrected the sentence |
| `df.dropna()` applied to the whole frame | would drop rows with a missing temperature too, if any | read the code line by line | changed to `dropna(subset=["flow_L_min"])` |

## 4. Verification of the final result

- [x] Every number in the report comes from the script's output or a cited table.
- [x] Hand check: day 1, ΔP = 20 kPa, Q = 0.78 L/min → k = 2.56 × 10⁻¹¹ m²; fitted value 2.57 × 10⁻¹¹ m².
- [x] Units checked on Darcy's law; limiting case: Q → 0 as ΔP → 0 (fit through the origin).
- [x] Both viscosity values checked against a property table.
- [x] Script runs from a clean clone with `pip install -r requirements.txt`; 6 tests pass.

## 5. Privacy and security decisions

- The raw export had a header row with group members' names; removed before sharing with the AI.
- University account used, per the course policy; no personal API key in the repository (`.gitignore` covers `.env`).
- Copilot's suggestions accepted only inside the project folder; no agent permissions beyond it.

## 6. Disclosure statement

> AI assistance (university Claude account and GitHub Copilot, October 2026) was used to draft the analysis and figure code from my specification, to draft the method section from my outline, and to proof-read. All computed values were checked against a hand calculation; property values were checked against a table; the results and discussion are my own. Prompts and checks are recorded in PROCESS.md.

## 7. Reflection (320 words)

The most useful thing I learned is that the quality of what I got back tracked the quality of what I put in almost exactly. My first prompt was a question; my last prompts were specifications, and the difference in output was not subtle. The thirty seconds spent profiling the data before asking anything was the best thirty seconds in the project: it found the temperature difference that the AI's first answer had averaged away, and without it I would have reported a permeability that was true of neither day.

The AI was best at volume: matplotlib boilerplate, a method section from bullets, a README. It was worst at anything it had to recall rather than compute - the viscosity value was off, and the bed dimensions in the first answer were simply invented. The rule "make it compute, not recall" would have saved one of the five errors in my table; the other four needed reading.

I kept the thinking: which readings were warm-up, what the result means, whether the two days agreeing to 2 % is good (it is, for this rig). I am glad I did, because the discussion was the only part of the project I could explain fluently in the oral check-in.

What I would do differently: write the test cases before the first prompt, not after the first failure; and give the AI the delegation brief for figures from the start instead of "plot the data". Both would have saved an iteration. I would also keep the verification log as I went rather than reconstructing it at the end - it took an hour to remember what I had checked.

The process record felt like overhead for the first week and like insurance by the third. When my partner asked where the viscosity values came from, the answer was one line in a table.
