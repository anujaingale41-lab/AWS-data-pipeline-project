from awsglue.transforms import *
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

from configs.config import DATABASE_NAME, TABLE_NAME, S3_OUTPUT_PATH
from app.utils.logger import logging

#Initialize spark and glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark= glue.Context.spark_session
job= Job(glueContext)

def load_main():
    logger.info('Loading data from Glue Catlog')

    datasource = glueContext.crate_dynamic_frame.from_catalog(
        database=DATABASE_NAME,
        table_name=TABLE_NAME
    )

def clean_data(df):
    logger.info('Cleaning data')

    df=df.dropna()

    df=df.dropDuplicates()   
    return df

def transform_data(df):
    logger.info('Transforming data')

    df=df.withColumnRenamed('show_id','id')
    return df

def write_data(df):
    logger.info('Writing processed data to s3')

    cleaned_df= DynamicFrame.fromDF(
        df,
        glueContext,
        'cleaned_df'
    )

    glueContext.write_dynamic_frame.from_options(
        frame=cleaned_df,
        connection_type='s3',
        connection_options={'path': S3_OUTPUT_PATH},
        format='parquet'
    )

def run_pipeline():
    logger.info('Starting ETL pipeline')

    datasource= load_main()

    cleaned_data= clean_data(datasource.toDF())

    transformed_data= transform_data(cleaned_data)

    write_data(transformed_data)

    logger.info('ETL pipeline completed successfully')

if __name__ == "__main__":
    run_pipeline()