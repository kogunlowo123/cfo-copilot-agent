# CFO Copilot Agent

[![CI](https://github.com/kogunlowo123/cfo-copilot-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/cfo-copilot-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Executive | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

CFO copilot agent that synthesizes financial performance, manages cash flow projections, tracks investor relations metrics, assesses financial risks, and provides financial strategy recommendations.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `synthesize_financials` | Synthesize financial performance with commentary |
| `project_cash_flow` | Project cash flow with scenario analysis |
| `track_ir_metrics` | Track investor relations metrics and analyst consensus |
| `assess_financial_risk` | Assess financial risks (FX, interest rate, credit, liquidity) |
| `recommend_capital_allocation` | Generate capital allocation recommendations |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/cfo-copilot/synthesize` | Synthesize data |
| `POST` | `/api/v1/cfo-copilot/analyze` | Analyze |
| `GET` | `/api/v1/cfo-copilot/track` | Track metrics |
| `POST` | `/api/v1/cfo-copilot/recommend` | Get recommendation |
| `POST` | `/api/v1/cfo-copilot/report` | Generate report |

## Features

- Cfo
- Copilot
- Strategic Insights
- Decision Support

## Integrations

- Snowflake
- Tableau
- Salesforce
- Workday
- Jira

## Architecture

```
cfo-copilot-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── cfo_copilot_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Enterprise Data Platform + LLM + BI**

---

Built as part of the Enterprise AI Agent Platform.
