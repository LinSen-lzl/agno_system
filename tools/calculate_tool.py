from agno.tools import tool

@tool()
def add_tool(x: int, y: int) -> str:
    """计算两个数之和"""
    return x + y

@tool()
def multiply_tool(x: int, y: int) -> str:
    """计算两个数的乘积"""
    return x * y