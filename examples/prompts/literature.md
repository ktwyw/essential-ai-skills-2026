# Prompts for literature work

Rule: an AI without tools cannot look things up; it can only recall and recombine. References it produces are **unverified until you open them** (worked example 2, [`check_citations.py`](../python/check_citations.py)). The safe prompts work on text *you* give it.

## Understand a paper I have

```
Here is a paper [attach / paste]. For a [second-year] student in [field], explain: (1) the question it asks, (2) the method in plain words, (3) the main result with the figure or table it comes from, (4) one limitation the authors admit and one they do not. Quote the sentence that states the main claim.
```

## Search terms, not references

```
I am looking for literature on [topic]. Give me 10 search terms and phrases, including synonyms and the names of methods or standard quantities, and three related topics I might not have thought of. Do not give me references.
```

## Summarise MY notes across papers

```
Here are my notes on [n] papers: [paste, one block per paper with my citation key]. Build a table with: paper, method, main result, conditions, limitation (from my notes only). Then write a 150-word synthesis that cites papers by my keys. Do not add any paper or claim that is not in my notes.
```

## Check a claim against a source I have

```
Does the attached paper support this claim: "[claim]"? Quote the passage that supports or contradicts it, with the section or page. If the paper does not address the claim, say so.
```

## Spot the fabrication

```
Here is a reference list an AI generated: [paste]. For each entry, state what I should verify (DOI resolves, title matches, journal matches, the paper contains the claimed result) in a checklist. Do not tell me whether they are real; you cannot know.
```

## Explain a method or equation from a paper

```
In the attached paper, equation [n] is [paste]. Explain each symbol, where the equation comes from, and the assumptions behind it. Then show what it reduces to in the limit [case] and whether that makes physical sense.
```

## Draft a related-work paragraph from verified sources

```
Using ONLY these sources, which I have read and summarised here: [keys and one-line summaries], write a 150-word related-work paragraph for a report on [topic]. Cite by key. Mark any sentence where you had to generalise beyond my summaries with [CHECK].
```
