from langchain_openai import ChatOpenAI
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import openai_api_key,openai_model

logger=get_logger(__name__)

def load_llm(openai_model:str=openai_model,openai_api_key:str=openai_api_key):
    logger.info("loading llm from openai")
    llm=ChatOpenAI(model=openai_model,temperature=0.7,api_key=openai_api_key)
    logger.info("loaded llm")
    return llm

