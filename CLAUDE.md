## Project Overview

This is an ISA (Individual Savings Account) portfolio management system designed as a multi-agent architecture for quarterly analysis and rebalancing recommendations. The system focuses on long-term, low-risk investment in Vanguard Stocks and Shares ISA, using Advanced Context Engineering principles.

## Development Commands

### Environment Setup
```bash
# Uses uv for package management (Python 3.14+)
uv sync

# Install pre-commit hooks (includes Pyrefly type checking and Ruff linting/formatting)
pre-commit install
```

### Code Quality
```bash
# Type checking with Pyrefly
pyrefly check

# Linting and formatting with Ruff
ruff check --fix .
ruff format .

# Run pre-commit hooks manually
pre-commit run --all-files
```

### Running the Application
```bash
# Main entry point (currently minimal)
python src/main.py
```

## Architecture Overview

### Multi-Agent System Design

The system operates on a quarterly cycle with three main layers:

1. **Research Layer** - Gathers and synthesizes external information
   - Macro Research Agent: Analyzes macroeconomic environment (interest rates, currencies, commodities, inflation, geopolitical factors)
   - Fund Performance Agent: Analyzes Vanguard fund universe

2. **Analysis Layer** - Applies models and generates recommendations
   - Portfolio State Agent: Analyzes current portfolio composition, drift, and concentration
   - Analyst Agent: Assesses portfolio risk metrics and scenario analysis
   - Allocation Strategist Agent: Proposes target allocations

3. **Output Layer** - Produces human-readable deliverables
   - Recommendation Synthesizer: Converts allocation strategy into actionable recommendations
   - Report Writer Agent: Produces quarterly markdown reports

### Context Engineering Principles

The system is built around these core principles:
- **Frequent Intentional Compaction**: Each agent produces compact summaries (200-500 tokens), not raw data
- **Sub-agent Isolation**: Agents see only final artifacts, not each other's working memory
- **Artifact-First Workflows**: Research documents are primary outputs; recommendations are compiled from them
- **Historical Context**: Each agent receives previous quarter's summary (~500 tokens), two quarters ago (~150 tokens), year-ago quarter (~50 tokens), and forecast accuracy (~100 tokens) - total ~800 tokens per agent
- **Orchestrator Pattern**: The orchestrator coordinates workflow but remains "context-light" - knows what and when, not how

### Workflow Execution

Planned to use Temporal workflow for durable execution:
- Each sub-agent will be its own Temporal workflow
- Main workflow orchestrates the sequence:
  1. Macro research (interest rates, currency, inflation, index performance)
  2. Performance analysis (portfolio vs forecasts)
  3. Analysis (macro + portfolio)
  4. Final report generation

## Directory Structure

```
/quarterly-research/
├── portfolio.yaml                    # Current portfolio state
├── YEAR/
    └── QUARTER/
        ├── macro/
        │   ├── summary.yaml          # Summary of main findings
        │   ├── interest_rate.yaml    # Interest rate data
        │   ├── currency.yaml         # Currency data
        │   └── inflation.yaml        # Inflation data
        ├── performance/
        │   ├── summary.yaml          # Portfolio performance summary
        │   └── q-1_tracking.yaml     # Comparison with prior quarter forecasts
        ├── analysis/
        │   ├── forecast_aggregation.yaml    # Macro forecasts over time horizons
        │   └── portfolio_assessment.yaml    # Current forecast vs findings
        └── year_quarter_report.yaml  # Complete quarterly report
```

## Agent Specifications

Agent prompt templates are stored in `/agents/` directory:
- Each agent has a markdown file defining its role, mandate, input context, tasks, output requirements, and constraints
- Agents produce two outputs: Full Artifact (YAML/JSON) and Compacted Summary (~200-500 tokens)
- File paths for full artifacts are included so downstream agents can choose to read full or partial reports

## Investment Constraints

- **Fund Universe**: Vanguard funds only
- **Risk Profile**: Long-term (10+ year), low-risk strategy
- **Currency**: GBP-denominated portfolio
- **Rebalancing**: Quarterly analysis cycle

## Data Sources

External data sources the system will integrate:
- FRED (Federal Reserve Economic Data) - interest rates, economic indicators
- IMF World Economic Outlook
- Bank of England publications
- Vanguard fund fact sheets and KIIDs (Key Investor Information Documents)
- Market data providers (Yahoo Finance / Alpha Vantage) for indices, currencies, commodities

## Code Organization

- `/src/` - Main application code (currently minimal scaffold)
- `/agents/` - Agent prompt templates and specifications
- `/quarterly-research/` - Historical research artifacts and portfolio state
- Architecture documentation in `isa-rebalancing-system-architecture.md`
