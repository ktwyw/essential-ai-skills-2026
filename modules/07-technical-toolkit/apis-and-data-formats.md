# APIs and Data Formats

## Why it matters

An **API** (application programming interface) lets your code talk to another service, including AI models themselves. Once you can send a request to an AI API from Python, you move from using AI tools to building your own. **JSON** and **YAML** are the text formats that carry data between these systems and store settings.

## Learn first

**JSON**, the format most APIs use:

```json
{
  "student": "Aruzhan",
  "grades": [92, 88, 95],
  "enrolled": true
}
```

**YAML**, common for configuration files:

```yaml
student: Aruzhan
grades:
  - 92
  - 88
  - 95
enrolled: true
```

**An API request** has a URL (where), a method such as GET or POST (what kind), headers (such as your API key), and often a JSON body (the data). The response usually comes back as JSON.

## Tips for becoming proficient

- **Make one working call to an AI model's API from Python**, then build a small tool around it. See [`examples/summarize.py`](../../examples/summarize.py).
- **Open real JSON responses and read them** until their structure feels familiar. Print them with indentation: `json.dumps(data, indent=2)`.
- **Keep API keys out of your code and out of GitHub.** Store them in environment variables.
- **Read the official documentation** for any API you use. AI may remember older versions.
- **Watch your usage.** AI APIs are usually paid per use, so set spending limits.

## Practice

1. Write a JSON file describing yourself, then load it in Python with the `json` module.
2. Run `examples/summarize.py` on a text file of your choice.
3. Extend the script: ask the model to return its summary as JSON with keys `title`, `summary`, and `keywords`, then parse it in Python.

## Resources

- Claude API documentation: https://docs.claude.com/en/api/overview
- JSON: https://www.json.org
- YAML: https://yaml.org
