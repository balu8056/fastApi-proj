from datetime import datetime
import app.db.dbhelper as esConnection
from app.schema.jobsSchema import JobSchema
from fastapi import status
from app.helpers.constants import success, failure


async def getJobs():
    status_code, res = await esConnection.getIndex(index="sample")
    if status_code == failure:
        return status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": failure, "error": res}
    return status.HTTP_200_OK, {"message": success, "data": res["hits"]}


async def addJob(job: JobSchema):
    job.created_on = datetime.now()
    status_code, res = await esConnection.insertDoc("sample", "job", job.dict())
    if status_code == failure:
        return status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": failure, "error": res}
    return status.HTTP_201_CREATED, {"message": success, "data": res}


async def updateJob(Id: str, job: JobSchema):
    del job.created_on
    job.updated_on = datetime.now()
    status_code, res = await esConnection.updateDoc("sample", Id, job.dict())
    if status_code == failure:
        return status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": failure, "error": res}
    return status.HTTP_200_OK, {"message": success, "data": res}


async def deleteJob(Id: str):
    status_code, res = await esConnection.deleteDoc("sample", Id)
    if status_code == failure:
        return status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": failure, "error": res}
    return status.HTTP_200_OK, {"message": success, "data": res}