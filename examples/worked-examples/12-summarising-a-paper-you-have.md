# Worked example 12: Summarising a paper you have

**Modules:** 2, 5, 8 · **Time:** 25 minutes

## The task

Aruzhan has a 14-page paper on membrane fouling for a journal club. She attaches the PDF and asks for a summary. This is the *safe* use of AI in literature work - the paper is in the context, so the AI is not recalling, it is reading. It is still not checking.

## The prompt

> Summarise the attached paper in 200 words for a journal club: question, method, main result with the figure it comes from, and the authors' main limitation.

## What came back (abridged)

> The paper investigates whether periodic backwashing reduces fouling in ultrafiltration of surface water. Using a pilot-scale hollow-fibre module over 60 days, the authors compared four backwash intervals. Their main finding is that backwashing every 15 minutes reduced the fouling rate by 62 % relative to every 60 minutes (Figure 4) and that chemical cleaning frequency could be halved. They also report that the optimal interval depends on feed turbidity, with a threshold at 8 NTU above which more frequent backwashing is needed (Table 3). The authors note as the main limitation that the trial was run at a single site and that the economic analysis assumed constant energy prices.

Fluent and structured. Aruzhan checked every claim against the PDF, which took fifteen minutes.

## What the check found

| Claim | In the paper? | Notes |
|-------|--------------|-------|
| Periodic backwashing, UF, surface water | yes | |
| Pilot-scale hollow-fibre, 60 days | **partly** | 45 days; the 60 appears in a cited earlier study |
| Four backwash intervals | yes | |
| 62 % reduction, 15 vs 60 min, Figure 4 | **partly** | the number is in the text, but the comparison is 15 vs 45 min; Figure 4 shows it |
| Chemical cleaning frequency halved | **not in the paper** | the discussion says it "could be reduced"; no number is given |
| Turbidity threshold at 8 NTU, Table 3 | **wrong** | Table 3 gives 5 NTU; 8 NTU appears in the introduction, citing another study |
| Limitation: single site, constant energy prices | **partly** | single site, yes; the energy-price point is Aruzhan's own instructor's comment from a lecture, which the AI could not have seen - it invented a plausible limitation |

Three of seven claims were exact; four were blended, inflated or invented. Every wrong number was a *real number from the paper or its citations*, attached to the wrong comparison. This is harder to catch than a fabricated reference: nothing looks fake.

## Why it happens even with the paper attached

The model reads the whole document and generates a summary that is *consistent with* it in style and vocabulary, pulling numbers from wherever they appear. It does not keep the table of "which number belongs to which comparison" that a careful reader builds. The longer and denser the paper, the more such transpositions.

## The better prompt

> Summarise the attached paper in 200 words. For every number you state, quote the sentence or table cell it comes from in brackets after it. If the paper does not state something explicitly (for example, implications), say "the authors do not quantify this". Do not include anything that is not in this paper.

The new summary had quotes after each number, which made checking a two-minute job, and it replaced the "halved" claim with "the authors suggest cleaning frequency could be reduced but do not quantify it".

## What to take from this

- **Attaching the source makes the AI read; it does not make it accurate.** Transposed numbers are the characteristic error.
- **Ask for the quote beside every number.** It converts a 15-minute check into a 2-minute one, and the AI is less likely to transpose when it must quote.
- **"Not in the paper" is a legitimate answer** and a good prompt tells the AI it may give it.
- Use the summary to decide whether to read the paper closely - never as a substitute for having read it when you are going to cite it.

## Try it

Attach a paper you know well and ask for a summary without the quoting instruction. Count the transposed numbers. Then add the instruction and count again.
