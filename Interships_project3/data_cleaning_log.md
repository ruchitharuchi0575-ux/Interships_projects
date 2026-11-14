# Data Cleaning Log – Bank Customer Churn

## Dataset
- Dataset: Bank Customer Churn (Maven Analytics Data Playground)
- Original file used in the notebook: `Bank_Churn.csv`
- Original shape: **10,000 rows × 13 columns**
- Target column: `Exited` (1 = customer exited; 0 = customer did not exit)

Source: https://mavenanalytics.io/data-playground/bank-customer-churn

> Add the actual date the dataset was downloaded before final submission. Check the provider's current usage terms before redistributing the source data.

## Quality checks and results

| Check | Result |
|---|---|
| Missing values | 0 |
| Duplicate rows | 0 |
| Invalid credit scores outside 300–850 | 0 |
| Ages outside the checked 18–100 range | 0 |
| Invalid values in `Exited` | 0 |
| Customers with `Exited = 0` | 7,963 |
| Customers with `Exited = 1` | 2,037 |

## Preparation steps
1. Loaded the CSV into pandas and inspected its shape, column names, data types and sample rows.
2. Checked missing values and duplicate records.
3. Reviewed basic ranges and categories, including credit score, age, geography, gender and target values.
4. Kept `CustomerId` for identifying and joining customer-level outputs, but excluded it from model predictors.
5. Excluded `Surname` from model predictors because it is an identifier-like text field.
6. Used numeric scaling and categorical one-hot encoding through a scikit-learn preprocessing pipeline.
7. Used a stratified train-test split to preserve the churn/non-churn proportions.

## Important notes
- A zero account balance was not automatically treated as an error; it can be a valid customer state.
- No rows were removed for missing values or duplicates because these checks found none.
- The cleaned/scored output files should be checked against the notebook before submission.
