from financial_qa import ask_financial_question, load_vectorstore

if __name__ == "__main__":
    question = input("Enter prompt:")

    try:
        db = load_vectorstore()
        answer = ask_financial_question(question, db)
        print("🧠 Answer:\n", answer)
    except Exception as e:
        print("❌ Error:", str(e))