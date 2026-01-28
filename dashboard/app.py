import streamlit as st
import requests

API_URL = "http://ai-api-service:8000"

st.title("AI User Intelligence Dashboard")

st.subheader("Churn Prediction")

sessions = st.number_input("Sessions", min_value=0, step=1)
time_spent = st.number_input("Time Spent", min_value=0.0)
purchases = st.number_input("Purchases", min_value=0, step=1)
last_active_days = st.number_input("Last Active Days", min_value=0, step=1)

if st.button("Predict Churn"):
    payload = {
        "sessions": sessions,
        "time_spent": time_spent,
        "purchases": purchases,
        "last_active_days": last_active_days
    }

    with st.spinner("Predicting..."):
        response = requests.post(
            f"{API_URL}/predict-churn",
            json=payload,
            timeout=5
        )

    if response.status_code == 200:
        result = response.json()

        if result["churn"]:
            st.error(f"⚠️ High Churn Risk | Score: {result['risk_score']}")
        else:
            st.success(f"✅ Low Churn Risk | Score: {result['risk_score']}")
    else:
        st.error("API call failed")
