import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
# Generating sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
# Plotting the sample data
plt.figure(figsize=(12, 6))
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title('Sample Data for Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.grid(True)
plt.show()
# Implementing KMeans clustering
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
kmeans_labels = kmeans.labels_
# Plotting the results of KMeans clustering
plt.figure(figsize=(12, 6))
plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels, s=50, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red',
marker='*', label='Centroids')
plt.title('KMeans Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()
# Implementing Agglomerative Clustering
agglomerative = AgglomerativeClustering(n_clusters=4)
agglomerative.fit(X)
agglomerative_labels = agglomerative.labels_
# Plotting the results of Agglomerative Clustering
plt.figure(figsize=(12, 6))
plt.scatter(X[:, 0], X[:, 1], c=agglomerative_labels, s=50, cmap='viridis')
plt.title('Agglomerative Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.grid(True)
plt.show()
# Evaluating clustering performance using silhouette score
kmeans_score = silhouette_score(X, kmeans_labels)
agglomerative_score = silhouette_score(X, agglomerative_labels)
print("Silhouette Score for KMeans: {:.2f}".format(kmeans_score))
print("Silhouette Score for Agglomerative Clustering: {:.2f}".format(agglomerative_score))
