import sys
import time

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from scipy.spatial.distance import pdist, squareform

import layout
from app_usage_utils import (annotate_app_usage, app_usage_distance,
                             get_variance, load_app_usage)
from layout import DrawLayout
from layout.spring_models import BaseSpringLayout
from layout.layout import _create_algorithm
from layout.utils import get_size


# helper function
def tsne_embedding(app_usage, iterations, metric, i, random_state=None):
    if metric == "seuclidean":
        embedding = TSNE(n_iter=int(iterations / i),
                         random_state=random_state,
                         metric="precomputed",
                         perplexity=30,
                         early_exaggeration=1).fit_transform(app_usage)
    else:
        embedding = TSNE(n_iter=int(iterations / i),
                         random_state=random_state,
                         metric=metric,
                         perplexity=30,
                         early_exaggeration=1).fit_transform(app_usage)
    return embedding


options = {
    'true': True,
    'false': False,
}

metrics = ['euclidean', 'seuclidean', 'hamming']

# error handling
if len(sys.argv) < 3:
    print(
        f'\nusage: python3 tsne_layout.py *REQUIRED* <num apps> <dataset size> *OPTIONAL* <metric> <iterations> <high dimensional> <clusters> <intermediate steps>'
    )
    print('\tApps: see datasets/app_usage')
    print('\tSizes: see datasets/app_usage')
    print('\tMetric: seuclidean, euclidean, hamming')
    print(
        '\tIterations: Multiple of 5 between 250 and 5000. Between 1250 and 5000 if intermediate steps argument is true.'
    )
    print('\tHigh Dimensional Clusters: true, false')
    print('\tClusters: 1 - 10')
    print('\tIntermediate Steps: true, false')
    exit(1)

if len(sys.argv) > 3 and sys.argv[3].lower() not in metrics:
    print('\tAvailable metrics: euclidean, hamming')

if len(sys.argv) > 4 and (int(sys.argv[4]) < 100 or int(sys.argv[4]) > 5000
                          or int(sys.argv[4]) % 5 != 0):
    print(
        '\tIterations must be of a multiple of 5 and between 250 and 5000. 1250 if intermediate_steps is true'
    )

if len(sys.argv) > 5 and sys.argv[5].lower() not in options:
    print('\tAvailable options for high dimensional clusters: true, false')

if len(sys.argv) > 6 and (int(sys.argv[6]) > 10 or int(sys.argv[6]) < 1):
    print('\tPlease enter a number of clusters between 1 and 10')
    exit(1)

if len(sys.argv) > 7 and sys.argv[7].lower() not in options:
    print('\tAvailable options for intermediate steps: true, false')
    exit(1)

# initialise variables of command line arguments
top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
metric = sys.argv[3].lower() if len(sys.argv) > 3 else 'seuclidean'
iterations = int(sys.argv[4]) if len(sys.argv) > 4 else 1000
high_dimensional_text = sys.argv[5].lower() if len(sys.argv) > 5 else 'true'
clusters = int(sys.argv[6]) if len(sys.argv) > 6 else 2
intermediate_steps_text = sys.argv[7].lower() if len(sys.argv) > 7 else 'false'
high_dimensional = options[high_dimensional_text]
intermediate_steps = options[intermediate_steps_text]
app_usage = load_app_usage(top_apps, data_set_size)
variance = get_variance()

# this has to be done as currently there is no ability to pass in metric parameters for t-SNE
data = squareform(pdist(
    app_usage, metric, V=variance[0])) if metric == 'seuclidean' else app_usage

print(
    f"Creating layout of {len(app_usage)} app usage entries using a metric of {metric} with {iterations} iterations. High dimensional clusters - {high_dimensional}, Intermediate Steps - {intermediate_steps}"
)

start = time.time()
plt.figure(figsize=(16.0, 16.0))

# find low-dimensional embedding, find clusters and create layout
if intermediate_steps == True:
    random_state = np.random.randint(0, 100)
    step = iterations / 5
    for i in range(1, 6):
        embedding = tsne_embedding(data, int(step * i), metric, i,
                                   random_state)
        if high_dimensional:
            k = KMeans(n_clusters=clusters).fit_predict(app_usage)
        else:
            k = KMeans(n_clusters=clusters).fit_predict(embedding)
        spring_layout = _create_algorithm(dataset=data,
                                          algorithm=TSNE,
                                          distance=app_usage_distance,
                                          metric=metric)
        draw_layout = DrawLayout(dataset=app_usage,
                                 spring_layout=spring_layout)
        draw_layout.draw_tsne_facets(data=embedding,
                                     current_plot=i,
                                     current_iters=int(step * i),
                                     alpha=0.7,
                                     point_colors=k,
                                     annotate=annotate_app_usage,
                                     algorithm_highlights=True)
else:
    embedding = tsne_embedding(data, iterations, metric, 1)
    runtime_total = time.time() - start
    print("Runtime: ", runtime_total)

    if high_dimensional:
        k = KMeans(n_clusters=clusters).fit_predict(app_usage)
    else:
        k = KMeans(n_clusters=clusters).fit_predict(embedding)
    spring_layout = _create_algorithm(dataset=data,
                                      algorithm=TSNE,
                                      distance=app_usage_distance,
                                      metric=metric)
    draw_layout = DrawLayout(dataset=app_usage, spring_layout=spring_layout)
    draw_layout.draw_tsne(data=embedding,
                          alpha=0.7,
                          point_colors=k,
                          annotate=annotate_app_usage,
                          algorithm_highlights=True)

    print("Max Memory: ", get_size(draw_layout))

total = time.time() - start

# save layout
if intermediate_steps == True:
    plt.savefig(
        "../../data/outputs/tsne_plots/IntermediateSteps_%dapps_%dentries_%s_%diterations_%r%dclusters_%.0fs.jpg"
        % (top_apps, data_set_size, metric, iterations, high_dimensional,
           clusters, total))
else:
    plt.savefig(
        "../../data/outputs/tsne_plots/%dapps_%dentries_%s_%diterations_%r%dclusters_%.0fs.jpg"
        % (top_apps, data_set_size, metric, iterations, high_dimensional,
           clusters, total))

print(f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()
