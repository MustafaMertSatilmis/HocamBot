from dotenv import load_dotenv
from typing import Any, Dict
from graph.state import GraphState
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.3)


system = """Given the following search query, refine it to improve document retrieval.
Make it clearer and include relevant keywords while maintaining the original intent.

ONLY return the refined query as plain text, without explanations or bullet points.
Do NOT provide multiple options, just return the single most relevant refined query.
"""

refine_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "User question: {question}"),
    ]
)


query_refiner_chain = refine_prompt | llm

def refine_query(state: GraphState) -> Dict[str, Any]:
    """
    Takes a user's question and refines it for better document retrieval.

    Args:
        state (GraphState): The current graph state.

    Returns:
        Dict[str, Any]: Updated state with the refined query.
    """
    print(f"REFINING QUERY {state['refine_count']}")
    question = state["question"]
    count = state["refine_count"] + 1
    refined_question = query_refiner_chain.invoke({"question": question})

    return {"question": refined_question.content, "refine_count": count}
