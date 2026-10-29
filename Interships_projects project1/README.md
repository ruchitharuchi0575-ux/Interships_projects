# Online Retail Sales KPI Analysis Using SQL and Excel

## 1. Project Overview
This project analyzes online retail transaction data using SQL and Microsoft Excel. The goal is to understand sales performance, customer behavior, product performance, and country-level revenue.

## 2. Tools Used
- DuckDB SQL
- Microsoft Excel
- CSV transaction data

## 3. Key Performance Indicators
- Total Revenue: 10,666,702.54
- Total Quantity: 5,660,980
- Total Orders: 20,726
- Total Customers: 4,339
- Total Countries: 38
- Average Order Value: 514.65
- Repeat Customer Rate: 65.57%

## 4. Key Findings
- November 2011 was the highest full month for revenue, at 1,509,496.33.
- PAPER CRAFT, LITTLE BIRDIE was the top product by quantity sold, with 80,995 units.
- The United Kingdom generated approximately 84.6% of total revenue.
- The repeat customer rate was 65.57% among customers with identified customer IDs.
- The dataset covers December 2010 through December 9, 2011.

## 5. Business Recommendations
1. Study successful promotions and test offers during weaker sales months.
2. Monitor stock levels for best-selling products.
3. Test loyalty programs and personalized customer offers.
4. Explore promising international markets.
5. Test product bundles and complementary-item recommendations to increase average order value.

## 6. Data Cleaning
- Excluded invoices beginning with C.
- Excluded transactions with quantity less than or equal to zero.
- Excluded transactions with negative prices.
- Excluded missing customer IDs when calculating customer metrics.
- Parsed invoice dates using the day-month-year format.

## 7. Limitations
- December 2011 is a partial month, with data ending on December 9.
- Missing customer IDs prevent some transactions from being linked to identified customers.
- Recommendations are proposed actions and should be tested before implementation.

## 8. Verification
SQL queries were used to calculate KPIs and analyze monthly revenue, products, customers, countries, and repeat purchasing. Results were checked against the source transaction data.