from tools.retrieval_tool import (
    retrieve_documents
)


def code_agent(state):

    query = state["query"]

    results = retrieve_documents(
        query,
        doc_type="code"
    )

    state["code_results"] = results

    return state