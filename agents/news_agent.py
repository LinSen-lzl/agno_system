from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools

# 新闻agent
news_agent = Agent(
    name="news-agent",
    role="新闻播报员",
    instructions="你是一个专业的新闻播报 AI 助手，收集并播报全球范围内的新闻",
    tools=[DuckDuckGoTools],
)