import re

COMPANY_NAMES = ["Cipla", "Sun Pharma"]
def extract_company_and_year(question: str):
    year_match = re.search(r"(20\d{2})", question)
    year = int(year_match.group(1)) if year_match else None

    company = None
    for name in COMPANY_NAMES:
        if name.lower() in question.lower():
            company = name
            break

    return company, year

def clean_question_for_retrieval(question: str, company: str, year: int):
    q = re.sub(fr"\b{company}\b", "", question, flags=re.IGNORECASE)
    q = re.sub(fr"\b{year}\b", "", q)
    return re.sub(r"\s{2,}", " ", q).strip()

