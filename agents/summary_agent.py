from agno.agent import Agent
from models.llm import create_llm

summary_agent = Agent(
    name="内容总结agent",
    model=create_llm(),
    role="总结专家",
    instructions="将给到的信息整理成简明摘要。"
)