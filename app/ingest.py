import uuid
import pdfplumber
from fastapi import UploadFile
from app.store import DOCUMENT_STORE
from app.llm import embed_text
from app.vector_store import VECTOR_STORE


def chunk_text(text: str, size: int = 500):
    for i in range(0, len(text), size):
        yield text[i:i + size]

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

    # TEMP: store text only (embedding disabled for stability)
    # Keep this logic inside the function so `text`/`doc_id` are in-scope.
    for chunk in chunk_text(text):
        dummy_embedding = [0.0] * 1536
        VECTOR_STORE.add(dummy_embedding, chunk)

    return doc_id
