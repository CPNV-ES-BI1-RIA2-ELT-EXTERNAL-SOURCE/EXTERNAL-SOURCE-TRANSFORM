from fastapi import APIRouter, HTTPException
from app.schemas.requests import JobRequest
from app.schemas.responses import JobResponse
from app.services.data_transform_director import DataTransformDirector
from app.services.job_manager import JobManager

router = APIRouter()

@router.post("/{job_id}", response_model=JobResponse)
def job_objects(job_id: int, request: JobRequest):
    DataTransformDirector().transform_job_data(job_id, request.dataSource)
    return JobResponse(dataSource=f"/job/{job_id}/download")


@router.get("/{job_id}/download")
def job_objects_download(job_id: int):
    if not JobManager.is_existing_job(job_id):
        raise HTTPException(status_code=404, detail=f"Job {job_id} does not exist")
    return DataTransformDirector().download_job_data(job_id)