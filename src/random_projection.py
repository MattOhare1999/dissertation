import sys
import time

import matplotlib.pyplot as plt
import numpy as numpy
from sklearn.cluster import KMeans
from sklearn.random_projection import GaussianRandomProjection

from app_usage_utils import annotate_app_usage, load_app_usage
from forcelayout import DrawLayout
from forcelayout.algorithms import BaseSpringLayout
from forcelayout.forcelayout import _create_algorithm
from forcelayout.utils import get_size

if len(sys.argv) < 3:
    print(f'\nusage: python3 random_projection.py <num apps> <dataset size> <clusters>')
    print('\tApps: see datasets/app_usage')
    print('\tSizes: see datasets/app_usage')
    print('\tClusters: 1 - 10')
    exit(1)

if len(sys.argv) > 3 and (int(sys.argv[3]) > 10 or int(sys.argv[3]) < 1):
    print('\tPlease enter a number of clusters between 1 and 10')
    exit(1)

top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
clusters = int(sys.argv[3]) if len(sys.argv) > 3 else 4
app_usage = load_app_usage(top_apps, data_set_size)
print(
    f"Creating a low dimensional random projection layout of high dimensional {len(app_usage)} app usage entries with {clusters} clusters")

start = time.time()

random_projection = GaussianRandomProjection(n_components=2)
embedding = random_projection.fit_transform(app_usage)
k = KMeans(n_clusters=clusters).fit_predict(app_usage)

spring_layout = _create_algorithm(
    dataset=app_usage, algorithm=GaussianRandomProjection)
draw_layout = DrawLayout(
    dataset=app_usage, spring_layout=spring_layout)
draw_layout.draw_tsne(data=embedding, alpha=0.7, point_colors=k,
                      annotate=annotate_app_usage, algorithm_highlights=True)

total = time.time() - start

plt.savefig("../data/outputs/high_dimensional_plots/%dapps_%dentries_%dclusters_%.0fs.jpg" %
            (top_apps, data_set_size, clusters, total))

print("Max Memory: ", get_size(draw_layout))

print(
    f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()
