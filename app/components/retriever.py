from langchain_core.prompts import PromptTemplate

from app.components.llm import load_llm
from app.components.vector_store import load_vector_store

from app.config.config import openai_model, openai_api_key
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE = """ Answer the following medical question in 2-3 lines maximum using only the information provided in the context.

Context:
{context}

Question:
{question}

Answer:
"""

def set_custom_prompt():
    return PromptTemplate(template=CUSTOM_PROMPT_TEMPLATE,input_variables=["context","question"])

class MedicalQAChain:
    def __init__(self):
        logger.info("Loading vector store")
        self.db = load_vector_store()
        logger.info("Loading LLM")
        self.llm=load_llm(openai_model=openai_model,openai_api_key=openai_api_key)
        self.prompt = set_custom_prompt()

        logger.info(
                "Medical QA Chain initialized successfully"
        )
        
    
    def ask(self,question:str):
        retriever=self.db.as_retriever(search_kwargs={'k':1})
        docs=retriever.invoke(question)
        context="\n".join([doc.page_content for doc in docs])
        final_prompt=self.prompt.format(context=context,question=question)
        response=self.llm.invoke(final_prompt)
        return response.content
        