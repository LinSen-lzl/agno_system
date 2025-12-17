from agno.agent import Agent
from models.llm import create_llm
from tools.calculate_tool import add_tool
from tools.calculate_tool import multiply_tool

# 数学计算专用agent
calculate_agent = Agent(
    name="数学计算Agent",
    model=create_llm(),
    tools=[add_tool, multiply_tool],
    instructions="你是一个数学计算专用的 AI 助手，任何数学计算你都能解决。在没有对应 Tool 时，也可以直接给出结果",
)