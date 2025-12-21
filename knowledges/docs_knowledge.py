from agno.knowledge.knowledge import Knowledge
from dbs.milvus_db import milvus_db

docs_knowledge = Knowledge(
    vector_db=milvus_db
)