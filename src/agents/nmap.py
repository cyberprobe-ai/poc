import subprocess
from contextlib import AsyncExitStack
from typing import Tuple

from google.adk import Agent
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import MCPToolset
from mcp import StdioServerParameters

from models.gemini import MODEL_GEMINI_2_0_FLASH


async def create_nmap_agent() -> Tuple[Agent, AsyncExitStack]:
    # TODO: `npm root -g` 以外で良い方法がないか検討する
    npm_root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=StdioServerParameters(
            command="node",
            args=[f"{npm_root}/mcp-nmap-server/dist/index.js"],
        ),
    )

    agent = LlmAgent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="network_security_scanner",
        description="ネットワークセキュリティ診断のためのポートスキャンと脆弱性検出を実行するエージェント",
        instruction=(
            "このエージェントはnmapを使用したネットワークスキャン機能を提供します。"
            "ユーザーからの指示に基づいて、特定のIPアドレスやホスト、ネットワーク範囲に対して"
            "ポートスキャン、サービス検出、OS検出、脆弱性スキャンなどを実行します。"
            "スキャン結果は構造化された形式で返却し、セキュリティ上の問題点や推奨される対策を"
            "技術的に正確かつ簡潔に提示します。"
            "ユーザーのセキュリティ意識向上と、防御態勢の強化をサポートします。"
        ),
        tools=tools,
    )
    return agent, exit_stack
