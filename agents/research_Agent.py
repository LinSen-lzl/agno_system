from agno.agent import Agent
from models.llm import create_llm
from agno.tools.baidusearch import BaiduSearchTools

# 主题调查agent
research_agent = Agent(
    name="主题调查agent",
    model=create_llm(),
    instructions="你负责通过搜索工具调查用户给定主题并提供详细结果",
    tools=[BaiduSearchTools()],
)