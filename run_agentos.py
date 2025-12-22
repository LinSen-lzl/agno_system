from agno.os import AgentOS
from agents.normal_agent import normal_agent
from agents.calculate_agent import calculate_agent
from agents.router_agent import router_agent
from agents.qa_agent import qa_agent
from agents.file_agent import file_agent
from teams.news_weather_team import news_weather_team
from workflows.doc_summary_workflow import doc_summary_workflow
from workflows.write_article_workflow import write_article_workflow
from api.upload import upload_router
from api.workflow_calling import wc_router

# 实体构建
agent_os = AgentOS(
    agents=[normal_agent, calculate_agent, router_agent, qa_agent, file_agent],
    teams=[news_weather_team],
    workflows=[doc_summary_workflow, write_article_workflow],
)

app = agent_os.get_app()
app.include_router(upload_router)
app.include_router(wc_router)

if __name__ == "__main__":
    agent_os.serve("run_agentos:app", reload=False)
