from agno.os import AgentOS
from agents.normal_agent import normal_agent
from agents.calculate_agent import calculate_agent
from teams.news_weather_team import news_weather_team

# 实体构建
agent_os = AgentOS(
    agents=[normal_agent,calculate_agent],
    teams=[news_weather_team],
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve("main:app", reload=True)
