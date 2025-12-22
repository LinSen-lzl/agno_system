from agno.agent import Agent
from models.deepseek_llm import deepseek_llm
from tools.file_mcp_tool import file_mcp_tool

# 文件Agent
file_agent = Agent(
    name="文件Agent",
    role="文件助手",
    instructions="""
        你是一个文件系统助手，帮助用户浏览文件和目录。
        - 通过文件系统来回答问题
        - 通过mcp工具查找你可以访问的目录
        - 对你查看的文件提供清晰的上下文说明
        - 保持简洁，聚焦于相关信息
    """,
    model=deepseek_llm(),
    tools=[file_mcp_tool]
)