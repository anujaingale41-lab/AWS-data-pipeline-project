from fastapi import FastAPI
from app.routes.pipeline_routes import router as pipeline_router

app= FastAPI(
    title="AWS Data Pipelien API",
    version="1.0.0"
)

app.include_router(pipeline_router)

@app.get("/")
def home():
    return{
        'message':'AWS Data Pipeline API Running'
    }

@app.get("/health")
def health_check():
    return {
        'status':'healthy'
    }