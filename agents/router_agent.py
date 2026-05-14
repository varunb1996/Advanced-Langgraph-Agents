def router_agent(state):

    query = state["query"].lower()

    if any(word in query for word in [
        "function",
        "class",
        "retriever",
        "code",
        "python"
    ]):

        state["route"] = "code"

    else:

        state["route"] = "pdf"

    return state