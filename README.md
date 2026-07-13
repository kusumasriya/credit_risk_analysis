# Credit Risk Assessment Pipeline using Azure Data Factory, Azure Databricks & Microsoft Fabric

![Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Delta Lake](https://img.shields.io/badge/Delta%20Lake-003B5C?style=for-the-badge)
![ADF](https://img.shields.io/badge/Azure%20Data%20Factory-0062AD?style=for-the-badge)
![Microsoft Fabric](https://img.shields.io/badge/Microsoft%20Fabric-742774?style=for-the-badge)

---

# Project Overview

This project implements an enterprise-grade **Credit Risk Assessment Pipeline** using Microsoft Azure services following the **ELT (Extract, Load, Transform)** approach and **Medallion Architecture (Bronze → Silver → Gold).**

The pipeline ingests raw credit risk datasets from Kaggle, converts CSV files into Parquet using Azure Data Factory, stores them in Azure Data Lake Storage Gen2, processes them with Azure Databricks and Delta Lake, creates analytical Star Schema tables, and visualizes business insights using Microsoft Fabric and Power BI.

The solution demonstrates production-ready Data Engineering concepts including:

- Azure Data Factory Pipelines
- Azure Data Lake Storage Gen2
- Azure Databricks
- PySpark
- Delta Lake
- Unity Catalog
- Schema Evolution
- Watermarking
- Incremental Loading
- Audit Logging
- Error Handling
- SCD Type 2
- Delta Time Travel
- Databricks SQL Warehouse
- Microsoft Fabric
- Power BI Dashboards
- Git Integration
- CI/CD Ready Architecture

---

# Business Problem

Financial institutions process thousands of loan applications every day. Manual processing is slow, error-prone, and difficult to scale.

This project automates the complete data engineering workflow by:

- Ingesting applicant and loan datasets
- Cleaning and validating records
- Performing business transformations
- Calculating risk metrics
- Building analytical models
- Producing dashboards for business users

---

# Solution Architecture

```text
Kaggle Dataset
      │
Azure Data Factory
      │
Azure Data Lake Storage Gen2
      │
Azure Databricks
      │
Bronze
      │
Silver
      │
Gold
      │
Databricks SQL Warehouse
      │
Microsoft Fabric / Power BI
```

---

# High Level Architecture

<p align="center">
<img src="architecture/credit risk analysis_HLD.png" width="100%">
</p>

---

# Low Level Design

<p align="center">
<img src="architecture/credit risk analysis_Low level.png" width="100%">
</p>

---

# Medallion Architecture

<p align="center">
<img src="architecture/Medallion_Architecture.png" width="100%">
</p>

---

# Star Schema

<p align="center">
<img src="architecture/STAR_SCHEMA.jpeg" width="100%">
</p>

---

# Tables List (Bronze, Silver & Gold)

<p align="center">
<img src="architecture/Tabels_list.jpeg" width="100%">
</p>

---

# Technology Stack

| Layer | Technology |
|---------|------------|
| Cloud | Microsoft Azure |
| Data Ingestion | Azure Data Factory |
| Storage | Azure Data Lake Storage Gen2 |
| Processing | Azure Databricks |
| Programming | PySpark |
| Storage Format | Delta Lake |
| Governance | Unity Catalog |
| SQL Engine | Databricks SQL Warehouse |
| Dashboard | Microsoft Fabric |
| Reporting | Power BI |
| Version Control | Git |
| CI/CD | Azure DevOps |
| Testing | PyTest |

---

# Source Dataset

The project uses the following datasets:

- applicant_profiles.csv
- credit_applications.csv
- credit_history.csv
- loan_details.csv
- economic_indicators.csv

---

# ADLS Folder Structure

```text
ADLS

SRC_Files/

TGT_Files/

Bronze/

Silver/

Gold/

Archive/

Logs/
```

---

# Batch Processing Flow

```text
CSV Files
      ↓
Azure Data Factory
      ↓
Convert CSV → Parquet
      ↓
Azure Data Lake Storage Gen2
      ↓
Azure Databricks
      ↓
Bronze
      ↓
Silver
      ↓
Gold
      ↓
Databricks SQL Warehouse
      ↓
Microsoft Fabric Dashboard
```

---

# Streaming Pipeline

```text
CSV Files
      ↓
Python Producer
      ↓
Azure Event Hub
      ↓
Databricks Structured Streaming
      ↓
Bronze
      ↓
Silver
      ↓
Gold
```

---

# Bronze Layer

### Features

- Raw Data Storage
- Schema Evolution
- Watermarking
- Audit Logging
- Error Handling
- Delta Tables
- Immutable Storage

### Tables

- Bronze_Applicant_Profiles
- Bronze_Credit_Applications
- Bronze_Credit_History
- Bronze_Loan_Details
- Bronze_Economic_Indicators
- Bronze_Audit_Log
- Bronze_Error_Log

---

# Silver Layer

### Transformations

- Remove Duplicates
- Null Handling
- Data Standardization
- Type Casting
- Business Rule Validation
- Data Quality Checks
- Merge (Upsert)
- SCD Type 2
- Delta Optimization
- Time Travel

### Tables

- Silver_Applicant
- Silver_Credit
- Silver_Loan
- Silver_Economic
- Silver_Data_Quality

---

# Gold Layer

### Dimension Tables

- DIM_APPLICANT
- DIM_DATE
- DIM_REGION
- DIM_LOAN_TYPE
- DIM_CREDIT_SCORE_BAND
- DIM_ECONOMIC_INDICATOR

### Fact Table

- FACT_CREDIT_RISK

### KPI Tables

- Executive Dashboard
- Regional Dashboard
- Customer Dashboard
- Credit Risk Dashboard

---

# Business KPIs

- Total Applications
- Approved Loans
- Rejected Loans
- Average Credit Score
- Average Loan Amount
- High Risk Customers
- Default Rate
- Loan Approval Rate
- Debt-To-Income Ratio
- Loan-To-Value Ratio
- Region-wise Performance
- Risk Distribution

---

# Data Quality Checks

- Duplicate Validation
- Null Validation
- Schema Validation
- Data Type Validation
- Range Validation
- Business Rule Validation
- Referential Integrity Checks

---

# Delta Lake Features

- ACID Transactions
- Time Travel
- Merge
- Vacuum
- Optimize
- Z-Ordering
- Schema Evolution
- Delta History

---

# Security & Governance

- Unity Catalog
- RBAC
- Azure Key Vault
- Managed Identity
- Secrets Management
- Audit Logging
- Data Lineage

---

# Monitoring & Logging

- Azure Monitor
- Log Analytics
- Pipeline Monitoring
- Slack Notifications
- Email Alerts
- Error Logs
- Audit Logs

---

# Testing

- Unit Testing
- Integration Testing
- Schema Validation
- Row Count Validation
- Data Quality Testing
- Business Rule Validation

---

# Repository Structure

```text
Credit-Risk-Assessment-Pipeline
│
├── architecture
│   ├── credit risk analysis_HLD.png
│   ├── credit risk analysis_Low level.png
│   ├── Medallion_Architecture.png
│   ├── STAR_SCHEMA.jpeg
│   └── Tabels_list.jpeg
│
├── datasets
├── adf
├── databricks
├── sql
├── dashboards
├── streaming
├── tests
├── docs
├── screenshots
└── README.md
```

---

# Future Enhancements

- Machine Learning Credit Scoring
- Real-Time Fraud Detection
- Azure Synapse Integration
- Great Expectations
- Azure Purview
- Data Observability
- CI/CD Deployment using Azure DevOps

---

# Author

## CHAGARLAMUDI KUSUMA SRIYA

Azure Data Engineer

Developed an end-to-end Credit Risk Assessment Pipeline using Azure Data Factory, Azure Data Lake Storage Gen2, Azure Databricks, Delta Lake, Unity Catalog, Databricks SQL Warehouse, Microsoft Fabric, and Power BI following the Medallion Architecture.

GitHub: https://github.com/kusumasriya
