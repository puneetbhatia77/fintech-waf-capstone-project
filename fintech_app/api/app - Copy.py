from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)
DB_URL = os.getenv("DATABASE_URL")

@app.route("/")
def index():
    return "API is running"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO applications (name, age, income, loan_amount, status)
        VALUES (%s, %s, %s, %s, %s)
    """, (data['name'], data['age'], data['income'], data['loan_amount'], 'pending'))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Application submitted."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
