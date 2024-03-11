import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from web import explorer, creature, user
from pathlib import Path
from typing import Generator


app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
# app.include_router(user.router)


# --- Uploading Files ---
@app.post("/small")
async def upload_small_file(small_file: bytes = File()) -> str:
    return f"file size: {len(small_file)}"


# For large files use UploadFile
@app.post("/big")
async def upload_big_file(big_file: UploadFile) -> str:
    return f"file size: {big_file.size}, name: {big_file.filename}"


# --- Downloading Files ---
@app.get("/small/{name}")
async def download_small_file(name):
    return FileResponse(name)


# Streaming Response for large files
def gen_file(path: str) -> Generator:
    with open(file=path, mode="rb") as file:
        yield file.read()


@app.get("/download_big/{name}")
async def download_big_file(name: str):
    gen_expr = gen_file(name)
    response = StreamingResponse(
        content=gen_expr,
        status_code=200,
    )
    return response


# starting uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
# run this file

# to start from terminal; run `uvicorn main:app`
