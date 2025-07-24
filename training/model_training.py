import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv('data/indian_liver_patient.csv')

# Data cleaning
data['Albumin_and_Globulin_Ratio'].fillna(data['Albumin_and_Globulin_Ratio'].mean(), inplace=True)
data['Dataset'] = data['Dataset'].map({1: 1, 2: 0})  # 1 is liver disease, 2 is no disease

# Feature engineering
X = data.drop('Dataset', axis=1)
y = data['Dataset']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing
numeric_features = ['Age', 'Total_Bilirubin', 'Direct_Bilirubin', 
                   'Alkaline_Phosphotase', 'Alamine_Aminotransferase',
                   'Aspartate_Aminotransferase', 'Total_Protiens', 
                   'Albumin', 'Albumin_and_Globulin_Ratio']
categorical_features = ['Gender']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Model pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train model
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save model and preprocessor
joblib.dump(model.named_steps['classifier'], 'models/rf_acc_68.pkl')
joblib.dump(preprocessor, 'models/preprocessor.joblib')