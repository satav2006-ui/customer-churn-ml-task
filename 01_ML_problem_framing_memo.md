# ML Problem-Framing Memo: Customer Churn

## Decision
The dataset may support a limited decision-support workflow for identifying customers who may be at higher risk of churn so that a human customer-success team can consider appropriate retention outreach.

The model must not automatically cancel accounts, deny service, change pricing, or make other high-impact decisions without human review.

## Prediction target
- Target: `churned`
- 1 = customer churned
- 0 = customer did not churn

## Unit of observation
One row represents one customer record in the supplied training dataset.

## Proposed prediction framing
Use customer information available before a retention decision to estimate churn risk. Features in the supplied dataset are:
- `tenure_months`
- `support_tickets`
- `monthly_spend_inr`
- `last_login_days`
- `plan_type`

`customer_id` is an identifier and should not be used as a predictive feature.

## Action window
The supplied dataset does not specify an exact future prediction window. Therefore, the prediction horizon should be explicitly defined before production use. This notebook treats the supplied `churned` label as the training target only and does not claim a validated real-world forecasting horizon.

## Non-ML baseline
A simple illustrative rule is:
> Flag a customer as potentially at risk when `last_login_days >= 10`.

This is a transparent baseline, not a validated business policy. It should be reviewed against real operational costs before use.

## Model baseline
A logistic-regression baseline can be trained using the numeric features and one-hot encoded `plan_type`. `customer_id` is excluded.

Because the supplied dataset contains only 12 rows, any measured performance is highly uncertain and must not be treated as evidence of production performance.

## Error costs
- False positive: a customer is flagged as at risk when they would not churn. This can waste outreach time and may annoy customers.
- False negative: a customer who is likely to churn is not flagged. This may cause a missed retention opportunity.

The relative cost of these errors should be confirmed with the business team before selecting a production threshold.

## Human review and fallback
Model output should be treated as a prioritization signal. A human should review the context before taking action. If the model is unavailable, the fallback should be the existing non-ML customer-success process rather than an automatic adverse action.

## Monitoring and rollback
Monitor data quality, missingness, feature distribution, prediction volume, calibration, false-positive/false-negative rates, and performance by relevant groups where legally and ethically appropriate. Roll back to the non-ML process if data quality or model performance falls below agreed thresholds.
