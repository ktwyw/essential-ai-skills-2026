# Instructor notes

What strong and weak answers look like in the exercise bank, the traps students fall into, and how to grade quickly. Keep this file out of student-facing copies if you use the exercises for assessment.

## General patterns

- **The commonest weak answer is a vague judgement:** "the second prompt worked better". Ask for a specific difference every time (what guess was removed, which fact changed). Marking points in the bank are written to reward specifics.
- **Students under-report AI errors** in exercises that ask them to find some, often because they did not look hard enough rather than because there were none. A rule that helps: an exercise that asks for errors and reports none needs an explanation of what was checked.
- **"I asked the AI and it confirmed"** appears as verification in about a third of first submissions. Treat it as no verification and point to worked example 5.
- **Honesty over outcome.** Exercise 5.2 (hints-only, redo a week later) is more valuable when students report that they could not redo the problems. Grade the reflection, not the score.
- Expect the course to date: tool names, capabilities and policies change each term. The exercises are written to survive this; the instructor notes may not. Update the "traps" below from what your students actually find.

## Module 1

- 1.2 *Fabrication hunt:* strong answers list inferred facts (days of the week, titles, relationships) as well as invented ones. Weak answers list only obvious fabrications. The corrected prompt should contain an explicit "do not invent; mark gaps as [BRACKET]".
- 1.3 *Audience shift:* the expert version almost always contains an oversimplification or an outdated statement. A student who reports none has probably not read it as an expert would; ask them to compare one claim with the textbook.
- 1.5 *The specification:* the insight you are looking for is that a human colleague brings shared context that the prompt had to spell out - and that spelling it out is useful for the colleague too.

## Module 2

- 2.1 *Statistics audit:* typical result is 2-3 of 5 confirmed, 1 partly (right figure, wrong year or population), 1 not found. A student reporting 5/5 confirmed should show the sources. "Not found" is not "wrong"; make sure the two statuses are used correctly.
- 2.2 *Reference check:* the trap is grading from the title. Require the "supports claim?" column to cite a sentence or figure. Expect at least one blended reference (real title, wrong journal) - worked example 2.
- 2.3 *Bug hunt:* reward tests written first. Common missed cases: "n/a", whitespace, lower-case units, values with a degree sign. The second prompt should contain the test table.
- 2.5 *Two opinions:* the independent source is the point. A third AI run is not independent.

## Module 3

- 3.1 *Find the edge:* letter counting and 6-digit multiplication usually fail without a code tool and succeed with one; students should say which. Capital of a small country usually succeeds; recent news fails or triggers search.
- 3.2 *Variability measured:* word overlap between runs is typically 0.3-0.6 for open questions; numbers often agree. The lesson is that agreement is not correctness; look for a student who verified the number independently.
- 3.3 *Context in, context out:* the first answer (without the document) is usually a confident generic answer rather than "I cannot see it". Students who find this unremarkable have missed the point of the module.

## Module 4

- 4.1 *Task table:* the row that matters is the one for the assessed thinking (discussion, interpretation). It should say "me". Rows marked "AI" for data cleaning are a red flag - the student knows which readings are bad, the AI does not.
- 4.2 *Delegation brief:* check clauses like "make sure it is correct" are not checks. A good one names a comparison, a test, or a condition that can fail.
- 4.5 *Agent supervision:* confirm that permissions were limited (a scratch folder). An agent given the home directory for a toy task is the responsible-use failure to catch.

## Module 5

- 5.3 *Find the error in the familiar:* almost every explanation of a concept the student knows well contains something to annotate. "I found nothing" usually means the student read it as a novice. Suggest comparing with the textbook's statement of assumptions.
- 5.4 *Quiz yourself:* the deliverable must show at least one answer checked against the notes; quizzes generated from notes contain misreadings often enough that an unchecked quiz is a problem.

## Module 6

- 6.1 *Traffic lights:* personal data about classmates (grades, health, contact details) must be red regardless of the tool. Group-project data with names is a frequent "yellow" that should be red or anonymised.
- 6.3 *Injection in the wild:* strong answers connect the harm to the permissions the system had, and name a defence from the module (least privilege, human-in-the-loop, separating instructions from data). Weak answers describe the incident without the mechanism.
- 6.5 *Disclosure statement:* the template asks for tools, uses, checks, and what was the student's own. A statement that only says "AI was used for grammar" when the exercise involved drafting is the thing to catch - gently; it is often ignorance of the norm rather than dishonesty.

## Module 7

- 7.2 *Read AI code:* fabricated library functions appear regularly; a student who opened documentation will have found at least one surprise (an argument that does not exist, a deprecated call). Ask what the links showed.
- 7.5 *The pipeline:* "runs from a clean clone" is the test; clone it yourself. Missing requirements files and hard-coded paths are the usual failures and are themselves teachable.

## Module 8

- 8.1 *Dimensional detective:* about one derivation in three or four from current tools contains an error (a sign, a factor, an assumption introduced silently). Reward students who found none but can show every line checked; the habit is the outcome.
- 8.2 *Compute, don't recall:* recalled and computed answers often differ by a few percent (a property value) and sometimes by a factor (a unit). The student's hand check must be the arbiter.
- 8.3 *The packed bed:* the temperature correction is the whole exercise; a single regression through both days is the expected weak answer. The hand check should reproduce one row's permeability to two significant figures. For the extra question (repeat number), there is no effect in the data; a student who "finds" one has over-read noise - a useful discussion.
- 8.4 *Lab report with AI:* use the capstone rubric rows for verification and responsible use. The PROCESS.md should name at least one error caught; a report whose PROCESS says the AI made no errors needs a conversation.
- 8.5 *Reference list from scratch:* every DOI must resolve (run the script yourself) and each sentence must match the paper. This exercise is where students learn that the AI's job in literature work is explanation, not retrieval.

## Grading quickly

For most ★ and ★★ exercises a three-level scale is enough: *meets* (deliverable complete, marking points present), *partial* (deliverable complete, a marking point missing - name it), *redo* (deliverable incomplete or verification claimed without evidence). Oral check-ins (Teaching Guide) remain the fastest way to confirm understanding of ★★★ work.
