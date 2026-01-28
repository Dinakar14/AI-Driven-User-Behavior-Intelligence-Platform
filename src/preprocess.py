import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess(path):
    df = pd.read_csv(path)
    features = df.drop(columns=["user_id"])
    scaler = StandardScaler()
    X = scaler.fit_transform(features)
    return X, df["user_id"]

if __name__ == "__main__":
    preprocess("data/user_events.csv")
