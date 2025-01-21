from pydantic import BaseModel
from typing import List
from app.schemas.departure import Departure

class JobResponse(BaseModel):
    dataSource: str


class JobDownloadResponse(BaseModel):
    any: []