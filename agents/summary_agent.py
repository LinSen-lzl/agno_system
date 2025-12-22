from agno.agent import Agent
from models.deepseek_llm import deepseek_llm

summary_agent = Agent(
    name="内容总结agent",
    model=deepseek_llm(),
    role="总结专家",
    instructions="将给到的信息整理成简明摘要。"
)