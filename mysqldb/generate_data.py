import random
import csv
import os
from faker import Faker
from datetime import datetime

# Initialize the Faker library
fake = Faker('en_CA')

# Create the 'csv' folder if it doesn't exist
os.makedirs('csv', exist_ok=True)

# Customer Table Schema
# Attribute         | Data Type | Description
# ------------------|-----------|----------------------------------
# customer_id       | INT       | Primary key, auto-incremented.
# first_name        | VARCHAR   | Customer's first name.
# last_name         | VARCHAR   | Customer's last name.
# date_of_birth     | DATE      | Customer's date of birth.
# email             | VARCHAR   | Customer's email address.
# phone_number      | VARCHAR   | Customer's contact number.
# address_line1     | VARCHAR   | First line of the customer's address.
# address_line2     | VARCHAR   | Second line of the customer's address (optional).
# city              | VARCHAR   | City of the customer's address.
# state_province    | VARCHAR   | State or province of the customer's address.
# postal_code       | VARCHAR   | Postal or ZIP code of the customer's address.
# country           | VARCHAR   | Country of the customer's address.
# activation_date   | DATE      | Date when the customer was activated.

# Billing Table Schema
# Attribute          | Data Type | Description
# -------------------|-----------|----------------------------------
# billing_id         | INT       | Primary key, auto-incremented.
# customer_id        | INT       | Foreign key, references Customers.
# billing_amount     | DECIMAL   | Amount billed to the customer.
# billing_date       | DATE      | Date when the bill was generated.
# due_date           | DATE      | Payment due date.
# payment_status     | VARCHAR   | Status of the payment (e.g., paid, due).
# plan_type          | VARCHAR   | Type of plan (e.g., Basic, Premium, Unlimited).
# latest_billed_date | DATE      | Date of the most recent billing.

# Cellular Service Usage Table Schema
# Attribute         | Data Type | Description
# ------------------|-----------|----------------------------------
# usage_id          | INT       | Primary key, auto-incremented.
# customer_id       | INT       | Foreign key, references Customers.
# service_type      | VARCHAR   | Type of service (e.g., call, SMS, data).
# usage_amount      | DECIMAL   | Amount of usage (e.g., minutes, messages, MBs).
# usage_date        | DATE      | Date of usage.
# usage_time        | TIME      | Time of usage.

# Home Internet Usage Table Schema
# Attribute         | Data Type | Description
# ------------------|-----------|----------------------------------
# usage_id          | INT       | Primary key, auto-incremented.
# customer_id       | INT       | Foreign key, references Customers.
# data_usage_amount | DECIMAL   | Amount of data used (in MBs/GBs).
# usage_date        | DATE      | Date of usage.
# usage_time        | TIME      | Time of usage.

# Function to generate a random customer
def generate_customer(customer_id):
    return {
        'customer_id': customer_id,
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=90),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
        'address_line1': fake.street_address(),
        'address_line2': fake.secondary_address(),
        'city': fake.city(),
        'state_province': fake.province(),
        'postal_code': fake.postcode(),
        'country': fake.country(),
        'activation_date': fake.date_between_dates(date_start=datetime(2020, 1, 1), date_end=datetime(2023, 12, 31))
    }

# Function to generate a random billing record
def generate_billing(customer):
    plan_types = ['Basic', 'Premium', 'Unlimited']
    return {
        'billing_id': customer['customer_id'],  # Use the same ID as the customer
        'customer_id': customer['customer_id'],
        'billing_amount': round(random.uniform(20, 200), 2),
        'billing_date': fake.date_between_dates(date_start=datetime(2022, 1, 1), date_end=datetime(2023, 12, 31)),
        'due_date': fake.date_between_dates(date_start=datetime(2022, 1, 15), date_end=datetime(2024, 1, 15)),
        'payment_status': random.choice(['Paid', 'Due']),
        'plan_type': random.choice(plan_types),
        'latest_billed_date': fake.date_between_dates(date_start=datetime(2023, 1, 1), date_end=datetime(2023, 12, 31))
    }

# Function to generate a random cellular service usage record
def generate_cellular_usage(usage_id, customer_id):
    service_types = ['call', 'SMS', 'data']
    return {
        'usage_id': usage_id,
        'customer_id': customer_id,
        'service_type': random.choice(service_types),
        'usage_amount': round(random.uniform(1, 1000), 2),
        'usage_date': fake.date_between_dates(date_start=datetime(2022, 1, 1), date_end=datetime(2023, 12, 31)),
        'usage_time': fake.time()
    }

# Function to generate a random home internet usage record
def generate_internet_usage(usage_id, customer_id):
    return {
        'usage_id': usage_id,
        'customer_id': customer_id,
        'data_usage_amount': round(random.uniform(100, 50000), 2),
        'usage_date': fake.date_between_dates(date_start=datetime(2022, 1, 1), date_end=datetime(2023, 12, 31)),
        'usage_time': fake.time()
    }

# Generate sample data
num_customers = 10000  # Change this number to generate more or fewer customers
customers = [generate_customer(i + 1) for i in range(num_customers)]
billings = [generate_billing(customers[i]) for i in range(num_customers)]
cellular_usages = [generate_cellular_usage(i + 1, random.choice(customers)['customer_id']) for i in range(num_customers)]
internet_usages = [generate_internet_usage(i + 1, random.choice(customers)['customer_id']) for i in range(num_customers)]

# Define the CSV file paths in the 'csv' folder
customers_csv_file = 'csv/customers.csv'
billings_csv_file = 'csv/billings.csv'
cellular_usage_csv_file = 'csv/cellular_usages.csv'
internet_usage_csv_file = 'csv/internet_usages.csv'

# Write the customer data to the CSV file
with open(customers_csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=customers[0].keys())
    writer.writeheader()
    writer.writerows(customers)

# Write the billing data to the CSV file
with open(billings_csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=billings[0].keys())
    writer.writeheader()
    writer.writerows(billings)

# Write the cellular usage data to the CSV file
with open(cellular_usage_csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=cellular_usages[0].keys())
    writer.writeheader()
    writer.writerows(cellular_usages)

# Write the internet usage data to the CSV file
with open(internet_usage_csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=internet_usages[0].keys())
    writer.writeheader()
    writer.writerows(internet_usages)