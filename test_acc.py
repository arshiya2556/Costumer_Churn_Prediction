import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('cleaned_telco_churn.csv')
df_ml = df.drop('customerID', axis=1)

categorical_cols = df_ml.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df_ml[col] = LabelEncoder().fit_transform(df_ml[col])
    
X = df_ml.drop('Churn', axis=1)
y = df_ml['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(n_estimators=200, max_depth=10, class_weight='balanced', random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)

gb_model = GradientBoostingClassifier(n_estimators=150, learning_rate=0.05, max_depth=4, random_state=42)
gb_model.fit(X_train, y_train)
gb_pred = gb_model.predict(X_test)
gb_acc = accuracy_score(y_test, gb_pred)

if gb_acc > rf_acc:
    print(f"Gradient Boosting Won! Accuracy: {gb_acc:.4f}")
    print(classification_report(y_test, gb_pred))
else:
    print(f"Random Forest Won! Accuracy: {rf_acc:.4f}")
    print(classification_report(y_test, rf_pred))
