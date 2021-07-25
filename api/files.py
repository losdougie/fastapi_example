from typing import List
from fastapi import APIRouter, File, UploadFile

router = APIRouter(prefix="/files")

@router.post("/filesize/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}

@router.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}