from fastapi import FastAPI

from langgraph_workflow import (
    graph
)

app = FastAPI()


@app.get("/query")

def query_agent(q: str):

    result = graph.invoke(

        {
            "query": q
        }
    )

    return {

        "query": q,

        "answer": result[
            "final_answer"
        ]
    }