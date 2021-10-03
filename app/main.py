from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/get")
async def GetRoot():
    return {"message": "Hello get"}


@app.get("/add")
async def GetRoot():
    return {"message": "Hello add"}

#
# if __name__ == '__main__':
#     uvicorn.run("main:app", host="localhost", port=7070)
