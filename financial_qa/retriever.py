from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainFilter
from langchain.chains import LLMChain

from .llm_setup import get_llm, get_financial_prompt

def build_compression_retriever(db):
    """
    Builds a ContextualCompressionRetriever using a document filter LLM.

    Args:
        db: A Chroma vectorstore.

    Returns:
        ContextualCompressionRetriever
    """
    llm = get_llm()
    prompt = get_financial_prompt()
    filter_chain = LLMChain(llm=llm, prompt=prompt)

    return ContextualCompressionRetriever(
        base_retriever=db.as_retriever(),
        base_compressor=LLMChainFilter.from_llm(llm)
    )
