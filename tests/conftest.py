"""Test configuration for CFO Copilot Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "cfo-copilot-agent", "category": "Executive"}
