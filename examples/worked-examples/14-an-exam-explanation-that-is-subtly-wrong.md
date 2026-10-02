# Worked example 14: An exam explanation that is subtly wrong

**Modules:** 5, 8 · **Time:** 15 minutes

## The task

Revising chemical equilibrium, Sanzhar asks an AI to explain what happens to the equilibrium N₂ + 3H₂ ⇌ 2NH₃ when an inert gas is added.

## The prompt

> Explain, using Le Chatelier's principle, what happens to the ammonia equilibrium when argon is added to the reactor.

## What came back

> Adding an inert gas like argon increases the total pressure in the reactor. By Le Chatelier's principle, the system responds to the increase in pressure by shifting toward the side with fewer moles of gas. Since the forward reaction produces 2 moles of gas from 4, the equilibrium shifts to the right, increasing the yield of ammonia. This is why industrial reactors are operated at high pressure.

Clear, confident, well-structured - and the standard exam mistake. Sanzhar knew the topic well enough to pause at "shifts to the right".

## The check: redo it from the governing equation

Le Chatelier is a rule of thumb; the governing fact is that at equilibrium K_p = (p_NH₃)² / (p_N₂ · p_H₂³) is fixed at a given temperature, and each partial pressure is p_i = x_i P.

- **Argon added at constant volume:** the partial pressures of N₂, H₂ and NH₃ do not change (same moles, same volume, same temperature), so the reaction quotient equals K_p and **nothing shifts**. The total pressure rises, but the total pressure is not what the equilibrium depends on.
- **Argon added at constant total pressure:** the reacting gases are now diluted - each x_i falls - and the quotient changes in the direction that favours *more* moles of gas: the equilibrium shifts **left**, reducing the ammonia yield.

So the AI's answer is wrong in both cases: in one there is no shift, in the other the shift is the opposite of what it said. The last sentence ("this is why industrial reactors are operated at high pressure") is true but about compressing the *reacting* gases, not adding an inert one - a correct fact stapled to a wrong argument.

## Why the AI said it

"Pressure increases → shifts to fewer moles" is the sentence that appears most often next to "Le Chatelier" in text. The model produced the common pattern, not the analysis. The question "constant volume or constant pressure?" is exactly what a good student asks and a pattern-matcher does not.

## The tutor-mode version

In a fresh chat Sanzhar asked:

> I think adding argon at constant volume does not shift the ammonia equilibrium, because the partial pressures of the reacting gases are unchanged. Check my reasoning from K_p and the definition of partial pressure, and tell me what changes if the argon is added at constant total pressure instead.

The answer was correct in both cases and derived from K_p. The difference was that Sanzhar supplied the reasoning and asked for a check; the AI's job was to find a flaw, and there was none.

## What to take from this

- **Rules of thumb are the AI's comfort zone.** When a topic has a famous shortcut (Le Chatelier, "like dissolves like", "turbulent above Re 2300"), expect the shortcut even where it fails.
- **Redo from the governing equation.** It takes two lines and it is what the exam wants anyway.
- **The subtly wrong explanation is the one you need expertise to catch** (module 5). A student who did not know the topic would have learned a wrong fact with a persuasive argument attached - and the AI would have "confirmed" it on request.
- Put your own reasoning first and ask for a check. The quality of what comes back rises with the quality of what goes in.

## Try it

Ask an AI each of these and check against your textbook: "Does a catalyst change the equilibrium constant?", "Does increasing temperature always increase reaction rate?", "Is flow in a pipe turbulent above Re = 2300?" Each has a famous shortcut and a more careful answer.
