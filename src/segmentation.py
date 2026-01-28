from sklearn.cluster import KMeans
from preprocess import preprocess

X, users = preprocess("data/user_events.csv")

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

print("User Segments:", dict(zip(users, clusters)))
