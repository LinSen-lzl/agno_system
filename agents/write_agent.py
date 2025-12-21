from agno.agent import Agent
from models.llm import create_llm

write_agent = Agent(
    name="写文章agent",
    model=create_llm(),
    role="写文章专家",
    instructions="基于给到的调查研究信息和数据检验到的真实性写文章。"
)