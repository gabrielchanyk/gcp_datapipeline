import pandas as pd
import yaml
from sqlalchemy import create_engine
from google.cloud import bigquery
import logging
import os

logging.basicConfig(level=logging.INFO)  # Ensure logs are visible

logging.info('Initializing')

yaml_path = 'yaml_sql/customers_info.yaml'
if not os.path.exists(yaml_path):
    logging.error(f"YAML file not found at: {yaml_path}")
else:
    logging.info(f"YAML file found at: {yaml_path}")

secret_path = "/secrets/my_sql_pw"

#gcp
# Read the secret value from the file
with open(secret_path, 'r') as secret_file:
    secret_value = secret_file.read().strip()

password = secret_value

# localrun
# Define the MySQL password
# password = ''


project_id = 'bellassignment-453021'

# Read MySQL URL, dataset ID, table name, and query from YAML file
with open(yaml_path, 'r') as file:
    config = yaml.safe_load(file)
    mysql_url = config['url']
    dataset_id = config['dataset_id']
    table_name = config['table']['name']
    query = config['table']['query']

# Replace <password> with the actual password
mysql_url = mysql_url.replace('<password>', password)

# Create SQLAlchemy engine
engine = create_engine(mysql_url)

# Load data into a pandas DataFrame
df = pd.read_sql(query, engine)
logging.info('df: %s', df)
# Initialize BigQuery client
client = bigquery.Client(project=project_id)

# Define BigQuery table reference
table_ref = client.dataset(dataset_id).table(table_name)

# Load data into BigQuery
job = client.load_table_from_dataframe(df, table_ref)
job.result()  # Wait for the job to complete

print(f'Data loaded into BigQuery table: {dataset_id}.{table_name}')
