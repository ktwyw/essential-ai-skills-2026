# Worked example 1: A prompt makeover

**Modules:** 1 (clear communication) · **Time:** 15 minutes

## The task

Maria, a second-year chemical engineering student, needs an email to her lab instructor asking to reschedule a practical session she will miss because of a conference.

## Attempt 1: the search-engine prompt

> Write an email to reschedule a lab.

**What came back (abridged):**

> Subject: Request to Reschedule Lab Session
>
> Dear [Instructor's Name],
>
> I hope this email finds you well. I am writing to request a rescheduling of my upcoming lab session due to unforeseen circumstances. I would greatly appreciate it if we could find an alternative time that works for both of us. Please let me know your availability.
>
> Thank you for your understanding.
>
> Best regards,
> [Your Name]

**Diagnosis.** Nothing is wrong, and nothing is useful. The AI had to guess the reason ("unforeseen circumstances"), the course, the date, the tone, and whether Maria has a proposal. Every guess is generic. Note the template brackets: the AI knew it was missing information and said so, in its way.

## Attempt 2: adding context

> Write an email to my lab instructor, Dr. Serikova, asking to reschedule the CHME 302 distillation lab on 14 October. I'm presenting a poster at the Student Research Conference that day. There is another section of the same lab on 16 October.

**What came back (abridged):**

> Subject: CHME 302 Distillation Lab on 14 October - Request to Attend 16 October Section
>
> Dear Dr. Serikova,
>
> I am scheduled for the CHME 302 distillation lab on Tuesday 14 October. On that day I will be presenting a poster at the Student Research Conference, so I will be unable to attend. Would it be possible for me to join the section on Thursday 16 October instead?
>
> I have attached the conference programme showing my presentation slot. I am happy to complete any pre-lab work in advance.
>
> Thank you for considering this.
>
> Kind regards,
> Maria Alieva

**Diagnosis.** Specific, polite, and it proposes a solution. Two things to catch:

- The AI invented a reassuring detail: "I have attached the conference programme". Maria has not. This is the kind of small fabrication that slips into sent emails. **Read every sentence of AI-written text as if you were signing it, because you are.**
- The days of the week (Tuesday, Thursday) were inferred, not given. In 2026, 14 October *is* a Wednesday. The AI guessed and guessed wrong; a reader with a calendar would notice.

## Attempt 3: adding constraints and format

> Same as above, plus: keep it under 120 words, no attachments mentioned, don't state days of the week, and end with a sentence offering to do the pre-lab quiz before the 16 October session. Formal but not stiff.

**What came back:**

> Subject: CHME 302 distillation lab - request to switch to the 16 October section
>
> Dear Dr. Serikova,
>
> I am registered for the CHME 302 distillation lab on 14 October, but I will be presenting a poster at the Student Research Conference that day. Could I join the 16 October section instead?
>
> I will complete the pre-lab quiz before the 16 October session so that I arrive fully prepared.
>
> Thank you for considering this request.
>
> Kind regards,
> Maria Alieva

**Diagnosis.** Ready to send after one read. 78 words. Every statement is true.

## Attempt 4: show, don't tell

For an email this short, attempt 3 is enough. But if Maria had to write ten similar emails in a particular house style, the fastest route would be to paste one good example and say "write the others in this style". One example communicates tone better than any adjective list.

## What to take from this

| Attempt | What was added | Effect |
|---------|---------------|--------|
| 1 | nothing | generic template, all guesses |
| 2 | goal + context | specific and useful, but with an invented detail and a wrong inference |
| 3 | constraints + format | correct and sendable |

The four ingredients from module 1 - goal, context, constraints, format - are not a ritual. Each one removed a specific guess the AI would otherwise have made. And even the good version needed reading: the fabricated attachment in attempt 2 is a reminder that fluent text is not checked text.

## Try it

Take the last message you asked an AI to write. List every fact in the output that you did not provide. Were they all true?
