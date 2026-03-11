-- SQL Queries for Telco Customer Churn Business Analysis
-- Assumption: The cleaned data has been loaded into a table named 'telco_churn'

-- 1. What is the overall churn rate percentage?
-- Business Value: Provides a high-level KPI to monitor the overall health of the customer base. 
-- A high churn rate indicates systemic challenges with retention or customer satisfaction.
SELECT 
    COUNT(CASE WHEN Churn = 'Yes' THEN 1 END) AS ChurnedCustomers,
    COUNT(*) AS TotalCustomers,
    ROUND((COUNT(CASE WHEN Churn = 'Yes' THEN 1 END) * 100.0) / COUNT(*), 2) AS ChurnRatePercentage
FROM telco_churn;


-- 2. How does the churn rate differ by Contract type?
-- Business Value: Helps identify which contract types are most vulnerable.
-- Typically, Month-to-Month contracts have higher churn, indicating an opportunity to create incentives to lock customers into 1-year or 2-year contracts.
SELECT 
    Contract,
    COUNT(*) AS TotalCustomers,
    COUNT(CASE WHEN Churn = 'Yes' THEN 1 END) AS ChurnedCustomers,
    ROUND((COUNT(CASE WHEN Churn = 'Yes' THEN 1 END) * 100.0) / COUNT(*), 2) AS ChurnRatePercentage
FROM telco_churn
GROUP BY Contract
ORDER BY ChurnRatePercentage DESC;


-- 3. Which InternetService has the highest churn rate?
-- Business Value: Pinpoints potential service quality or pricing issues with specific internet offerings.
-- E.g., if Fiber Optic has high churn, there could be pricing sensitivity or reliability issues relative to competitors.
SELECT 
    InternetService,
    COUNT(*) AS TotalCustomers,
    COUNT(CASE WHEN Churn = 'Yes' THEN 1 END) AS ChurnedCustomers,
    ROUND((COUNT(CASE WHEN Churn = 'Yes' THEN 1 END) * 100.0) / COUNT(*), 2) AS ChurnRatePercentage
FROM telco_churn
GROUP BY InternetService
ORDER BY ChurnRatePercentage DESC;


-- 4. What is the average tenure and MonthlyCharges for customers who churned vs. those who stayed?
-- Business Value: Helps profile churners behaviorally and financially. 
-- Do they churn early in their lifecycle (low tenure)? Are they paying significantly more than retained customers, suggesting they find 'MonthlyCharges' too expensive?
SELECT 
    Churn,
    COUNT(*) AS NumberOfCustomers,
    ROUND(AVG(tenure), 2) AS AverageTenureMonths,
    ROUND(AVG(MonthlyCharges), 2) AS AverageMonthlyCharges
FROM telco_churn
GROUP BY Churn;
