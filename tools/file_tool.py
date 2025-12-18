from agno.tools import tool
import pdfplumber

# 读取pdf文件
@tool
def read_pdf(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text