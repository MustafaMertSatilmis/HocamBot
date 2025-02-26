from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

def get_data() -> str:
    
    url = "https://kafeterya.metu.edu.tr/"

    doc = WebBaseLoader(url).load()
    docs_list = [item for sublist in doc for item in sublist]
    
    result = docs_list[2]
    result = result[1].replace("\n", " ").strip()

    return result
