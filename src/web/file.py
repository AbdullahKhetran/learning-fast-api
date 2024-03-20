from fastapi import APIRouter
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from typing import Generator


router = APIRouter(prefix="/file")


# --- Uploading Files ---
@router.post("/small")
async def upload_small_file(small_file: bytes = File()) -> str:
    return f"file size: {len(small_file)}"


# For large files use UploadFile
@router.post("/big")
async def upload_big_file(big_file: UploadFile) -> str:
    return f"file size: {big_file.size}, name: {big_file.filename}"


# --- Downloading Files ---
@router.get("/small/{name}")
async def download_small_file(name):
    return FileResponse(name)


# Streaming Response for large files
def gen_file(path: str) -> Generator:
    with open(file=path, mode="rb") as file:
        yield file.read()


@router.get("/download_big/{name}")
async def download_big_file(name: str):
    gen_expr = gen_file(name)
    response = StreamingResponse(
        content=gen_expr,
        status_code=200,
    )
    return response
