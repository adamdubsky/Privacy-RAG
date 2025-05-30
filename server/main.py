from fastapi import FastAPI
from routers import upload, chat

app = FastAPI()

app.include_router(upload.router, prefix="/upload", tags=["upload"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])

@app.get("/")
def root():
    return {"message": "Secure RAG backend running"}
