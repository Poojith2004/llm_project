import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_DIR = "./chroma_store"

def load_vectorstore():
    """
    Loads an existing Chroma vectorstore from disk.

    Returns:
        Chroma: LangChain-compatible vectorstore instance.

    Raises:
        FileNotFoundError: If Chroma directory does not exist.
    """
    if not os.path.exists(CHROMA_DIR):
        raise FileNotFoundError("❌ Chroma vectorstore directory not found.")

    embedding_model = HuggingFaceEmbeddings(model_name="intfloat/e5-large-v2")
    print("✅ Chroma vectorstore loaded.")
    return Chroma(persist_directory=CHROMA_DIR, embedding_function=embedding_model)
