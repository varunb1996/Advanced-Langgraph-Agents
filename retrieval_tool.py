from retrieval import search


def retrieve_documents(query, doc_type=None):

    results = search(
        query,
        doc_type=doc_type
    )

    return results