from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Define the default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 8),
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'hello_airflow',
    default_args=default_args,
    description='A simple Hello World DAG',
    schedule_interval='@daily',
)

# Define the task
def print_hello():
    print("Hello, Airflow!")

# Create the task
hello_task = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)