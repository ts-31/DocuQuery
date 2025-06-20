# routes/upload.py
from fastapi import APIRouter, UploadFile, File
from app.db.mongo import documents_collection
from app.utils.file_handler import extract_text_from_pdf
from datetime import datetime

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files supported for now."}
    
    content = extract_text_from_pdf(file)
    doc = {
        "filename": file.filename,
        "filetype": "pdf",
        "upload_time": datetime.utcnow(),
        "content": content
    }
    result = documents_collection.insert_one(doc)
    return {"file_id": str(result.inserted_id)}
