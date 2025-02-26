from dotenv import load_dotenv

load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("Hello Advanced RAG")
    res = app.invoke(input={"question": "çift Anadal Yönergeleri nelerdir?"})
    print(res["question"])
    print(res["generation"])