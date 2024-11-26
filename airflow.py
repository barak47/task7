from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import data_collection, data_preprocessing

def collect_data():
    data_collection.collect()

def preprocess_data():
    data_preprocessing.preprocess()

with DAG('weather_data_pipeline', start_date=datetime(2024, 1, 1)) as dag:
    collect_task = PythonOperator(task_id='collect_data', python_callable=collect_data)
    preprocess_task = PythonOperator(task_id='preprocess_data', python_callable=preprocess_data)
    
    collect_task >> preprocess_task
