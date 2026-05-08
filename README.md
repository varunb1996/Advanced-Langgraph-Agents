## Advanced Agentic Engineering Assistant

An advanced multi-agent GraphRAG system built using LangGraph, FastAPI, Streamlit, ChromaDB, and free online LLMs via OpenRouter.

The project combines:

-semantic document retrieval
-repository-aware code search
-dependency parsing
-multi-agent orchestration
-context summarization
-reasoning-based response generation
-modular AI infra design
-memory/state persistence

to create an AI-powered engineering knowledge assistant capable of handling technical documents and source code repositories together.

## Tech Stack
Python
LangGraph
FastAPI
Streamlit
ChromaDB
Sentence Transformers
OpenRouter APIs
NetworkX

advanced_langgraph_agents/
│
├── agents/
├── tools/
├── data/
├── embeddings/
├── memory/
│
├── ingest.py
├── embed.py
├── retrieval.py
├── dependency_parser.py
├── langgraph_workflow.py
├── api.py
├── app.py
│
├── requirements.txt
├── .gitignore
└── README.md


# Setup & Run Workflow

## 1. Clone the repository

git clone https://github.com/varunb1996/Advanced-Langgraph-Agents.git

cd advanced_langgraph_agents

---

## 2. Create virtual environment

### Windows

python -m venv venv

venv\Scripts\activate

### Linux / Mac

python3 -m venv venv

source venv/bin/activate

---

## 3. Install dependencies

pip install -r requirements.txt

---

## 4. Create `.env` file in root folder

Add:

OPENROUTER_API_KEY=your_api_key_here

Get free API key from:
https://openrouter.ai

---

## 5. Add PDFs

Place PDFs inside:

data/pdfs/

---

## 6. Clone repository dataset

Example:

git clone https://github.com/langchain-ai/langchain.git data/repos/langchain

---

## 7. Run ingestion pipeline

python ingest.py

---

## 8. Generate embeddings

python embed.py

---

## 9. Start FastAPI backend

python -m uvicorn api:app --reload

---

## 10. Open second terminal and launch Streamlit UI

python -m streamlit run app.py

---

## 11. Open browser

FastAPI Docs:
http://127.0.0.1:8000/docs

Streamlit UI:
http://localhost:8501

## 12. MLflow Integration

This project uses MLflow for experiment tracking and observability of the LangGraph agent workflow, including embedding pipelines, query latency, parameters, metrics, and artifacts.

Run MLflow locally:

mlflow ui

Open:

http://127.0.0.1:5000
