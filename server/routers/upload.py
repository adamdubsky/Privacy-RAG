#http://localhost:8000/docs#/

import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path

router = APIRouter()
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    try:
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        return {"message": f"File '{file.filename}' uploaded successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
