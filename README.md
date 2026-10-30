# AI Opportunity Studio 🧭

**Which AI projects should a business pilot first—and why?**

A consulting-style proof of concept that turns operational assumptions into a transparent AI portfolio, first-year/three-year business case, risk gates, and an actionable roadmap.

> **Portfolio prototype, not a real client engagement.** Every example and estimate is synthetic. Cost savings are *modeled*, not achieved. This is not a production AI solution or an official governance approval.

## What it demonstrates

- **AI use-case assessment:** five editable business scenarios, cross-functional prioritization and clear decision criteria.
- **Financial reasoning:** estimated annual hours freed, first-year/three-year net benefit and simple payback.
- **Responsible AI planning:** privacy and data-readiness gates can block an apparently attractive idea.
- **Stakeholder communication:** downloadable decision brief and portfolio CSV, suitable for discussing an implementation roadmap.
- **Explainability:** fixed published weights, no hidden ML model, and deterministic calculations.

## Quick start

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Run tests with `python -m pytest -q`.

## Suggested 2-minute walkthrough

1. Open **Customer email triage** and review initial modeled savings.
2. Increase implementation cost and lower effort-saved percentage to test sensitivity.
3. Select **Employee hiring screen** to see the *privacy governance hold* override the numeric score.
4. Download a short decision brief for a stakeholder conversation.

## Core assumptions and formulas

- `hours_saved = tasks_per_month × minutes_per_task / 60 × 12 × share_of_effort_saved`
- `gross_annual_savings = hours_saved × hourly_cost`
- `year_1_net = gross_annual_savings - annual_operating_cost - initial_cost`
- `three_year_net = 3 × (gross_annual_savings - annual_operating_cost) - initial_cost`
- `simple_payback_months = initial_cost / ((gross_annual_savings - annual_operating_cost) / 12)` (if positive)
- `priority_score = 20 × (0.35 × strategic_fit + 0.30 × data_readiness + 0.25 × feasibility + 0.10 × (6 - privacy_risk))`

These are **illustrative** productivity assumptions: time saved does not automatically become cash saved. They do not include change-management costs, uncertainty ranges, implementation delays, opportunity costs, legal considerations, or model evaluation. A genuine business case would validate all assumptions with an owner and baselines.

## Decision logic

| Condition | Decision |
|---|---|
| Privacy risk ≥ 4 without human review | Hold for governance review |
| Data readiness ≤ 2 | Validate data readiness first |
| Score ≥ 75 and positive ongoing value | Recommend controlled pilot |
| Otherwise | Refine business case |

### Next iterations

Stakeholder interview template, estimate sensitivity charts, data-quality checks and an operating-model RACI.

**Skills:** AI strategy, business-case modeling, stakeholder storytelling, data governance, responsible AI, Python, Streamlit, pandas.
