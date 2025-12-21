import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]  # 项目根目录

env = os.getenv("APP_ENV", "prod")
ENV_FILE = BASE_DIR / f".env.{env}"

if not ENV_FILE.exists():
    raise RuntimeError(f"❌ 环境文件不存在: {ENV_FILE}")

load_dotenv(ENV_FILE)

# ===== 通用配置 =====
LLM_PROVIDER = os.getenv("LLM_PROVIDER")
MODEL_NAME = os.getenv("MODEL_NAME")
BASE_URL = os.getenv("BASE_URL")

MAX_TOKENS = int(os.getenv("MAX_TOKENS", 256))
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.3))

VECTOR_DB_URL = os.getenv("VECTOR_DB_URL")
VECTOR_DB_COLLECTION = os.getenv("VECTOR_DB_COLLECTION")
VECTOR_DB_TOKEN = os.getenv("VECTOR_DB_TOKEN")

# ===== API KEY（仅远程需要）=====
API_KEY = os.getenv("API_KEY")
EMBEDDING_API_KEY = os.getenv("EMBEDDING_API_KEY")
EMBEDDING_URL = os.getenv("EMBEDDING_URL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

# ===== 校验逻辑 =====
if not LLM_PROVIDER:
    raise RuntimeError("❌ LLM_PROVIDER 未设置")

if not MODEL_NAME:
    raise RuntimeError("❌ MODEL_NAME 未设置")

if not BASE_URL:
    raise RuntimeError("❌ BASE_URL 未设置")

if LLM_PROVIDER != "ollama" and not API_KEY:
    raise RuntimeError("❌ 远程模型必须配置 API KEY")

# ===== 给 Agent 用的统一配置 =====
LLM_CONFIG = {
    "provider":LLM_PROVIDER,
    "model": MODEL_NAME,
    "base_url": BASE_URL,
    "api_key": API_KEY,
    "max_tokens": MAX_TOKENS,
    "temperature": TEMPERATURE,
}

DB_CONFIG = {
    "vector_db_url":VECTOR_DB_URL,
    "vector_db_collection":VECTOR_DB_COLLECTION,
    "token":VECTOR_DB_TOKEN,
    "embedding_api_key":EMBEDDING_API_KEY,
    "embedding_url":EMBEDDING_URL,
    "embedding_model":EMBEDDING_MODEL,
}

