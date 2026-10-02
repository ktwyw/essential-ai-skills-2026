# LaTeX and Typst

## Why it matters

**LaTeX** is the standard for typesetting mathematics and scientific papers. It is essential in academia, mathematics, physics, and much of computer science research. **Typst** is a modern alternative with simpler syntax and fast compilation, worth considering if you are starting fresh. Outside these fields both are optional, and AI can now write most of the markup for you.

## Learn first

A minimal LaTeX document:

```latex
\documentclass{article}
\begin{document}
\section{Introduction}
The area of a circle is $A = \pi r^2$.
\[
  \int_0^1 x^2 \, dx = \frac{1}{3}
\]
\end{document}
```

The same in Typst:

```typst
= Introduction
The area of a circle is $A = pi r^2$.

$ integral_0^1 x^2 dif x = 1/3 $
```

## Tips for becoming proficient

- **Start from a template for your field** rather than a blank page.
- **Use an online editor** (Overleaf for LaTeX, the Typst web app) so there is nothing to install.
- **Let AI draft complex equations and tables**, then check that they render and mean what you intended.
- **Learn to read error messages** by line number; most errors are a missing brace or `$`.
- **Remember Markdown supports math too:** GitHub and VS Code render `$...$` in Markdown files.

## Practice

1. Write a one-page document with a title, two sections, an inline formula, and a displayed equation.
2. Ask an AI to convert a formula from a textbook photo into LaTeX. Check every symbol.
3. Recreate the same document in Typst and compare the experience.

## Resources

- Overleaf learning guides: https://www.overleaf.com/learn
- Typst documentation: https://typst.app/docs
