import json
import mlflow
import chromadb

from sentence_transformers import SentenceTransformer

# -----------------------------
# MLflow setup
# -----------------------------

mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("Embedding Pipeline")

print("MLflow initialized")

# -----------------------------
# Load documents
# -----------------------------

with open(
    "data/processed/documents.json",
    "r",
    encoding="utf-8"
) as f:
    docs = json.load(f)

print(f"Loaded {len(docs)} documents")

texts = [doc["content"] for doc in docs]
ids = [str(i) for i in range(len(docs))]

# -----------------------------
# Load embedding model
# -----------------------------

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Embedding model loaded")

# -----------------------------
# Start MLflow run
# -----------------------------

with mlflow.start_run() as run:

    print("MLflow run started")

    embeddings = model.encode(texts).tolist()

    print("Embeddings generated")

    # Log parameters
    mlflow.log_param(
        "embedding_model",
        "all-MiniLM-L6-v2"
    )

    mlflow.log_param(
        "num_documents",
        len(texts)
    )

    # Log metrics
    mlflow.log_metric(
        "total_embeddings",
        len(embeddings)
    )

    # -----------------------------
    # ChromaDB storage
    # -----------------------------

    client = chromadb.PersistentClient(
        path="embeddings"
    )

    collection = client.get_or_create_collection(
        name="docs"
    )

    collection.add(
        documents=texts,
        embeddings=embeddings,
        ids=ids
    )

    print("Stored in ChromaDB")

    # -----------------------------
    # Log artifact
    # -----------------------------

    mlflow.log_artifact(
        "data/processed/documents.json"
    )

    print("Artifact logged")

    print(f"RUN ID: {run.info.run_id}")

print("Embedding pipeline completed")