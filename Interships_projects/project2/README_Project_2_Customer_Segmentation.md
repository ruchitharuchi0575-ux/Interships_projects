# Project 2: Customer Segmentation and Retention Analysis

**Internship track:** Data Analytics  
**Dataset:** Online Retail II (UCI Machine Learning Repository)  
**Tools:** Python, Pandas, Matplotlib, Seaborn, Jupyter Notebook / Google Colab  
**Analysis period in source data:** December 2009 to December 2011

## 1. Project Overview

This project analyses retail transactions to understand customer purchasing behaviour and customer retention. It uses **RFM analysis** (Recency, Frequency and Monetary value) to group customers and **cohort analysis** to study how customer activity changes after a customer's first purchase.

The project is based on the Online Retail II dataset. The analysis uses only the dataset downloaded for this project; it does not collect customer or sales data from live websites.

## 2. Objectives

- Clean and prepare the transaction data for analysis.
- Calculate transaction revenue and customer-level RFM measures.
- Assign customer scores and create customer segments.
- Build a monthly cohort customer-count matrix and retention-percentage matrix.
- Visualise cohort retention with a heatmap.
- Recommend practical ways to encourage repeat purchases and retain customers.

## 3. Dataset

The source workbook contains two sheets: `Year 2009-2010` and `Year 2010-2011`. The combined source data contains **1,067,371 rows and 8 columns**.

| Field | Description |
|---|---|
| Invoice | Invoice or transaction identifier |
| StockCode | Product code |
| Description | Product description |
| Quantity | Number of items in the transaction line |
| InvoiceDate | Transaction date and time |
| Price | Unit price |
| Customer ID | Customer identifier |
| Country | Customer country |

**Source:** Chen, D. (2012). *Online Retail II* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5CG6D

## 4. Data Cleaning Summary

| Cleaning item | Result |
|---|---:|
| Original records | 1,067,371 |
| Duplicate rows removed | 34,335 |
| Rows with missing Customer ID removed | 235,151 |
| Cancelled invoice records removed | 18,390 |
| Invalid quantity / price records removed | 70 |
| Final valid transaction rows | **779,425** |
| Total transaction revenue | **17,374,804.27** |

Missing product descriptions were replaced with `Unknown`. Cancelled invoices were identified by invoice values beginning with `C`. Valid sales were restricted to positive quantities and positive prices. Transaction revenue was calculated as `Quantity × Price`.

Five automated data-quality checks passed on the cleaned dataset: no duplicate rows, no missing Customer IDs, no cancelled invoices, all quantities positive and all prices positive.

## 5. Methods

### RFM analysis

- **Recency:** number of days since the customer's latest purchase, relative to the day after the last transaction in the dataset.
- **Frequency:** number of distinct invoices for the customer.
- **Monetary:** sum of transaction revenue for the customer.
- Customer scores were assigned on a 1–4 scale using quartiles. Lower recency receives a higher recency score; higher frequency and monetary values receive higher scores.

A simple rule-based segmentation was applied. Segment labels are analytical groupings for this project, not externally validated customer classifications.

### Cohort analysis

Each customer's cohort month is the month of their first recorded purchase. The cohort index measures the number of months between that first-purchase month and each later transaction month. Unique customers are counted in each cohort-month cell. Retention percentage is calculated by dividing each cell by the cohort's month-zero customer count and multiplying by 100.

## 6. RFM Segment Summary

The analysis identified **5,878 customers**.

| Segment | Customers | Avg. Recency (days) | Avg. Frequency | Avg. Monetary |
|---|---:|---:|---:|---:|
| At Risk Customers | 1,470 | 514.03 | 2.02 | 712.90 |
| Big Spenders | 204 | 42.17 | 2.33 | 2,416.85 |
| Loyal Customers | 2,051 | 29.62 | 12.94 | 6,485.55 |
| Others | 1,469 | 225.47 | 4.01 | 1,541.84 |
| Recent Customers | 684 | 39.81 | 1.61 | 390.32 |

## 7. Retention Recommendations

- **Loyal Customers:** recognise repeat purchases with loyalty benefits and relevant exclusive offers.
- **At-Risk Customers:** test personalised win-back messages and carefully targeted offers. Prioritise high-value customers within this group.
- **Big Spenders:** offer relevant premium products or personalised service without assuming that high spend alone means loyalty.
- **Recent Customers:** provide helpful onboarding, product suggestions and a reason to make a second purchase.
- **All segments:** monitor repeat-purchase and cohort-retention trends over time to assess whether retention campaigns are working.

## 8. Repository Contents

A suggested GitHub structure is:

```text
Project_2_Customer_Segmentation/
├── data/
│   └── cleaned_online_retail.csv.gz
├── notebooks/
│   └── Project_2_Customer_Segmentation.ipynb
├── outputs/
│   ├── customer_rfm_analysis.csv
│   ├── customer_segment_summary.csv
│   ├── cohort_customer_counts.csv
│   ├── cohort_retention_percentage.csv
│   └── cohort_retention_heatmap.png
├── reports/
│   ├── data_cleaning_log.md
│   ├── data_quality_checks.py
│   ├── customer_retention_plan.md
│   └── project_conclusion.md
├── README.md
└── README_Project_2_Customer_Segmentation.pdf
```

The original Excel workbook is approximately 43.5 MB and should not be uploaded through GitHub's standard browser uploader. Link to the UCI source dataset instead. The cleaned compressed CSV was previously measured at approximately **12.45 MB**. If the team uses three compressed parts instead, document their filenames and reassemble them in row order before analysis.

## 9. How to Run

1. Download the dataset from the UCI source listed above, or obtain the team's approved cleaned CSV.
2. Open `Project_2_Customer_Segmentation.ipynb` in Google Colab or Jupyter Notebook.
3. Install the required Python packages if needed: `pandas`, `openpyxl`, `matplotlib` and `seaborn`.
4. Update the dataset path in the notebook to match the file location.
5. Run the notebook cells in order.
6. Review the cleaning checks, RFM segment summary and cohort heatmap.

Example installation command:

```bash
pip install pandas openpyxl matplotlib seaborn
```

## 10. Limitations

- The source transactions cover 2009–2011 and may not represent current retail behaviour.
- Transactions without a Customer ID are excluded from customer-level RFM and cohort calculations.
- The RFM segments use simple quartile scores and project-specific rules; thresholds can be adjusted for a business context.
- Cohort retention describes observed repeat purchasing, not the reason a customer did or did not return.
- The retention recommendations are proposed actions. Their effectiveness would need to be tested using future data or controlled experiments.

## 11. Conclusion

The project prepared **779,425 valid sales records** and analysed **5,878 identified customers**. RFM analysis produced five customer groups, while cohort analysis provided monthly customer-count and retention views. Together, these methods help describe purchasing patterns and support targeted customer-retention planning.

---

**Team contributions:** Member 1 - data preparation, data-quality checks, RFM analysis and segmentation. Member 2 - cohort analysis, retention matrix and heatmap, and retention plan. Both members - integration, review and final submission. Replace these role labels with the actual team member names before submission if required.
