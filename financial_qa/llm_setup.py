from langchain_together import ChatTogether
from langchain.prompts import PromptTemplate

# Setup LLM
def get_llm():
    return ChatTogether(
        model="NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
        together_api_key="e0130414248a0d07d380f02e1bdd067d0d7c75bec1acf4e20146884a0733ba94"
    )
# Prompt template
def get_financial_prompt():
    return PromptTemplate(
        input_variables=["context", "question"],
        template="""You are a financial analyst.You have to read a lot of tables,
Using only the provided context, answer the question as clearly and precisely as possible.
Do not answer unrelated questions or summarize.

Context:
{context}

Question:
{question}

Answer:"""
    )

