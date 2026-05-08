import streamlit as st
import requests

st.title(
    "Advanced Agentic Engineering Assistant"
)

query = st.text_input(
    "Ask a question"
)

if st.button("Search"):

    response = requests.get(

        "http://127.0.0.1:8000/query",

        params={
            "q": query
        }
    )

    st.write(
        "Status Code:",
        response.status_code
    )

    st.write("Raw Response:")

    st.write(response.text)

    try:

        data = response.json()

        st.subheader("Answer")

        st.write(
            data["answer"]
        )

    except Exception as e:

        st.error(str(e))