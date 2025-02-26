from typing import Any, Dict
from graph.state import GraphState
from graph.chains.get_menu import get_data

def get_menu_node(state: GraphState) -> Dict[str, Any]:
    """
    LangGraph node that returns data containing today's menu.

    Args:
        state (GraphState): The current graph state.

    Returns:
        Dict[str, Any]: Updated state with the question and relevant document.
    """

    print("--- EXECUTING QUERY REFINING NODE ---")
    
    doc = get_data()
    question = state["question"]
    print(f"--- GETTING MENU ---")

    return {"question": question, "documents": doc}
