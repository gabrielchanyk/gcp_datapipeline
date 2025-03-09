# **Technical Designs**

The design of the Cloud Run job and DAG creation focuses on making the system easily configurable with YAML files. This allows data producers and data scientists, even if not as technical as data engineers, to maintain and configure workflows as needed.

For data engineers, the entire end-to-end pipeline is designed with Terraform, making it easily maintainable and portable with minimal changes required (e.g., project ID or ownership).

---

## **Table of Contents**

1. [Cloud Run Job Design](#cloud-run-job-design)
2. [Composer DAG Design](#composer-dag-design)
3. [Terraform](#terraform)

---

## **Cloud Run Job Design**

The Cloud Run job is designed to use a YAML file configuration. Currently, for this project, the YAML folder is within the same image. However, the methodology is to specify a GCS bucket for YAML files, while the Cloud Run image reads and runs jobs. This approach makes the system easier to maintain and use.

### **Key Features**

- **Serverless**: Cost-effective as it runs only for as long as needed to load data.
- **Configurable**: YAML files allow for easy configuration without modifying the core code.
- **Scalable**: Can handle varying workloads efficiently.

---

## **Composer DAG Design**

The Composer DAG follows a similar design, using YAML file configuration. This is akin to `workflow.xml`, where a YAML file defines dependencies. This allows users to configure the YAML file and queries based on the complexity of the queries, including joins, unions, and other operations.

### **Key Features**

- **Flexible**: YAML files enable easy customization of workflows.
- **Dependency Management**: YAML files define dependencies, making it easier to manage complex workflows.
- **User-Friendly**: Non-technical users can configure workflows with minimal assistance.

---

## **Terraform**

The entire end-to-end data ingestion pipeline is built with Terraform, with the exception of the visualization layer (due to Looker being blocked on the free tier). This makes the pipeline easily maintainable and reproducible on demand.

### **Key Features**

- **Infrastructure as Code**: Terraform scripts define the infrastructure, making it version-controlled and reproducible.
- **Portable**: Minimal changes (e.g., project ID or ownership) are needed to deploy the pipeline in different environments.
- **Scalable**: Terraform allows for easy scaling of resources as needed.

---
