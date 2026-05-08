import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="embeddings/chroma_db"
)

collection = client.get_collection(
    "knowledge_base"
)

def search(query, doc_type=None):

    query_embedding = model.encode(query).tolist()

    if doc_type:

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3,
            where={"type": doc_type}
        )

    else:

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3
        )

    return results