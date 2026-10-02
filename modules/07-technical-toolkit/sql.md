# SQL

## Why it matters

SQL is the standard language for querying databases and has stayed remarkably stable for decades. Most real-world data lives in databases, and SQL pairs naturally with Python. AI can write SQL quickly, but only you can confirm that a query answers the question you actually meant.

## Learn first

```sql
SELECT title, year FROM books;                    -- choose columns
SELECT * FROM books WHERE year > 2000;            -- filter rows
SELECT * FROM books ORDER BY year DESC;           -- sort
SELECT genre, COUNT(*) FROM books GROUP BY genre; -- summarize
SELECT b.title, a.name
FROM books b JOIN authors a ON b.author_id = a.id; -- combine tables
```

## Tips for becoming proficient

- **Practice on a small dataset on your own laptop.** SQLite and DuckDB need no server and no setup.
- **Write the query yourself first**, then compare it with the AI's version and work out why they differ.
- **Always sanity-check results** against a quick manual count. A query that runs is not necessarily a query that is right.
- **Learn to read a query aloud in plain English.** If you can't explain it, you can't trust it.

## Practice

Use the starter database in [`examples/sql/library.sql`](../../examples/sql/library.sql):

```bash
sqlite3 library.db < examples/sql/library.sql
sqlite3 library.db
```

Then answer these questions with SQL:

1. Which books were published after 2000?
2. How many books are there in each genre?
3. Which author has written the most books in the database?
4. Ask an AI to write the query for question 3. Is its answer the same as yours?

## Resources

- SQLite: https://sqlite.org
- DuckDB: https://duckdb.org
