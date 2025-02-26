from dotenv import load_dotenv
# from langchain.text_splitter import RecursiveCharacterTextSplitter # can be used for chunking
from langchain_chroma import Chroma
from langchain_community.document_loaders import JSONLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import json
from langchain.schema import Document

load_dotenv()

datas = [
    r"C:\Users\musta\OneDrive\Desktop\HocamBot\Data\FAQ\documents_1.json",
    r"C:\Users\musta\OneDrive\Desktop\HocamBot\Data\FAQ\documents_2.json",
    r"C:\Users\musta\OneDrive\Desktop\HocamBot\Data\FAQ\documents_3.json",
]

jq_schema = ". | {text: .markdown, source: .metadata.url}"

docs = []
for file in datas:
    with open(file, "r", encoding="utf-8") as f:
        json_data = json.load(f)

        if isinstance(json_data, list):
            for item in json_data:
                if (
                    isinstance(item, dict)
                    and "markdown" in item
                    and "metadata" in item
                    and "url" in item["metadata"]
                ):
                    text = item["markdown"]
                    url = item["metadata"]["url"]
                    docs.append(Document(page_content=text, metadata={"source": url}))

"""
vectorstore = Chroma.from_documents(
    documents=docs,
    collection_name="faq-question-tr",
    embedding=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"),
    persist_directory="./.chroma",
)
"""  # Embedding data at the start

retriever = Chroma(
    collection_name="faq-question-tr",
    persist_directory="./.chroma",
    embedding_function=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"),
).as_retriever()
