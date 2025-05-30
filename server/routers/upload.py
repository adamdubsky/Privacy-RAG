#http://localhost:8000/docs#/

import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
from services.encryption import encrypt_data

router = APIRouter()
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / f"{file.filename}.encrypted"

    try:
        content = await file.read()
        encrypted_content = encrypt_data(content)

        with open(file_path, "wb") as f:
            f.write(encrypted_content)

        return {"message": f"File '{file.filename}' encrypted and saved."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
