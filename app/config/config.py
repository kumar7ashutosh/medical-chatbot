import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
embeddings_model = os.getenv("embeddings_model")
openai_model = os.getenv("openai_model")

db_faiss_path="vectorstore/db"
DATA_PATH="data/"
CHUNK_SIZE=500
CHUNK_OVERLAP=50