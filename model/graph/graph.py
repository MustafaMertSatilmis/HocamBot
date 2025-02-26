from dotenv import load_dotenv

from langgraph.graph import END, StateGraph

from graph.const import RETRIEVE, GRADE_DOCUMENTS, GENERATE, REFINE, GETMENU 
from graph.nodes import generate, grade_documents, retrieve, refine_query_node, get_menu_node
from graph.state import GraphState

load_dotenv()

def start_node(state):
    state["refine_count"] = 0
    return state 

def decide_to_route(state):
    
    question = state["question"].lower()
    
    menu_keywords = ["menu", "food", "yemek", "lunch", "dinner", "yemeği"]
    
    if any(keyword in question for keyword in menu_keywords):
        return GETMENU
    else:
        return RETRIEVE
    
def decide_to_generate(state):
    
    if state["docs_good"] != 1 and state["refine_count"] < 1:
        return REFINE
    else:
        return GENERATE

workflow = StateGraph(GraphState)

workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(GENERATE, generate)
workflow.add_node(REFINE, refine_query_node)
workflow.add_node(GETMENU, get_menu_node)
workflow.add_node("start", start_node)
workflow.set_entry_point("start")

workflow.add_conditional_edges("start", decide_to_route,{
        GETMENU: GETMENU,
        RETRIEVE: RETRIEVE,
    },)

workflow.add_edge(GETMENU, GENERATE)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)

workflow.add_conditional_edges(GRADE_DOCUMENTS, decide_to_generate,{
        REFINE: REFINE,
        GENERATE: GENERATE,
    },)

workflow.add_edge(REFINE, RETRIEVE)
workflow.add_edge(GENERATE, END)


app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph.png")