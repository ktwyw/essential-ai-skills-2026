-- A small practice database for the SQL exercises in module 7.
-- Load it with:  sqlite3 library.db < examples/sql/library.sql

DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    id      INTEGER PRIMARY KEY,
    name    TEXT NOT NULL,
    country TEXT
);

CREATE TABLE books (
    id        INTEGER PRIMARY KEY,
    title     TEXT NOT NULL,
    year      INTEGER,
    genre     TEXT,
    author_id INTEGER REFERENCES authors(id)
);

INSERT INTO authors (id, name, country) VALUES
    (1, 'Abai Kunanbayuly', 'Kazakhstan'),
    (2, 'Mukhtar Auezov', 'Kazakhstan'),
    (3, 'Chinghiz Aitmatov', 'Kyrgyzstan'),
    (4, 'Jane Austen', 'United Kingdom'),
    (5, 'Ursula K. Le Guin', 'United States'),
    (6, 'Chimamanda Ngozi Adichie', 'Nigeria');

INSERT INTO books (id, title, year, genre, author_id) VALUES
    (1, 'Book of Words', 1918, 'Philosophy', 1),
    (2, 'The Path of Abai', 1942, 'Historical fiction', 2),
    (3, 'Jamilia', 1958, 'Fiction', 3),
    (4, 'The Day Lasts More Than a Hundred Years', 1980, 'Fiction', 3),
    (5, 'Pride and Prejudice', 1813, 'Fiction', 4),
    (6, 'Emma', 1815, 'Fiction', 4),
    (7, 'A Wizard of Earthsea', 1968, 'Fantasy', 5),
    (8, 'The Left Hand of Darkness', 1969, 'Science fiction', 5),
    (9, 'The Dispossessed', 1974, 'Science fiction', 5),
    (10, 'Half of a Yellow Sun', 2006, 'Historical fiction', 6),
    (11, 'Americanah', 2013, 'Fiction', 6);
