# Prompts for data analysis

Profile the data yourself first ([`data_explore.py`](../python/data_explore.py)), then ask for **code and figures, not conclusions** (worked example 4).

## Analysis as code

```
I have a CSV with these columns and properties: [paste the profile from data_explore.py]. Facts I noticed: [missing values, units, anything odd].
Physics / model: [the equation or hypothesis, with symbols defined and constants given with units and sources].
Write Python (pandas, matplotlib) that: (1) [plot, with axes and units specified], (2) [fit or test, specifying exactly what is fitted to what], (3) prints [the quantities] with uncertainties.
State every assumption and every constant you use. Do not interpret the results; I will.
```

## Cleaning plan before cleaning

```
Here is a profile of my data: [paste]. Before writing any code, list the cleaning steps you would take, what each would remove or change, and how many rows you expect each to affect. Wait for my approval.
```

*Why:* silent dropping of rows is the most common way an AI analysis goes wrong.

## Figure to specification

```
Make a matplotlib figure from [dataframe / columns]: [what on each axis, units, scale], separate [markers / colours] for [groups], error bars from [what], a dashed horizontal line at [reference value], colour-blind-safe palette, width [mm] for a [one / two]-column report, saved as PNG at 200 dpi. Code only.
```

## Choosing a statistical test

```
I want to know whether [question] in data with [structure: groups, sizes, paired or not, measurement type]. List the two or three tests that could apply, the assumption each needs, how I would check that assumption on my data, and which you would choose and why. Do not run anything yet.
```

## Reproduce the AI's claim

```
You said [claim the AI made about the data]. Show me the exact code that produces that number from the file, and the rows it used. Then rerun it.
```

## Sanity check a result

```
My analysis gives [result with units]. Here is the method: [summary]. Give me three independent ways to sanity-check this number (an order-of-magnitude estimate, a known reference value, a limiting case), and compute the first one.
```

## Describe a figure I made

```
Here is a figure [attach or describe axes and series]. Describe what it shows in two sentences for a results section, using only what is visible. Then list two things a sceptical reader might ask about it.
```
