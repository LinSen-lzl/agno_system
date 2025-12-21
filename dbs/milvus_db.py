from agno.vectordb.milvus import Milvus
from config.env import DB_CONFIG
from agno.knowledge.embedder.openai import OpenAIEmbedder

ollamaEmbedder = OpenAIEmbedder(
    id=DB_CONFIG["embedding_model"],
    base_url=DB_CONFIG["embedding_url"],
    api_key="",
)

milvus_db = Milvus(
    collection=DB_CONFIG["vector_db_collection"],
    uri=DB_CONFIG["vector_db_url"],
    token=DB_CONFIG["token"],
    embedder=ollamaEmbedder,
)