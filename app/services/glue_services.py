import boto3
import os

from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv('AWS_REGION')
Glue_JOB_NAME = os.getenv('GLUE_JOB_NAME')

glue_client = boto3.client('glue',
                           region_name=AWS_REGION
)

def trigger_glue_job():

    response = glue_client.start_job_run(
        JobName= Glue_JOB_NAME
    )
    print(response)

    return response.get('JobRunId')

def get_job_status(job_run_id):
    response = glue_client.get_job_run(
        JobName = Glue_JOB_NAME,
        RunId = job_run_id
    )
    return response['JobRunId']['JobRunState']