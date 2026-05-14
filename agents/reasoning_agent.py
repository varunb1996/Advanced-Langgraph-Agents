import os
import requests
import mlflow

from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# API CONFIG
# -----------------------------

API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)

MODEL = (
    "nvidia/nemotron-3-super-120b-a12b:free"
)

# -----------------------------
# REASONING AGENT
# -----------------------------

def reasoning_agent(state):

    context = ""

    if "summarized_context" in state:

        context += "\n".join(
            state["summarized_context"]
        )

    if "dependencies" in state:

        context += (
            "\n\nDependencies:\n"
            + str(state["dependencies"])
        )

    prompt = f"""
    You are an advanced engineering AI assistant.

    Answer the question using the provided context.

    Question:
    {state['query']}

    Context:
    {context}
    """

    with mlflow.start_run(
        nested=True
    ):

        mlflow.log_param(
            "llm_model",
            MODEL
        )

        mlflow.log_param(
            "query",
            state["query"]
        )

        mlflow.log_metric(
            "context_length",
            len(context)
        )

        response = requests.post(

            "https://openrouter.ai/api/v1/chat/completions",

            headers={

                "Authorization":
                f"Bearer {API_KEY}",

                "Content-Type":
                "application/json"
            },

            json={

                "model": MODEL,

                "messages": [

                    {
                        "role": "user",

                        "content": prompt
                    }
                ]
            }
        )

        result = response.json()

        state["final_answer"] = result[
            "choices"
        ][0]["message"]["content"]

    return state