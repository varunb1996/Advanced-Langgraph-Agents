from pypdf import PdfReader
from pathlib import Path
import json

DATA = []

def chunk_text(text, chunk_size=500, overlap=100):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks

# -----------------------------
# PDF INGESTION
# -----------------------------

pdf_dir = Path("data/pdfs")

for pdf_file in pdf_dir.glob("*.pdf"):

    reader = PdfReader(str(pdf_file))

    text = ""

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    chunks = chunk_text(text)

    for idx, chunk in enumerate(chunks):

        DATA.append({
            "type": "pdf",
            "source": str(pdf_file),
            "chunk_id": idx,
            "content": chunk
        })

# -----------------------------
# CODE INGESTION
# -----------------------------

repo_dir = Path("data/repos/langchain")

TARGET_FOLDERS = [
    "chains",
    "retrievers",
    "vectorstores"
]

for folder in TARGET_FOLDERS:

    target_path = repo_dir / "libs/langchain/langchain" / folder

    for file in target_path.rglob("*.py"):

        try:

            content = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            chunks = chunk_text(content)

            for idx, chunk in enumerate(chunks):

                DATA.append({
                    "type": "code",
                    "source": str(file),
                    "folder": folder,
                    "chunk_id": idx,
                    "content": chunk
                })

        except:
            pass

Path("data/processed").mkdir(
    parents=True,
    exist_ok=True
)

with open(
    "data/processed/documents.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(DATA, f, indent=2)

print("Ingestion complete")