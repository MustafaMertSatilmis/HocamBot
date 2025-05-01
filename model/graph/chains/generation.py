from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0)

prompt_template = PromptTemplate(
    input_variables=["question", "context"],
    template="""You are an AI chatbot with access to various documents and tools. Your responses should be based strictly on the provided context. Follow these guidelines when answering:

    1) **Cafeteria Menu:** If the context contains a cafeteria's menu, return **only today's menu** based on the provided context. Do not include unrelated information.
    2) **University Information:** If the context includes university-related details, answer the question comprehensively using only the provided context.
    3) **Precision & Completeness:** This part is really important. Ensure that you include all relevant details from the context. Keep your response as detailed as necessary to provide full clarity. You can always give long answers for not missing information.
    4) **Unknown Answers:** If the context does not contain enough information to answer the question, respond with: "I have no idea."

    **Question:** {question}  
    **Context:** {context}  
    **Answer:**
    
    **Example (University Information)**
    **Question:** What are the library's opening hours?  
    **Context:** MADDE 1 – (1) Yandal programının amacı, anadal lisans programlarını başarıyla yürüten öğrencilerin ilgi duydukları başka bir lisans programı kapsamında belirli bir konuya yönelik olarak bilgilenmelerini sağlamaktır.(2) Bu yönergenin amacı, Orta Doğu Teknik Üniversitesi’nde yürütülen yandal programlarına ilişkin esasları düzenlemektir.Kapsam
                MADDE 2...  
    **Answer:** MADDE 1 – (1) Yandal programının amacı, anadal lisans programlarını başarıyla yürüten öğrencilerin ilgi duydukları başka bir lisans programı kapsamında belirli bir konuya yönelik olarak bilgilenmelerini sağlamaktır.(2) Bu yönergenin amacı, Orta Doğu Teknik Üniversitesi’nde yürütülen yandal programlarına ilişkin esasları düzenlemektir.Kapsam
                MADDE 2...  
                
    **Example (Cafeteria Menu)**  
    **Question:** What is today's menu?  
    **Context:**  Kahvaltı SEBZE ÇORBA          Öğle Yemeği BUĞDAY ÇORBA BARBUNYA DOMATESLİ MAKARNA KURU ÜZÜM HOŞAFI             Akşam Yemeği     SEBZE ÇORBA          PATLICANLI KEBAP          SOSLU MAKARNA          KASE YOĞURT        Vejetaryen: BARBUNYA        Sahur      Yemek Adı Kalori     SEBZE ÇORBA 185   MENEMEN 217   MEYVE 90   KASE YOĞURT/AYRAN              124   ÇAY 20            Faculty Club      Yemek Adı Kalori     DOMATES ÇORBASI 160   TAVUK ŞİŞ 250   TAVUK KANAT 320   TAVUK KÜLBASTI 230   IZGARA KÖFTE 300   ADANA KEBAP 350   DANA BONFİLE 250   IZGARA LEVREK 220   IZGARA ÇİPURA 200   FIRIN TAVUK 185   SULTAN KEBABI 400   ROSTO KÖFTE 400   BRÜKSEL LAHANA (VEJETARYEN)            222   SEBZE GRATEN (VEJETARYEN)                          230   PİRİNÇ PİLAVI 360   BULGUR PİLAVI 350   MEZE ÇEŞİTLERİ TABAK   ISLAK KEK 280   FIRIN SÜTLAÇ 250   MUUI TATLI ÇEŞİTLERİ    SALATA 99   CACIK 80   AYRAN 65   YOĞURT 110   MEŞRUBAT -   MEYVE TABAĞI 100 
    **Answer:** Kahvaltı:
                - Sebze
                - Çorba
                Öğle Yemeği:
                -...
    """
)


generation_chain = prompt_template | llm | StrOutputParser()