# Cafe Sales - Exploratory Data Analysis Report

## OBJECTIVE

To uncover key trends, patterns, and actionable insights in café sales data to support data-driven decision-making related to customer behavior, product performance, and operational efficiency.

## Data Overview

The Dirty Cafe Sales dataset contains 10,000 rows of synthetic data representing sales transactions in a cafe. This dataset is intentionally "dirty," with missing values, inconsistent data, and errors introduced to provide a realistic scenario for data cleaning and exploratory data analysis (EDA). It can be used to practice cleaning techniques, data wrangling, and feature engineering.

## File Information

- **Source:** Café Sales – Dirty Data for Cleaning Training (Kaggle)  
- **Size:** 15,000+ transactions  
- **Period:** 1 year (Daily records)  
- **Columns:** Date, Time, Transaction, Item, Quantity, Total_Price, etc.

## Data Cleaning & Preprocessing

- Handled missing/null values  
- Converted Date and Time columns into unified Datetime  
- Standardized item names  
- Removed outliers in Quantity  
- Derived features: DayOfWeek, Hour, Month, Category

## Business Recommendations

1. **Focus on Best-Selling Items**  
   - Certain products consistently dominate sales volume across locations.  
   - Recommendation - Promote these top items through combo deals, loyalty programs, or seasonal campaigns to boost repeat purchases.

2. **Optimize Inventory by Location**  
   - Some café branches show significantly higher transaction volumes.  
   - Recommendation - Adjust inventory and staff allocation based on location-level performance. Consider scaling up high-performing locations or revisiting underperforming ones.

3. **Leverage Payment Preferences**  
   - A clear dominance of certain payment methods (e.g., digital wallets or credit cards) is observed.  
   - Recommendation - Ensure seamless support for preferred payment methods and incentivize digital payments via cashback or discounts.

4. **Utilize Time-Based Sales Trends**  
   - Weekends and certain days show spikes in sales, especially for specific items.  
   - Recommendation - Launch weekend-specific offers or promotions, and adjust staff schedules to handle peak times.

5. **Understand Customer Behavior Patterns**  
   - Quantity and total spending are positively correlated, especially with high-value items.  
   - Recommendation - Encourage bulk buying by offering quantity-based discounts or “Buy 2 Get 1 Free” deals.

6. **Maintain Clean Data Practices**  
   - Data inconsistencies like EERROR, UNKNOWN, and mismatched entries were present.  
   - Recommendation - Improve front-end data capture systems at POS (Point-of-Sale) to reduce manual errors and ensure reliable reporting.

7. **Monitor Outliers & Fraud**  
   - Outliers in total_spent may represent bulk purchases or errors.  
   - Recommendation - Set up automatic anomaly detection to flag transactions significantly outside the norm for review.

---

*With slight menu optimization and smarter promotions, we can boost both revenue and customer satisfaction without increasing operational load.*
