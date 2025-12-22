from agno.models.ollama import Ollama
from config.env import LLM_CONFIG


def ollama_llm():
    return Ollama(
        model=LLM_CONFIG["model"],
        base_url=LLM_CONFIG["base_url"],
        temperature=LLM_CONFIG["temperature"],
        max_tokens=LLM_CONFIG["max_tokens"],
    )