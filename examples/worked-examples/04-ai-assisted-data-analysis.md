# Worked example 4: AI-assisted data analysis

**Modules:** 7, 8 · **Time:** 40 minutes

## The task

A group has measured the flow rate through a packed bed at several pressure drops, three repeats each, on two days. The data are in [`examples/data/packed_bed.csv`](../data/packed_bed.csv). They want to know whether flow rate is proportional to pressure drop (Darcy's law) and to report the permeability.

## The wrong way (what happened first)

Zhanel pasted the whole CSV into the chat and asked:

> Analyse this data and tell me the permeability.

The AI replied with a paragraph: "The data show a clear linear relationship between pressure drop and flow rate, consistent with Darcy's law. A linear regression gives a slope of 0.0412 L/min per kPa, corresponding to a permeability of approximately 2.3 × 10⁻¹¹ m². The small scatter indicates good experimental technique."

Three problems:

1. **No code, no plot, no way to reproduce it.** Where did 0.0412 come from? Which rows were used?
2. **The AI cannot have computed a permeability** without the bed length, cross-section and fluid viscosity, which were not in the file. It made them up or used "typical" values silently.
3. **"Clear linear relationship"** was not checked against the day-2 data, which look different (see below). A fluent conclusion from data the model only read as text.

## The right way

### Step 1: look at the data yourself

Running [`data_explore.py`](../python/data_explore.py) on the file:

```
data/packed_bed.csv: 24 rows, 5 columns

column          type      non-null  min       max       examples
day             int64     24        1         2         1, 2
dp_kPa          float64   24        5         40        5.0, 10.0, 20.0
repeat          int64     24        1         3         1, 2, 3
flow_L_min      float64   23        0.19      1.96      0.2, 0.19, 0.38
temp_C          float64   24        18.5      29        18.5, 19.0, 19.5

Missing values: flow_L_min 1
Duplicate rows: 0
Columns that look categorical: day (2 values), repeat (3 values)
Strongly correlated pairs (|r| > 0.8): day-temp_C (1.00), dp_kPa-flow_L_min (0.98)
Means by day:
     dp_kPa  repeat  flow_L_min  temp_C
day
1     18.75     2.0       0.732  18.958
2     18.75     2.0       0.957  28.458
```

Three facts the AI could not know from a paragraph: one flow reading is missing, day 2 was ten degrees warmer, and the mean flow on day 2 is 30 % higher at the same pressure drops. Water is about 20 % less viscous at 28 °C than at 19 °C, so Darcy's law predicts *higher* flow on day 2 at the same pressure drop - a difference that looks like scatter if you do not know it is there.

### Step 2: give the AI the schema, the facts, and the physics

> I have a CSV with columns day (1 or 2), dp_kPa (pressure drop), repeat (1-3), flow_L_min (volumetric flow, one value missing), temp_C (water temperature; day 1 ≈ 19 °C, day 2 ≈ 28 °C). The bed is L = 0.30 m long with cross-section A = 7.85 × 10⁻³ m². Darcy's law: Q = k A ΔP / (μ L). Write Python (pandas, matplotlib) that: (1) plots flow vs pressure drop with separate markers per day, (2) fits Q = s·ΔP through the origin separately per day, (3) computes k from each slope using the water viscosity at that day's mean temperature (give the viscosity values you use and their source), and (4) prints the two permeabilities with their standard errors. Do not interpret the results; I will.

### Step 3: run the code, read the plot

The code ran. The plot showed two clean lines of different slope. The printed output:

```
day 1: slope 0.03916 L/min/kPa (se 0.00041), mu = 1.03e-3 Pa s at 19.0 C -> k = 2.57e-11 m2
day 2: slope 0.04794 L/min/kPa (se 0.00058), mu = 0.83e-3 Pa s at 28.5 C -> k = 2.53e-11 m2
```

Once the viscosity difference was accounted for, the two days agreed to 2 %. The "scatter" was temperature. The AI's first answer (one regression through both days, 0.0412) had averaged two different physical conditions and reported a number that was true of neither.

### Step 4: check one number by hand

Zhanel took one row (day 1, ΔP = 20 kPa, Q = 0.78 L/min), converted units by hand (0.78 L/min = 1.3 × 10⁻⁵ m³/s), and computed k = Q μ L / (A ΔP) = 2.56 × 10⁻¹¹ m². It matched the fitted value. Now the code was trusted, and the viscosity values were checked against a table.

## What to take from this

- **Profile first, prompt second.** Thirty seconds with `data_explore.py` found the missing value and the temperature difference that the whole analysis hinged on.
- **Ask for code and a plot, not conclusions.** Conclusions cannot be checked; code can be rerun and read.
- **State the physics and the constants.** Without L, A and μ the AI invented them; with them it did the arithmetic correctly.
- **One hand calculation** turns "the code ran" into "the code is right".
- **The report's conclusion** - "k = 2.5 × 10⁻¹¹ m², consistent across two days once viscosity is corrected" - is both stronger and more honest than the AI's original "clear linear relationship, good technique".

## Try it

Take any dataset from a lab course. Run `data_explore.py`, write down three facts it shows you, and include them in your prompt. Compare the analysis you get with one from a prompt that just pastes the data.
