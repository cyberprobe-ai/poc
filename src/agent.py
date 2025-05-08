from contextlib import AsyncExitStack

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from agents.exploitation.agent import create_exploitation_agent
from agents.intelligence_gathering import create_intelligence_gathering_agent
from agents.vulnerability_analysis import create_vulnerability_analysis_agent
from models import MODEL_GEMINI_2_0_FLASH


async def create_root_agent():
    common_exit_stack = AsyncExitStack()

    intelligence_gathering_agent, exit_stack = await create_intelligence_gathering_agent()
    # noinspection PyTypeChecker
    common_exit_stack.push_async_exit(exit_stack.aclose)

    vulnerability_analysis_agent, exit_stack = await create_vulnerability_analysis_agent()
    # noinspection PyTypeChecker
    common_exit_stack.push_async_exit(exit_stack.aclose)

    exploitation_agent, exit_stack = await create_exploitation_agent()
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
            - Vulnerability Analysis: use: `vulnerability_analysis_agent`
            - Exploitation: use: `exploitation_agent`
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
        - スキャン、攻撃など、内部で実行している処理は、実行計画と実行ログを逐一報告すること。ただし、攻撃以外は許可不要で実行して良い。
        - チャットコミュニケーションは、英語で行うこと。

        ## ヒント

        あなたは、WordPress の攻撃能力しか保有していません。
        intelligence_gathering_agent tool で、

        1. 開いているポートを、Fast Scan でスキャンする。
        2. 各ポートで、動いているサービスを検出する。
        3. WordPress が動いているポートに絞り込み、後続のステップに進む。

        wordpress が動いている場合 Vulnerability Analysis (vulnerability_analysis_agent) -> Exploitation (exploitation_agent) を実行する。
        レポートは、human-readable な形式で出力すること。

        ### レポートについて

        対象システム情報、脆弱性情報、重篤度などを報告すること。
        なお、攻撃により何らかのリソース (ユーザ、ファイルなど) を作成/編集/破壊した場合は、その詳細情報も報告すること。
        """,
        tools=[AgentTool(intelligence_gathering_agent), AgentTool(vulnerability_analysis_agent), AgentTool(exploitation_agent)],
    )
    return agent, exit_stack


root_agent = create_root_agent()
