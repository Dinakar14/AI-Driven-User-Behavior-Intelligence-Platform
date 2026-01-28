from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserFeatures(BaseModel):
    sessions: int
    time_spent: float
    purchases: int
    last_active_days: int

@app.get("/")
def home():
    return {"message": "AI User Intelligence API Running"}

@app.post("/predict-churn")
def predict_churn(data: UserFeatures):
    """
    Dynamic churn scoring logic
    (simulates real ML behavior)
    """

    score = 0.0

    if data.sessions < 5:
        score += 0.25
    if data.time_spent < 50:
        score += 0.25
    if data.purchases == 0:
        score += 0.2
    if data.last_active_days > 15:
        score += 0.35

    churn = score >= 0.5

    return {
        "churn": churn,
        "risk_score": round(score, 2),
        "message": "High risk user" if churn else "Low risk user"
    }
