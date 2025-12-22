from agno.agent import Agent
from models.deepseek_llm import deepseek_llm
from agno.tools.baidusearch import BaiduSearchTools

# 新闻agent
news_agent = Agent(
    name="news-agent",
    role="新闻播报员",
    model=deepseek_llm(),
    instructions="你是一个专业的新闻播报 AI 助手，收集并播报全球范围内的新闻",
    tools=[BaiduSearchTools()],
)