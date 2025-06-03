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
    file_name = Path(file.filename).name
    if not file_name:
        raise HTTPException(status_code=400, detail="Invalid file name")
    if not file_name.endswith(('.pdf', '.xls', '.xlsx')):
        raise HTTPException(status_code=400, detail="Unsupported file type. Only PDF and Excel files are allowed.")
    if len(file_name) > 255:
        raise HTTPException(status_code=400, detail="File name is too long. Maximum length is 255 characters.")
    if not file_name.isascii():
        raise HTTPException(status_code=400, detail="File name contains non-ASCII characters.")
    if not file_name.isidentifier():
        raise HTTPException(status_code=400, detail="File name contains invalid characters. Only alphanumeric characters and underscores are allowed.")
    if not file_name[0].isalpha():
        raise HTTPException(status_code=400, detail="File name must start with an alphabetic character.")
    file_path = UPLOAD_DIR / f"{file_name}.encrypted"

    try:
        content = await file.read()
        encrypted_content = encrypt_data(content)

        with open(file_path, "wb") as f:
            f.write(encrypted_content)

        return {"message": f"File '{file.filename}' encrypted and saved."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
