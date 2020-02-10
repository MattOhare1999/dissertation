from app_usage_utils import load_app_usage, app_usage_distance, annotate_app_usage
import matplotlib.pyplot as plt
import forcelayout as fl
import time
import sys
import numpy as np
from sklearn.cluster import KMeans

algorithms = {
    'brute': fl.SpringForce,
    'chalmers96': fl.NeighbourSampling,
    'hybrid': fl.Hybrid,
    'pivot': fl.Pivot,
}

if len(sys.argv) < 3:
    print(f'\nusage: python3 app_usage_layout.py <dataset size> <algorithm>')
    print('\tApps: see datasets/app_usage')
    print('\tSizes: see datasets/app_usage')
    print('\tAvailable algorithms: brute, chalmers96, hybrid, pivot')
    exit(1)

if len(sys.argv) > 3 and sys.argv[3] not in algorithms:
    print('\tAvailable algorithms: brute, chalmers96, hybrid, pivot')
    exit(1)

top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
app_usage = load_app_usage(top_apps, data_set_size)
algorithm_text = sys.argv[3].lower() if len(sys.argv) > 3 else 'pivot'
print(
    f"Creating Layout of {len(app_usage)} app usage using {algorithm_text} algorithm")

algorithm = algorithms[algorithm_text]

# best seems to be 50 and 400
iters = [50, 400]
# optimal clusters seems to be 2, 4, 5
clusters = [2, 4, 5]

for i in iters:
    for j in clusters:
        start = time.time()
        k = KMeans(n_clusters=j).fit_predict(app_usage)
        plt.figure(figsize=(8.0, 8.0))
        spring_layout = fl.draw_spring_layout(dataset=app_usage,
                                              distance=app_usage_distance,
                                              iterations=i,
                                              algorithm=algorithm,
                                              alpha=0.7,
                                              point_colors=k,
                                              annotate=annotate_app_usage,
                                              algorithm_highlights=True)

        total = time.time() - start
        plt.savefig("../data/outputs/spring_models_plots/%s_%s_%d_%.0fs.jpg" %
                    (algorithm_text, j, i, total))
        print(
            f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()

# Outliers
# 6308
# 10621
# 6384
# 1617
