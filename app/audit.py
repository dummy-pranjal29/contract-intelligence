from app.store import DOCUMENT_STORE

def audit_contract(document_id: str):
    doc = DOCUMENT_STORE.get(document_id)
    if not doc:
        return []

    text = doc["text"].lower()
    risks = []

    if "automatically renew" in text or "auto-renew" in text:
        risks.append({
            "risk": "Auto-renewal clause detected",
            "severity": "MEDIUM",
            "evidence": "Contract contains automatic renewal language"
        })

    if "unlimited liability" in text or "without limitation of liability" in text:
        risks.append({
            "risk": "Unlimited liability detected",
            "severity": "HIGH",
            "evidence": "Liability appears to be uncapped"
        })

    if "indemnify" in text and "all claims" in text:
        risks.append({
            "risk": "Broad indemnification clause",
            "severity": "MEDIUM",
            "evidence": "Indemnification language is very broad"
        })

    return risks
