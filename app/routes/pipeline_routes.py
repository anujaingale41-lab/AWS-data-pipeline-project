from fastapi import APIRouter, HTTPException
from app.services.glue_services import trigger_glue_job, get_job_status 

router = APIRouter()

@router.post("/run-pipeline")
def execute_pipeline():
    
    try:
        job_run_id = trigger_glue_job()

        return {
            'status':'success',
            'message':'Pipeline executed properly',
            'job_run_id': job_run_id
        }
    except Exception as e:
        return {
            'status':'error',
            'message':str(e)
        }
    
@router.get("/pipeline-status/{job_run_id}")
def check_job_status(job_run_id: str):

    try:
        status = get_job_status(job_run_id)

        return {
            'status':'success',
            'job_run_id': job_run_id,
            'job_status': status
        }
    except Exception as e:
        return {
            'status':'error',
            'message':str(e)
        }
    