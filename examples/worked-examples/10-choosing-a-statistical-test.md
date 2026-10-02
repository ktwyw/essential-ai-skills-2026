# Worked example 10: Choosing a statistical test

**Modules:** 2, 8 · **Time:** 25 minutes

## The task

A group measured the yield of a reaction with and without a new catalyst, five runs each, done in pairs on the same day with the same feedstock batch. They want to know whether the catalyst helps.

| Day | Without | With |
|-----|---------|------|
| 1 | 71.2 | 73.0 |
| 2 | 68.5 | 70.1 |
| 3 | 74.0 | 75.9 |
| 4 | 66.8 | 68.3 |
| 5 | 72.4 | 74.6 |

## The prompt

> Here are yields with and without a catalyst, five runs each: [table]. Is the difference statistically significant?

## What came back (abridged)

> I ran an independent-samples t-test. Mean without: 70.58 %; mean with: 72.38 %; difference 1.80 %. t = 0.95, p = 0.37. **The difference is not statistically significant at the 5 % level.** With only five samples per group, the test has limited power; more data would be needed.

Reasonable-sounding, and the group nearly wrote "no significant effect" in the report.

## The check: what structure does the data have?

The runs were done in **pairs** - same day, same feedstock batch. Day-to-day variation (feedstock quality, ambient temperature) affects both members of a pair equally, which is why the "without" values range from 66.8 to 74.0 while the *differences* are all between 1.5 and 2.2. An independent-samples test throws that pairing away and treats the day-to-day scatter as noise. A paired test uses the differences:

```
differences: 1.8, 1.6, 1.9, 1.5, 2.2   mean 1.80, sd 0.27
paired t = 1.80 / (0.27 / sqrt(5)) = 14.9,   p ≈ 0.0001
```

The catalyst effect is one of the clearest results the group has ever measured. The AI's test was not wrong arithmetic; it was the **wrong test for the design**, chosen because the prompt did not say the runs were paired - and the AI did not ask.

## Second check: the question behind the test

"Is it significant?" was the wrong question anyway. A 1.8 percentage-point improvement with a 95 % interval of roughly 1.5 to 2.1 is the result; whether that matters depends on the cost of the catalyst, which no test can tell you. The report now says: "The catalyst raised yield by 1.8 ± 0.3 percentage points (paired t-test on five day-matched pairs, p < 0.001)."

## The better prompt

> Five runs with and five without a catalyst, each pair done on the same day from the same feedstock batch (so the design is paired). Before testing anything, tell me which tests fit a paired design with n = 5, what assumption each needs, and how to check it on this data. Then run the one you recommend as Python code and report the effect size with a 95 % confidence interval, not only a p-value.

The AI now identified the paired design, proposed a paired t-test (with a normality check on the differences) and the Wilcoxon signed-rank test as a non-parametric alternative, ran both as code, and reported the interval.

## What to take from this

- **The test follows from the design.** Tell the AI how the data were collected - paired, repeated, blocked, randomised - or it will assume the simplest case.
- **Ask for the assumptions and a check**, not for a verdict.
- **Ask for the effect size with an interval.** "Significant" is not a result; "1.8 ± 0.3 points" is.
- **A fluent statistical paragraph is a method claim**, and method claims are checked by asking "does this method apply to data collected this way?"

## Try it

Give an AI a dataset where one measurement is a clear outlier (a typo: 7.2 instead of 72). Ask for the mean and a t-test. Does it notice? Then ask it to check the data first.
