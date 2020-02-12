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

progression_options = {
    'true': True,
    'false': False,
}

if len(sys.argv) < 3:
    print(f'\nusage: python3 app_usage_layout.py <num apps> <dataset size> <algorithm> <clusters> <iterations> <progression graph>')
    print('\tApps: see datasets/app_usage')
    print('\tSizes: see datasets/app_usage')
    print('\tAvailable algorithms: brute, chalmers96, hybrid, pivot')
    print('\tClusters: 1 - 10')
    print('\tIterationns: Multiple of 5 between 50 and 1000')
    print('\tProgression graph: true, false')
    exit(1)

if len(sys.argv) > 3 and sys.argv[3] not in algorithms:
    print('\tAvailable algorithms: brute, chalmers96, hybrid, pivot')
    exit(1)

if len(sys.argv) > 4 and int(sys.argv[4]) > 10:
    print('\tMax number of clusters is 10, please enter a number between 1 and 10')
    exit(1)

if len(sys.argv) > 5 and (int(sys.argv[5]) < 5 or int(sys.argv[5]) > 1000 or int(sys.argv[5]) % 5 != 0):
    print('\tIterations must be of a multiple of 5 between 50 and 1000 ')
    exit(1)

if len(sys.argv) > 6 and sys.argv[6] not in progression_options:
    print('\tAvailable options for progression: true, false')
    exit(1)

top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
algorithm_text = sys.argv[3].lower() if len(sys.argv) > 3 else 'chalmers96'
clusters = int(sys.argv[4]) if len(sys.argv) > 4 else 4
iterations = int(sys.argv[5]) if len(sys.argv) > 5 else 50
progression_text = sys.argv[6].lower() if len(sys.argv) > 6 else 'false'
progression = progression_options[progression_text]
algorithm = algorithms[algorithm_text]
app_usage = load_app_usage(top_apps, data_set_size)
print(
    f"Creating layout of {len(app_usage)} app usage entries using {algorithm_text} algorithm with {iterations} iterations and {clusters} clusters. Progression graph - {progression}")

# best seems to be 50 and 400
# optimal clusters seems to be 2, 4, 5
k = KMeans(n_clusters=clusters).fit_predict(app_usage)

plt.figure(figsize=(16.0, 16.0))
start = time.time()
spring_layout = fl.draw_spring_layout(dataset=app_usage,
                                      distance=app_usage_distance,
                                      iterations=iterations,
                                      algorithm=algorithm,
                                      alpha=0.7,
                                      point_colors=k,
                                      annotate=annotate_app_usage,
                                      algorithm_highlights=True,
                                      show_progression=progression)

total = time.time() - start

if progression == True:
    plt.savefig("../data/outputs/spring_models_plots/IntermediateSteps_%s_%dapps_%dentries_%dclusters_%diterations_%.0fs.jpg" %
                (algorithm_text, top_apps, data_set_size, clusters, 50, total))
else:
    plt.savefig("../data/outputs/spring_models_plots/%s_%dapps_%dentries_%dclusters_%diterations_%.0fs.jpg" %
                (algorithm_text, top_apps, data_set_size, clusters, 50, total))

print(
    f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()
