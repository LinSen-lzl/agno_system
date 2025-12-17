from agno.models.openai import OpenAIChat
from agno.models.ollama import Ollama
from config.env import LLM_CONFIG

# 模型构建函数
def create_llm():
    provider = LLM_CONFIG["provider"]

    # 本地ollama
    if provider == "ollama":
        return Ollama(
            provider=LLM_CONFIG["model"],
            base_url=LLM_CONFIG["base_url"],
            temperature=LLM_CONFIG["temperature"],
            max_tokens=LLM_CONFIG["max_tokens"],
        )

    # 线上平台
    if provider == "deepseek":
        return OpenAIChat(
            id=LLM_CONFIG["model"],
            api_key=LLM_CONFIG["api_key"],
            base_url=LLM_CONFIG["base_url"],
            temperature=LLM_CONFIG["temperature"],
            max_tokens=LLM_CONFIG["max_tokens"],
            role_map={
                "system": "system",
                "user": "user",
                "assistant": "assistant",
                "tool": "tool",
                "model": "assistant",
            }
        )

    raise ValueError(f"不支持的 LLM_PROVIDER: {provider}")