import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

COMPANY_NAMES = ["Cipla", "Sun Pharma"]
CHROMA_DIR = "./chroma_store"

# Load existing Chroma DB
def load_vectorstore():
    embedding_model = HuggingFaceEmbeddings(model_name="intfloat/e5-large-v2")
    if not os.path.exists(CHROMA_DIR):
        raise FileNotFoundError("❌ Chroma vectorstore not found at the specified path.")
    print("✅ Chroma vectorstore loaded.")
    return Chroma(persist_directory=CHROMA_DIR, embedding_function=embedding_model)

