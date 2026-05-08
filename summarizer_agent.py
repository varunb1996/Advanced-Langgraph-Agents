def summarizer_agent(state):

    combined_context = []

    if "pdf_results" in state:

        combined_context.extend(
            state["pdf_results"]["documents"][0]
        )

    if "code_results" in state:

        combined_context.extend(
            state["code_results"]["documents"][0]
        )

    unique_context = list(
        dict.fromkeys(combined_context)
    )

    summarized_context = unique_context[:5]

    state["summarized_context"] = (
        summarized_context
    )

    return state