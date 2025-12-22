from agno.agent import Agent
from models.deepseek_llm import deepseek_llm

# 通用型agent
normal_agent = Agent(
    name="通用型agent",
    model=deepseek_llm(),
    instructions="你是一个友好的 AI 助手，回答要清晰、简洁。回答时用中文回答。",
)