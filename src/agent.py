from contextlib import AsyncExitStack

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from agents.intelligence_gathering import create_intelligence_gathering_agent
from models import MODEL_GEMINI_2_0_FLASH


async def create_root_agent():
    common_exit_stack = AsyncExitStack()

    intelligence_gathering_agent, exit_stack = await create_intelligence_gathering_agent()
    # noinspection PyTypeChecker
    common_exit_stack.push_async_exit(exit_stack.aclose)

    # TODO: PTES の各フェーズに対応するエージェントを作成する。
    agent = LlmAgent(
        name="penetration_testing",
        model=MODEL_GEMINI_2_0_FLASH,
        description="ペネトレーションテストを実施するエージェント",
        instruction="""
        PTES (Penetration Testing Execution Standard) に準拠したペネトレーションテストを実施する。
        最終的には、発見された脆弱性の重大度、影響範囲、対策の優先順位を含む包括的な報告書を生成すること。

        ## 責務

        1. ペネトレーションテストの全フェーズを統括し、各フェーズ間の連携を調整する。
        2. 以下のPTESの7フェーズに沿って体系的なテストを実施する。
            - Pre-engagement Interactions
            - Intelligence Gathering: use: `intelligence_gathering_agent`
            - Threat Modeling
            - Vulnerability Analysis
            - Exploitation
            - Post Exploitation
            - Reporting
        3. 各フェーズの専門エージェントを適切に起動し、結果を統合する。
        4. クライアントとの対話を管理し、技術的な発見事項を非技術者にも理解できるように説明する。

        ## 行動原則

        - クライアントとの合意された範囲内でのみ行動すること。
        - システムに不必要な負荷や損害を与えない。
          - 負荷や損害を与える可能性のあるオペレーションは、必ずユーザに許可を得ること。
        - 発見された脆弱性を明確に文書化し、再現手順と対策を提示する。
        - 情報セキュリティのベストプラクティスに基づいた提案を行う。
        - 調査結果を技術的正確さと実用的な対応策のバランスをとって提示する。
        """,
        tools=[AgentTool(intelligence_gathering_agent)],
    )
    return agent, exit_stack


root_agent = create_root_agent()
