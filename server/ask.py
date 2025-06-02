from services.qa_chain import answer_question

if __name__ == "__main__":
    while True:
        user_q = input("Ask a question (or 'q' to quit): ")
        if user_q.lower() == 'q':
            break
        answer = answer_question(user_q)
        print(f"\n Answer: {answer}\n")
