# Glossary

Plain-language definitions of the terms used in this course and in the tools' own documentation. Where a term is contested or changing, the entry says so.

**Agent.** An AI system that carries out multi-step tasks on its own - browsing, editing files, running code - rather than answering a single question. Your role shifts from asking to delegating and supervising (module 4). Agents inherit every risk of the model plus the risks of the permissions they hold (module 6).

**API (application programming interface).** The way one program talks to another. Calling an AI model's API from your own code lets you automate it, pay per use, and choose the model; `examples/summarize.py` is one call.

**API key.** A secret string that identifies your account to an API. Treat it like a password: environment variable, never in code or a repository.

**Context window.** The amount of text (measured in tokens) a model can take into account at once: your prompt, pasted documents, earlier turns, and its own replies. Beyond it, earlier content is dropped or summarised. Large windows reduce but do not remove the need to say what matters (module 3).

**Fine-tuning.** Further training of a model on specific data to change its behaviour or style. Most users never need it; good prompting and provided context achieve most of what people imagine fine-tuning for.

**Grounding.** Giving a model the facts it should rely on - documents, search results, data - instead of leaving it to recall. Grounded answers can be checked against the provided material; recalled ones cannot (module 8).

**Hallucination.** Confident output that is false or unsupported: an invented statistic, a reference that does not exist, a library function that was never written. Not a glitch but a consequence of how models generate plausible text (module 3). Reduced by grounding and tools; removed only by checking.

**Large language model (LLM).** A model trained to predict the next token in text, at a scale that makes it fluent across languages, styles and domains. Assistants add instructions, tools and safety layers on top of one.

**Least privilege.** Giving a system only the permissions the current task needs. For AI agents: the scratch folder, not the drive; read, not send (module 6).

**Prompt.** Everything you give the model: the request, context, examples, constraints. A specification, not a search query (module 1).

**Prompt injection.** Instructions hidden in content the model reads (a web page, a document, an email) that it then follows as if they came from you. Dangerous in proportion to what the system can do (module 6, worked example 7).

**RAG (retrieval-augmented generation).** A system that searches a document collection for relevant passages and gives them to the model along with the question. A form of grounding; answers are only as good as what was retrieved.

**Reasoning / thinking mode.** A setting in which the model works through a problem step by step before answering, often producing visible intermediate steps. Improves multi-step tasks; does not remove the need to check each step (worked example 5).

**System prompt.** Instructions set by the tool's maker (or by you, in the API) that apply to the whole conversation: role, style, rules. Some assistants let you add your own ("custom instructions").

**Temperature.** A parameter controlling how much randomness the model uses when choosing words. Low values make answers more repeatable, not more correct (module 3, `compare_answers.py`).

**Token.** The unit models read and write, roughly three-quarters of an English word or a few characters of code. Context windows and prices are measured in tokens. Counting letters is hard for models partly because they do not see letters.

**Tool use.** The model's ability to call functions - run code, search the web, read files, query a database - and use the results. Tools cover many of the model's weaknesses (arithmetic, recency) and create new responsibilities (permissions).

**Verification.** Establishing that an output is correct by means independent of the model: a source, a test, a calculation, a limiting case, a person who knows (module 2). Asking the model whether it is right is not verification.
