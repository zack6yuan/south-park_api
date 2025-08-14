import csv
import psycopg2

conn = psycopg2.connect(dbname="south_park", user="postgres", password="pass213", host="localhost")
cur = conn.cursor()

# Load episodes
with open('data/episodes.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cur.execute("""
            INSERT INTO episodes (name, season, episode, directed_by, written_by, release_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (row['name'], row['season'], row['episode'], row['directed_by'], row['written_by'], row['release_date']))

# Load characters
with open('data/characters.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cur.execute("""
            INSERT INTO characters (name, age, gender, voiced_by)
            VALUES (%s, %s, %s, %s)
        """, (row['name'], row['age'], row['gender'], row['voiced_by']))

conn.commit()
cur.close()
conn.close()
