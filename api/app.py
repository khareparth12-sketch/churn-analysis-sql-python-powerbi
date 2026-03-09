from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title="Customer Churn Prediction API")

model = joblib.load("models/xgb_tuned_model.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.get("/")
def home():
    return {"message": "Churn Prediction API running"}

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])
    df_scaled = scaler.transform(df)

    prob = model.predict_proba(df_scaled)[0][1]

    risk = "High" if prob > 0.35 else "Low"

    return {
        "churn_probability": float(prob),
        "churn_risk": risk
    }