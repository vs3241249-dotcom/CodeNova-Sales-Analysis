# Sales Data Analysis
### CodeNova Data Science Internship — Task 1

## 1. Project Overview

This project presents an exploratory sales data analysis of the Sample Superstore dataset using Python. The objective is to evaluate sales performance, profitability, product performance, and time-based and geographic sales patterns.

The analysis transforms raw sales records into summary metrics, visualizations, and business-oriented observations that can support data-informed decision-making.

## 2. Business Objectives

- Calculate key performance indicators (KPIs), including total sales revenue, total profit, profit margin, average order value, and units sold.
- Identify monthly, quarterly, and seasonal sales patterns.
- Compare sales and profitability across product categories and individual products.
- Examine sales performance across regions and states.
- Analyze customer-segment performance.
- Present findings through clear visualizations and exported summary tables.

## 3. Dataset Description

**Dataset:** Sample - Superstore.csv

The dataset contains transaction-level information used to analyze orders, products, sales, profits, dates, locations, and customer segments.

Key fields used in this project include:

| Field | Purpose |
|---|---|
| Order ID | Count unique orders |
| Order Date | Analyze sales over time |
| Sales | Measure sales revenue |
| Profit | Evaluate profitability |
| Quantity | Measure units sold |
| Category | Compare product categories |
| Product Name | Analyze individual products |
| Region and State | Analyze geographic performance |
| Segment | Compare customer groups |

The dataset is loaded using Pandas. Date fields are converted to datetime format where required, and data quality checks are performed before analysis.

## 4. Tools and Technologies

- **Python** — analysis and calculations
- **Pandas** — data cleaning, grouping, aggregation, and analysis
- **Matplotlib** — data visualization
- **Jupyter Notebook** — interactive analysis and documentation

## 5. Key Performance Indicators

| Metric | Result |
|---|---:|
| Total Sales Revenue | 2,297,200.86 |
| Total Profit | 286,397.02 |
| Profit Margin | 12.47% |
| Average Order Value (AOV) | 458.61 |
| Total Units Sold | 37,873 |
| Unique Orders | 5,009 |

**Metric definitions**

- **Total Sales Revenue:** Sum of the Sales column.
- **Total Profit:** Sum of the Profit column.
- **Profit Margin:** Total Profit divided by Total Sales Revenue, multiplied by 100.
- **Average Order Value (AOV):** Total Sales Revenue divided by the number of unique Order IDs.
- **Total Units Sold:** Sum of the Quantity column.
- **Unique Orders:** Number of distinct Order IDs.

*Note: Currency formatting follows the source values; a currency symbol is not specified because the dataset's currency has not been independently verified.*

## 6. Analysis Performed

### 6.1 Time-Based Sales Analysis

Sales were aggregated by month, quarter, and season to examine changes in sales performance over time.

- Monthly sales trend analysis
- Quarterly sales comparison
- Seasonal sales comparison

### 6.2 Category and Product Analysis

Product performance was evaluated using sales, profit, quantity sold, and profit margin.

- Category-level sales and profit comparison
- Top 10 products by total sales
- Product-level profitability analysis

### 6.3 Geographic Analysis

Sales performance was compared across regions and states to identify locations with relatively high sales.

- Region-level sales and profit
- Top 15 states by sales

### 6.4 Customer Segment Analysis

Sales, profit, units sold, and unique orders were compared across the available customer segments.

*The Segment field represents customer groups in the dataset; it is not age- or gender-based demographic data.*

## 7. Key Findings

The following findings are calculated from the dataset analyzed in this project:

- **Leading sales category:** Technology
- **Leading profit category:** Technology
- **Leading sales region:** West
- **Leading state by sales:** California
- **Leading customer segment by sales:** Consumer
- **Highest-sales season:** Fall
- **Highest-sales quarter:** 2017Q4
- **Highest-sales month:** November 2017
- **Highest-sales product:** Canon imageCLASS 2200 Advanced Copier
- **Highest-total-profit product:** Canon imageCLASS 2200 Advanced Copier

These findings identify the top-performing groups by the stated measures. High sales do not necessarily imply high profitability; sales and profit should be assessed together.

## 8. Business Recommendations

Based on the analysis framework and observed performance, the following actions are worth considering:

1. **Improve category-level decisions:** Review both sales and profit by category before allocating promotional budgets.
2. **Investigate product profitability:** Compare high-sales products with their profit margins to avoid prioritizing revenue alone.
3. **Plan around sales patterns:** Use monthly and quarterly trends to inform inventory, staffing, and promotional planning.
4. **Review geographic performance:** Investigate differences in regional and state sales to identify opportunities for further analysis.
5. **Understand customer segments:** Compare sales and order patterns across segments when planning customer-focused campaigns.
6. **Validate before acting:** Confirm that observed patterns persist over time before making major operational or financial decisions.

These recommendations are starting points for further investigation, not proof of causation.

## 9. Visualizations and Output Files

Charts are exported as high-resolution PNG images, and summary tables are saved as CSV files in the `outputs/` directory.

| File | Description |
|---|---|
| `monthly_sales_trend.png` | Monthly sales trend |
| `quarterly_sales_analysis.png` | Quarterly sales comparison |
| `seasonal_sales_analysis.png` | Seasonal sales comparison |
| `category_sales_profit.png` | Category-level sales and profit |
| `top_10_products.png` | Top 10 products by sales |
| `region_sales_profit.png` | Regional sales and profit |
| `top_15_states_sales.png` | Top 15 states by sales |
| `customer_segment_sales.png` | Sales by customer segment |
| `category_performance.csv` | Category performance metrics |
| `product_performance.csv` | Product performance metrics |
| `high_margin_products.csv` | Selected higher-margin products |
| `region_performance.csv` | Regional performance metrics |
| `top_15_states.csv` | State-level sales summary |
| `customer_segment_analysis.csv` | Customer-segment summary |

## 10. Project Structure

```text
CodeNova-Sales-Analysis/
├── data/
│   └── Sample - Superstore.csv
├── outputs/
│   ├── monthly_sales_trend.png
│   ├── quarterly_sales_analysis.png
│   ├── seasonal_sales_analysis.png
│   ├── category_sales_profit.png
│   ├── top_10_products.png
│   ├── region_sales_profit.png
│   ├── top_15_states_sales.png
│   └── customer_segment_sales.png
├── Sales_Data_Analysis.ipynb
├── sales_analysis.py
└── README.md
```

The `outputs/` directory also contains the CSV summary tables generated during the analysis.

## 11. How to Run the Project

1. Install Python and Jupyter Notebook, or use Visual Studio Code with the Python and Jupyter extensions.
2. Install the required libraries:

   ```bash
   python -m pip install pandas matplotlib jupyter
   ```

3. Open the project folder in Visual Studio Code.
4. Select a Python environment in which the required libraries are installed.
5. Open `Sales_Data_Analysis.ipynb`.
6. Run the notebook cells in order from top to bottom.

Ensure that `data/Sample - Superstore.csv` exists at the expected relative path and that the `outputs/` directory is writable.

## 12. Limitations

- Findings describe the provided dataset and may not generalize to other businesses or periods.
- Profit margin is calculated from the aggregate profit and sales values; individual product margins can differ.
- Seasonal labels use a calendar-based Northern Hemisphere season mapping.
- Customer-segment analysis is limited to the groups available in the dataset.
- The analysis identifies patterns and associations; it does not establish the causes of sales or profit changes.
- Recommendations should be validated against business context and additional evidence before implementation.

## 13. Conclusion

This project demonstrates an end-to-end exploratory sales analysis workflow using Python, Pandas, and Matplotlib. It combines KPI calculation, time-based analysis, product and category comparisons, geographic analysis, customer-segment analysis, and visual reporting.

The resulting notebook, charts, and summary tables provide a foundation for understanding sales performance and identifying areas for further business investigation.

---

**Project:** Sales Data Analysis  
**Program:** CodeNova Data Science Internship  
**Task:** Task 1
