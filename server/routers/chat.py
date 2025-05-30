#http://localhost:8000/docs#/

from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def chat_placeholder():
    return {"message": "Chat endpoint is working"}
