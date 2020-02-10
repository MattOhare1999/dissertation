import sys
import numpy as np
import pandas as pd
import umap
import umap.plot
import time
import seaborn as sns
from app_usage_utils import load_app_usage, load_id, app_usage_distance, annotate_app_usage
import forcelayout as fl
import matplotlib.pyplot as plt
from forcelayout.forcelayout import _create_algorithm
from sklearn.cluster import KMeans
from forcelayout import DrawLayout


start = time.time()

top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
metric = sys.argv[3]
app_usage = load_app_usage(top_apps, data_set_size)
user_ids = load_id(top_apps, data_set_size)
user_ids = pd.DataFrame({'ID': user_ids})
k = KMeans(n_clusters=4).fit_predict(app_usage)

embedding = umap.UMAP(metric=metric, min_dist=0.1, spread=0.75).fit(app_usage)


# split this stuff up
spring_layout = _create_algorithm(
    dataset=app_usage, algorithm=umap, distance=app_usage_distance)

draw_layout = DrawLayout(dataset=app_usage, spring_layout=spring_layout)

draw_layout.draw_umap(
    data=embedding,
    dataset=app_usage,
    alpha=0.7,
    point_colors=k,
    annotate=annotate_app_usage,
    algorithm_highlights=True)

# umap.plot.points(embedding,
#  values=embedding.transform(app_usage)[:, 0],
#  cmap='inferno',
#  height=800,
#  width=800)
# umap.plot.connectivity(embedding, show_points=True,
# height=1600, width=1600, edge_bundling='hammer')
# umap.plot.diagnostic(embedding, diagnostic_type="neighborhood")

total = time.time() - start

# umap.plot.output_file('../data/outputs/umap_plots/%d_%s_%.0fs.html' %
#   (data_set_size, metric, total))

# p = umap.plot.interactive(embedding,
#   values=embedding.transform(app_usage)[:, 0],
#   hover_data=user_ids,
#   cmap='inferno',
#   height=800,
#   width=800)
# umap.plot.show(p)

print(f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()
