# Worked example 13: A bilingual technical glossary

**Modules:** 2, 5 · **Time:** 25 minutes

## The task

A study group wants an English-Russian-Kazakh glossary of thirty terms from their fluid-mechanics course, to use when the lecture is in one language and the textbook in another.

## The prompt

> Make a table of these 30 fluid-mechanics terms in English, Russian and Kazakh: [list].

## What came back (abridged)

A clean 30-row table. The students, who between them speak all three languages, checked it against their course textbook in each language. Most rows were right. The problems:

| English | AI's Russian | AI's Kazakh | Problem |
|---------|-------------|-------------|---------|
| head (as in pump head) | голова | бас | literal "head" (the body part); the technical term is напор / арын |
| yield stress | предел текучести | аққыштық шегі | the Russian is right; the Kazakh is a word-for-word construction nobody uses - the textbook has аққыштық кернеуі |
| boundary layer | пограничный слой | шекаралық қабат | both correct |
| manometer | манометр | манометр | correct, and shows that many terms are shared loans |
| fitting (pipe fitting) | подгонка | сәйкестендіру | "fitting" read as "adjusting"; the technical term is фитинг / арматура |
| draft (in a chimney) | черновик | жоба | "draft" read as "rough version" |

Six of thirty rows were wrong or unidiomatic, and every wrong one was a **polysemous English word** translated in its everyday sense. The model has far more training text about heads and drafts in ordinary English than about pump heads and chimney drafts, so the everyday meaning wins unless the context forces the technical one.

## The checks that worked

1. **Give the context.** Changing the list to "head (pump head, m of fluid)", "fitting (pipe fitting)", "draft (chimney draft)" fixed all three polysemy errors on the next run.
2. **Back-translate.** Asking the AI to translate its own Kazakh column back into English, in a fresh chat, exposed "аққыштық шегі" (it came back as "limit of fluidity", which is not a term) and "сәйкестендіру" ("matching").
3. **Compare with the textbook.** The only reliable source for the *standard* term in a field is the field's own literature in that language. Two of the Kazakh terms the AI produced were understandable but not the ones the national curriculum uses, which matters in an exam.
4. **Ask the speaker.** For the Kazakh column the group's one native speaker was the final check, exactly as module 5 says: expertise - including linguistic expertise - is what makes the AI's output judgeable.

## The result

A thirty-row table, every term checked against a textbook, with a fourth column recording the source of each term (textbook page or standard) - which turned the glossary from "what an AI said" into something the group could defend.

## What to take from this

- For lower-resource languages the error rate is higher and the errors are plausible to a non-speaker. The checks are the same as for any AI output: context in the prompt, an independent source, a person who knows.
- Back-translation in a fresh chat is a cheap, surprisingly effective test.
- Record the source of each term. A glossary with sources is a reference; one without is a rumour.

## Try it

Make a ten-term glossary for your own course in the languages you work in. Include at least three English words with everyday meanings (head, draft, fitting, stress, yield, charge, current, moment). Count how many the AI gets right without context, then with it.
