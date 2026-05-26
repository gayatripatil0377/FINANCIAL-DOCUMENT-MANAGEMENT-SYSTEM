from fastapi import FastAPI

from database import engine
from models import Base

from routers.auth_router import router as auth_router
from routers.document_router import router as document_router
from routers.rag_router import router as rag_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(document_router)
app.include_router(rag_router)


@app.get("/")
def home():

    return {
        "message": "Financial Document Management System"
    }