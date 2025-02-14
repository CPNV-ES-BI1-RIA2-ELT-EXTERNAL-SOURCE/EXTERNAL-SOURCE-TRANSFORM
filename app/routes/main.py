from fastapi import APIRouter

from app.routes import jobs

api_router = APIRouter()

# TODO NGY https://fastapi.tiangolo.com/tutorial/bigger-applications/
api_router.include_router(jobs.router, prefix="/job", tags=["job"])
