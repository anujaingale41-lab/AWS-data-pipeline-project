import os

from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")

GLUE_JOB_NAME = os.getenv("GLUE_JOB_NAME")