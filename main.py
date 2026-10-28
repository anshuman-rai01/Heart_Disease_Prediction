from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI app
app = FastAPI(title="Heart Disease Prediction API")

# Load saved model and scaler
model = joblib.load('model.joblib')
scaler = joblib.load('scaler.joblib')

# Define input schema matching heart.csv features
class HeartData(BaseModel):
    age: float
    sex: float
    cp: float
    trestbps: float
    chol: float
    fbs: float
    restecg: float
    thalach: float
    exang: float
    oldpeak: float
    slope: float
    ca: float
    thal: float

@app.get("/")
def home():
    return {"message": "Heart Disease Prediction API is running!"}

@app.post("/predict")
def predict(data: HeartData):
    # Convert input data to array
    features = np.array([[
        data.age, data.sex, data.cp, data.trestbps, data.chol,
        data.fbs, data.restecg, data.thalach, data.exang,
        data.oldpeak, data.slope, data.ca, data.thal
    ]])
    
    # Scale features and predict
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)[0]
    probability = model.predict_proba(scaled_features)[0].max()
    
    return {
        "prediction": int(prediction),
        "result": "Heart Disease Detected" if prediction == 1 else "No Heart Disease Detected",
        "confidence": float(probability)
    }