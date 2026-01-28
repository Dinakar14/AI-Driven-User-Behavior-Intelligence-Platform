import shap
import pandas as pd
from xgboost import XGBClassifier

df = pd.read_csv("data/user_events.csv")
X = df.drop(columns=["user_id"])
model = XGBClassifier().fit(X, df["last_active_days"] > 15)

explainer = shap.Explainer(model)
shap_values = explainer(X)

shap.summary_plot(shap_values, X)
