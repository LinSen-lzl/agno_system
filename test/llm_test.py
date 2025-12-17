import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# 模型测试

BASE_DIR = Path(__file__).resolve().parent.parent

env = os.getenv("APP_ENV", "prod")
load_dotenv(BASE_DIR / f".env.{env}")

api_key = os.getenv("API_KEY")
base_url = os.getenv(
    "BASE_URL",
    "https://api.deepseek.com/v1"
)
model_name = os.getenv("MODEL_NAME")
max_tokens = int(os.getenv("LLM_MAX_TOKENS", 256))
temperature = float(os.getenv("LLM_TEMPERATURE", 0.7))

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

def ask(question):
    response = client.chat.completions.create(
        model=model_name,
        temperature=temperature,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": "你是一个友好的 AI 助手。"},
            {"role": "user", "content": question}
        ]
    )
    choice = response.choices[0].message
    return choice.content

q = "你好！DeepSeek Agent，解释一下向量数据库是什么？"
ans = ask(q)
print("模型回答")
print(ans)