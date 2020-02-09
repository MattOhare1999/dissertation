import sys
import time
import numpy as np
from app_usage_utils import load_app_usage, annotate_app_usage, app_usage_distance
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
app_usage = load_app_usage(top_apps, data_set_size)

for i in range(1, 10):
    plt.figure(figsize=(8.0, 8.0))
    start = time.time()
    k = KMeans(n_clusters=i).fit_predict(app_usage)
    #k2 = KMeans().fit_transform(app_usage)

    embedding = TSNE(n_iter=5000, perplexity=30).fit_transform(app_usage)
    # kmeans just finds the clusters doesnt actually plot them
    #print("There are %d clusters" % len(np.unique(k.predict(app_usage))))

    #points = k.transform(app_usage)
    #print(points)
    #print(k.cluster_centers_)

    plt.scatter(embedding[:, 0], embedding[:, 1], c=k)

    total = time.time() - start
    print(f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()

# standard_embedding = umap.UMAP(random_state=42).fit_transform(mnist.data)
# plt.scatter(standard_embedding[:, 0], standard_embedding[:,
#                                                          1], c=mnist.target, s=0.1, cmap='Spectral')

# kmeans_labels = cluster.KMeans(n_clusters=10).fit_predict(mnist.data)
# plt.scatter(standard_embedding[:, 0], standard_embedding[:,
#                                                          1], c=kmeans_labels, s=0.1, cmap='Spectral')
