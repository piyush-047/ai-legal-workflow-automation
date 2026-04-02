from rag_pipeline import get_response

def main():
    print("⚖️ AI Legal Assistant Started (type 'exit' to quit)\n")

    while True:
        query = input("Ask legal question: ")

        if query.lower() == "exit":
            break

        response = get_response(query)
        print("Answer:", response, "\n")

if __name__ == "__main__":
    main()
