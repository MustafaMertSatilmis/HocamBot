from dotenv import load_dotenv

from pprint import pprint

load_dotenv()


from graph.chains.retrieval_grader import GradeDocuments, retrieval_grader
from graph.chains.query_refiner import refine_query
from ingestion import retriever


def test_retrival_grader_answer_yes() -> None:
    question = "Who can use METU Survey Service?"
    docs = retriever.invoke(question)
    pprint(docs)
    found_relevant = False
    for idx, doc in enumerate(docs):
        res: GradeDocuments = retrieval_grader.invoke(
            {"question": question, "document": doc.page_content}
        )

        print(f"\n Grader Response for Document {idx+1}: {res.binary_score}")

        if res.binary_score == "yes":
            found_relevant = True
            break

    assert found_relevant


def test_retrival_grader_answer_no() -> None:
    question = "Horde iletilerini nasıl filtreleyebilirim?"
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content

    res: GradeDocuments = retrieval_grader.invoke(
        {"question": "how to make pizaa", "document": doc_txt}
    )

    assert res.binary_score == "no"
    
    
def test_query_refiner() -> None:
    res = refine_query({"question": "Horde ileti filtrele "})
    print("\n--- Query Refinement Result ---")
    pprint(res)


