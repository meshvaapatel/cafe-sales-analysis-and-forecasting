# 📊 Cafe Sales Analysis & Forecasting 

An end-to-end data analytics project that transforms raw, messy transactional data into actionable business intelligence. This project encompasses a full Exploratory Data Analysis (EDA) using **Python**, an interactive **Power BI** Dashboard for visualization, and a predictive **Streamlit** web application powered by a machine learning model.

---

### 🎯 Project Objective

The primary objective of this project is to perform an in-depth exploratory data analysis on the "Cafe Sales – Dirty Data" dataset to uncover key trends, patterns, and actionable insights that drive sales and customer engagement. By transforming raw transactional data into strategic knowledge, this project aims to empower the café to make smarter, data-driven decisions.

The core goals are to:
* **Clean and Prepare Data -** Structure and sanitize messy sales data to ensure accuracy, consistency, and reliability for analysis.
* **Uncover Actionable Insights -** Identify key trends related to customer behavior, product performance, and operational efficiency.
* **Analyze Key Business Drivers -** Explore customer preferences, payment trends, item popularity, spending behavior, and time-based sales fluctuations.
* **Develop Strategic Recommendations -** Translate analytical findings into actionable strategies that can improve product offerings, optimize inventory, and enhance marketing campaigns.
* **Deploy a Predictive Tool -** Build and integrate a machine learning model into a user-friendly application to forecast customer spending.

---

### 📂 End-to-End Project Structure

```bash
├── data/
│   ├── raw/
│   │   └── cafe_sales.csv
│   └── processed/
│       └── cafe_sales_cleaned.csv
├── notebooks/
│   └── eda_workflow_process.ipynb
├── reports/
│   ├── sales_summary_report.md
│   └── Dashboard.png
├── src/
│   └── app.py
├── models/
│   └── cafe_sales_model.joblib
├── README.md
└── requirements.txt
```

---

### 💡 Key Insights & Findings

The analysis successfully converted raw data into a clear performance summary.

#### Key Performance Indicators (KPIs)
| Metric | Value |
| :--- | :--- |
| **Total Revenue** | $85,094.50 |
| **Total Transactions** | 9,510 |
| **Average Basket Size** | 3.03 |

#### Product & Customer Insights
* **Best-Selling Item (by Volume):** Juice (5,695 units sold).
* **Highest Revenue Item:** Juice ($16,943 in revenue).
* **Top Customer Payment Method:** Digital Wallet, used in **53%** of transactions.

---

### 📊 Interactive Power BI Dashboard

An interactive dashboard was created using **Power BI** to visualize key insights and allow for dynamic exploration of the data. This dashboard provides a high-level overview of sales performance, customer patterns, and product trends.

[Dashboard](/Dashboard.png)

---

### 🧠 About the Predictive Model

A machine learning pipeline was built using Scikit-learn to predict a customer's total spending based on their transaction details.

* **Model: Random Forest Regressor**
    * A `RandomForestRegressor` with 100 estimators was chosen for this task. This powerful ensemble model builds multiple decision trees and merges them, which helps to prevent overfitting and improve predictive accuracy on complex, tabular data.

* **Preprocessing Pipeline**
    * A `ColumnTransformer` was used to apply different transformations to different types of features:
        * **Categorical Features** (`item`, `payment_method`, `location`, `weekday`): Transformed using `OneHotEncoder` to convert them into a numerical format.
        * **Numerical Features** (`quantity`, `day`, `month`, `is_weekend`): Passed through without modification.

* **Evaluation**
    * The model's performance was evaluated on a hold-out test set using **Root Mean Squared Error (RMSE)** to measure the average difference between the predicted and actual spending values.

---

### 🚀 Streamlit Forecasting App

An interactive web application was built using **Streamlit** to provide a user-friendly interface for the predictive model.

#### How to Run the App
1.  Ensure all dependencies are installed (`pip install -r requirements.txt`).
2.  Run the app from your terminal:
    ```bash
    streamlit run app.py
    ```
3.  Select the item, quantity, payment method, and other details in the web interface to get an instant prediction of the total spend.

---

### 📈 Future Improvements

To further enhance this project, the following steps could be taken:

* **Hyperparameter Tuning -** Utilize GridSearchCV or RandomizedSearchCV to find the optimal hyperparameters for the RandomForestRegressor model, potentially improving its predictive accuracy.
* **Cloud Deployment -** Deploy the Streamlit application to a public cloud service (e.g., Streamlit Community Cloud, Heroku, or AWS) to make it accessible to a wider audience.
* **Automated Model Retraining -** Implement a CI/CD pipeline to automatically retrain and deploy the model as new sales data becomes available, preventing model drift.
* **Deeper Customer Segmentation: -** Perform a more in-depth customer analysis (e.g., RFM - Recency, Frequency, Monetary) to create targeted marketing campaigns.
* **Inventory Optimization Model -** Develop a separate time-series forecasting model to predict daily demand for specific items, helping to reduce waste and prevent stockouts.

---

### 🛠️ Tools & Libraries Used

| Tool / Library | Purpose |
| :--- | :--- |
| `pandas` / `numpy` | Data manipulation & numerical computations |
| `matplotlib` / `seaborn` | Data visualization |
| `scikit-learn` | Machine learning (Pipeline, Model, Preprocessing) |
| `joblib` | Saving & loading the trained model pipeline |
| `Power BI` | Interactive Dashboard creation |
| `Streamlit` | Building the interactive web application |

---

### 📄 Summary Report
For a detailed explanation of the project, insights, and business recommendations, please read the full summary report.
👉 **[Click here to read the full Summary Report](./reports/sales_summary_report.md)**

---

### 🌟 About Me

Hi, I’m **Meshva Patel**

A **Data Analyst** and **aspiring Data Scientist** with a passion for uncovering stories hidden in data. My journey is all about exploring how data shapes strategy, and each project helps me grow closer to that goal.

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/meshvaapatel/) or explore more of my work on [GitHub](https://github.com/meshvaapatel/).

---

### 📌 Tags
`#CafeSales` `#EDA` `#DataAnalytics` `#Python` `#PowerBI` `#Streamlit` `#PortfolioProject` `#DashboardDesign` `#BusinessInsights` `#MachineLearning` `#RandomForest`


