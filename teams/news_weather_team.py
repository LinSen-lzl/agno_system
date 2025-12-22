from agno.team import Team
from models.deepseek_llm import deepseek_llm
from agents.news_agent import news_agent
from agents.weather_agent import weather_agent

news_weather_team = Team(
    name="新闻和天气预报团队",
    members=[news_agent, weather_agent],
    model=deepseek_llm(),
    instructions="与团队成员协调，提供全面的信息。根据用户的需求分配任务。",
)