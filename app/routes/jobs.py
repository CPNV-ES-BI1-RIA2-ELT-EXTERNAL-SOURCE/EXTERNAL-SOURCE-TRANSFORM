from fastapi import APIRouter
from app.schemas.requests import JobRequest
from app.schemas.responses import JobResponse, JobDownloadResponse
from app.services.data_transform_director import DataTransformDirector
from app.services.job_manager import JobManager

router = APIRouter()

@router.post("/{job_id}", response_model=JobResponse)
def job_objects(job_id: str, request: JobRequest):
    DataTransformDirector().transform_job_data(job_id, request.dataSource)
    return JobResponse(dataSource=request.base_url + f"/jobs/{job_id}/download")


@router.post("/{job_id}/download", response_model=JobDownloadResponse)
def job_objects_download(job_id: str):
    if not JobManager.is_existing_job(job_id):
        raise Exception(f"Job {job_id} does not exist in the system")
    return DataTransformDirector().download_job_data(job_id)