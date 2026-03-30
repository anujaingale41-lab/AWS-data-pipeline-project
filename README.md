#  AWS End-to-End Data Pipeline Project

##  Overview

This project demonstrates an event-driven data pipeline built using AWS services to ingest, transform, and analyze data.

---

##  Architecture

* Amazon S3 (Data Lake)
* AWS Lambda (Trigger)
* AWS Glue (ETL - PySpark)
* Amazon Athena (Query Engine)

---

##  Workflow

1. Upload raw data to S3 (`raw/`)
2. Lambda triggers Glue job automatically
3. Glue cleans and transforms data
4. Processed data stored in `processed/` (Parquet)
5. Athena used for querying

---

##  Technologies Used

* AWS S3
* AWS Lambda
* AWS Glue (PySpark)
* AWS Athena
* Python

---

##  Sample Query

```sql
SELECT type, COUNT(*)
FROM netflix_titles
GROUP BY type;
```

---

##  Key Features

* Event-driven pipeline
* Serverless architecture
* Data stored in optimized Parquet format
* Scalable and cost-efficient

---

## 🚀 Future Improvements

* Add partitioning
* Add dashboard (QuickSight)
* CI/CD pipeline
