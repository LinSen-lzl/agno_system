from agno.agent import Agent
from models.deepseek_llm import deepseek_llm
from knowledges.docs_knowledge import docs_knowledge

#
qa_agent = Agent(
    name="泰国菜问答Agent",
    role="基于知识库的返回进行问答的Agent",
    model=deepseek_llm(),
    instructions="""你是一个基于知识库进行问答的 AI 助手。
        请严格根据提供的上下文回答用户问题。
        如果上下文中没有相关信息，请直接回答“不知道”，不要编造答案。
        回答要简洁、准确。""",
    markdown=True,
    knowledge=docs_knowledge,
    search_knowledge=True,
)