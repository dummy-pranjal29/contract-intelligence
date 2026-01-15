from app.extract import extract_contract_fields
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


from pydantic import BaseModel

class ExtractRequest(BaseModel):
    document_id: str

@app.post("/extract")
def extract(req: ExtractRequest):
    return extract_contract_fields(req.document_id)
