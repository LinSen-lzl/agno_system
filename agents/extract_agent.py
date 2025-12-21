from agno.agent import Agent
from models.llm import create_llm

# 从文本中收集关键信息
extract_agent = Agent(
    role="信息抽取专家",
    instructions="从文本中提取关键数据，如日期、金额、人物等。",
    model=create_llm(),
)