from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from app.ingest import ingest_pdf
from app.ask import ask_question

app = FastAPI(title="Contract Intelligence API")

class AskRequest(BaseModel):
    question: str

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

@app.post("/ingest")
async def ingest(files: list[UploadFile] = File(...)):
    document_ids = []
    for file in files:
        document_ids.append(ingest_pdf(file))
    return {"document_ids": document_ids}

@app.post("/ask")
def ask(req: AskRequest):
    return ask_question(req.question)
