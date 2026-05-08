import chromadb
import mlflow

from sentence_transformers import (
    SentenceTransformer
)

# -----------------------------
# LOAD MODEL
# -----------------------------

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# LOAD CHROMADB
# -----------------------------

client = chromadb.PersistentClient(
    path="embeddings/chroma_db"
)

collection = client.get_collection(
    "knowledge_base"
)

# -----------------------------
# SEARCH FUNCTION
# -----------------------------

def search(query, doc_type=None):

    query_embedding = model.encode(
        query
    ).tolist()

    with mlflow.start_run(
        nested=True
    ):

        mlflow.log_param(
            "query",
            query
        )

        mlflow.log_param(
            "document_type",
            str(doc_type)
        )

        if doc_type:

            results = collection.query(

                query_embeddings=[
                    query_embedding
                ],

                n_results=3,

                where={
                    "type": doc_type
                }
            )

        else:

            results = collection.query(

                query_embeddings=[
                    query_embedding
                ],

                n_results=3
            )

        mlflow.log_metric(

            "results_returned",

            len(results["documents"][0])
        )

    return results