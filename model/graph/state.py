from typing import List, TypedDict


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        generation: LLM generation
        documents: list of documents
        docs_good: if there are any relevant docs
        refine_count: Count number of refiner usage
    """

    question: str
    generation: str
    documents: List[str]
    docs_good: bool
    refine_count: int