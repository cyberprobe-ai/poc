from contextlib import AsyncExitStack

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from agents.nmap import create_nmap_agent
from models.gemini import MODEL_GEMINI_2_0_FLASH


async def create_root_agent():
    common_exit_stack = AsyncExitStack()

    nmap_agent, exit_stack = await create_nmap_agent()
    common_exit_stack.push_async_exit(exit_stack.aclose)

    agent = LlmAgent(
        name="penetration_test_agent",
        model=MODEL_GEMINI_2_0_FLASH,
        description="ペネトレーションテストのためのエージェント",
        instruction="""
        あなたはネットワーク分析のエキスパートです。
        ユーザーの要求に応じて適切な処理を行ってください。
        ネットワークスキャンが必要な場合は、適切なツールを使用します。
        スキャン結果を分析し、セキュリティの観点から適切なアドバイスを提供してください。
        """,
        tools=[AgentTool(nmap_agent)],
    )
    return agent, exit_stack
