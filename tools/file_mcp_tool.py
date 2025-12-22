import os
from agno.tools.mcp import MCPTools

UPLOAD_DIR = os.path.abspath(r".\uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)
print("Using directory:", UPLOAD_DIR)

file_mcp_tool = MCPTools(
    command=f'npx -y @modelcontextprotocol/server-filesystem "{UPLOAD_DIR}"'
)

