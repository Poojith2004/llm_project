from langchain_together import ChatTogether
from langchain.prompts import PromptTemplate

def get_llm():
    """
    Loads the TogetherAI model.

    Returns:
        ChatTogether: A Together-compatible chat model instance.
    """
    return ChatTogether(
        model="NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
        together_api_key="e0130414248a0d07d380f02e1bdd067d0d7c75bec1acf4e20146884a0733ba94"
    )


def get_financial_prompt():
    """
    Returns the financial prompt template for Q&A.

    Returns:
        PromptTemplate: LangChain prompt template.
    """
    return PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a financial analyst.
Using only the provided context, answer the question as clearly and precisely as possible.
Do not answer unrelated questions or summarize.

Context:
{context}

Question:
{question}

Answer:
""")



#e0130414248a0d07d380f02e1bdd067d0d7c75bec1acf4e20146884a0733ba94