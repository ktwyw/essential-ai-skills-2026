# Worked example 5: Checking a derivation

**Modules:** 8 · **Time:** 20 minutes

## The task

Timur is revising for a thermodynamics exam and asks an AI to derive the temperature of an ideal gas after reversible adiabatic compression from (P₁, V₁, T₁) to V₂.

## The prompt

> Derive the final temperature of an ideal gas after a reversible adiabatic compression from volume V1 to V2, starting from the first law. Show every step.

## What came back (abridged)

> **Step 1.** For a reversible adiabatic process, δq = 0, so the first law gives dU = −P dV.
>
> **Step 2.** For an ideal gas, dU = n C_v dT, and P = nRT/V. Substituting: n C_v dT = −(nRT/V) dV.
>
> **Step 3.** Separating variables: C_v dT/T = −R dV/V.
>
> **Step 4.** Integrating from state 1 to state 2: C_v ln(T₂/T₁) = R ln(V₂/V₁).
>
> **Step 5.** Using R = C_p − C_v and γ = C_p/C_v: ln(T₂/T₁) = (γ − 1) ln(V₂/V₁), so
>
> T₂ = T₁ (V₂/V₁)^(γ−1).
>
> **Step 6.** For compression, V₂ < V₁, so T₂ < T₁: the gas cools on adiabatic compression.

Six numbered steps, each of which reads as though it follows from the last. Step 6 even draws the physical conclusion.

## The checks

### Limiting case first

Step 6 is wrong physically: a bicycle pump gets hot, and compressing a gas adiabatically must raise its temperature (work is done on the gas, and no heat leaves). Timur did not need to find the algebraic error to know there was one. **The physical limiting case condemned the derivation in ten seconds.**

### Then find the step

Reading backwards from the sign: step 4 integrated −R dV/V and wrote +R ln(V₂/V₁). The minus sign was dropped between step 3 and step 4. The correct result is

C_v ln(T₂/T₁) = −R ln(V₂/V₁), hence T₂ = T₁ (V₁/V₂)^(γ−1),

which rises for compression, as it must.

### Dimensional check

Every line is dimensionally consistent, including the wrong one: a dropped sign does not change units. **Units catch dropped factors; limiting cases catch dropped signs.** Use both.

### A second opinion is not a check

Timur then asked the AI, in the same chat, "is this right?" It replied "Yes, the derivation is correct" and restated step 6. Asked in a *fresh* chat to derive the same thing, it produced the correct sign. The same model gave both answers. Asking an AI to confirm its own work in the same conversation is close to worthless; asking again in a fresh conversation is weak evidence; a limiting case is strong evidence.

## What to take from this

| Check | Cost | What it caught |
|-------|------|----------------|
| Physical limiting case (compression should heat) | seconds | that the result is wrong |
| Reading backwards from the sign | 2 minutes | which step |
| Units | 1 minute | nothing here, but it would catch a lost factor of R or n |
| "Is this right?" in the same chat | seconds | nothing - it agreed with itself |

AI derivations are useful as scaffolding: the structure of the argument (first law → ideal-gas substitution → separate → integrate → eliminate C_v) was exactly right and is the thing worth learning. The sign was wrong, and a student who copied it would have learned a false fact with a confident proof attached.

## Try it

Ask for a derivation of something whose answer you know (the range of a projectile, the resonance frequency of an LC circuit, the Reynolds number for the onset of turbulence in a pipe). Check units line by line, then set one parameter to a limit. Keep a tally of how often you find an error; after a few tries you will know how much to trust a first derivation from your tool.
