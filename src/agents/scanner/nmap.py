import subprocess
from contextlib import AsyncExitStack

from google.adk.tools.mcp_tool import MCPToolset, MCPTool
from mcp import StdioServerParameters


async def create_nmap_tools() -> tuple[list[MCPTool], AsyncExitStack]:
    # TODO: `npm root -g` 以外で良い方法がないか検討する
    npm_root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    return await MCPToolset.from_server(
        connection_params=StdioServerParameters(
            command="node",
            args=[f"{npm_root}/mcp-nmap-server/dist/index.js"],
        ),
    )
