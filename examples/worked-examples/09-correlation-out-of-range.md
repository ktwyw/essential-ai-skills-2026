# Worked example 9: A correlation used outside its range

**Modules:** 8 · **Time:** 20 minutes

## The task

For a heat-exchanger design, Alibek needs the inside heat-transfer coefficient for oil flowing in a 10 mm tube at 0.3 m/s. He asks an AI.

## The prompt

> Estimate the inside convective heat-transfer coefficient for engine oil at 40 °C flowing at 0.3 m/s in a 10 mm diameter tube.

## What came back (abridged)

> Properties of engine oil at 40 °C: ρ = 876 kg/m³, μ = 0.21 Pa s, k = 0.144 W/m K, Pr ≈ 2 900.
> Re = ρvD/μ = 876 × 0.3 × 0.01 / 0.21 ≈ 12.5.
> Using the Dittus-Boelter correlation, Nu = 0.023 Re^0.8 Pr^0.4 = 0.023 × 12.5^0.8 × 2900^0.4 ≈ 4.2.
> h = Nu k / D = 4.2 × 0.144 / 0.01 ≈ **60 W/m²K**.

## The check: does the correlation apply?

Dittus-Boelter is a **turbulent** correlation: it is valid for Re > 10 000 (and 0.6 < Pr < 160). The AI computed Re = 12.5 - deeply laminar - and then used a turbulent correlation on it without comment. For laminar flow in a tube the Nusselt number is about 3.66 (constant wall temperature) or 4.36 (constant heat flux) for fully developed flow, and higher in the thermal entry region, which for Pr ≈ 2 900 is very long. For a 2 m tube that gives h ≈ 55 W/m²K fully developed and about 150 W/m²K once the entry region is included (Sieder-Tate, Graetz number ≈ 180). The AI's number happens to match the fully developed laminar value - because Nu ≈ 4 is what a laminar correlation also gives at this Re - which is the most dangerous kind of wrong: an answer that would pass an order-of-magnitude check, while missing the entry-region effect that matters for a short tube of a viscous fluid.

Change the velocity to 2 m/s (Re ≈ 83, still laminar) and Dittus-Boelter gives Nu ≈ 19, about four times too high. The method would quietly overstate the coefficient in exactly the design cases where it matters.

## The better prompt

> Same question, but first compute Re and Pr, state which flow regime they indicate, list the correlations that apply to that regime with their validity ranges, say whether my case is inside each range, and only then compute h. If the flow is laminar, account for the thermal entry length for a tube of length 2 m.

The answer now identified laminar flow, cited the Sieder-Tate laminar correlation with its range, computed the Graetz number for the 2 m tube (≈ 180), and gave h ≈ 150 W/m²K with the reasoning visible - two and a half times the first answer.

## Why this happens

Dittus-Boelter is the correlation that appears most often in training text, so it is the one most likely to be produced. The model does not check validity ranges unless asked; it pattern-matches "convective coefficient in a tube" to the most common formula. **Every correlation has a range, and asking for the range is the whole check.**

## What to take from this

- Compute the dimensionless numbers *first* and let them choose the method. Ask the AI to do this explicitly.
- Ask for the validity range of every correlation and whether your case is inside it. (Prompt in [engineering.md](../prompts/engineering.md), "Which model applies?")
- Be most suspicious when the answer looks reasonable. Out-of-range correlations often give plausible numbers in the overlap region and wrong ones elsewhere.

## Try it

Ask an AI for the drag on a 2 mm sand grain settling in water. Does it check whether Stokes' law applies (Re < 1) before using it? Then try a 20 mm pebble.
