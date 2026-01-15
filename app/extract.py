from app.ingest import DOCUMENT_STORE

def extract_contract_fields(document_id: str):
    doc = DOCUMENT_STORE.get(document_id)

    if not doc:
        return {"error": "Document not found"}

    text = doc["text"].lower()

    def find_section(keywords):
        # Allow passing a single string or a list/tuple of strings.
        if isinstance(keywords, str):
            keywords = [keywords]

        for keyword in keywords:
            if keyword in text:
                idx = text.find(keyword)
                return text[idx : idx + 300]
        return ""

    return {
        "parties": [],
        "effective_date": "",
        "termination": find_section(["terminate", "termination"]),
        "governing_law": find_section(["governing law", "governing-law"]),
        "payment_terms": find_section(["payment", "fees", "compensation"]),
    }
