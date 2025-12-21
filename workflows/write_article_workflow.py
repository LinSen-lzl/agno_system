from agno.workflow import Workflow,StepInput,Step,Condition
from agents.research_Agent import research_agent
from agents.fact_check_agent import fact_check_agent
from agents.summary_agent import summary_agent
from agents.write_agent import write_agent

# 检查关键词
def fact_keys_checking(step_input: StepInput) -> bool:
    summary = step_input.previous_step_content or ""

    keys = [
        "研究显示",
        "突破",
        "研究表明",
        "根据",
        "统计",
        "数据显示",
        "调查",
        "报告",
        "百万",
        "十亿",
        "百分比",
        "%",
        "增加",
        "下降",
        "创新",
        "新发现",
        "证据表明",
        "实验证明",
        "官方数据显示",
        "全球趋势",
        "最新研究",
        "显著变化",
        "增长",
        "减少",
    ]

    return any(key in summary for key in keys)


research_step = Step(
    name="主题调查步骤",
    description="调查研究主题",
    agent=research_agent,

)

summarize_step = Step(
    name="总结步骤",
    description="总结调查到的信息",
    agent=summary_agent,
)

keys_check_step = Step(
    name="真实数据关键词检查步骤",
    description="真实数据关键词检查",
    agent=fact_check_agent,
)

write_article_step = Step(
    name="写文章步骤",
    description="写文章",
    agent=write_agent,
)

write_article_workflow = Workflow(
    name="写学术文章工作流",
    description="这是一个根据用户给到的主题进行调查、总结、真实数据核实、写文章的工作流",
    steps=[
        research_step,
        summarize_step,
        Condition(
            name="真实数据检查关键词的条件判断",
            description="看看有没有真实数据，是否需要检查找到的真实数据的真实性",
            evaluator=fact_keys_checking,
            steps=[keys_check_step],
        ),
        write_article_step,
    ]
)