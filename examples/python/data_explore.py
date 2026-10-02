"""
data_explore.py: a one-page profile of a CSV file to read before you ask an AI about the data.

Usage:
    python examples/python/data_explore.py path/to/file.csv

Prints the shape, each column's type, non-null count, range and a few example values, the number of
missing values, duplicate rows, and columns that look like categories. Paste the output into your prompt
instead of the whole file: the AI then knows what you know (worked example 4).

Requires: pip install pandas
No API key needed.
"""

import sys

import pandas as pd


def profile(path: str) -> str:
    df = pd.read_csv(path, comment="#")
    lines = [f"{path}: {len(df)} rows, {df.shape[1]} columns", ""]
    lines.append(f"{'column':<16}{'type':<10}{'non-null':<10}{'min':<10}{'max':<10}examples")
    for col in df.columns:
        s = df[col]
        if pd.api.types.is_numeric_dtype(s):
            lo, hi = f"{s.min():.4g}", f"{s.max():.4g}"
        else:
            lo = hi = "-"
        examples = ", ".join(str(v) for v in s.dropna().unique()[:3])
        lines.append(f"{col:<16}{s.dtype!s:<10}{s.notna().sum():<10}{lo:<10}{hi:<10}{examples}")
    missing = df.isna().sum()
    missing = missing[missing > 0]
    lines.append("")
    lines.append("Missing values: " + (", ".join(f"{c} {n}" for c, n in missing.items()) if len(missing) else "none"))
    lines.append(f"Duplicate rows: {int(df.duplicated().sum())}")
    cats = [c for c in df.columns if df[c].nunique() <= max(10, len(df) // 10) and not pd.api.types.is_float_dtype(df[c])]
    if cats:
        lines.append("Columns that look categorical: " + ", ".join(f"{c} ({df[c].nunique()} values)" for c in cats))
    num = df.select_dtypes("number")
    if num.shape[1] >= 2:
        corr = num.corr().abs()
        pairs = [(a, b, corr.loc[a, b]) for i, a in enumerate(corr.columns) for b in corr.columns[i + 1 :] if corr.loc[a, b] > 0.8]
        if pairs:
            lines.append("Strongly correlated pairs (|r| > 0.8): " + ", ".join(f"{a}-{b} ({r:.2f})" for a, b, r in pairs))
    for c in cats:
        if pd.api.types.is_numeric_dtype(df[c]) and num.shape[1] > 1:
            spread = df.groupby(c)[[x for x in num.columns if x != c]].mean().round(3)
            lines.append(f"Means by {c}:\n{spread.to_string()}")
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python examples/python/data_explore.py path/to/file.csv")
    print(profile(sys.argv[1]))
