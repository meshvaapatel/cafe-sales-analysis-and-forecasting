## 📊 Cafe Sales - Exploratory Data Analysis

An end-to-end data analytics project that transforms raw, messy transactional data into actionable business intelligence. This project encompasses a full Exploratory Data Analysis (EDA) using **Python** and an interactive **Power BI** Dashboard for visualization.

---

### 🎯 Project Objective

The primary objective of this project is to perform an in-depth exploratory data analysis on the "Cafe Sales – Dirty Data" dataset to uncover key trends, patterns, and actionable insights. By transforming raw transactional data into strategic knowledge, this project aims to empower the café to make smarter, data-driven decisions.

The core goals are to:

- **Clean and Prepare Data** - Structure and sanitize messy sales data to ensure accuracy, consistency, and reliability for analysis.  
- **Uncover Actionable Insights** - Identify key trends related to customer behavior, product performance, and operational efficiency.  
- **Analyze Key Business Drivers** - Explore customer preferences, payment trends, item popularity, spending behavior, and time-based sales fluctuations.  
- **Develop Strategic Recommendations** - Translate analytical findings into actionable strategies that can improve product offerings, optimize inventory, and enhance marketing campaigns.  

---

### 📂 Project Structure

```bash
├── data/                # Contains all project data
│   ├── raw/             # Original, immutable data
│   │   └── cafe_sales_dirty.csv
│   └── processed/       # Cleaned and feature-engineered data
│       └── cafe_sales_cleaned.csv
├── notebooks/           # Jupyter notebooks for analysis and experimentation
│   └── eda_workflow_process.ipynb
├── reports/             # Generated reports, figures, and summaries
│   ├── sales_summary_report.md
│   └── figures/
│       └── Dashboard.png
├── src/                 # Source code for the application
│   └── app.py
├── models/              # Trained and serialized machine learning models
│   └── cafe_sales_model.joblib
├── .gitignore           # Specifies files for Git to ignore
├── README.md            # Project overview and documentation (this file)
└── requirements.txt     # Project dependencies for installation
```
---
### 🔄 Workflow Process

The analysis follows a structured process as detailed in the Jupyter Notebook:

1.  **Data Loading & Initial Overview**: The dataset was loaded to understand its structure, shape (15,000 rows, 8 columns), and initial data types.
2.  **Data Cleaning & Preprocessing**: This phase involved correcting inconsistent values (e.g., "ERROR", "UNKNOWN"), converting data types, and imputing missing data using appropriate methods (mode, mean, median, and linear regression).
3.  **Outlier Detection & Capping**: Outliers in the `total_spent` column were identified using the Interquartile Range (IQR) method and capped to prevent skewing the analysis.
4.  **Exploratory Data Analysis (EDA)**: Both univariate and bivariate analyses were conducted to explore data distributions and relationships between variables.
5.  **Feature Engineering**: New features (`day`, `month`, `is_weekend`) were created from the date column, and categorical variables were encoded for analysis.
6.  **Data Visualization & Insight Generation**: Findings were visualized to generate actionable business recommendations.
   
---

### 🛠️ Tools & Libraries Used

| Tool / Library           | Purpose                                     |
|--------------------------|-------------------------------------------- |
| `pandas` / `numpy`       | Data manipulation & numerical computations  |
| `matplotlib` / `seaborn` | Data visualization                          |
| `Power BI`               | Interactive Dashboard creation              |

---

### 💡 Key Insights & Findings

The analysis successfully converted raw data into a clear performance summary.

#### Descriptive Analysis

| Metric | Value |
| :--- | :--- |
| **Total Revenue** | **$85,094.50** |
| **Total Transactions** | **9,510** |
| **Unique Items Sold** | **8** |
| **Avg. Basket Size** | **3.03** |
| **Top Category (by Qty)** | **Juice** |

#### Data Visualization Analysis

**🛒 Best-Selling Items (by Quantity)**
| Rank | Item | Quantity Sold |
| :--- | :--- | :--- |
| 1 | Juice | 5695 |
| 2 | Coffee | 3459 |
| 3 | Cake | 3367 |

**💸 Revenue by Item**
| Rank | Item | Total Revenue |
| :--- | :--- | :--- |
| 1 | Juice | $16,943 |
| 2 | Salad | $16,468 |
| 3 | Sandwich | $13,170 |

**💳 Customer Payment Preferences**
* Digital Wallet - **53.0%**
* Credit Card - **23.6%**
* Cash - **23.4%**

---

### 📊 Interactive Power BI Dashboard

An interactive dashboard was created using **Power BI** to visualize key insights and allow for dynamic exploration of the data. This dashboard provides a high-level overview of sales performance, customer patterns, and product trends.

---

### 📄 Summary Report

For a detailed explanation of the project, insights, and business recommendations, please read the full summary report.  
👉 **[Click here to read the full Summary Report](https://www.google.com/search?q=./reports/sales_summary_report.md)**

---

### 🌟 About Me

Hi, I’m **Meshva Patel**  

A **Data Analyst** and **aspiring Data Scientist** with a passion for uncovering stories hidden in data. My journey is all about exploring how data shapes strategy, and each project helps me grow closer to that goal.

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/meshvaapatel/) or explore more of my work on [GitHub](https://github.com/meshvaapatel/).

---

## 📌 Tags

`#CafeSales` `#EDA` `#DataAnalytics` `#Python` `#PowerBI` `#PortfolioProject` `#DashboardDesign` `#BusinessInsights`



