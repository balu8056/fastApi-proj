from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import jobsRouter
import uvicorn

app = FastAPI()

origin = [
    "http://localhost",
    "http://localhost:3000/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
async def GetRoot():
    return {"message": "Hello world"}

app.include_router(jobsRouter.jobsRouter)

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=7070, debug=True, reload=True)
