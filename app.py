from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load models
model = joblib.load('models/rf_acc_68.pkl')
preprocessor = joblib.load('models/preprocessor.joblib')

# Feature names (must match training data)
feature_names = [
    'Age', 'Gender', 'Total_Bilirubin', 'Direct_Bilirubin', 
    'Alkaline_Phosphotase', 'Alamine_Aminotransferase', 
    'Aspartate_Aminotransferase', 'Total_Protiens',
    'Albumin', 'Albumin_and_Globulin_Ratio'
]

@app.route('/')
def home():
    return render_template('index.html', features=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data and convert to proper types
        form_data = request.form.to_dict()
        
        # Convert string values to appropriate types
        input_values = []
        for feature in feature_names:
            value = form_data[feature]
            if feature == 'Gender':
                input_values.append(value)
            else:
                input_values.append(float(value))
        
        # Convert to DataFrame with correct feature order
        input_data = pd.DataFrame([input_values], columns=feature_names)
        
        # Preprocess
        processed_data = preprocessor.transform(input_data)
        
        # Predict
        prediction = model.predict(processed_data)[0]
        probability = model.predict_proba(processed_data)[0][1]
        
        # Format results
        result = "High Risk of Liver Disease" if prediction == 1 else "Low Risk of Liver Disease"
        confidence = f"{probability*100:.2f}%"
        
        return render_template('result.html', 
                             prediction_text=result, 
                             confidence=confidence,
                             features=zip(feature_names, input_values))
    
    except Exception as e:
        return render_template('result.html', 
                             prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)