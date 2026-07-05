"""CFO Copilot Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_synthesize_financials():
    """Test Synthesize financial performance with commentary."""
    tools = AgentTools()
    result = await tools.synthesize_financials(period="test", sections="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_project_cash_flow():
    """Test Project cash flow with scenario analysis."""
    tools = AgentTools()
    result = await tools.project_cash_flow(months_ahead=1, scenarios="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_ir_metrics():
    """Test Track investor relations metrics and analyst consensus."""
    tools = AgentTools()
    result = await tools.track_ir_metrics(metrics="test", include_consensus=True)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_assess_financial_risk():
    """Test Assess financial risks (FX, interest rate, credit, liquidity)."""
    tools = AgentTools()
    result = await tools.assess_financial_risk(risk_types="test", exposure="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.cfo_copilot_agent_agent import CfoCopilotAgentAgent
    agent = CfoCopilotAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
