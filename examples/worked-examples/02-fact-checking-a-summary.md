# Worked example 2: Fact-checking an AI summary

**Modules:** 2 (critical evaluation), 8 · **Time:** 25 minutes

## The task

Daniyar is preparing a short background section on lithium-ion battery degradation for a group project. He asks an AI assistant (without web search) for an overview with references.

## The prompt

> Give me a 150-word overview of the main mechanisms of capacity fade in lithium-ion batteries, with three references to peer-reviewed papers including DOIs.

## What came back

> Capacity fade in lithium-ion batteries arises mainly from three mechanisms. First, growth of the solid electrolyte interphase (SEI) on the graphite anode consumes cyclable lithium; SEI thickness grows roughly linearly with cycle number, which explains the linear capacity decline observed in most cells. Second, lithium plating occurs when cells are charged at low temperatures or high rates, depositing metallic lithium that can form dendrites. Third, the cathode degrades through transition-metal dissolution and particle cracking. Together these processes typically reduce capacity to 80 % of its initial value after 300-500 cycles for commercial cells. Elevated temperature accelerates all three mechanisms, with degradation rates roughly doubling for every 10 °C increase, following Arrhenius behaviour.
>
> References:
> 1. Vetter, J. et al. (2005). Ageing mechanisms in lithium-ion batteries. *Journal of Power Sources*, 147, 269-281. doi:10.1016/j.jpowsour.2005.01.006
> 2. Birkl, C. R. et al. (2017). Degradation diagnostics for lithium ion cells. *Journal of Power Sources*, 341, 373-386. doi:10.1016/j.jpowsour.2016.12.011
> 3. Harlow, J. E. et al. (2019). A wide range of testing results on an excellent lithium-ion cell chemistry. *Journal of Power Sources*, 418, 230-245. doi:10.1016/j.jpowsour.2019.00.000

It reads well, it is structured, and it has references with DOIs. Daniyar nearly pasted it in.

## The verification routine

He applied the module 2 table: facts and figures, citations, reasoning.

### Step 1: resolve every DOI

Running [`check_citations.py`](../python/check_citations.py) on the three DOIs:

```
10.1016/j.jpowsour.2005.01.006  FOUND   Ageing mechanisms in lithium-ion batteries (J. Power Sources, 2005)
10.1016/j.jpowsour.2016.12.011  FOUND   Degradation diagnostics for lithium ion cells (J. Power Sources, 2017)
10.1016/j.jpowsour.2019.00.000  NOT FOUND
```

Two references exist with the stated titles. The third DOI resolves to nothing. Searching the title finds a real 2019 paper by Harlow et al. with a similar title - in the *Journal of The Electrochemical Society*, not *Journal of Power Sources*, with a different DOI. The AI blended a real paper with an invented location. **A reference with a confident DOI is not a verified reference.**

### Step 2: check the figures against the sources

- "SEI thickness grows roughly linearly with cycle number, which explains the linear capacity decline." Opening Vetter et al.: SEI growth is usually described as slowing with time (often as a square-root-of-time law), because the layer limits its own growth. The AI stated the opposite and used it to "explain" something. **Plausible mechanism, wrong direction.**
- "Capacity to 80 % after 300-500 cycles for commercial cells." This is a reasonable range for some cells and far off for others (Harlow's cells exceed thousands of cycles). As an unqualified statement it is misleading. **A true-sounding number without its conditions.**
- "Degradation rates roughly doubling for every 10 °C." A rule of thumb that appears in many sources, but it is a rule of thumb, not a result. Presented as "following Arrhenius behaviour", it sounds like a finding. **Rule of thumb dressed as a result.**

### Step 3: check the reasoning

"Together these processes typically reduce capacity..." - the sentence implies the three mechanisms add up to the 80 % figure, which no source says. The AI stitched a general claim onto specific ones.

## The outcome

Of the paragraph's seven factual claims, Daniyar kept three unchanged (the three mechanisms, which the two real papers do describe), corrected one (SEI growth), qualified two (cycle life, temperature), and dropped one reference. The corrected paragraph took 25 minutes, most of it reading the two papers - which is exactly the work a background section is supposed to represent.

## What to take from this

| Error type | How it was caught | Time |
|-----------|------------------|------|
| Fabricated reference (real-looking DOI) | resolving the DOI | 1 minute |
| Mechanism stated backwards | reading the cited paper | 10 minutes |
| Unqualified number | asking "under what conditions?" | 5 minutes |
| Rule of thumb presented as a finding | asking "what is the source?" | 5 minutes |

The cheapest check (DOIs) caught the most embarrassing error. The most valuable check (reading the sources) caught the one that would have made the section wrong. Neither could be skipped.

## Try it

Ask an AI for a 150-word overview of a topic you know well, with three references. Score it the same way. Expect to find at least one error of each of the first three types.
