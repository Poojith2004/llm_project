from .utils import extract_company_and_year, clean_question_for_retrieval
from .llm_setup import get_llm, get_financial_prompt
from langchain.chains import LLMChain
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainFilter

def ask_financial_question(question: str, db):
    """
    Asks a financial question grounded on vectorstore data and answers using LLM.

    Args:
        question (str): The user query.
        db (Chroma): The loaded Chroma vectorstore.

    Returns:
        str: The LLM's answer to the question.

    Raises:
        ValueError: If company or year cannot be extracted from the question.
    """
    company, year = extract_company_and_year(question)
    print("🔍 Extracted company:", company)
    print("🔍 Extracted year:", year)

    if not company or not year:
        raise ValueError("❌ Could not extract company or year from question.")

    tag = f"{company}_{year}"
    cleaned_question = clean_question_for_retrieval(question, company, year)
    print("🔍 Cleaned Question:", cleaned_question)

    retriever = ContextualCompressionRetriever(
        base_retriever=db.as_retriever(search_kwargs={"k": 5, "filter": {"tag": tag}}),
        base_compressor=LLMChainFilter.from_llm(get_llm())
    )

    docs = retriever.get_relevant_documents(cleaned_question)
    context = "\n\n".join(doc.page_content for doc in docs)

    print("\n📄 Retrieved Context:\n" + "=" * 40)
    print(context)
    print("=" * 40 + "\n")

    qa_chain = LLMChain(llm=get_llm(), prompt=get_financial_prompt())
    response = qa_chain.invoke({"context": context, "question": question})
    return response["text"] if isinstance(response, dict) else response
