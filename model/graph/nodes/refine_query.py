from typing import Any, Dict
from graph.state import GraphState
from graph.chains.query_refiner import refine_query

def refine_query_node(state: GraphState) -> Dict[str, Any]:
    """
    LangGraph node that executes the query refining function.

    Args:
        state (GraphState): The current graph state.

    Returns:
        Dict[str, Any]: Updated state with the refined query.
    """

    print("--- EXECUTING QUERY REFINING NODE ---")
    
    refined_state = refine_query(state)

    print(f"--- REFINED QUERY: {refined_state['question']} ---")

    return refined_state  
