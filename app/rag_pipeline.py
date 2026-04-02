from translator import translate_to_english, translate_back
from embeddings import get_relevant_context

def get_response(query):
    # Step 1: Translate to English
    query_en = translate_to_english(query)

    # Step 2: Get relevant data
    context = get_relevant_context(query_en)

    # Step 3: Generate response (dummy AI)
    answer = f"Based on law: {context}"

    # Step 4: Translate back
    final_answer = translate_back(answer)

    return final_answer
