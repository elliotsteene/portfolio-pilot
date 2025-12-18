# Quarterly ISA Rebalancing System: Multi-Agent Architecture

## Executive Summary

This document describes a multi-agent system for quarterly analysis and rebalancing recommendations for a long-term, low-risk Vanguard Stocks and Shares ISA. The system is designed around **Advanced Context Engineering** principles: frequent intentional compaction, sub-agent isolation, artifact-first workflows, and strategic human leverage points.

The system runs quarterly, producing:
1. Accumulated research artifacts that build institutional knowledge over time
2. Structured macro trend reports (interest rates, currencies, commodities)
3. Portfolio movement analysis
4. Risk-aware rebalancing recommendations

Human involvement is limited to final review of recommendations—the system operates autonomously through research and synthesis phases.

---

## Part 1: Core Design Principles

### 1.1 Context Engineering Fundamentals

The system treats **context as the primary lever for output quality**. Each agent operates with carefully curated, minimal context rather than access to everything. This prevents context pollution, reduces hallucination risk, and keeps each agent focused on its specialty.

**Key principles applied:**

| Principle | Application in This System |
|-----------|---------------------------|
| Frequent Intentional Compaction | Each agent produces compact summaries; orchestrator never receives raw data |
| Sub-agent Isolation | Agents cannot see each other's working memory, only final artifacts |
| Research-Plan-Implement | Adapted as Research → Synthesize → Recommend workflow |
| Artifact-First | Research documents are primary outputs; recommendations are "compiled" from them |
| Human Leverage at High-Impact Points | Human reviews final recommendations only, not intermediate research |

### 1.2 Statefulness and Knowledge Accumulation

Unlike coding agents that can discard context after task completion, this system **must accumulate knowledge across quarters**. Past forecasts, market readings, and portfolio snapshots form a growing corpus that enables:

- Forecast accuracy tracking (did our macro thesis play out?)
- Trend identification across multiple quarters
- Drift pattern recognition
- Model calibration based on historical recommendation performance

This requires a **persistent knowledge layer** with careful compaction to prevent unbounded growth.

### 1.3 Constraint: Vanguard Fund Universe

All recommendations must be from Vanguard's fund range. This is both a constraint and a simplification—it bounds the search space and ensures consistent data sources (Vanguard fact sheets, KIIDs).

---

## Part 2: System Architecture Overview

### 2.1 Temporal Workflow
- Use Temporal workflow for durable execution.
- Each sub-agent will be it's own Temporal workflow
- The main workflow orchestrates the sequence for the research report:
    
  - Macro research
    
    - Interest rates
    - Currency rates
    - Inflation rates
    - Index performance
  
  - Performance
    
    - Porfolio performance over last quarter
    - Comparison with forecasts and summaries from previous quarter
  
  - Analysis
    
    - Analyse macro research and aggregate forecasts
    - Analyse portfolio performance

  - Final Report
    
    - Using all available research, produce a report


### 2.1 Layer Definitions

**Research Layer** — Gathers and synthesizes external information
- Macro
- Fund Performance 

**Analysis Layer** — Applies models and generates recommendations
- Macro and Performance analysis

**Output Layer** — Produces human-readable deliverables
- Report Writer Agent

---

## Part 3: Agent Specifications

### 3.1 Orchestrator Agent

**Role:** Workflow coordination, context management, artifact routing

**Responsibilities:**
1. Initialize quarterly run with timestamp and run ID
2. Inject relevant historical context (compacted) to each sub-agent
3. Sequence agent execution respecting dependencies
4. Receive and validate artifacts from each agent
5. Perform inter-phase compaction
6. Manage the artifact registry
7. Handle failures and retries

**Context Window Contents:**
- System prompt with workflow definition
- Current run metadata (date, quarter, run ID)
- Compacted summaries from previous 2-4 quarters (not full artifacts)
- Agent status and artifact receipt log
- Error handling protocols

**Does NOT contain:**
- Raw market data
- Full historical artifacts
- Individual agent working memory

**Key Design Decision:** The orchestrator is deliberately "context-light." It knows *what* each agent should produce and *when*, but not *how*. This prevents the orchestrator from becoming a bottleneck or single point of context bloat.

---

### 3.2 Macro Research Agent

**Role:** Analyze macroeconomic environment relevant to long-term investing

**Input Context:**
- Current date and analysis period
- Previous quarter's macro summary (compacted, ~500 tokens)
- Previous quarter's forecasts (for accuracy tracking)
- Data source access instructions (FRED, IMF, financial news)

**Research Domains:**
1. **Interest Rates** — Central bank policies (BoE, Fed, ECB), yield curves, rate expectations
2. **Currency** — GBP strength/weakness, hedging implications for international funds
3. **Commodities** — Oil, gold, broad commodity indices (relevant for inflation expectations)
4. **Inflation** — CPI trends, inflation expectations, real return calculations
5. **Geopolitical** — Trade policy, regulatory changes, systemic risks

**Compacted Summary Example (for orchestrator):**
```
Q4 2025 Macro: Rates declining (BoE 4.75%, expecting 3.75% in 12m). 
GBP stable. Oil weak, gold strong. Inflation normalizing (UK 2.3%). 
Key risk: US trade policy affecting Asia-Pacific. 
Previous forecast accuracy: rates slightly off (BoE more cautious).
Bond duration now favorable. Hedged bonds, unhedged equity recommended.
```

**Output artifacts:**
The agent outputs files capturing their findings in the research domains. .

---

### 3.3 Fund Performance Agent

**Role:** Analyze Vanguard fund universe for suitability and performance

**Input Context:**
- Vanguard fund universe list with OCFs
- Fund fact sheet access instructions
- Previous quarter's fund analysis summary
- Current portfolio holdings (fund names only, not amounts)

**Analysis Scope:**
1. **Currently Held Funds** — Deep analysis of funds in portfolio
2. **Alternative Candidates** — Similar funds that might be superior
3. **New Opportunities** — Funds that match risk profile not currently held

**Evaluation Criteria:**
- Ongoing Charges Figure (OCF) — lower is better
- Tracking error (for index funds)
- Holdings overlap with other portfolio funds
- Geographic and sector exposure
- Historical performance vs benchmark
- Fund size and liquidity

---

### 3.4 Portfolio State Agent

**Role:** Analyze current portfolio composition, drift, and concentration

**Input Context:**
- Current holdings snapshot (from manual input or data extraction)
- Previous quarter's portfolio state
- Target allocations from last rebalancing (if any)

**Analysis Scope:**
1. Current value and weight of each holding
2. Drift from targets
3. Geographic concentration
4. Sector concentration  
5. Asset class breakdown
6. Performance attribution

---

### 3.5 Analyst Agent

**Role:** Assess portfolio risk metrics and scenario analysis

**Input Context:**
- Portfolio state summary (compacted)
- Macro environment summary (compacted)
- Fund characteristics (duration, volatility, correlations)
- Risk parameters (max drawdown threshold, concentration limits)
- Use different perspectives: optimistic, negative and neutral

**Analysis Scope:**
1. Historical volatility
2. Maximum drawdown analysis
3. Correlation matrix
4. Scenario stress tests
5. Risk-adjusted return metrics


---

### 3.6 Allocation Strategist Agent

**Role:** Propose target allocations based on all inputs

**Input Context:**
- Macro summary (compacted)
- Fund analysis summary (compacted)
- Portfolio state summary (compacted)
- Risk assessment summary (compacted)
- Risk parameters
- Investment mandate (long-term, low-risk, steady returns)

**This is the critical synthesis agent.** It receives compacted summaries from all research agents and must propose allocations that:
1. Respect risk parameters
2. Align with macro outlook
3. Optimize for long-term steady returns
4. Minimize unnecessary trading

---

### 3.7 Recommendation Synthesizer Agent

**Role:** Convert allocation strategy into specific, actionable recommendations

**Input Context:**
- Allocation strategy summary
- Current portfolio values
- Fund trading information (minimums, settlement)

---

### 3.8 Report Writer Agent

**Role:** Produce human-readable quarterly report

**Input Context:**
- All agent summaries (compacted)
- Recommendations
- Historical comparison data

**Output:** Structured markdown report covering:
1. Executive Summary
2. Macro Environment Review
3. Portfolio Performance
4. Risk Assessment
5. Rebalancing Recommendations
6. Appendices (detailed data)

---

## Part 4: Context Flow and Compaction Strategy

### 4.1 The Compaction Principle

Each agent produces two outputs:
1. **Full Artifact** — Complete structured data (YAML/JSON)
2. **Compacted Summary** — ~200-500 tokens for downstream agents

The orchestrator routes **only summaries** between agents. Full artifacts are stored but not passed in context. File path for the full 
artifact are included - the agents can choose to read the full report or partially read it.

### 4.2 Historical Context Injection

Each quarterly run needs historical context without unbounded growth. Strategy:

**For each agent, inject:**
- Previous quarter's summary (full, ~500 tokens)
- Two quarters ago (heavily compacted, ~150 tokens)
- Year-ago quarter (one-line summary, ~50 tokens)
- Forecast accuracy from previous quarters (~100 tokens)

**Total historical context per agent: ~800 tokens**

This enables trend awareness without context bloat.

---

## Part 5: Artifact Storage and Knowledge Graph

### 5.1 Directory Structure
```
/quarterly-research/
├── portfolio.yaml                          # Curreny portfolio state
├── YEAR/                                   # Year of analysis
    ├── QUARTER/                            # Quarter of analysis
        ├── macro/
        │     ├── summary.yaml               # Summary of main findings
        │     ├── interest_rate.yaml         # Interest rate information from this quarter
        │     ├── currency.yaml              # Currency information from this quarter
        │     ├── inflation.yaml             # Inflation rate information from this quarter
        ├── performance/
        │     ├── summary.yaml               # Summary of portfolio performance over last quarter
        │     ├── q-1_tracking.yaml          # Comparison with forecasts and summaries made in prior quarter
        ├── analysis/
        │     ├── forecast_aggregation.yaml  # Macro forecasts over multiple time horizons
        │     ├── portfolio_assessment.yaml  # Current forecast evaluated against current quarter findings
        ├── year_quarter_report.yaml         # Summaries report with all findings
```
---

## Part 11: Appendices

### Appendix A: Complete Artifact Schemas

{Would contain full JSON Schema definitions for all YAML artifacts}

### Appendix B: Data Source Integration Specs

```yaml
data_sources:
  fred:
    base_url: "https://api.stlouisfed.org/fred"
    series:
      - "FEDFUNDS"  # Fed Funds Rate
      - "GB10Y"     # UK 10Y Gilt
      - "CPIUK"     # UK CPI
    auth: "API_KEY"
    rate_limit: "120/min"
    
  imf:
    base_url: "https://www.imf.org/external/datamapper/api"
    datasets:
      - "WEO"  # World Economic Outlook
    auth: "none"
    
  vanguard:
    method: "Web scraping or manual download"
    data_points:
      - "Fund fact sheets"
      - "KIIDs"
      - "OCF schedules"
    frequency: "Monthly publication"
    
  market_data:
    provider: "Yahoo Finance / Alpha Vantage"
    data_points:
      - "Index prices"
      - "Currency rates"
      - "Commodity prices"
```
---

## Conclusion

This architecture applies Advanced Context Engineering principles to create a robust, repeatable quarterly investment analysis system. Key design decisions:

1. **Agent isolation** prevents context pollution and keeps each agent focused
2. **Frequent compaction** ensures context stays manageable across the workflow
3. **Artifact-first approach** creates durable knowledge that compounds over time
4. **Forecast tracking** enables continuous improvement
5. **Minimal human touchpoints** reduce friction while maintaining oversight

The system is designed to evolve: as forecasts are tracked and learnings accumulated, the prompts and parameters can be refined based on evidence.
