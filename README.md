# Telco Customer Churn Analysis: End-to-End Data Pipeline

![Power BI Dashboard](https://img.shields.io/badge/Power_BI-Dashboard-yellow?style=for-the-badge&logo=powerbi)
![Python](https://img.shields.io/badge/Python-Data_Cleaning_%26_ML-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Data_Analytics-blue?style=for-the-badge&logo=sqlite)

## 📌 Project Overview
This is an end-to-end data portfolio project analyzing the popular Kaggle **Telco Customer Churn** dataset. The goal of this project is to build an automated ETL pipeline, analyze business metrics related to customer retention, and predict future churn using Machine Learning.

The project is divided into three core phases:
1. **Python ETL & Machine Learning**: Automates data cleaning, generates Exploratory Data Analysis (EDA) visualizations, uploads the cleaned data to a local SQL database, and trains a tuned Gradient Boosting Classifier to predict churn.
2. **SQL Analytics**: Extracts critical business insights strictly utilizing aggregate SQL queries (Churn Rate, Revenue Impact, Contract vulnerabilities).
3. **Power BI Dashboarding**: Visualizes the insights to make them easily consumable for stakeholders.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** `pandas`, `sqlite3`, `matplotlib`, `seaborn`, `scikit-learn`
* **Database:** SQLite
* **Visualization:** Power BI Desktop

---

## 🚀 How to Run the Project

### Phase 1: Python Data Pipeline & ML
1. Ensure you have Python installed, then clone this repository.
2. Install the required dependencies:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn
   ```
3. Run the automated data pipeline:
   ```bash
   python 1_data_pipeline.py
   ```
   **What this script does:**
   - Cleans the raw CSV dataset (handles hidden nulls in `TotalCharges`).
   - Generates and saves EDA charts to the `/plots/` directory.
   - Exports `cleaned_telco_churn.csv`.
   - **Automated ETL**: Creates a local SQLite database (`telco.db`) and uploads the cleaned data into a `telco_churn` table.
   - **Machine Learning**: Trains and compares a Balanced Random Forest and a Gradient Boosting model, outputting a full classification report (Achieves ~80% Accuracy).

### Phase 2: SQL Business Analytics
With the `telco.db` SQLite database successfully generated from Phase 1, you can instantly run the business queries directly from your terminal/Command Prompt using PowerShell:

```powershell
Get-Content 2_business_queries.sql | sqlite3 telco.db -box
```
*Note: This requires `sqlite3` to be installed and available in your system PATH.*

### Phase 3: Power BI Dashboard
1. Open **Power BI Desktop**.
2. Import the `cleaned_telco_churn.csv`.
3. Follow the instruction manual provided in `3_powerbi_dashboard_guide.md` to recreate the DAX measures (Total Customers, Churn Rate %) and recommended interactive visualizations.

---

## 📊 Key Business Insights Discovered
1. **Overall Churn**: The baseline churn rate is **26.58%**.
2. **Contract Vulnerability**: Customers on `Month-to-month` contracts churn at an alarming **42.71%**, compared to just **2.85%** for users locked into a Two-year contract.
3. **Product Red Flags**: The `Fiber optic` internet service experiences a severe **41.89%** churn rate, strongly suggesting a need to investigate the pricing and competitive reliability of this specific tier compared to the `DSL` tier (19.0% churn).
4. **Behavioral Footprint**: Customers who churn typically do so early in their lifecycle (average tenure of **17.98 months**) and generally face higher monthly bills ($74.44 vs $61.31) than retained customers.

## 📝 Dataset Reference
The dataset used is the IBM Telco Customer Churn dataset available publicly on [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).