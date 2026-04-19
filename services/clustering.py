from sklearn.cluster import KMeans
import numpy as np

class DrugCluster:
    def cluster(self, embeddings, n_clusters=50):
        model = KMeans(n_clusters=n_clusters, random_state=42)
        labels = model.fit_predict(embeddings)
        return labels