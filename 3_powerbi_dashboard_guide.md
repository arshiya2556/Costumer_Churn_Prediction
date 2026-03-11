# Power BI Dashboard Guide: Telco Customer Churn

This guide provides step-by-step instructions to build a comprehensive Power BI dashboard using the cleaned dataset to identify actionable churn insights.

## Step 1: Data Import
1. Open Power BI Desktop.
2. Click on **Get Data** -> **Text/CSV**.
3. Select `cleaned_telco_churn.csv` and click **Load**. 
4. Check the data types in the Data View. Ensure that `TotalCharges` is highly accurate (Decimal Number) and `tenure` is categorized as a Whole Number.

---

## Step 2: Create DAX Measures (KPIs)
Right-click on the imported `cleaned_telco_churn` table and select **New Measure** to create the following foundational formulas. These will power your dashboard cards and visuals.

**1. Total Customers:**
```dax
Total Customers = COUNTROWS('cleaned_telco_churn')
```

**2. Churned Customers:**
```dax
Churned Customers = CALCULATE([Total Customers], 'cleaned_telco_churn'[Churn] = "Yes")
```

**3. Retained Customers:**
```dax
Retained Customers = CALCULATE([Total Customers], 'cleaned_telco_churn'[Churn] = "No")
```

**4. Churn Rate %:**
```dax
Churn Rate % = DIVIDE([Churned Customers], [Total Customers], 0)
```
*(Note: After creating this measure, highlight it and click the **%** icon in the Measure Tools formatting tab at the top).*

---

## Step 3: Recommended Visualizations

Use the following visuals to build an effective, stakeholder-ready reporting page.

### 1. KPI Summary Cards (Top of Dashboard)
Use **Card** visuals to prominently array high-level metrics across the top.
*   **Card 1**: `Total Customers`
*   **Card 2**: `Churned Customers`
*   **Card 3**: `Churn Rate %`

### 2. Churn Rate by Contract Type (Donut Chart)
*   **Visual Type**: Donut Chart
*   **Legend**: `Contract`
*   **Values**: `Churned Customers` or `Churn Rate %`
*   **Purpose**: Vividly demonstrates the proportion of churn arising from unstable Month-to-Month contracts.

### 3. Churn Status by Internet Service (Clustered Bar Chart)
*   **Visual Type**: Clustered Bar Chart
*   **Y-axis**: `InternetService`
*   **X-axis**: `Total Customers`
*   **Legend**: `Churn`
*   **Purpose**: Outlines the volume of retained vs. churning customers strictly by their internet provision plan (DSL vs. Fiber Optic vs. None).

### 4. Demographic Churn Analysis (Stacked Column Chart)
*   **Visual Type**: Stacked Column Chart
*   **X-axis**: `SeniorCitizen` *(Optional Prep: Convert 0/1 to "No"/"Yes" in Power Query for better readability)*
*   **Y-axis**: `Total Customers`
*   **Legend**: `Churn`
*   **Purpose**: Analyzes how senior citizen groups churn compared to standard demographics.

### 5. Churn Rate by Tenure Group (Line and Clustered Column Chart)
*   *(Optional Prep)* First, create a **New Column** (not a Measure!) to bin the tenure months:
    ```dax
    Tenure Group = SWITCH(
        TRUE(),
        'cleaned_telco_churn'[tenure] <= 12, "0-1 Year",
        'cleaned_telco_churn'[tenure] <= 24, "1-2 Years",
        'cleaned_telco_churn'[tenure] <= 36, "2-3 Years",
        'cleaned_telco_churn'[tenure] <= 48, "3-4 Years",
        'cleaned_telco_churn'[tenure] <= 60, "4-5 Years",
        "5+ Years"
    )
    ```
*   **Visual Type**: Line and Clustered Column Chart
*   **X-axis**: `Tenure Group`
*   **Column Y-axis**: `Total Customers`
*   **Line Y-axis**: `Churn Rate %`
*   **Purpose**: Demonstrates customer lifecycle drop-off. You typically see churn rates plummet after the 1-2 year mark as loyalty settles.

---

## Step 4: Add Interactive Slicers (Filters)
Add **Slicer** visuals on the left margin or top right of the dashboard to empower stakeholders to interactably drill into specific segments.
1.  **Gender Slicer**: Field = `gender` (Format as Dropdown or Tile).
2.  **Payment Method Slicer**: Field = `PaymentMethod`. (Identifies if Electronic Check users are more prone to churn).
3.  **Dependents Slicer**: Field = `Dependents`.

## Step 5: Formatting and Polish
*   **Color Theme**: Apply a consistent layout logic. Example: Red/Orange for Churned Customers, Blue/Green for Retained.
*   **Titles**: Replace auto-generated Power BI titles with human-readable titles (e.g., Change "Total Customers by InternetService" to "Customer Base by Internet Service").
*   **Header**: Add a clean Text Box Title at the very top: "Telco Customer Churn Overview Dashboard".
