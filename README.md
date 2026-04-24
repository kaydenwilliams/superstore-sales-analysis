# Superstore Sales & Business Intelligence Analysis

## Overview
End-to-end retail analytics project analyzing 9,994 US orders from 2014 to 2017. 
Combines SQL business intelligence queries and Python EDA to uncover the financial 
impact of discounting on profitability across regions, categories, and states.

## Tools
Python (pandas, matplotlib, seaborn), MySQL, Tableau

## Dataset
Sample Superstore: 9,994 US retail orders across 3 product categories and 4 regions.
https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

## Key Findings
- Orders with 0% discount generated 29.5% profit margin vs -77.4% for orders 
  with 40%+ discounts — a 107 percentage point swing
- Texas, Ohio, and Pennsylvania account for $58,000+ in combined losses
- Furniture sub-categories (Tables, Bookcases) generated high revenue but 
  deeply negative profit margins
- Technology was the most profitable category at 17.4% margin
- The Central region was the weakest performer driven by aggressive discounting
- The West region was the strongest performer with the healthiest margins

## Business Recommendations
1. Implement a hard discount cap of 20% across all categories
2. Prioritize discount reduction in Texas and Ohio immediately
3. Review Furniture pricing strategy — current model generates revenue but 
   destroys margin
4. Shift marketing focus toward Technology in the West region where margins 
   are strongest

## SQL Concepts Demonstrated
GROUP BY aggregations, HAVING clauses, CASE WHEN statements, window functions 
(RANK, running totals), subqueries, multi-table joins

## Files
- `analysis.sql` — 10 business intelligence SQL queries
- `analysis.py` — Python data cleaning and EDA script
- `load_to_mysql.py` — Python script to load CSV into MySQL
- `outputs/` — exported query results and charts used in Tableau

## Tableau Dashboards
Sales Analysis:
https://public.tableau.com/app/profile/kayden.williams2622/viz/SuperstoreSalesPerformanceDashboard_17759623279820/SuperstoreSalesPerformanceDashboard2014-2017

Business Intelligence:
https://public.tableau.com/app/profile/kayden.williams2622/viz/SuperstoreProfitabilityandDiscountImpactAnalysis/SuperstoreProfitabilityandDiscountImpactAnalysis?publish=yes

## Note
This project is included as supplementary portfolio work demonstrating SQL and 
Python proficiency. The primary analytics portfolio consists of Walmart Sales 
Analysis, TheLook Financial Analysis, Customer Segmentation, and Excel Financial 
Dashboard.
