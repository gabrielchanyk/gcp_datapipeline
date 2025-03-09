from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.utils.dates import days_ago
import yaml
from datetime import timedelta
import os

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),  # Start date for the DAG
    'retries': 3,  # Number of retries for each task
    'retry_delay': timedelta(minutes=5),  # Delay between retries
}

# Define the DAG
dag = DAG(
    'bq_steps_dag',
    default_args=default_args,
    schedule_interval=None,  # Disable automatic scheduling (manual trigger only)
    catchup=False,  # Disable catchup to avoid backfilling
)

# Path to the steps YAML file
steps_yaml_path = os.path.join(os.path.dirname(__file__), 'maps/steps.yaml')

# Function to load YAML file
def load_yaml_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Load the steps YAML configuration
steps_config = load_yaml_config(steps_yaml_path)

# GCP Project ID
gcp_project_id = 'bellassignment-453021'

# Dictionary to store tasks for each step
step_tasks = {}

# Loop through steps in the steps YAML file
for step, yaml_files in steps_config['steps'].items():
    step_task_list = []
    
    # Loop through YAML files in the current step
    for yaml_file in yaml_files:
        yaml_file_path = os.path.join(os.path.dirname(__file__), 'maps', yaml_file)
        config = load_yaml_config(yaml_file_path)
        
        # Loop through jobs in the current YAML file and create tasks
        for index, job in enumerate(config['jobs']):
            task_id = f"{step}_{yaml_file.replace('.yaml', '')}_task_{index + 1}"
            destination_table = f"{job['destination_dataset']}.{job['destination_table']}"
            
            # Use the query as defined in the YAML file
            query = job['query']
            
            transform_task = BigQueryInsertJobOperator(
                task_id=task_id,
                configuration={
                    "query": {
                        "query": query,  # Use the query directly from the YAML file
                        "destinationTable": {
                            "projectId": gcp_project_id,  # Use your GCP project ID
                            "datasetId": job['destination_dataset'],
                            "tableId": job['destination_table'],
                        },
                        "writeDisposition": job['write_disposition'],
                        "useLegacySql": False,
                    }
                },
                dag=dag,
            )
            
            # Add the task to the current step's task list
            step_task_list.append(transform_task)
    
    # Store the task list for the current step
    step_tasks[step] = step_task_list

# Set dependencies between steps
for i in range(len(steps_config['steps']) - 1):
    current_step = list(steps_config['steps'].keys())[i]
    next_step = list(steps_config['steps'].keys())[i + 1]
    
    # Set all tasks in the next step to depend on all tasks in the current step
    for current_task in step_tasks[current_step]:
        for next_task in step_tasks[next_step]:
            current_task >> next_task