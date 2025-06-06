from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import psycopg2
import os
from ml_model.predict import predict

def run_scoring():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()
    cur.execute("SELECT id, age, income, loan_amount FROM applications WHERE status = 'pending'")
    rows = cur.fetchall()
    for row in rows:
        app_id, age, income, loan_amount = row
        score = predict({"age": age, "income": income, "loan_amount": loan_amount})
        status = 'approved' if score > 0.5 else 'rejected'
        cur.execute("UPDATE applications SET score=%s, status=%s WHERE id=%s", (score, status, app_id))
    conn.commit()
    cur.close()
    conn.close()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('credit_risk_scoring', default_args=default_args, schedule_interval='*/5 * * * *')

predict_task = PythonOperator(
    task_id='run_credit_scoring',
    python_callable=run_scoring,
    dag=dag
)

predict_task
