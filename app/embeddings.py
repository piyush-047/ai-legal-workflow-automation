import json

def get_relevant_context(query):
    with open("../data/constitution.json", "r") as file:
        data = json.load(file)

    # Simple search logic
    for key, value in data.items():
        if "life" in query.lower():
            return value

    return "No relevant law found"
