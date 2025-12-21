from agno.workflow import Step, Workflow, StepInput, StepOutput
from agents.extract_agent import extract_agent
from agents.summary_agent import summary_agent

# 读取文档步骤
def read_file_step(step_input: StepInput) -> StepOutput:
    """读取上传文件的内容"""
    file_content = step_input.input  # 这里 input 是二进制内容
    text = file_content.decode("utf-8", errors="ignore")
    return StepOutput(content=text)

doc_summary_workflow = Workflow(
    name="文档分析总结工作流",
    steps=[
        Step(name="读取文件内容", executor=read_file_step),
        Step(name="提取关键词", agent=extract_agent),
        Step(name="总结输出", agent=summary_agent),
    ]
)