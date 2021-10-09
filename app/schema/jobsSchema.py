from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime


class JobSchema(BaseModel):
    source: str
    job_type: str
    job_title: str
    bgtocc: str
    jobdate: str
    state: str
    degree: str
    salary: str
    created_on: Optional[datetime] = None
    updated_on: Optional[datetime] = None
    deleted_on: Optional[str] = None
    is_deleted: Optional[str] = False
