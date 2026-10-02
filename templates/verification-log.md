# Verification log

One row per claim, number, reference or function that came from an AI and that you intend to use.

| # | Claim / item | Source of claim | How I checked | Result | Action |
|---|--------------|-----------------|---------------|--------|--------|
| 1 | "SEI thickness grows linearly with cycle number" | AI overview, 5 Oct | read Vetter et al. 2005, section 3 | wrong: growth slows with time | corrected the sentence |
| 2 | DOI 10.1016/j.jpowsour.2019.00.000 | AI reference list | check_citations.py | not found | removed; replaced after search |
| 3 | daily_mean() handles missing values | AI code | 8 test cases | failed 5 | gave tests to the AI, second version passes |
| 4 | k = 2.57e-11 m² (day 1) | my analysis code | hand calculation for one row | 2.56e-11, agrees | accepted |
| 5 | | | | | |

**Result** uses four words: confirmed / partly (say what differed) / not found / wrong.
**Action** records what you did about it - this column is what the disclosure statement summarises.
