# Risk Register: Customer Churn Baseline

| ID | Risk | Impact | Mitigation / Safeguard |
|---|---|---|---|
| R1 | Extremely small dataset (12 rows) | High uncertainty and poor generalization | Collect a substantially larger, representative dataset before production use |
| R2 | Unknown data provenance/consent | Privacy/compliance risk | Document source, permission, consent, and licensing before real-world use |
| R3 | Feature leakage | Inflated evaluation and invalid deployment | Establish a timestamp-based feature cutoff and audit feature generation |
| R4 | False positives | Unnecessary customer outreach | Tune threshold using documented business costs; monitor precision |
| R5 | False negatives | Missed retention opportunities | Monitor recall and review missed-churn cases |
| R6 | Identifier used as a feature | Memorization/privacy risk | Exclude `customer_id` from model features |
| R7 | Model treated as an automatic decision | Customer harm / misuse | Human review and non-ML fallback |
| R8 | Distribution shift | Performance degradation | Monitor feature distributions and agreed performance thresholds |
| R9 | Unknown group representation | Potential unequal performance | Document population coverage and evaluate relevant groups when possible |
| R10 | Perfect-looking result on tiny test set | False confidence | Report sample size and uncertainty; do not claim production readiness |
