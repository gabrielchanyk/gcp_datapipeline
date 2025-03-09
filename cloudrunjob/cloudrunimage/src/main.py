import pandas as pd
import yaml
from sqlalchemy import create_engine
from google.cloud import bigquery
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def load_config(yaml_path: str) -> dict:
    """Load configuration from a YAML file."""
    if not os.path.exists(yaml_path):
        logger.error(f"YAML file not found at: {yaml_path}")
        raise FileNotFoundError(f"YAML file not found at: {yaml_path}")
    logger.info(f"YAML file found at: {yaml_path}")
    with open(yaml_path, 'r') as file:
        return yaml.safe_load(file)

def get_secret(secret_path: str) -> str:
    """Read a secret value from a file."""
    try:
        with open(secret_path, 'r') as secret_file:
            return secret_file.read().strip()
    except Exception as e:
        logger.error(f"Failed to read secret from {secret_path}: {e}")
        raise

def load_data_from_mysql(mysql_url: str, query: str) -> pd.DataFrame:
    """Load data from MySQL into a pandas DataFrame."""
    try:
        engine = create_engine(mysql_url)
        logger.info('Loading data from MySQL into DataFrame')
        df = pd.read_sql(query, engine)
        logger.info('DataFrame loaded successfully')
        return df
    except Exception as e:
        logger.error(f"Failed to load data from MySQL: {e}")
        raise

def load_data_to_bigquery(df: pd.DataFrame, project_id: str, dataset_id: str, table_name: str) -> None:
    """Load data into BigQuery."""
    try:
        client = bigquery.Client(project=project_id)
        table_ref = client.dataset(dataset_id).table(table_name)
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_TRUNCATE",
            autodetect=True
        )
        logger.info(f'Loading data into BigQuery table: {dataset_id}.{table_name}')
        job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
        job.result()  # Wait for the job to complete
        logger.info(f'Data loaded into BigQuery table: {dataset_id}.{table_name}')
    except Exception as e:
        logger.error(f"Failed to load data into BigQuery: {e}")
        raise

def main():
    logger.info('Initializing')

    # Load configuration
    yaml_path = 'yaml_sql/customers_info.yaml'
    config = load_config(yaml_path)

    # GCP
    # Read the secret value
    secret_path = "/secrets/my_sql_pw"
    password = get_secret(secret_path)

    # local
    # password = ''
    
    # Define project ID
    project_id = 'bellassignment-453021'

    # Replace <password> in the MySQL URL
    mysql_url = config['url'].replace('<password>', password)

    # Process each table in the configuration
    for table_config in config['tables']:
        table_name = table_config['name']
        query = table_config['query']

        # Load data from MySQL
        df = load_data_from_mysql(mysql_url, query)

        # Load data into BigQuery
        load_data_to_bigquery(df, project_id, config['dataset_id'], table_name)

if __name__ == "__main__":
    main()