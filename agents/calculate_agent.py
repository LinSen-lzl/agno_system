from agno.agent import Agent
from models.llm import create_llm
from tools.calculate_tool import add_tool
from tools.calculate_tool import multiply_tool
from tools.calculate_tool import divide_tool

# 数学计算专用agent
calculate_agent = Agent(
    name="数学计算Agent",
    model=create_llm(),
    tools=[add_tool, multiply_tool, divide_tool],
    instructions="""
    你只能使用提供的工具进行数学运算。
    不允许自行计算。
    """,
)