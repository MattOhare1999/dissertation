import sys
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import umap
import umap.plot
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

from app_usage_utils import (annotate_app_usage, app_usage_distance,
                             get_variance, load_app_usage, load_id)
from layout import DrawLayout
from layout.layout import _create_algorithm
from layout.utils import get_size

options = {'true': True, 'false': False}

metrics = ['euclidean', 'seuclidean', 'hamming']

visuals = [
    'default', 'connectivity', 'diagnostic', 'interactive1', 'interactive2',
    '3d'
]


# helper functions to avoid repeated code
def save_visualisation(plt, type_visual, top_apps, data_set_size, metric,
                       high_dimensional, clusters, total):
    plt.savefig(
        '../../data/outputs/umap_plots/%s_%dapps_%dentries_%s_%r%dclusters_%.0fs.jpg'
        % (type_visual, top_apps, data_set_size, metric, high_dimensional,
           clusters, total))
    return


def umap_embedding(app_usage, metric, dimensions, variance_dict):
    if metric == "seuclidean":
        embedding = umap.UMAP(metric=metric,
                              min_dist=0.75,
                              n_components=dimensions,
                              spread=3,
                              n_neighbors=50,
                              metric_kwds=variance_dict).fit(app_usage)
    else:
        embedding = umap.UMAP(metric=metric,
                              min_dist=0.75,
                              n_components=dimensions,
                              spread=3,
                              n_neighbors=50).fit(app_usage)
    return embedding


def get_time(start):
    return time.time() - start


# error handling
if len(sys.argv) < 3:
    print(
        f'\nusage: python3 umap_layout.py *REQUIRED* <num apps> <dataset size> *OPTIONAL* <metric> <type> <high dimensional> <clusters>'
    )
    print('\tApps: see datasets/app_usage')
    print('\tSizes: see datasets/app_usage')
    print('\tMetric: seuclidean, euclidean, hamming')
    print(
        '\tType: default, connectivity, diagnostic, interactive1, interactive2, 3d'
    )
    print('\tHigh dimensional clusters: true, false')
    print('\tClusters: 1 - 10')
    exit(1)

if len(sys.argv) > 3 and sys.argv[3].lower() not in metrics:
    print('\tAvailable metrics: euclidean, seuclidean, hamming')
    exit(1)

if len(sys.argv) > 4 and sys.argv[4].lower() not in visuals:
    print(
        '\tAvailable options for type: default, connectivity, diagnostic, interactive1, interactive2, 3d'
    )
    exit(1)

if len(sys.argv) > 5 and sys.argv[5].lower() not in options:
    print('\tAvailable options for high dimensional clusters: true, false')
    exit(1)

if len(sys.argv) > 6 and (int(sys.argv[6]) > 10 or int(sys.argv[6]) < 1):
    print('\tPlease enter a number of clusters between 1 and 10')
    exit(1)

# initialise variables of command line arguments
top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
metric = sys.argv[3].lower() if len(sys.argv) > 3 else 'seuclidean'
type_visual = sys.argv[4].lower() if len(sys.argv) > 4 else 'default'
high_dimensional_text = sys.argv[5].lower() if len(sys.argv) > 5 else 'true'
clusters = int(sys.argv[6]) if len(sys.argv) > 6 else 2
high_dimensional = options[high_dimensional_text]
app_usage = load_app_usage(top_apps, data_set_size)
user_ids = load_id(top_apps, data_set_size)
user_ids = pd.DataFrame({'ID': user_ids})
variance = get_variance()

variance_dict = {}
variance_dict['V'] = variance[0]

print(
    f"Creating {type_visual} layout of {len(app_usage)} app usage entries using a metric of {metric} with {clusters} clusters. High dimensional clusters - {high_dimensional}"
)

start = time.time()

# find low-dimensional embedding, find clusters, create specified layout and save layout
if type_visual == '3d':
    fig = plt.figure()
    embedding = umap_embedding(app_usage, metric, 3, variance_dict)
    points = embedding.transform(app_usage)
    runtime_total = get_time(start)
    print("Runtime: ", runtime_total)

    k = KMeans(n_clusters=clusters).fit_predict(app_usage)

    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=k, s=100)

    total = get_time(start)
    save_visualisation(plt, type_visual, top_apps, data_set_size, metric,
                       high_dimensional, clusters, total)

else:
    embedding = umap_embedding(app_usage, metric, 2, variance_dict)
    runtime_total = get_time(start)
    points = embedding.transform(app_usage)

    print("Runtime: ", runtime_total)

    if high_dimensional:
        k = KMeans(n_clusters=clusters).fit_predict(app_usage)
    else:
        k = KMeans(n_clusters=clusters).fit_predict(points)

    if type_visual == "default":
        umap.plot.points(embedding,
                         values=k,
                         cmap='jet',
                         height=800,
                         width=800)
        total = get_time(start)
        save_visualisation(plt, type_visual, top_apps, data_set_size, metric,
                           high_dimensional, clusters, total)

    elif type_visual == "connectivity":
        umap.plot.connectivity(embedding,
                               show_points=True,
                               height=1600,
                               width=1600,
                               edge_bundling='hammer')
        total = get_time(start)
        save_visualisation(plt, type_visual, top_apps, data_set_size, metric,
                           high_dimensional, clusters, total)

    elif type_visual == "diagnostic":
        # numba warning will show however the code works, the warning messages are just verbose
        umap.plot.diagnostic(embedding, diagnostic_type="neighborhood")
        total = get_time(start)
        save_visualisation(plt, type_visual, top_apps, data_set_size, metric,
                           high_dimensional, clusters, total)

    elif type_visual == "interactive1":
        plt.figure(figsize=(16.0, 16.0))
        spring_layout = _create_algorithm(dataset=app_usage,
                                          algorithm=umap,
                                          distance=app_usage_distance,
                                          metric=metric,
                                          metric_kwds=variance_dict)

        draw_layout = DrawLayout(dataset=app_usage,
                                 spring_layout=spring_layout)

        draw_layout.draw_umap(data=embedding,
                              dataset=app_usage,
                              alpha=0.7,
                              point_colors=k,
                              annotate=annotate_app_usage,
                              algorithm_highlights=True)

        total = get_time(start)
        save_visualisation(plt, type_visual, top_apps, data_set_size, metric,
                           high_dimensional, clusters, total)

        print("Max Memory: ", get_size(draw_layout))

    elif type_visual == "interactive2":
        total = get_time(start)
        umap.plot.output_file(
            '../../data/outputs/umap_plots/%s_%dapps_%dentries_%s_%r%dclusters_%.0fs.html'
            % (type_visual, top_apps, data_set_size, metric, high_dimensional,
               clusters, total))

        p = umap.plot.interactive(embedding,
                                  values=k,
                                  hover_data=user_ids,
                                  cmap='jet',
                                  height=800,
                                  width=800)

        umap.plot.show(p)

print(f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()
