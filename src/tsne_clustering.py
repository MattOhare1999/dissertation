import sys
import time
import numpy as np
import seaborn as sns
from sklearn.manifold import TSNE
from app_usage_utils import load_app_usage, annotate_app_usage, app_usage_distance, get_variance
import matplotlib.pyplot as plt
import forcelayout
from forcelayout import DrawLayout
from forcelayout.algorithms import BaseSpringLayout
from forcelayout.forcelayout import _create_algorithm
from sklearn.cluster import KMeans

if len(sys.argv) < 3:
    print(f'\nusage: python3 umap_clustering.py <num apps> <dataset size> <metric>')
    print('\tApps: see datasets/app_usage')
    print('\tSizes: see datasets/app_usage')
    print('\tMetric: euclidean, hamming')
    exit(1)

top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
metric = sys.argv[3].lower() if len(sys.argv) > 3 else 'euclidean'
app_usage = load_app_usage(top_apps, data_set_size)
variance = get_variance()

print(
    f"Creating layout of {len(app_usage)} app usage entries using a metric of {metric}")

plt.figure(figsize=(8.0, 8.0))
start = time.time()

# best one seems to be 50 for 7500
perplex = [20, 30, 40, 50]
k = KMeans(n_clusters=4).fit_predict(app_usage)
embedding = TSNE(n_iter=5000, metric=metric,
                 perplexity=50).fit_transform(app_usage)

spring_layout = _create_algorithm(dataset=app_usage,
                                  algorithm=TSNE,
                                  distance=app_usage_distance, metric=metric)

draw_layout = DrawLayout(dataset=app_usage, spring_layout=spring_layout)

draw_layout.draw_tsne(
    data=embedding,
    alpha=0.7,
    point_colors=k,
    annotate=annotate_app_usage,
    algorithm_highlights=True)

total = time.time() - start
plt.savefig("../data/outputs/tsne_plots/%dapps_%dentries_%s_%dperplexity_%.0fs.jpg" %
            (top_apps, data_set_size, metric, perplex[3], total))
print(f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()
