from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

conn = psycopg2.connect(dbname="south_park", user="postgres", password="pass213", host="localhost")

@app.route("/characters", methods=["GET"])
def get_characters():
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM characters;")
        return jsonify(cur.fetchall())

@app.route("/episodes", methods=["GET"])
def get_episodes():
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM episodes;")
        return jsonify(cur.fetchall())

if __name__ == "__main__":
    app.run(debug=True)
