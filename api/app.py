from fastapi import FastAPI
import joblib
import pandas as pd
from api.utils import FEATURE_COLUMNS, NUMERIC_COLUMNS
from api.schema import CustomerData

app = FastAPI(title="Customer Churn Prediction API")

model = joblib.load("models/xgb_tuned_model.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.get("/")
def home():
    return {"message": "Churn Prediction API running"}

@app.post("/predict")
def predict(data: CustomerData):
    input_dict = data.dict()

    df = pd.DataFrame([input_dict])
    df = df.reindex(columns=FEATURE_COLUMNS, fill_value=0)
    df[NUMERIC_COLUMNS] = scaler.transform(df[NUMERIC_COLUMNS])

    prob = model.predict_proba(df)[0][1]

    risk = "High" if prob > 0.35 else "Low"

    return {
        "churn_probability": float(prob),
        "churn_risk": risk
    }

@app.get("/health")
def health_check():
    return {"status": "API running"}

@app.get("/model-info")
def model_info():
    return {
        "model": "XGBoost Churn Classifier",
        "version": "1.0",
        "threshold": 0.35,
        "features": len(FEATURE_COLUMNS)
    }