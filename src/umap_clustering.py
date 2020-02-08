import sys
import numpy as np
import pandas as pd
import umap
import umap.plot
import time
import seaborn as sns
from app_usage_utils import load_app_usage, load_id
import forcelayout as fl
import matplotlib.pyplot as plt

start = time.time()

top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
metric = sys.argv[3]
app_usage = load_app_usage(top_apps, data_set_size)
user_ids = load_id(top_apps, data_set_size)
user_ids = pd.DataFrame({'ID': user_ids})

embedding = umap.UMAP(metric=metric, min_dist=0.1, spread=0.75).fit(app_usage)

umap.plot.points(embedding, values=embedding.transform(app_usage)[
                 :, 0], cmap='inferno', height=800, width=800)
# umap.plot.connectivity(embedding, show_points=True,
# height=1600, width=1600, edge_bundling='hammer')
# umap.plot.diagnostic(embedding, diagnostic_type="neighborhood")

umap.plot.output_file('plot.html')
p = umap.plot.interactive(embedding, values=embedding.transform(
    app_usage)[:, 0], hover_data=user_ids, cmap='inferno', height=800, width=800)
umap.plot.show(p)

total = time.time() - start
print(f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()
