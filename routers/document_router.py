from fastapi import APIRouter, UploadFile, File
import shutil
from datetime import datetime

from rag import process_pdf

router = APIRouter(prefix="/documents")

documents = []


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    path = "uploads/" + file.filename

    with open(path, "wb") as f:

        shutil.copyfileobj(file.file, f)

    process_pdf(path)

    document = {
        "document_id": len(documents) + 1,
        "title": file.filename,
        "company_name": "ExcelR",
        "document_type": "Financial Report",
        "uploaded_by": "admin",
        "created_at": str(datetime.now()),
        "file_path": path
    }

    documents.append(document)

    return {
        "message": "File Uploaded Successfully",
        "document": document
    }


@router.get("/")
def get_documents():

    return documents


# SEARCH API SHOULD COME BEFORE document_id API
@router.get("/search/")
def search_documents(company_name: str):

    result = []

    for doc in documents:

        if company_name.lower() in doc["company_name"].lower():

            result.append(doc)

    return result


@router.get("/{document_id}")
def get_document(document_id: int):

    for doc in documents:

        if doc["document_id"] == document_id:

            return doc

    return {
        "message": "Document Not Found"
    }


@router.delete("/{document_id}")
def delete_document(document_id: int):

    for doc in documents:

        if doc["document_id"] == document_id:

            documents.remove(doc)

            return {
                "message": "Document Deleted"
            }

    return {
        "message": "Document Not Found"
    }