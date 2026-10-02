# Worked example 8: Units and property values

**Modules:** 8 · **Time:** 20 minutes

## The task

Dana needs the pumping power for a water line in a plant-design assignment: 12 m³/h of water at 60 °C through 180 m of 50 mm steel pipe with a 15 m rise. She asks an AI without a code tool.

## The prompt

> Calculate the pump power needed for 12 m³/h of water at 60 °C through 180 m of 50 mm diameter steel pipe with a 15 m elevation gain. Show the steps.

## What came back (abridged)

> Velocity: v = Q/A = (12/3600) / (π × 0.025²) = 1.70 m/s.
> Reynolds number: Re = ρvD/μ = 998 × 1.70 × 0.05 / 1.0 × 10⁻³ = 84 800 (turbulent).
> Friction factor (steel, ε = 0.045 mm, ε/D = 0.0009): f ≈ 0.022.
> Friction head: h_f = f (L/D)(v²/2g) = 0.022 × 3600 × 0.147 = 11.7 m.
> Total head: 15 + 11.7 = 26.7 m.
> Power: P = ρ g Q H = 998 × 9.81 × 0.00333 × 26.7 = 871 W. Allowing for 70 % pump efficiency: **1.24 kW**.

The structure is textbook-correct. Dana checked three kinds of thing.

## Check 1: recalled property values

The AI used ρ = 998 kg/m³ and μ = 1.0 mPa s. Those are values for water at **20 °C**. At 60 °C, from a steam table: ρ ≈ 983 kg/m³, μ ≈ 0.47 mPa s. The AI recalled the "default" water and ignored the temperature it had been given. Re doubles (to about 177 000); the friction factor and head change modestly (f ≈ 0.021, h_f ≈ 11.1 m), the power drops by about 3 %. Small here - but the same reflex gives a 20 % error for viscosity-dominated flows and a wrong answer for anything near a phase change.

**Rule:** a property value an AI *recalls* is a claim. Look it up, or make the AI compute it from a stated source.

## Check 2: unit conversions

The AI wrote Q = 0.00333 m³/s in the power line. 12 m³/h is 0.003333 m³/s - fine. But in the velocity line it wrote (12/3600)/(π × 0.025²) and got 1.70 m/s; the arithmetic gives 1.698, fine too. Dana recomputed both because *the failure she was looking for* - m³/h kept as m³/s, or diameter used for radius - is the commonest error in these calculations, and it costs a factor of 3600 or 4.

**Rule:** recompute every line that converts units. Those lines are short, and that is where factors of 1000 hide.

## Check 3: a reference value

An order-of-magnitude check: 12 m³/h is 3.3 kg/s; lifting that 15 m needs 3.3 × 9.81 × 15 ≈ 490 W of useful power before friction. Friction roughly doubles it; a pump at 70 % gives a bit over 1 kW. The AI's 1.24 kW is in the right place. **An estimate you can do in your head is the check that catches factor-of-ten errors**, which are the ones that embarrass people.

## The compute-not-recall version

Dana then asked:

> Write Python for the same calculation. Take ρ and μ for water at 60 °C from a table (state which), compute Re, use the Swamee-Jain equation for f with ε = 0.045 mm, and print every intermediate value with units.

The script printed ρ = 983.2 kg/m³, μ = 4.67 × 10⁻⁴ Pa s, Re = 178 000, f = 0.0211, h_f = 11.1 m, P = 1.20 kW at 70 %. Every number traceable, every unit visible, and the property values now had a source she could check.

## What to take from this

| Error class | Found by | Cost of missing it |
|-------------|----------|-------------------|
| Property values for the wrong temperature | a property table | 3 % here, 20 %+ elsewhere |
| Unit conversion slips | recomputing conversion lines | factors of 4 to 3600 |
| Everything else | an order-of-magnitude estimate | factor-of-ten errors |

The AI's method was right and its arithmetic was right; its *inputs* were stale. In engineering calculations the inputs are the thing to check first.

## Try it

Ask for the same calculation with glycerol at 30 °C instead of water. Does the AI notice that the flow is now laminar? Does its viscosity match a table?
