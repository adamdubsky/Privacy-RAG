#http://localhost:8000/docs#/

from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def upload_placeholder():
    return {"message": "Upload endpoint is working"}
