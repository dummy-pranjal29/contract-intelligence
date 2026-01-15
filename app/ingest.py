import uuid
import pdfplumber
from fastapi import UploadFile

DOCUMENT_STORE = {}

def ingest_pdf(file: UploadFile) -> str:
    text = ""

    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

    doc_id = str(uuid.uuid4())

    DOCUMENT_STORE[doc_id] = {
        "filename": file.filename,
        "text": text
    }

    return doc_id
