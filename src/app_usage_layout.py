import sys
import time

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

import forcelayout as fl
from app_usage_utils import (annotate_app_usage, app_usage_distance,
                             load_app_usage)
from forcelayout.metrics import LayoutMetrics

algorithms = {
    'brute': fl.SpringForce,
    'chalmers96': fl.NeighbourSampling,
    'hybrid': fl.Hybrid,
    'pivot': fl.Pivot,
}

options = {
    'true': True,
    'false': False,
}

if len(sys.argv) < 3:
    print(f'\nusage: python3 app_usage_layout.py *REQUIRED* <num apps> <dataset size> *OPTIONAL* <algorithm> <iterations> <high dimensional> <clusters> <intermediate_steps>')
    print('\tApps: see datasets/app_usage')
    print('\tSizes: see datasets/app_usage')
    print('\tAvailable algorithms: brute, chalmers96, hybrid, pivot')
    print('\tHigh Dimensional: true, false')
    print('\tClusters: 1 - 10')
    print('\tIterationns: Multiple of 5 between 50 and 1000')
    print('\tIntermediate_steps: true, false')
    exit(1)

if len(sys.argv) > 3 and sys.argv[3] not in algorithms:
    print('\tAvailable algorithms: brute, chalmers96, hybrid, pivot')
    exit(1)

if len(sys.argv) > 4 and (int(sys.argv[4]) < 5 or int(sys.argv[4]) > 1000 or int(sys.argv[4]) % 5 != 0):
    print('\tIterations must be of a multiple of 5 between 50 and 1000 ')
    exit(1)

if len(sys.argv) > 5 and sys.argv[5].lower() not in options:
    print('\tAvailable options for high dimensional clusters: true, false')
    exit(1)

if len(sys.argv) > 6 and (int(sys.argv[6]) > 10 or int(sys.argv[6]) < 1):
    print('\tPlease enter a number of clusters between 1 and 10')
    exit(1)

if len(sys.argv) > 7 and sys.argv[7].lower() not in options:
    print('\tAvailable options for intermediate steps: true, false')
    exit(1)

start = time.time()

top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
algorithm_text = sys.argv[3].lower() if len(sys.argv) > 3 else 'chalmers96'
iterations = int(sys.argv[4]) if len(sys.argv) > 4 else 50
high_dimensional_text = sys.argv[5].lower() if len(sys.argv) > 5 else 'false'
clusters = int(sys.argv[6]) if len(sys.argv) > 6 else 4
intermediate_steps_text = sys.argv[7].lower() if len(sys.argv) > 7 else 'false'
algorithm = algorithms[algorithm_text]
high_dimensional = options[high_dimensional_text]
intermediate_steps = options[intermediate_steps_text]
app_usage = load_app_usage(top_apps, data_set_size)
print(
    f"Creating layout of {len(app_usage)} app usage entries using {algorithm_text} algorithm with {iterations} iterations and {clusters} clusters. High dimensional clusters - {high_dimensional}, Intermediate Steps - {intermediate_steps}")

spring_layout = fl.draw_spring_layout(dataset=app_usage,
                                      distance=app_usage_distance,
                                      iterations=iterations,
                                      algorithm=algorithm,
                                      alpha=0.7,
                                      annotate=annotate_app_usage,
                                      algorithm_highlights=True,
                                      high_dimensional=high_dimensional,
                                      show_progression=intermediate_steps,
                                      clusters=clusters)

total = time.time() - start

if intermediate_steps == True:
    plt.savefig("../data/outputs/spring_models_plots/IntermediateSteps_%s_%dapps_%dentries_%r%dclusters_%diterations_%.0fs.jpg" %
                (algorithm_text, top_apps, data_set_size, high_dimensional, clusters, 50, total))
else:
    plt.savefig("../data/outputs/spring_models_plots/%s_%dapps_%dentries_%r%dclusters_%diterations_%.0fs.jpg" %
                (algorithm_text, top_apps, data_set_size, high_dimensional, clusters, 50, total))

print(
    f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()
