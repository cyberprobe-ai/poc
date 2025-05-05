from contextlib import AsyncExitStack

from google.adk.tools.mcp_tool import MCPTool, MCPToolset
from mcp import StdioServerParameters

from utils.npm import get_npm_root


async def create_nmap_tools() -> tuple[list[MCPTool], AsyncExitStack]:
    return await MCPToolset.from_server(
        connection_params=StdioServerParameters(
            command="node",
            args=[f"{get_npm_root()}/mcp-nmap-server/dist/index.js"],
        ),
    )
