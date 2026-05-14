from tools.retrieval_tool import (
    retrieve_documents
)


def pdf_agent(state):

    query = state["query"]

    results = retrieve_documents(
        query,
        doc_type="pdf"
    )

    state["pdf_results"] = results

    return state