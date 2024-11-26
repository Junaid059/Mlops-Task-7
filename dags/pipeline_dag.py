from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def collect_data():
    os.system("python scripts/collect_data.py")

def preprocess_data():
    os.system("python scripts/preprocess_data.py")

def train_model():
    os.system("python scripts/train_model.py")

with DAG("weather_pipeline", start_date=datetime(2024, 11, 1), schedule_interval="@daily", catchup=False) as dag:
    collect_task = PythonOperator(task_id="collect_data", python_callable=collect_data)
    preprocess_task = PythonOperator(task_id="preprocess_data", python_callable=preprocess_data)
    train_task = PythonOperator(task_id="train_model", python_callable=train_model)

    collect_task >> preprocess_task >> train_task
