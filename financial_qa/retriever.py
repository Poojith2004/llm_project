from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainFilter

def get_compression_retriever(db, tag: str, llm):
    base_retriever = db.as_retriever(
        search_kwargs={
            "k": 5,
            "filter": {"tag": tag}
        }
    )
    compressor = LLMChainFilter.from_llm(llm)
    return ContextualCompressionRetriever(
        base_retriever=base_retriever,
        base_compressor=compressor
    )
