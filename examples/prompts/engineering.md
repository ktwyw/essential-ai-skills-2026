# Prompts for engineering problem solving

Every prompt here asks for something that can be checked by units, limits, code, or a reference value (module 8).

## Derivation with built-in checks

```
Derive [quantity] for [system] starting from [first principles / governing equation]. Number each step. After the final expression: (1) check the units of every term, (2) evaluate the limit [parameter → 0 or ∞] and state whether it is physically sensible, (3) list every assumption used and the step it was introduced in.
```

*Then do the checks yourself.* Worked example 5 shows an AI that passed its own unit check with a sign error.

## Calculation as code

```
Compute [quantity] for: [inputs with units]. Write and run Python that does the calculation with explicit unit conversions, prints intermediate quantities with units, and prints the result. Use these property values with their sources: [list], or state clearly which values you assumed.
```

*Why:* a recalled number is a claim; a computed one is a calculation you can read.

## Design calculation with a reference check

```
Size a [pump / heat exchanger / beam / pipe] for [duty]: [all specifications with units]. Show the method (standard / correlation used, with its validity range and whether my inputs are inside it), the calculation as code, and the result. Then compare with a rule-of-thumb or reference value and comment on any difference larger than 20 %.
```

## Which model applies?

```
For [situation with numbers], which of these models applies: [list, e.g. laminar vs turbulent correlation; ideal vs real gas; thin-wall vs thick-wall]? Compute the dimensionless numbers or criteria that decide, show the values, and state the decision. If it is borderline, say so and what to do.
```

## Error and uncertainty propagation

```
The result R = [formula] is computed from measured quantities [list with values and uncertainties]. Propagate the uncertainties to R (show the partial derivatives or a Monte Carlo with 10 000 samples, as code), and identify which input contributes most to the uncertainty of R.
```

## Safety and failure modes

```
I am planning [experiment / process] with [conditions, chemicals, equipment]. List the hazards you can identify from this description, the standard control for each, and what information you would need to assess the ones you cannot. Mark anything that must be checked against the safety data sheet or a competent person; do not guess thresholds.
```

*This is one of the places where the "do not guess" clause is essential, and where the AI's answer is a starting list for a human review, never the review itself.*

## Interpreting a correlation or chart

```
Explain how to use [correlation / chart, e.g. the Moody chart] for [case]: the inputs, their units, the range of validity, and the typical accuracy. Then walk through one example with my numbers: [inputs]. Show every intermediate value.
```

## Unit conversion with a trace

```
Convert [value with unit] to [unit]. Show the conversion chain factor by factor, with the source of each factor, and the final value to [n] significant figures.
```
