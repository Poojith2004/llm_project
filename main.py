from financial_qa.vectorstore import load_vectorstore
from financial_qa.qa_engine import ask_financial_question

db = load_vectorstore()

question = input("Enter prompt:")
answer = ask_financial_question(question, db)

print("🧠 Answer:\n", answer)