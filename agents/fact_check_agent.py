from agno.agent import Agent
from models.llm import create_llm
from agno.tools.baidusearch import BaiduSearchTools

fact_check_agent = Agent(
    name="真实数据核查agent",
    model=create_llm(),
    role="真实数据核查专家",
    instructions="负责将给到的真实数据通过搜索工具核实是否真实",
    tools=[BaiduSearchTools()],
)