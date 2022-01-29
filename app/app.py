from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import FileResponse
import subprocess as sp
import randomname as rn
import os
from fastapi import HTTPException
import sys

app = FastAPI()
dirn = os.path.dirname(os.path.abspath(__file__))

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}


@app.get("/build/{url:path}")
async def build(url: str):
    name = rn.get_name()
    sp.run([f"{dirn}/build.sh", url, name])
    apkPath = f"{dirn}/../output/{name}.apk"
    print(apkPath)
    if os.path.isfile(apkPath):
        return FileResponse(apkPath, filename=f"{name}.apk")
    else :
        raise HTTPException(status_code=403, detail="Can't process this link. Try a different one") 
