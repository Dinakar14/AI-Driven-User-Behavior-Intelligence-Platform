import numpy as np
from sklearn.decomposition import TruncatedSVD

interaction_matrix = np.array([
    [1,0,1],
    [0,1,0],
    [1,1,1]
])

svd = TruncatedSVD(n_components=2)
latent = svd.fit_transform(interaction_matrix)

print("User embeddings:", latent)
