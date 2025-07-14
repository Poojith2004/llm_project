from .llm_setup import get_llm, get_financial_prompt
from .utils import extract_company_and_year, clean_question_for_retrieval
from .retriever import get_compression_retriever
from langchain.chains import LLMChain

def ask_financial_question(question: str, db):
    company, year = extract_company_and_year(question)
    if not company or not year:
        raise ValueError("❌ Could not extract company or year from question.")

    tag = f"{company}_{year}"
    cleaned_question = clean_question_for_retrieval(question, company, year)

    llm = get_llm()
    prompt = get_financial_prompt()
    qa_chain = LLMChain(llm=llm, prompt=prompt)
    retriever = get_compression_retriever(db, tag, llm)

    print(f"🔍 Cleaned Question: {cleaned_question}")
    retrieved_docs = retriever.get_relevant_documents(cleaned_question)
    context = "\n\n".join(doc.page_content for doc in retrieved_docs)

    print("\n📄 Retrieved Context:\n" + "=" * 40)
    print(context)
    print("=" * 40 + "\n")

    response = qa_chain.invoke({"context": context, "question": question})
    return response["text"] if isinstance(response, dict) else response