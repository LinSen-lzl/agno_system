from agno.agent import Agent
from models.deepseek_llm import deepseek_llm
from agno.tools.baidusearch import BaiduSearchTools

# 天气预报agent
weather_agent = Agent(
    name="weather-agent",
    role="天气预报播报员",
    model=deepseek_llm(),
    instructions="你是一个专业的天气预报播报 AI 助手，收集并播报全球范围内前后7天的天气预报",
    tools=[BaiduSearchTools()],
)

