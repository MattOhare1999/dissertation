from app_usage_utils import load_app_usage, app_usage_distance, annotate_app_usage
import matplotlib.pyplot as plt
import forcelayout as fl
import time
import sys
import numpy as np

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
algorithm = sys.argv[3].lower() if len(sys.argv) > 3 else 'pivot'
print(
    f"Creating Layout of {len(app_usage)} app usage using {algorithm} algorithm")

algorithm = algorithms[algorithm]

plt.figure(figsize=(8.0, 8.0))

start = time.time()

spring_layout = fl.draw_spring_layout(dataset=app_usage,
                                      distance=app_usage_distance,
                                      algorithm=algorithm,
                                      alpha=0.7,
                                      color_by=lambda d: d[3],
                                      annotate=annotate_app_usage,
                                      algorithm_highlights=True)

total = time.time() - start
print(f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()
