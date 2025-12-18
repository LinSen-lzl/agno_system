from agno.tools import tool

@tool()
def add_tool(x: int, y: int) -> str:
    """计算两个数之和"""
    return x + y

@tool()
def multiply_tool(x: int, y: int) -> str:
    """计算两个数的乘积"""
    return x * y

@tool
def divide_tool(a: float, b: float) -> float:
    """除法"""
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b