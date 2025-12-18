# Quarterly Research Directory Guide

This directory stores all quarterly research artifacts produced by the multi-agent ISA analysis system.

## Key Principles

- **Artifact-First**: Each agent produces structured YAML files as primary outputs
- **Compacted Summaries**: Each artifact includes a ~200-500 token summary for downstream agents
- **Historical Context**: Past quarters provide context for trend analysis and forecast accuracy tracking
- **File Path References**: Agents receive file paths and can choose to read full or partial artifacts

## Directory Structure

```
/quarterly-research/
├── portfolio.yaml                    # Current portfolio state (funds, values, allocations)
└── YEAR/                             # e.g., 2025/
    └── QUARTER/                      # e.g., Q4/
        ├── macro/
        │   ├── summary.yaml          # Compacted findings from all macro research
        │   ├── interest_rate.yaml    # Central bank rates, yield curves, forecasts
        │   ├── currency.yaml         # GBP strength, hedging implications
        │   └── inflation.yaml        # CPI trends, real return expectations
        ├── performance/
        │   ├── summary.yaml          # Portfolio performance over last quarter
        │   └── q-1_tracking.yaml     # How prior quarter forecasts performed
        ├── analysis/
        │   ├── forecast_aggregation.yaml    # Multi-horizon macro forecasts
        │   └── portfolio_assessment.yaml    # Current position vs macro outlook
        └── year_quarter_report.yaml  # Final comprehensive quarterly report
```

## File Conventions

**YAML Structure**: All artifacts follow a consistent schema:
- `metadata`: timestamp, quarter, agent_id
- `summary`: compacted text for downstream agents (max 500 tokens)
- `data`: structured findings specific to each artifact type
- `forecasts`: forward-looking predictions with rationale (where applicable)

**Naming**: Use lowercase with underscores (e.g., `interest_rate.yaml`, not `InterestRate.yaml`)

## Agent Workflow

1. **Research Layer** writes to `macro/` and `performance/`
2. **Analysis Layer** reads research artifacts, writes to `analysis/`
3. **Output Layer** reads all artifacts, produces final `year_quarter_report.yaml`
4. Each agent receives compacted summaries from prior quarters for historical context

## Historical Context Strategy

When processing a new quarter, agents receive:
- Previous quarter: full summary (~500 tokens)
- Two quarters ago: heavily compacted (~150 tokens)
- Year-ago quarter: one-line summary (~50 tokens)
- Forecast accuracy tracking (~100 tokens)

Total: ~800 tokens of historical context per agent
