from app.vector_store import VECTOR_STORE

def ask_question(question: str):
    dummy_embedding = [0.0] * 1536

    chunks = VECTOR_STORE.search(dummy_embedding, k=3)

    # ✅ HANDLE EMPTY STATE
    if not chunks:
        return {
            "answer": "No documents have been ingested yet, or no relevant content was found.",
            "citations": []
        }

    answer = (
        "Based on the uploaded contract, the following excerpts are relevant "
        "to your question."
    )

    citations = [
        {
            "source": "uploaded_contract",
            "excerpt": chunk[:300]
        }
        for chunk in chunks
    ]

    return {
        "answer": answer,
        "citations": citations
    }
