from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

prompt_template = PromptTemplate(
    input_variables=["question", "context"],
    template="""You are a chatbot with access to different tools. Depending on the provided documents, answer accordingly:
    
    1) If the context is about a cafeteria's menu, return **only today's menu** based on the provided context.
    2) If the context contains university-related information, answer the question based on the provided details.
    3) If you do not know the answer, simply reply: "I have no idea."

    **Question:** {question}  
    **Context:** {context}  
    **Answer:** 
    """
)

generation_chain = prompt_template | llm | StrOutputParser()