# **Telecom Data Schema Design**

This document outlines the schema design for a telecom data system, focusing on three main components: **Customer**, **Billing**, and **Usage**. It also discusses the roles of different personas in schema design and includes a dashboard visualization.

---

## **Table of Contents**

1. [Introduction](#introduction)
2. [Customer](#customer)
   - [Customer Schema](#customer-schema)
   - [Customer Schema Discussion](#customer-schema-discussion)
3. [Billing](#billing)
   - [Billing Schema](#billing-schema)
   - [Billing Schema Discussion](#billing-schema-discussion)
4. [Usage](#usage)
   - [Cellular Usage](#cellular-usage)
   - [Internet Usage](#internet-usage)
   - [Usage Schema Discussion](#usage-schema-discussion)
5. [Persona Discussion on Schema Design](#persona-discussion-on-schema-design)
   - [Data Producers](#data-producers)
   - [Data Engineers](#data-engineers)
   - [Data Consumers](#data-consumers)
6. [Dashboard Visualization](#dashboard-visualization)

---

## **Introduction**

When designing the initial schemas for the tables, it was important to consider the multiple aspects of telecom usage, such as cellular, home internet, and payphones. For this example, three key components were chosen: **Customer**, **Billing**, and **Usage**.

To make the schema cleaner and more specific, two separate usage tables were created for **Home Internet** and **Cellular** usage. While these could have been combined into a single table, separating them allows for clearer insights into service types and usage patterns.

---

## **Customer**

### **Customer Schema**

| Attribute         | Data Type | Description                                       |
| ----------------- | --------- | ------------------------------------------------- |
| `customer_id`     | INT       | Primary key, auto-incremented.                    |
| `first_name`      | VARCHAR   | Customer's first name.                            |
| `last_name`       | VARCHAR   | Customer's last name.                             |
| `date_of_birth`   | DATE      | Customer's date of birth.                         |
| `email`           | VARCHAR   | Customer's email address.                         |
| `phone_number`    | VARCHAR   | Customer's contact number.                        |
| `address_line1`   | VARCHAR   | First line of the customer's address.             |
| `address_line2`   | VARCHAR   | Second line of the customer's address (optional). |
| `city`            | VARCHAR   | City of the customer's address.                   |
| `state_province`  | VARCHAR   | State or province of the customer's address.      |
| `postal_code`     | VARCHAR   | Postal or ZIP code of the customer's address.     |
| `country`         | VARCHAR   | Country of the customer's address.                |
| `activation_date` | DATE      | Date when the customer was activated.             |

### **Customer Schema Discussion**

The schema includes detailed fields such as `address_line1`, `address_line2`, `city`, `state_province`, and `postal_code` to ensure uniform and specific address information. Additional fields like `activation_date` and `date_of_birth` are included for business insights, such as customer retention and age group analysis. The `email` field is added for marketing purposes.

---

## **Billing**

### **Billing Schema**

| Attribute            | Data Type | Description                                     |
| -------------------- | --------- | ----------------------------------------------- |
| `billing_id`         | INT       | Primary key, auto-incremented.                  |
| `customer_id`        | INT       | Foreign key, references `Customers`.            |
| `billing_amount`     | DECIMAL   | Amount billed to the customer.                  |
| `billing_date`       | DATE      | Date when the bill was generated.               |
| `due_date`           | DATE      | Payment due date.                               |
| `payment_status`     | VARCHAR   | Status of the payment (e.g., paid, due).        |
| `plan_type`          | VARCHAR   | Type of plan (e.g., Basic, Premium, Unlimited). |
| `latest_billed_date` | DATE      | Date of the most recent billing.                |

### **Billing Schema Discussion**

The billing schema is straightforward, with fields like `billing_amount`, `billing_date`, and `due_date`. The addition of `latest_billed_date` helps track customer retention. The `plan_type` field provides insights into customer preferences and revenue distribution across different regions.

---

## **Usage**

### **Cellular Usage**

| Attribute      | Data Type | Description                                     |
| -------------- | --------- | ----------------------------------------------- |
| `usage_id`     | INT       | Primary key, auto-incremented.                  |
| `customer_id`  | INT       | Foreign key, references `Customers`.            |
| `service_type` | VARCHAR   | Type of service (e.g., call, SMS, data).        |
| `usage_amount` | DECIMAL   | Amount of usage (e.g., minutes, messages, MBs). |
| `usage_date`   | DATE      | Date of usage.                                  |
| `usage_time`   | TIME      | Time of usage.                                  |

### **Internet Usage**

| Attribute           | Data Type | Description                          |
| ------------------- | --------- | ------------------------------------ |
| `usage_id`          | INT       | Primary key, auto-incremented.       |
| `customer_id`       | INT       | Foreign key, references `Customers`. |
| `data_usage_amount` | DECIMAL   | Amount of data used (in MBs/GBs).    |
| `usage_date`        | DATE      | Date of usage.                       |
| `usage_time`        | TIME      | Time of usage.                       |

### **Usage Schema Discussion**

The usage data is split into two tables: **Cellular Usage** and **Home Internet Usage**. This separation allows for detailed analysis of usage patterns and billing information. It also helps identify regional trends in usage when paired with customer data.

---

## **Persona Discussion on Schema Design**

### **Data Producers**

Data producers are responsible for:

- Collaborating with other personas to determine useful data types for visualization and business insights.
- Ensuring data governance, including tagging PII/HSPII data.
- Validating data completeness and credibility.
- Deciding on the frequency of data collection (e.g., daily, hourly, weekly).

### **Data Engineers**

Data engineers focus on:

- Designing clean schemas for data cleaning and transformation.
- Using tags from data producers to maintain consistency in the ETL pipeline.
- Understanding dependencies between tables and workflows.
- Building pipelines based on insights required by data consumers.

### **Data Consumers**

Data consumers are responsible for:

- Creating dashboards and visualizations to analyze customer behavior and usage trends.
- Using data types (e.g., INT, FLOAT) to calculate averages, totals, and other metrics.
- Providing insights into revenue, marketing strategies, and platform scalability.

---

## **Dashboard Visualization**

![Telecom Visuals](visuals/telecom_visuals.png)

---
