# Responsible Data Card

## Dataset purpose
The dataset may support a decision-support use case for identifying customers who may be at higher risk of churn so a human team can consider retention outreach.

It must not be used as the sole basis for automatic account cancellation, denial of service, pricing changes, or other high-impact decisions.

## Provenance and permission
The supplied file is a small training dataset named `customer-churn-training.csv`. The source materials do not state who created the data, how it was collected, whether customers consented, or what licensing restrictions apply.

These provenance and permission details must be confirmed before any real-world use.

## Population and representation
The dataset contains 12 customer records. The represented population, sampling method, time period, geography, and missing groups are not documented in the supplied materials.

Plan-type counts:
- Basic: 5
- Standard: 4
- Pro: 3

Because the dataset is extremely small, its representation and generalizability are unknown.

## Features and target
Features:
- `customer_id`: customer identifier; exclude from model training.
- `tenure_months`: customer tenure in months.
- `support_tickets`: number of support tickets.
- `monthly_spend_inr`: monthly spend in INR.
- `last_login_days`: days since last login.
- `plan_type`: Basic, Standard, or Pro plan.

Target:
- `churned`: binary target where 1 indicates churned and 0 indicates not churned.

Potential leakage:
- Any feature collected after the prediction decision or after churn occurs could leak future information. The supplied file does not document feature timestamps, so this must be checked before deployment.

Sensitive proxies:
- No explicit sensitive attributes are present in the supplied file. However, indirect proxies cannot be ruled out without additional metadata and domain review.

## Quality checks
- Rows: 12
- Columns: 7
- Missing values: none in the supplied dataset.
- Duplicate rows: none.
- Unique customer IDs: 12/12.
- Target balance: 5 churned (41.7%), 7 not churned (58.3%).
- Plan type: Basic 5, Standard 4, Pro 3.
- Numeric ranges:
  - tenure_months: 1 to 30
  - support_tickets: 0 to 5
  - monthly_spend_inr: 499 to 1499
  - last_login_days: 1 to 30

Train/test separation must be done before fitting preprocessing/model parameters, and the identifier must be excluded from model features.

## Risks and safeguards
### Bias and representation
Risk: only 12 records are available and the represented population is undocumented.
Mitigation: obtain a larger, representative dataset and document sampling and coverage before production use.

### Privacy
Risk: customer identifiers are included.
Mitigation: exclude `customer_id` from model training and restrict access to identifiable data.

### Misuse
Risk: a churn-risk score could be treated as a definitive statement about a customer.
Mitigation: use the score only as decision support with human review.

### False positives
Risk: unnecessary retention outreach.
Mitigation: set the threshold using documented business costs and monitor false-positive rates.

### False negatives
Risk: missed retention opportunities.
Mitigation: monitor recall and review missed-churn cases; keep a human fallback process.

### Leakage
Risk: post-outcome or future information could make evaluation unrealistically strong.
Mitigation: document feature timestamps and enforce a time-based feature cutoff.

## Intended evaluation
Before training, define:
- Non-ML baseline: a transparent rule such as `last_login_days >= 10`, clearly labelled as an illustrative baseline rather than a validated policy.
- Model performance: accuracy, precision, recall, F1, and balanced accuracy.
- Calibration: inspect whether predicted probabilities correspond to observed outcomes when enough data is available.
- Fairness: evaluate relevant group-level error rates only when appropriate group information is available and lawful to use.
- Error analysis: inspect false positives and false negatives separately.
