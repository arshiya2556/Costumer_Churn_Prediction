import pandas as pd
import numpy as np

# 1. Load the dataset
# Make sure the CSV file is in the same directory as your Python script
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# 2. Inspect the data
print(df.info())
print(df.head())

# 3. Data Cleaning
# The 'TotalCharges' column is currently an object (string) because of empty spaces.
# Let's replace the empty spaces with NaN and convert it to numeric.
df['TotalCharges'] = df['TotalCharges'].replace(" ", np.nan)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])

# Check how many null values we have
print("Missing values in TotalCharges:", df['TotalCharges'].isnull().sum())

# Since it's only 11 rows out of 7000+, we can safely drop them
df.dropna(inplace=True)

# 4. Save the cleaned data for SQL and Power BI
df.to_csv('cleaned_telco_churn.csv', index=False)
print("Cleaned dataset saved successfully!")