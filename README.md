# AWS Data Pipeline Orchestration Platform

A production-oriented cloud data engineering project that orchestrates AWS Glue ETL pipelines using FastAPI and Boto3. This project demonstrates backend-driven ETL orchestration, cloud integration, REST APIs, and AWS-based data processing workflows.

---

# Project Overview

This system enables triggering and monitoring AWS Glue ETL jobs through REST APIs built using FastAPI.

The pipeline processes raw Netflix dataset files using AWS Glue (PySpark), stores transformed data in Amazon S3, and exposes orchestration APIs for pipeline execution and monitoring.

---

# Architecture

```text id="0jlwms"
Client
   ↓
FastAPI REST API
   ↓
Route Layer
   ↓
Service Layer
   ↓
Boto3 AWS SDK
   ↓
AWS Glue ETL Job
   ↓
PySpark Transformations
   ↓
Amazon S3 Processed Data
```

---

# Features

* FastAPI backend APIs
* AWS Glue ETL orchestration
* Boto3 AWS integration
* REST-based pipeline triggering
* Glue job status monitoring
* Environment variable configuration
* Modular backend architecture
* S3-based processed data storage
* Swagger API documentation
* Logging-ready backend structure

---

# Tech Stack

## Backend

* Python
* FastAPI
* Uvicorn

## Cloud & Data Engineering

* AWS Glue
* Amazon S3
* Boto3
* PySpark

## Development Tools

* VS Code
* Git
* GitHub
* python-dotenv

---

# Project Structure

```text id="9jlwmd"
AWS-data-pipeline-project/
│
├── app/
│   ├── routes/
│   │   └── pipeline_routes.py
│   │
│   ├── services/
│   │   └── glue_services.py
│   │
│   ├── utils/
│   │   └── logger.py
│   │
│   └── main.py
│
├── configs/
│   └── config.py
│
├── pipelines/
│   └── netflix_etl_pipeline.py
│
├── logs/
├── tests/
├── docs/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# API Endpoints

## Health Check

```http id="7jlwmy"
GET /health
```

Checks backend health status.

---

## Run Pipeline

```http id="6jlwmb"
POST /run-pipeline
```

Triggers AWS Glue ETL job execution.

### Sample Response

```json id="1jlwmu"
{
  "status": "started",
  "job_run_id": "jr_xxxxxxxxx"
}
```

---

## Get Pipeline Status

```http id="0jlwms"
GET /job-status/{job_run_id}
```

Returns current Glue job execution status.

### Possible Status Values

* STARTING
* RUNNING
* SUCCEEDED
* FAILED
* STOPPED
* TIMEOUT

---

# Environment Variables

Created an `.env` file in the project root.

---

# AWS Services Used

* AWS Glue
* Amazon S3
* AWS IAM
* CloudWatch Logs

---

# How to Run Locally

## Clone Repository

```bash id="1jlwmu"
git clone <repository-url>
cd AWS-data-pipeline-project
```

---

## Create Virtual Environment

```bash id="0jlwms"
python -m venv .venv
```

---

## Activate Environment

### Windows

```bash id="9jlwmd"
.\.venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash id="7jlwmy"
pip install -r requirements.txt
```

---

## Run FastAPI Server

```bash id="6jlwmb"
python -m uvicorn app.main:app --reload
```

---

## Open Swagger Docs

```text id="1jlwmu"
http://127.0.0.1:8000/docs
```

---

# ETL Workflow

1. FastAPI endpoint triggers AWS Glue job
2. Glue job reads raw dataset from AWS Glue Catalog
3. PySpark transformations are applied
4. Processed data is written to Amazon S3 in Parquet format
5. API monitors job execution status

---

# Current Improvements Implemented

* Refactored monolithic ETL architecture
* Added backend orchestration layer
* Added AWS SDK integration
* Added modular project structure
* Added environment-based configuration
* Added API-based job monitoring
* Added scalable service architecture


---

# Author

Anuja Ingale

Data Engineering | Backend Engineering | Cloud Data Platforms
