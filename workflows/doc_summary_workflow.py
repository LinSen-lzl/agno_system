from agno.workflow import Workflow
from agents.doc_agent import doc_agent
from agents.extract_agent import extract_agent
from agents.summary_agent import summary_agent

doc_summary_workflow = Workflow(
    name="文档分析总结工作流",
    steps=[
        {"name": "读取PDF",
         "agent": doc_agent,
         "task": lambda file_path: doc_agent.run(file_path)},
        {"name": "信息抽取",
         "agent": extract_agent,
         "task": lambda text: extract_agent.run(text)},
        {"name": "总结",
         "agent": summary_agent,
         "task": lambda text: summary_agent.run(text)},
    ]
)