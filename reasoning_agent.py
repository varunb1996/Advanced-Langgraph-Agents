import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)

MODEL = "nvidia/nemotron-3-super-120b-a12b:free"


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

    Answer the question using the context.

    Question:
    {state['query']}

    Context:
    {context}
    """

    response = requests.post(

        "https://openrouter.ai/api/v1/chat/completions",

        headers={

            "Authorization": f"Bearer {API_KEY}",

            "Content-Type": "application/json"
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