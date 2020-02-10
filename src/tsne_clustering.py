import sys
import time
import numpy as np
import seaborn as sns
from sklearn.manifold import TSNE
from app_usage_utils import load_app_usage, annotate_app_usage, app_usage_distance, get_variance
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import forcelayout
from forcelayout import DrawLayout
from forcelayout.algorithms import BaseSpringLayout
from typing import Callable, Dict, Any, List, Optional
from forcelayout.forcelayout import _create_algorithm
from sklearn.cluster import KMeans

top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
app_usage = load_app_usage(top_apps, data_set_size)
metric = sys.argv[3]
variance = get_variance()

# best one seems to be 50 for 7500
perplex = [20, 30, 40, 50]
k = KMeans(n_clusters=4).fit_predict(app_usage)

# plt.figure(figsize=(8.0, 8.0)).add_subplot(111, projection='3d')
for i in perplex:
    plt.figure(figsize=(8.0, 8.0))

    start = time.time()

    if metric == 'hamming':
        embedding = TSNE(n_components=2,
                         metric='hamming').fit_transform(app_usage)
    elif metric == 'euclidean':
        embedding = TSNE(n_iter=5000, perplexity=i).fit_transform(app_usage)

    spring_layout = _create_algorithm(dataset=app_usage,
                                      algorithm=TSNE,
                                      distance=app_usage_distance)

    draw_layout = DrawLayout(dataset=app_usage, spring_layout=spring_layout)

    draw_layout.draw_tsne(
        data=embedding,
        alpha=0.7,
        point_colors=k,
        annotate=annotate_app_usage,
        algorithm_highlights=True)

    total = time.time() - start
    plt.savefig("../data/outputs/tsne_plots/%d_%s_%d_%.0fs.jpg" %
                (data_set_size, metric, perplexity, total))
    print(f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()
