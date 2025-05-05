from contextlib import AsyncExitStack

from google.adk import Agent
from google.adk.agents import LlmAgent

from models import MODEL_GEMINI_2_0_FLASH

from .nmap import create_nmap_tools


async def create_intelligence_gathering_agent() -> tuple[Agent, AsyncExitStack]:
    tools, exit_stack = await create_nmap_tools()

    agent = LlmAgent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="intelligence_gathering",
        description="ペネトレーションテストのための情報収集 (Intelligence Gathering) を実施するエージェント",
        instruction="""
        あなたはPTESの情報収集フェーズで活用されるnmapスキャンの専門エージェントです。

        ## 責務

        1. ターゲットシステムに対するポートスキャンの実行。
        2. 開いているポートで動作しているサービスの検出と識別。
        3. 検出した情報の Knowledge Base への記録。

        ## 行動指針

        1. 常に段階的なアプローチを取ること (基本スキャンから開始し、より詳細なスキャンへ)。
        2. ノイズを最小限に抑えるため、過度に攻撃的なスキャンは避ける。
        3. 発見した情報を明確に整理し、Exploitation Agent が使用できるよう準備する。
        4. スキャン対象の環境や条件に基づいて適切なスキャン手法を選択する。
        """,
        tools=tools,
    )
    return agent, exit_stack
