import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# 🔹 Load data from Glue Catalog (raw data)
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="anuja_db",
    table_name="netflix_titles_nov_2019_csv"
)

# 🔹 Convert to Spark DataFrame
df = datasource.toDF()

# 🔹 Basic Cleaning
df = df.dropna()

# 🔹 Example Transformations
df = df.withColumnRenamed("show_id", "id")

# Optional: Convert date column (if exists)
# from pyspark.sql.functions import to_date
# df = df.withColumn("date_added", to_date(df["date_added"], "MMMM d, yyyy"))

# 🔹 Convert back to DynamicFrame
from awsglue.dynamicframe import DynamicFrame
cleaned_dyf = DynamicFrame.fromDF(df, glueContext, "cleaned_dyf")

# 🔹 Write cleaned data to S3 (processed folder in Parquet format)
glueContext.write_dynamic_frame.from_options(
    frame=cleaned_dyf,
    connection_type="s3",
    connection_options={
        "path": "s3://anuja-aws-project-data/processed/"
    },
    format="parquet"
)

# Commit job
job.commit()
