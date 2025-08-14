DROP TABLE IF EXISTS episode;
DROP TABLE IF EXISTS characters;

CREATE TABLE IF NOT EXISTS episodes (
  id SERIAL PRIMARY KEY,
  season INT,
  episode INT,
  name TEXT,
  directed_by TEXT,
  written_by TEXT,
  release_date DATE
);

CREATE TABLE IF NOT EXISTS characters (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  age INT,
  gender TEXT,
  voiced_by TEXT
);

