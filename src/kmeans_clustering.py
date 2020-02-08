import sys
import time
import numpy as np
from app_usage_utils import load_app_usage, annotate_app_usage, app_usage_distance
from poker_utils import load_poker
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import umap

top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
app_usage = load_app_usage(top_apps, data_set_size)
#app_usage = load_poker(top_apps)

plt.figure(figsize=(16.0, 16.0))

start = time.time()

#embedding = TSNE(n_components=2, perplexity=30).fit_transform(app_usage)
embedding = umap.UMAP(metric='euclidean').fit_transform(app_usage)

k = KMeans().fit_transform(embedding)

x = k[:, 0]
y = k[:, 1]

plt.scatter(x, y)

total = time.time() - start
print(f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()

# standard_embedding = umap.UMAP(random_state=42).fit_transform(mnist.data)
# plt.scatter(standard_embedding[:, 0], standard_embedding[:,
#                                                          1], c=mnist.target, s=0.1, cmap='Spectral')

# kmeans_labels = cluster.KMeans(n_clusters=10).fit_predict(mnist.data)
# plt.scatter(standard_embedding[:, 0], standard_embedding[:,
#                                                          1], c=kmeans_labels, s=0.1, cmap='Spectral')
