import pymysql
import os
import csv

# Database connection parameters
db_config = {
    'user': 'avnadmin',
    'password': '',  # Add your password here
    'host': 'mysql-191e4b62-bellassignment55-04a3.g.aivencloud.com',
    'port': 18533,
    'database': 'defaultdb'
}

# Connect to the MySQL database
conn = pymysql.connect(**db_config)
cursor = conn.cursor()

# Create tables
create_tables_sql = [
    """
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        date_of_birth DATE,
        email VARCHAR(255),
        phone_number VARCHAR(50),
        address_line1 VARCHAR(255),
        address_line2 VARCHAR(255),
        city VARCHAR(100),
        state_province VARCHAR(100),
        postal_code VARCHAR(20),
        country VARCHAR(50),
        activation_date DATE
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Billing (
        billing_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        billing_amount DECIMAL(10, 2),
        billing_date DATE,
        due_date DATE,
        payment_status VARCHAR(50),
        plan_type VARCHAR(50),
        latest_billed_date DATE,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS CellularUsage (
        usage_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        service_type VARCHAR(50),
        usage_amount DECIMAL(10, 2),
        usage_date DATE,
        usage_time TIME,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS InternetUsage (
        usage_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        data_usage_amount DECIMAL(10, 2),
        usage_date DATE,
        usage_time TIME,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
    """
]

for sql in create_tables_sql:
    cursor.execute(sql)

# Define the CSV file paths in the 'csv' folder
csv_files = {
    'Customers': 'csv/customers.csv',
    'Billing': 'csv/billings.csv',
    'CellularUsage': 'csv/cellular_usages.csv',
    'InternetUsage': 'csv/internet_usages.csv'
}

# Function to load CSV data into MySQL table
def load_csv_to_table(csv_file, table_name, columns):
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            cursor.execute(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})", row)
        conn.commit()
    print (f"Loaded CSV {csv_file}")

# Load data from CSV files into the respective tables
load_csv_to_table(csv_files['Customers'], 'Customers', ['customer_id', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'address_line1', 'address_line2', 'city', 'state_province', 'postal_code', 'country', 'activation_date'])
load_csv_to_table(csv_files['CellularUsage'], 'CellularUsage', ['usage_id', 'customer_id', 'service_type', 'usage_amount', 'usage_date', 'usage_time'])
load_csv_to_table(csv_files['InternetUsage'], 'InternetUsage', ['usage_id', 'customer_id', 'data_usage_amount', 'usage_date', 'usage_time'])
load_csv_to_table(csv_files['Billing'], 'Billing', ['billing_id', 'customer_id', 'billing_amount', 'billing_date', 'due_date', 'payment_status', 'plan_type', 'latest_billed_date'])


# Close the database connection
cursor.close()
conn.close()

print("Data has been loaded into MySQL database.")
