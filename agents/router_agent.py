from agno.agent import Agent
from models.deepseek_llm import deepseek_llm

from workflows.doc_summary_workflow import doc_summary_workflow
import re

def extract_path(text: str) -> str | None:
    match = re.search(r"(uploads?/\S+)", text)
    return match.group(1) if match else None

def route(user_input: str):
    path = extract_path(user_input)
    if path:
        return doc_summary_workflow.run(path)

router_agent = Agent(
    name="请求路由Agent",
    instructions="""
        你是一个请求路由 Agent。
        如果用户输入中包含文件路径（uploads/xxx.pdf），
        请直接使用工具调用文档分析工作流程。
        否则，正常聊天。
        """,
    model=deepseek_llm(),
    tools=[route],
)
