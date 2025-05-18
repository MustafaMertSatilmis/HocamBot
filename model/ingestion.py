from dotenv import load_dotenv
import json
from langchain.schema import Document
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
import time

load_dotenv()

from pathlib import Path

root = Path.cwd()
datas = [
    root / "Data" / "FAQ",
    root / "Data" / "Metu_website" / "split_files",
]

docs = []

for file in datas:
    if os.path.isdir(file):
        json_files = [os.path.join(file, f) for f in os.listdir(file) if f.endswith(".json")]
    else:
        json_files = [file]

    for json_file in json_files:
        with open(json_file, "r", encoding="utf-8") as f:
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

                    elif (
                        isinstance(item, dict)
                        and "content" in item
                        and "url" in item
                    ):
                        text = item["content"]
                        url = item["url"]
                        docs.append(Document(page_content=text, metadata={"source": url}))
"""
vectorstore = Chroma.from_documents(
    documents=docs,
    collection_name="faq-question-tr",
    embedding=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"),
    persist_directory="./.chroma",
    )"""

retriever = Chroma(
    collection_name="faq-question-tr",
    persist_directory="./.chroma",
    embedding_function=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"),
).as_retriever()
