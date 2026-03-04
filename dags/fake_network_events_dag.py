# fake_network_events_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from fake_network_events import generate_fake_events

with DAG(
    dag_id="fake_network_events_dag",
    start_date=datetime(2026, 3, 4),
    schedule_interval="*/5 * * * *",
    catchup=False,
) as dag:
    task = PythonOperator(
        task_id="generate_fake_events",
        python_callable=generate_fake_events
    )