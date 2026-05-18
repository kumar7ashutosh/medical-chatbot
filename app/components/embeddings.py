from langchain_openai.embeddings import OpenAIEmbeddings
from app.common.custom_exception import CustomException
from app.config.config import embeddings_model
from app.common.logger import get_logger
logger=get_logger(__name__)

def get_embedding_model():
    logger.info("initializing embeddings model")
    model=OpenAIEmbeddings(model=embeddings_model)
    return model