import sys
import time
import numpy as np
from app_usage_utils import load_app_usage, annotate_app_usage, app_usage_distance
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift

top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
app_usage = load_app_usage(top_apps, data_set_size)

plt.figure(figsize=(8.0, 8.0))

start = time.time()

clustering = MeanShift().fit(app_usage)
print(clustering.labels_)
print(clustering.get_params())

# x = k[:, 0]
# y = k[:, 1]

# plt.scatter(x, y)

total = time.time() - start
print(f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()
