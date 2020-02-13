import sys
import numpy as np
import pandas as pd
import umap
import umap.plot
import time
import seaborn as sns
from app_usage_utils import load_app_usage, load_id, app_usage_distance, annotate_app_usage, get_variance
import matplotlib.pyplot as plt
from forcelayout.forcelayout import _create_algorithm
from sklearn.cluster import KMeans
from forcelayout import DrawLayout


def save_visualisation(plt, type_visual, top_apps, data_set_size, metric, clusters, total):
    if type_visual == "kmeans":
        plt.savefig('../data/outputs/umap_plots/%s_%dapps_%dentries_%s_%dclusters_%.0fs.jpg' %
                    (type_visual, top_apps, data_set_size, metric, clusters, total))
    else:
        plt.savefig('../data/outputs/umap_plots/%s_%dapps_%dentries_%s_%.0fs.jpg' %
                    (type_visual, top_apps, data_set_size, metric, total))
    return


def get_time(start):
    return time.time() - start


if len(sys.argv) < 3:
    print(f'\nusage: python3 umap_clustering.py <num apps> <dataset size> <metric> <type> *IF KMEANS* <clusters>')
    print('\tApps: see datasets/app_usage')
    print('\tSizes: see datasets/app_usage')
    print('\tMetric: euclidean, seuclidean, hamming')
    print('\tType: normal, connectivity, diagnostic, kmeans, interactive')
    exit(1)

top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
metric = sys.argv[3].lower() if len(sys.argv) > 3 else 'euclidean'
type_visual = sys.argv[4].lower() if len(sys.argv) > 4 else 'normal'
clusters = int(sys.argv[5]) if len(sys.argv) > 5 else 4
app_usage = load_app_usage(top_apps, data_set_size)
user_ids = load_id(top_apps, data_set_size)
user_ids = pd.DataFrame({'ID': user_ids})
variance = get_variance()

variance_dict = {}
variance_dict['V'] = variance[0]

print(
    f"Creating {type_visual} layout of {len(app_usage)} app usage entries using a metric of {metric}")

start = time.time()

embedding = umap.UMAP(metric=metric, min_dist=0.1,
                      spread=0.75, metric_kwds=variance_dict).fit(app_usage)
k = KMeans(n_clusters=clusters).fit_predict(
    embedding.transform(app_usage))

if type_visual == "normal":
    umap.plot.points(embedding,
                     values=embedding.transform(app_usage)[:, 0],
                     cmap='inferno',
                     height=800,
                     width=800)
    total = get_time(start)
    save_visualisation(plt, type_visual, top_apps,
                       data_set_size, metric, clusters, total)
elif type_visual == "connectivity":
    umap.plot.connectivity(embedding, show_points=True,
                           height=1600, width=1600, edge_bundling='hammer')
    total = get_time(start)
    save_visualisation(plt, type_visual, top_apps,
                       data_set_size, metric, clusters, total)
elif type_visual == "diagnostic":
    umap.plot.diagnostic(embedding, diagnostic_type="neighborhood")
    total = get_time(start)
    save_visualisation(plt, type_visual, top_apps,
                       data_set_size, metric, clusters, total)
elif type_visual == "kmeans":
    spring_layout = _create_algorithm(
        dataset=app_usage, algorithm=umap, distance=app_usage_distance, metric=metric, metric_kwds=variance_dict)

    draw_layout = DrawLayout(dataset=app_usage, spring_layout=spring_layout)

    draw_layout.draw_umap(
        data=embedding,
        dataset=app_usage,
        alpha=0.7,
        point_colors=k,
        annotate=annotate_app_usage,
        algorithm_highlights=True)

    total = get_time(start)
    save_visualisation(plt, type_visual, top_apps,
                       data_set_size, metric, clusters, total)

elif type_visual == "interactive":
    total = get_time(start)
    umap.plot.output_file('../data/outputs/umap_plots/%s_%dapps_%dentries_%s_%.0fs.html' %
                          (type_visual, top_apps, data_set_size, metric, total))

    p = umap.plot.interactive(embedding,
                              values=embedding.transform(app_usage)[:, 0],
                              hover_data=user_ids,
                              cmap='inferno',
                              height=800,
                              width=800)

    umap.plot.show(p)

print(f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()
