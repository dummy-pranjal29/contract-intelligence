# Contract Intelligence API

A production-style backend system for automated contract analysis built using **FastAPI**.  
The application supports PDF ingestion, document-grounded question answering, structured contract field extraction, and rule-based risk auditing via clean REST APIs.

---

## 🚀 Overview

The Contract Intelligence API enables users to upload legal contract PDFs and interact with them programmatically.  
It is designed to demonstrate backend system design, API engineering, retrieval-based reasoning, and robust error handling under real-world constraints.

Key goals of the system:

- Process unstructured contract documents
- Prevent hallucinations by grounding responses in source text
- Provide predictable and explainable outputs
- Maintain clean architecture and modular design

---

## ✨ Features

- **PDF Ingestion**

  - Upload one or more contract PDFs
  - Extract and store raw text content

- **Document-Grounded Q&A**

  - Ask questions answered only from uploaded documents
  - Retrieval-first approach to avoid hallucinations

- **Structured Contract Extraction**

  - Extract key fields such as termination clauses, governing law, and payment terms
  - Deterministic, keyword-based logic for stability

- **Risk Auditing**

  - Detect risky clauses like auto-renewal, unlimited liability, and broad indemnification
  - Rule-based detection with severity classification

- **Developer Friendly**
  - RESTful APIs
  - Swagger UI for testing and exploration
  - Clean modular codebase

---

## 🏗️ Architecture

app/
├── main.py # FastAPI app & routing
├── ingest.py # PDF ingestion & text extraction
├── ask.py # Retrieval-based question answering
├── extract.py # Structured field extraction
├── audit.py # Risk detection logic
├── vector_store.py # FAISS vector store abstraction
├── store.py # Shared in-memory document store
├── llm.py # Embedding / LLM helpers (optional)
└── init.py

Shared state (documents and vectors) is centralized to avoid circular dependencies and improve maintainability.

---

## 🧪 API Endpoints

| Method | Endpoint   | Description                        |
| ------ | ---------- | ---------------------------------- |
| POST   | `/ingest`  | Upload contract PDFs               |
| POST   | `/ask`     | Ask document-grounded questions    |
| POST   | `/extract` | Extract structured contract fields |
| POST   | `/audit`   | Detect risky contract clauses      |
| GET    | `/healthz` | Health check                       |
| GET    | `/docs`    | Swagger UI                         |

---

## ⚙️ Local Setup (Without Docker)

### 1️⃣ Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the server
uvicorn app.main:app --port 8001
4️⃣ Open Swagger UI
http://127.0.0.1:8001/docs
🐳 Docker Support
The application includes full Docker support via a standard Dockerfile and requirements.txt.

Build and run (standard Docker environments)
docker build -t contract-intelligence .
docker run -p 8000:8000 contract-intelligence
Swagger UI will be available at:

http://localhost:8000/docs
⚠️ Note on Windows / WSL
On some Windows systems, Docker Desktop may fail to install due to OS-level WSL or component store issues.
In such cases, the application can be run locally using uvicorn, and the provided Dockerfile remains compatible with any standard Docker-enabled environment.



🧠 Design Decisions-------------------------------------------------------------------------------------------


FastAPI chosen for performance, clarity, and built-in OpenAPI documentation

Rule-based extraction & auditing used for deterministic, explainable behavior

Retrieval-first Q&A prevents hallucinations and ensures traceability

Centralized shared store avoids circular imports and improves stability

Graceful fallbacks implemented for empty vector indexes and missing fields



🧩 Trade-offs-------------------------------------------------------------------------------------------------


LLM-based extraction and auditing were intentionally avoided to prioritize system reliability and predictable evaluation

In-memory storage is used for simplicity; can be replaced with a database without API changes

Embeddings can be upgraded or swapped without modifying endpoint contracts

🩺 Health Check
GET /healthz
Response:

{ "status": "ok" }



📌 Summary-----------------------------------------------------------------------------------------------------


This project demonstrates:

Backend API design

Modular Python architecture

Document processing pipelines

Retrieval-augmented reasoning

Practical engineering trade-offs under real constraints

It is designed to be clear, stable, and extensible, closely resembling how production systems are built and evaluated.
```
