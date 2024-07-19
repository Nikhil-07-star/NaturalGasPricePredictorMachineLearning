from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd
import datetime
import os

app = Flask(__name__)

joblib_path = os.path.join(os.path.dirname(__file__), 'gas.joblib')


try:
    data = joblib.load(joblib_path)
    model = data['model']
    scaler = data['scaler']
except Exception as e:
    print(f"Error loading model and scaler: {e}")
    model = None
    scaler = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return render_template('index.html', prediction_text='Model and scaler are not loaded correctly.')

    try:
        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])

        date = datetime.datetime(year, month, day)
        day_of_week = date.weekday()
        is_weekend = 1 if day_of_week >= 5 else 0

        # Create a DataFrame with the same columns as used during fitting
        input_features = pd.DataFrame([[year, month, day, day_of_week, is_weekend]], 
                                      columns=['year', 'month', 'day', 'day_of_week', 'is_weekend'])

        # Scale the input features
        input_features_scaled = scaler.transform(input_features)

        # Predict the price
        prediction = model.predict(input_features_scaled)[0]

        # Ensure prediction is not negative
        prediction = max(0, prediction)

        return render_template('index.html', prediction_text=f'Predicted Price: ${prediction:.2f}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)