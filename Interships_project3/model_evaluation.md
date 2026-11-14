# Model Evaluation – Bank Customer Churn

## Objective
Compare classification models for predicting whether a bank customer will exit (`Exited = 1`).

## Data split
- Training records: 8,000
- Test records: 2,000
- Stratified 80/20 train-test split (`random_state=42`)
- CustomerId and Surname were excluded from the model predictors.
- Numeric features were scaled and categorical features were one-hot encoded in preprocessing pipelines.

## Test-set performance

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 80.80% | 58.91% | 18.67% | 28.36% | 77.48% |
| Decision Tree | 85.60% | 78.74% | 40.05% | 53.09% | 84.23% |
| Balanced Decision Tree | 77.05% | 46.15% | 76.66% | 57.62% | 84.03% |

## Selected approach
The class-weighted (balanced) Decision Tree was selected for full-dataset churn-risk scoring because its recall was higher. Higher recall helps identify more customers who may churn, but the trade-off is lower precision and more false positives.

A probability threshold of **0.60** was used to label a customer as predicted churn when `Churn_Probability >= 0.60`. In the threshold comparison, this operating point gave:
- Accuracy: 80.2%
- Precision: 51.1%
- Recall: 68.6%
- F1-score: 58.6%
- Customers flagged in the test set: 546

The confusion matrix for the balanced Decision Tree at its default 0.50 threshold was:

| | Predicted not churn | Predicted churn |
|---|---:|---:|
| Actual not churn | 1,229 | 364 |
| Actual churn | 95 | 312 |

## Interpretation and limitations
- The standard Decision Tree had the highest accuracy and precision among the three models.
- The balanced Decision Tree had the highest recall and F1-score among the three models.
- The chosen threshold was explored using holdout test results. Therefore, threshold-specific performance may be optimistic. For a formal final evaluation, select the threshold on a separate validation set and evaluate it once on an untouched test set.
- Model predictions indicate risk, not certainty. They should support human review rather than automatic customer decisions.
