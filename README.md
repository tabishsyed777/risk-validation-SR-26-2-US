# Model Risk Validation Harness for LLMs

An evidence-first prototype for LLM validation. It runs performance, robustness, drift, population-segment fairness-screen, and challenger-model tests, then creates versioned JSON evidence and a Markdown validation report.

> Portfolio prototype only—not a compliance determination, legal advice, or a substitute for independent validation and governance. SR 26-2 superseded SR 11-7 in April 2026; generative/agentic AI is outside its formal scope. This project is inspired by model-risk-management principles.

## Case study

The deterministic demo uses the MLX fine-tuning lab's IT-support classifier. It is intentionally offline and repeatable.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m harness.run --config config/case_study.json
```

Outputs are created under `evidence/<run-id>/`:

- `validation_evidence.json` — structured test evidence and metrics
- `validation_report.md` — reviewer-facing pass/fail summary

## Controls demonstrated

| Control | Evidence |
|---|---|
| Performance | Held-out accuracy |
| Robustness | Typos and paraphrase invariance |
| Fairness screen | Accuracy by supplied segment; maximum gap |
| Drift | Population Stability Index (PSI) |
| Challenger | Champion-versus-challenger accuracy delta |
| Reproducibility | Versioned artifacts, config, and test cases |

To use a real model, replace `FixtureModel` with an approved adapter and retain the relevant security, privacy, retention, monitoring, and independent-review controls.

Sources: [Federal Reserve SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm) and [revised guidance](https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm).