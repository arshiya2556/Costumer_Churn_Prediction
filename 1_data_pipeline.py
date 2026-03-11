import os
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

def main():
    # Define paths
    raw_data_path = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'
    cleaned_data_path = 'cleaned_telco_churn.csv'
    plots_dir = 'plots'
    
    # Create plots directory if it doesn't exist
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)

    print("Loading data...")
    try:
        df = pd.read_csv(raw_data_path)
    except FileNotFoundError:
        print(f"Error: '{raw_data_path}' not found.")
        print("Please ensure the dataset is downloaded from Kaggle and placed in the project root.")
        return

    print("Cleaning data...")
    # Clean TotalCharges column: replace blank spaces, convert to float, drop nulls
    df['TotalCharges'] = df['TotalCharges'].replace(r'^\s*$', pd.NA, regex=True)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    
    # Check nulls before dropping
    null_count = df['TotalCharges'].isnull().sum()
    print(f"Found {null_count} nulls in TotalCharges. Dropping them...")
    df.dropna(subset=['TotalCharges'], inplace=True)
    
    print("Performing Exploratory Data Analysis (EDA)...")
    
    # Set plot style
    sns.set_theme(style="whitegrid")
    
    # Plot 1: Churn by Contract
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='Contract', hue='Churn', palette='Set2')
    plt.title('Customer Churn by Contract Type')
    plt.xlabel('Contract Type')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, 'churn_by_contract.png'))
    plt.close()
    
    # Plot 2: Churn by Tenure
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='tenure', hue='Churn', multiple='stack', palette='Set1', bins=30)
    plt.title('Customer Churn Distribution by Tenure')
    plt.xlabel('Tenure (months)')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, 'churn_by_tenure.png'))
    plt.close()
    
    print(f"EDA plots saved to ./{plots_dir}/")

    # Export cleaned dataset
    print(f"Exporting cleaned data to '{cleaned_data_path}'...")
    df.to_csv(cleaned_data_path, index=False)
    
    # Upload to SQLite Database
    print("\nUploading cleaned data to local SQL database (telco.db)...")
    try:
        conn = sqlite3.connect('telco.db')
        # Uploading the dataframe 'df' directly to an SQLite table named 'telco_churn'
        # 'replace' will overwrite the table if it already exists each time you run the script
        df.to_sql('telco_churn', conn, if_exists='replace', index=False)
        print("Data successfully uploaded to 'telco_churn' table in 'telco.db'")
    except Exception as e:
        print(f"Error uploading to database: {e}")
    finally:
        conn.close()
    
    print("\nPreparing data for Machine Learning...")
    # Drop customerID as it's an identifier, not a feature
    df_ml = df.drop('customerID', axis=1)
    
    # Encode categorical variables
    categorical_cols = df_ml.select_dtypes(include=['object']).columns
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df_ml[col] = le.fit_transform(df_ml[col])
        label_encoders[col] = le
        
    # Split features and target
    X = df_ml.drop('Churn', axis=1)
    y = df_ml['Churn']
    
    # Train-test split (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Tuned Machine Learning Models...")
    
    # Model 1: Random Forest with class_weight='balanced' to handle churn imbalance
    print("Training Random Forest (Balanced)...")
    rf_model = RandomForestClassifier(n_estimators=200, max_depth=10, class_weight='balanced', random_state=42)
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    rf_acc = accuracy_score(y_test, rf_pred)
    
    # Model 2: Gradient Boosting Classifier (Often provides superior accuracy)
    print("Training Gradient Boosting Classifier...")
    gb_model = GradientBoostingClassifier(n_estimators=150, learning_rate=0.05, max_depth=4, random_state=42)
    gb_model.fit(X_train, y_train)
    gb_pred = gb_model.predict(X_test)
    gb_acc = accuracy_score(y_test, gb_pred)
    
    # Select the best performing model based on accuracy
    if gb_acc > rf_acc:
        best_model_name = "Gradient Boosting Classifier"
        best_acc = gb_acc
        best_pred = gb_pred
    else:
        best_model_name = "Random Forest (Balanced)"
        best_acc = rf_acc
        best_pred = rf_pred
    
    print("\n--- Model Evaluation ---")
    print(f"Best Model Selected: {best_model_name}")
    print(f"Accuracy: {best_acc:.4f}\n")
    print("Classification Report:")
    print(classification_report(y_test, best_pred))
    
    print("Data Pipeline Execution Completed Successfully.")

if __name__ == "__main__":
    main()
