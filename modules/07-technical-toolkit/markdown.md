# Markdown

## Why it matters

Markdown is a simple way to format plain text with headings, lists, links, and code. It is the native format of large language models: prompts, AI answers, documentation, and notes are usually written in it. GitHub renders it automatically, which is why this whole course is written in Markdown.

## Learn first

````markdown
# Heading 1
## Heading 2

**bold** and *italic*

- bullet item
1. numbered item

[link text](https://example.com)

`inline code`

```python
print("code block")
```

| Column A | Column B |
|----------|----------|
| value    | value    |

> a quotation

- [ ] a task to tick off
````

## Recommended editors

| Editor | Best for | Cost |
|--------|----------|------|
| **VS Code** | Technical writing alongside code and Git | Free |
| **Obsidian** | Notes and personal knowledge bases | Free for personal use |
| **Typora** | Seeing formatted text as you type | Paid |
| **HackMD** | Writing together in real time, in the browser | Free tier |
| **GitHub** | README files and project documentation | Free |

## Setting up VS Code for Markdown

1. **Install VS Code** and save files with a `.md` extension.
2. **Open the live preview** beside your text with `Ctrl+K` then `V` (`Cmd+K V` on Mac).
3. **Install extensions** from the Extensions view (`Ctrl+Shift+X`):
   - *Markdown All in One* (Yu Zhang): shortcuts, list continuation, table formatting, table of contents
   - *markdownlint* (David Anson): flags inconsistent formatting
   - *Code Spell Checker* (Street Side Software): catches typos
   - Optional: *Markdown Preview Enhanced* for PDF/HTML export, *Markdown Preview Mermaid Support* for diagrams
4. **Tune your settings.** Press `Ctrl+Shift+P`, run *Preferences: Open User Settings (JSON)*, and add:

```json
"[markdown]": {
  "editor.wordWrap": "on",
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "yzhang.markdown-all-in-one"
},
"files.trimTrailingWhitespace": true
```

## Tips for becoming proficient

- **Write all your notes, drafts, and to-do lists in Markdown for a month.** Fluency follows quickly.
- **Use a live-preview editor** so you see the result as you type.
- **Structure your prompts in Markdown** with headings and lists. Models follow well-organized instructions more reliably.
- **Read the raw source of good README files** on GitHub to learn how others structure documents.

## Practice

1. Write your own Markdown cheat sheet in VS Code, using every element above.
2. Rewrite a long prompt you used in module 1 using headings for Goal, Context, Constraints, and Format.
3. Write a README for a small project, including a table and a code block.

## Resources

- CommonMark 10-minute tutorial: https://commonmark.org/help/
- GitHub Markdown guide: https://docs.github.com/en/get-started/writing-on-github
- VS Code Markdown docs: https://code.visualstudio.com/docs/languages/markdown
