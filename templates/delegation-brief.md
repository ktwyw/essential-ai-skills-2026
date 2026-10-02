# Delegation brief

For a task you give to an AI agent or assistant. Three parts; if you cannot fill one, you are not ready to delegate.

## Outcome

What "done" looks like, concretely: [files produced, their format and location; the question answered; the state of the repository afterwards].

## Context

- Background: [what the task is for, who will use the result]
- Inputs: [files, data, links - what they contain and what is known to be odd about them]
- Constraints: [tools and libraries allowed; style; length; what must not be changed; what must not be assumed]
- Examples: [one example of the wanted output, or a bad example labelled as such]
- Permissions: [exactly which folders, services and actions the agent may use]

## Check

How I will know it was done correctly: [a test that must pass; a value to compare with; a review step; "stop and show me the plan before starting"; "report after each of these milestones: ..."].

---

### Example

**Outcome:** two PNG figures, `fig_outlet_temps.png` and `fig_U_vs_Re.png`, 160 mm wide at 200 dpi, produced by `make_figures.py` from `results.csv`.

**Context:** `results.csv` columns: flow_L_min, T_hot_out_C, T_cold_out_C, Re, U_W_m2K, repeat (1-3). Figure 1: outlet temperatures vs flow with error bars from the three repeats, linear axes. Figure 2: U vs Re, log-log, manufacturer's U = 850 W/m²K as a dashed line. Colour-blind-safe palette, axis labels with units, matplotlib only. Write only to the `figures/` folder.

**Check:** the script runs from a clean folder containing only `results.csv`; I will compare three plotted points with the CSV by eye; show me the plot layout as a sketch (which series, which axes) before writing code.
