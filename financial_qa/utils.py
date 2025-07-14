import re

COMPANY_NAMES = ["Cipla", "Sun Pharma"]

def extract_company_and_year(question: str):
    """
    Extracts the company name and year from a financial question.

    Args:
        question (str): The input question string.

    Returns:
        tuple: (company_name, year) if found, else (None, None).
    """
    year_match = re.search(r"(20\d{2})", question)
    year = int(year_match.group(1)) if year_match else None

    company = None
    for name in COMPANY_NAMES:
        if name.lower() in question.lower():
            company = name
            break

    return company, year


def clean_question_for_retrieval(question: str, company: str, year: int):
    """
    Cleans the question by removing company and year to improve retrieval similarity.

    Args:
        question (str): The original question.
        company (str): Company name to remove.
        year (int): Year to remove.

    Returns:
        str: Cleaned version of the question.
    """
    q = question
    q = re.sub(fr"\b{company}\b", "", q, flags=re.IGNORECASE)
    q = re.sub(fr"\b{year}\b", "", q)
    q = re.sub(r"\s{2,}", " ", q).strip()
    return q
