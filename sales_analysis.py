# ============================================================
# CodeNova Internship - Task 1: Sales Data Analysis
# ============================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Project folders
DATA_FILE = os.path.join("data", "Sample - Superstore.csv")
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set_theme(style="whitegrid")

print("=" * 60)
print("CODENOVA INTERNSHIP - SALES DATA ANALYSIS")
print("=" * 60)

# 1. Load dataset
df = pd.read_csv(DATA_FILE, encoding="latin1")

print("\n1. DATASET OVERVIEW")
print("-" * 40)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nFirst five rows:")
print(df.head().to_string(index=False))

# 2. Check required columns
required_columns = [
    "Order Date", "Sales", "Profit",
    "Quantity", "Category", "Region", "Order ID"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Required columns not found: {missing_columns}. "
        f"Available columns: {df.columns.tolist()}"
    )

# 3. Prepare dates and numeric columns
df["Order Date"] = pd.to_datetime(
    df["Order Date"], errors="coerce"
)

for column in ["Sales", "Profit", "Quantity"]:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Remove rows missing essential analysis fields
analysis_df = df.dropna(
    subset=[
        "Order Date", "Sales", "Profit",
        "Quantity", "Category", "Region", "Order ID"
    ]
).copy()

if analysis_df.empty:
    raise ValueError("No valid rows remain after checking required fields.")

print("\nValid analysis rows:", len(analysis_df))
print("Rows excluded for missing/invalid required fields:",
      len(df) - len(analysis_df))

# 4. Calculate business metrics
total_revenue = analysis_df["Sales"].sum()
total_profit = analysis_df["Profit"].sum()
total_units = analysis_df["Quantity"].sum()
total_orders = analysis_df["Order ID"].nunique()

profit_margin = (
    total_profit / total_revenue * 100
    if total_revenue != 0 else np.nan
)

average_order_value = (
    total_revenue / total_orders
    if total_orders != 0 else np.nan
)

print("\n2. KEY BUSINESS METRICS")
print("-" * 40)
print(f"Total Revenue:       {total_revenue:,.2f}")
print(f"Total Profit:        {total_profit:,.2f}")
print(f"Profit Margin:       {profit_margin:.2f}%")
print(f"Average Order Value: {average_order_value:,.2f}")
print(f"Total Units Sold:    {total_units:,.0f}")
print(f"Unique Orders:       {total_orders:,}")

# 5. Monthly sales trend
analysis_df["YearMonth"] = (
    analysis_df["Order Date"].dt.to_period("M")
)

monthly_sales = (
    analysis_df.groupby("YearMonth")["Sales"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(12, 6))
monthly_sales.plot(marker="o", linewidth=2)
plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "monthly_sales.png"),
    dpi=300, bbox_inches="tight"
)
plt.close()

# 6. Quarterly sales trend
analysis_df["Quarter"] = (
    analysis_df["Order Date"].dt.to_period("Q")
)

quarterly_sales = (
    analysis_df.groupby("Quarter")["Sales"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(12, 6))
quarterly_sales.plot(
    kind="bar", color="steelblue"
)
plt.title("Quarterly Sales Trend", fontsize=16)
plt.xlabel("Quarter")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "quarterly_sales.png"),
    dpi=300, bbox_inches="tight"
)
plt.close()

# 7. Seasonal analysis by calendar quarter
analysis_df["Season"] = (
    "Q" + analysis_df["Order Date"].dt.quarter.astype(str)
)

seasonal_sales = (
    analysis_df.groupby("Season")["Sales"]
    .sum()
    .reindex(["Q1", "Q2", "Q3", "Q4"])
)

plt.figure(figsize=(9, 5))
seasonal_sales.plot(
    kind="bar", color="darkcyan"
)
plt.title("Sales by Calendar Quarter", fontsize=15)
plt.xlabel("Calendar Quarter")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "seasonal_sales.png"),
    dpi=300, bbox_inches="tight"
)
plt.close()

# 8. Category-wise performance
category_performance = (
    analysis_df.groupby("Category")
    .agg(
        Revenue=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Units_Sold=("Quantity", "sum")
    )
)

category_performance["Profit_Margin_Percent"] = (
    category_performance["Profit"]
    / category_performance["Revenue"].replace(0, np.nan)
    * 100
)

category_performance = category_performance.sort_values(
    "Revenue", ascending=False
)

print("\n3. CATEGORY-WISE PERFORMANCE")
print("-" * 40)
print(category_performance.round(2).to_string())

category_performance.to_csv(
    os.path.join(OUTPUT_DIR, "category_performance.csv")
)

# Revenue by category
plt.figure(figsize=(10, 6))
sns.barplot(
    data=category_performance.reset_index(),
    x="Category",
    y="Revenue"
)
plt.title("Revenue by Product Category", fontsize=15)
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "category_revenue.png"),
    dpi=300, bbox_inches="tight"
)
plt.close()

# Profit margin by category
plt.figure(figsize=(10, 6))
sns.barplot(
    data=category_performance.reset_index(),
    x="Category",
    y="Profit_Margin_Percent"
)
plt.title("Profit Margin by Product Category", fontsize=15)
plt.xlabel("Category")
plt.ylabel("Profit Margin (%)")
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "category_profit_margin.png"),
    dpi=300, bbox_inches="tight"
)
plt.close()

# 9. Geographic analysis
region_performance = (
    analysis_df.groupby("Region")
    .agg(
        Revenue=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Units_Sold=("Quantity", "sum")
    )
)

region_performance["Profit_Margin_Percent"] = (
    region_performance["Profit"]
    / region_performance["Revenue"].replace(0, np.nan)
    * 100
)

region_performance = region_performance.sort_values(
    "Revenue", ascending=False
)

print("\n4. REGION-WISE PERFORMANCE")
print("-" * 40)
print(region_performance.round(2).to_string())

region_performance.to_csv(
    os.path.join(OUTPUT_DIR, "region_performance.csv")
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=region_performance.reset_index(),
    x="Region",
    y="Revenue"
)
plt.title("Revenue by Region", fontsize=15)
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "regional_sales.png"),
    dpi=300, bbox_inches="tight"
)
plt.close()

# 10. Top-selling products
if "Product Name" in analysis_df.columns:
    product_performance = (
        analysis_df.groupby("Product Name")
        .agg(
            Revenue=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Units_Sold=("Quantity", "sum")
        )
        .sort_values("Revenue", ascending=False)
    )

    print("\n5. TOP 10 PRODUCTS BY REVENUE")
    print("-" * 40)
    print(product_performance.head(10).round(2).to_string())

    product_performance.to_csv(
        os.path.join(OUTPUT_DIR, "product_performance.csv")
    )

# 11. Export summary metrics
summary = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Total Profit",
        "Profit Margin (%)",
        "Average Order Value",
        "Total Units Sold",
        "Unique Orders"
    ],
    "Value": [
        total_revenue,
        total_profit,
        profit_margin,
        average_order_value,
        total_units,
        total_orders
    ]
})

summary.to_csv(
    os.path.join(OUTPUT_DIR, "business_metrics.csv"),
    index=False
)

# 12. Generate evidence-based business observations
best_category = category_performance["Revenue"].idxmax()
best_region = region_performance["Revenue"].idxmax()
best_month = monthly_sales.idxmax()

print("\n6. BUSINESS OBSERVATIONS")
print("-" * 40)
print(
    f"Highest-revenue category: {best_category} "
    f"({category_performance.loc[best_category, 'Revenue']:,.2f})"
)
print(
    f"Highest-revenue region: {best_region} "
    f"({region_performance.loc[best_region, 'Revenue']:,.2f})"
)
print(
    f"Highest-sales month: {best_month} "
    f"({monthly_sales.loc[best_month]:,.2f})"
)

print("\n7. OUTPUT FILES")
print("-" * 40)
print(f"Charts and reports saved in: {OUTPUT_DIR}/")
print("Analysis completed successfully!")