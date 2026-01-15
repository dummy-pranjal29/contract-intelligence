from fastapi import FastAPI, UploadFile, File
from app.ingest import ingest_pdf

app = FastAPI(title="Contract Intelligence API")

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

@app.post("/ingest")
async def ingest(files: list[UploadFile] = File(...)):
    document_ids = []

    for file in files:
        doc_id = ingest_pdf(file)
        document_ids.append(doc_id)

    return {"document_ids": document_ids}
