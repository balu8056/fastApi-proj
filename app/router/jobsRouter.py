from fastapi import APIRouter, Response
from app.schema.jobsSchema import JobSchema
from app.controllers import jobsController

jobsRouter = APIRouter(
    prefix="/jobs",
    tags=["jobs"],
)


@jobsRouter.get("/getjobs")
async def getjobs(response: Response):
    response.status_code, res = await jobsController.getJobs()
    return res


@jobsRouter.post("/addjob")
async def addjob(job: JobSchema, response: Response):
    response.status_code, res = await jobsController.addJob(job)
    return res


@jobsRouter.post("/updatejob/{Id}")
async def updatejob(Id: str, job: JobSchema, response: Response):
    response.status_code, res = await jobsController.updateJob(Id, job)
    return res


@jobsRouter.post("/deletejob/{Id}")
async def deletejob(Id: str, response: Response):
    response.status_code, res = await jobsController.deleteJob(Id)
    return res
