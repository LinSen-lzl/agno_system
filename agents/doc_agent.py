from agno.agent import Agent
from tools.file_tool import read_pdf

doc_agent=Agent(
    role="文档读取专家",
    instructions="读取 PDF 文件内容，并输出纯文本。",
    tools=[read_pdf]
)