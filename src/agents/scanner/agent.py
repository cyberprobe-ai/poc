from contextlib import AsyncExitStack

from google.adk import Agent
from google.adk.agents import LlmAgent

from models import MODEL_GEMINI_2_0_FLASH

from .nmap import create_nmap_tools


async def create_scanner_agent() -> tuple[Agent, AsyncExitStack]:
    tools, exit_stack = await create_nmap_tools()

    agent = LlmAgent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="scanner_agent",
        description="ネットワークセキュリティ診断のために、テスト対象システムをスキャンするエージェント",
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
