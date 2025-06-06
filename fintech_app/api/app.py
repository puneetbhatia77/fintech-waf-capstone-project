# app.py
from flask import Flask, request, jsonify, render_template
import psycopg2
import os

app = Flask(__name__)
DB_URL = os.getenv("DATABASE_URL")

@app.route("/")
def index():
#    return "API is running"
#def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    name = data.get("name")
    age = data.get("age")
    income = data.get("income")
    loan_amount = data.get("loan_amount")

    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO applications (name, age, income, loan_amount, status)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, age, income, loan_amount, 'pending'))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Application submitted."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
