# Architecture Overview

## System Goal

Advanced-Langgraph-Agents is a modular multi-agent engineering intelligence system built using LangGraph, FastAPI, Streamlit, ChromaDB, and free online LLMs through OpenRouter APIs.

The system is designed to combine:

- Semantic document retrieval
- Repository-aware code understanding
- Dependency analysis
- Multi-agent orchestration
- Memory-aware workflows
- Context summarization
- Code intelligence
- Reasoning-based response generation

to create an AI-powered engineering assistant capable of handling technical documents and source code repositories together.

---

# High-Level System Architecture

```text
                         ┌────────────────────┐
                         │      User Query     │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │   Streamlit UI      │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │   FastAPI Backend   │
                         └─────────┬──────────┘
                                   │
                                   ▼
                    ┌────────────────────────────┐
                    │    LangGraph Workflow       │
                    └─────────┬─────────┬────────┘
                              │         │
         ┌────────────────────┘         └────────────────────┐
         ▼                                                   ▼

┌──────────────────┐                           ┌──────────────────┐
│ Retrieval Agent   │                           │ Dependency Agent │
└─────────┬────────┘                           └─────────┬────────┘
          │                                              │
          ▼                                              ▼

┌──────────────────┐                           ┌──────────────────┐
│ ChromaDB Search  │                           │ Dependency Parser│
└──────────────────┘                           └──────────────────┘

         ┌────────────────────────────────────────────────────┐
         ▼                                                    ▼

┌──────────────────┐                           ┌──────────────────┐
│ Code Agent       │                           │ Summarizer Agent │
└─────────┬────────┘                           └─────────┬────────┘
          │                                              │
          └──────────────────┬───────────────────────────┘
                             ▼

                    ┌────────────────────┐
                    │ Reasoning Agent    │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │   Memory Agent      │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │ OpenRouter LLM API │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │   Final Response    │
                    └────────────────────┘
```

---

# Core Components

---

## 1. Document Ingestion Layer

### Purpose

Handles ingestion of:
- PDFs
- Technical documentation
- Source-code repositories

### Responsibilities

- Text extraction
- Intelligent chunking
- Metadata enrichment
- Repository parsing

### Main Files

```text
ingest.py
```

---

## 2. Embedding Pipeline

### Purpose

Converts chunks into semantic vector embeddings.

### Technologies

- Sentence Transformers
- HuggingFace Embedding Models

### Responsibilities

- Embedding generation
- Semantic representation
- Vector preparation

### Main Files

```text
embed.py
```

---

## 3. Retrieval Layer

### Purpose

Performs semantic retrieval over embedded documents and repositories.

### Technologies

- ChromaDB
- Sentence Transformers

### Responsibilities

- Similarity search
- Context retrieval
- Vector indexing

### Main Files

```text
retrieval.py
retrieval_tool.py
```

---

## 4. Dependency Intelligence Layer

### Purpose

Analyzes project dependencies and repository relationships.

### Responsibilities

- Dependency parsing
- Relationship extraction
- Package analysis
- Context enrichment

### Main Files

```text
dependency_parser.py
dependency_tool.py
```

---

## 5. Multi-Agent Workflow Layer

### Purpose

Coordinates specialized AI agents through graph-based orchestration.

### Technology

- LangGraph

### Responsibilities

- Workflow routing
- Multi-agent coordination
- State handling
- Sequential reasoning
- Context orchestration

### Main Files

```text
langgraph_workflow.py
```

---

# Agent Architecture

---

## 1. Router Agent

### Purpose

Routes incoming queries to the appropriate workflow path.

### Responsibilities

- Query classification
- Workflow selection
- Task routing

### Main File

```text
router_agent.py
```

---

## 2. Retrieval Agent

### Purpose

Handles semantic document retrieval.

### Responsibilities

- Context fetching
- Similarity retrieval
- Knowledge extraction

### Main File

```text
retrieval_agent.py
```

---

## 3. PDF Agent

### Purpose

Processes and analyzes PDF documents.

### Responsibilities

- PDF understanding
- Context extraction
- Document analysis

### Main File

```text
pdf_agent.py
```

---

## 4. Dependency Agent

### Purpose

Handles dependency analysis and repository understanding.

### Responsibilities

- Dependency reasoning
- Package relationship analysis
- Technical structure understanding

### Main File

```text
dependency_agent.py
```

---

## 5. Code Agent

### Purpose

Provides repository-aware code understanding and technical code analysis.

### Responsibilities

- Source-code understanding
- Repository-aware reasoning
- Code context extraction
- Technical code summarization
- Engineering workflow assistance

### Main File

```text
code_agent.py
```

---

## 6. Summarizer Agent

### Purpose

Creates concise contextual summaries.

### Responsibilities

- Context compression
- Information summarization
- Technical abstraction

### Main File

```text
summarizer_agent.py
```

---

## 7. Reasoning Agent

### Purpose

Generates final intelligent responses.

### Responsibilities

- Multi-context reasoning
- Final response synthesis
- Technical answer generation

### Main File

```text
reasoning_agent.py
```

---

## 8. Memory Agent

### Purpose

Maintains workflow memory and persistent context.

### Responsibilities

- State persistence
- Context retention
- Conversation continuity

### Main Files

```text
memory_agent.py
memory_tool.py
```

---

## 9. API Layer

### Purpose

Exposes backend services for querying the system.

### Technology

- FastAPI

### Responsibilities

- REST APIs
- Query handling
- Workflow execution
- Response serving

### Main Files

```text
api.py
```

---

## 10. Frontend Layer

### Purpose

Provides an interactive user interface.

### Technology

- Streamlit

### Responsibilities

- User interaction
- Query visualization
- Response rendering

### Main Files

```text
app.py
```

---

## 11. LLM Reasoning Layer

### Purpose

Provides reasoning and response generation.

### Technology

- OpenRouter APIs
- Nvidia Nemotron
- DeepSeek
- Mixtral

### Responsibilities

- Contextual reasoning
- Technical answer generation
- Multi-context synthesis

---

# Workflow Execution Pipeline

## Step 1: Document Ingestion

```text
PDFs / Code Repositories
        ↓
Chunking + Metadata Extraction
```

---

## Step 2: Embedding Generation

```text
Text Chunks
        ↓
Sentence Transformers
        ↓
Vector Embeddings
```

---

## Step 3: Vector Storage

```text
Embeddings
        ↓
ChromaDB Storage
```

---

## Step 4: User Query Processing

```text
User Query
        ↓
FastAPI Endpoint
        ↓
LangGraph Workflow
```

---

## Step 5: Multi-Agent Execution

```text
Router Agent
        ↓
Retrieval Agent
        ↓
Dependency Agent
        ↓
Code Agent
        ↓
Summarizer Agent
        ↓
Reasoning Agent
```

---

## Step 6: Memory Integration

```text
Workflow Context
        ↓
Memory Agent
        ↓
Persistent State Handling
```

---

## Step 7: Final Response Generation

```text
LLM Reasoning
        ↓
Final Technical Response
        ↓
Streamlit UI
```

---

# Tech Stack

## Backend

- Python
- FastAPI

## Frontend

- Streamlit

## Agent Framework

- LangGraph

## Retrieval

- ChromaDB
- Sentence Transformers

## Graph Intelligence

- NetworkX

## LLM APIs

- OpenRouter
- Nvidia Nemotron
- DeepSeek
- Mixtral

## Memory & State

- LangGraph State Management

---

# Project Structure

```text
advanced_langgraph_agents/
│
├── app.py
├── api.py
├── ingest.py
├── embed.py
├── retrieval.py
├── retrieval_tool.py
├── dependency_parser.py
├── dependency_tool.py
├── langgraph_workflow.py
├── requirements.txt
├── README.md
├── architecture.md
│
├── agents/
│   ├── router_agent.py
│   ├── retrieval_agent.py
│   ├── pdf_agent.py
│   ├── dependency_agent.py
│   ├── code_agent.py
│   ├── summarizer_agent.py
│   ├── reasoning_agent.py
│   └── memory_agent.py
│
├── tools/
│   ├── memory_tool.py
│   ├── retrieval_tool.py
│   └── dependency_tool.py
│
├── data/
├── embeddings/
├── memory/
├── documents/
└── utils/
```

---

# Future Improvements

- Autonomous repository understanding
- Tool-calling agents
- Multi-repository GraphRAG
- Neo4j integration
- Hybrid Retrieval (BM25 + Vector Search)
- Streaming responses
- Docker deployment
- Kubernetes orchestration
- CI/CD integration
- Long-term persistent memory
- Agent evaluation pipelines
- Multi-user sessions
- LangSmith tracing

---

# Design Philosophy

The system is intentionally designed as:

- Modular
- Extensible
- Open-source-first
- Agent-oriented
- Production-inspired
- Research-friendly

while remaining deployable locally using free APIs and lightweight infrastructure.

The architecture emphasizes:
- multi-agent collaboration
- modular orchestration
- repository intelligence
- semantic retrieval
- scalable AI workflow design
- code-aware engineering assistance

# MLflow Experiment Tracking

## Purpose

MLflow is integrated into the Advanced-Langgraph-Agents system for lightweight experiment tracking, observability, and workflow monitoring during embedding generation and retrieval workflows.

The integration helps monitor:
- Embedding pipeline execution
- Query workflows
- Retrieval operations
- Agent execution traces
- Runtime debugging
- Experiment reproducibility

---

# MLflow Architecture Integration

```text
User Query
     ↓
FastAPI Backend
     ↓
LangGraph Workflow
     ↓
MLflow Tracking Layer
     ↓
Metrics / Parameters / Traces / Logs
```

---

# MLflow Components Used

## 1. Experiment Tracking

Tracks:
- embedding runs
- retrieval runs
- workflow executions
- pipeline metadata

### Example

```python
mlflow.set_experiment("Embedding Pipeline")
```

---

## 2. Parameters Logging

Stores runtime configuration values such as:
- chunk sizes
- embedding model names
- retrieval settings
- query parameters

### Example

```python
mlflow.log_param("embedding_model", model_name)
```

---

## 3. Metrics Logging

Tracks runtime metrics such as:
- embedding latency
- retrieval latency
- execution duration
- processing statistics

### Example

```python
mlflow.log_metric("retrieval_time", retrieval_time)
```

---

## 4. Artifact Tracking

Stores generated artifacts including:
- embeddings
- logs
- temporary outputs
- experiment files

### Example

```python
mlflow.log_artifact("output.txt")
```

---

## 5. Tracing & Observability

MLflow tracing is used to monitor:
- workflow execution
- request lifecycle
- backend processing
- agent interactions

This provides lightweight observability for debugging and monitoring FastAPI workflows.

---

# MLflow Workflow Integration

## Embedding Pipeline Tracking

```text
Document Ingestion
        ↓
Chunk Creation
        ↓
Embedding Generation
        ↓
MLflow Parameter Logging
        ↓
MLflow Metrics Logging
        ↓
ChromaDB Storage
```

---

## Query Workflow Tracking

```text
User Query
        ↓
FastAPI Endpoint
        ↓
LangGraph Workflow
        ↓
Retrieval Execution
        ↓
MLflow Trace Logging
        ↓
Final Response
```

---

# MLflow UI Usage

The MLflow dashboard can be launched locally using:

```bash
mlflow ui
```

Default UI URL:

```text
http://127.0.0.1:5000
```

The dashboard can be used to inspect:
- experiments
- parameters
- metrics
- traces
- runtime logs
- artifacts

---

# MLflow Filesystem Structure

```text
mlruns/
│
├── experiment_id/
│   ├── run_id/
│   │   ├── artifacts/
│   │   ├── metrics/
│   │   ├── params/
│   │   └── tags/
```

---

# Benefits of MLflow Integration

- Lightweight experiment management
- Local observability
- Runtime debugging
- Workflow traceability
- Faster experimentation
- Reproducible embedding pipelines
- Easier monitoring of retrieval workflows

---

# Future Improvements

- SQLite backend migration
- Distributed tracking server
- Full LangGraph tracing integration
- Advanced observability dashboards
- Model versioning
- Agent performance analytics
- Production monitoring pipelines
