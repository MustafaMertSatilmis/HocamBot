import streamlit as st
from dotenv import load_dotenv
from graph.graph import app  

load_dotenv()

st.set_page_config(page_title="University AI Chatbot", layout="wide")

st.title("HOCAMBOT")


user_input = st.text_input("Ask me anything:", "")

if user_input:
    response = app.invoke(input={"question": user_input})

    question = response.get("question", "Unknown Question")
    generation = response.get("generation", "No response generated.")

    st.write("### HocamBot's Response")
    st.markdown(generation)

    if "retrieved_docs" in response:
        with st.expander("Retrieved Documents"):
            for i, doc in enumerate(response["retrieved_docs"]):
                st.markdown(f"**Document {i+1}:** {doc}")

st.markdown("---")
st.caption("Powered by ODTÜ YZT")
