import sys
import time
import numpy as np
import seaborn as sns
from sklearn.manifold import TSNE
from app_usage_utils import load_app_usage, annotate_app_usage, app_usage_distance, get_variance
import matplotlib.pyplot as plt
import forcelayout
from forcelayout import DrawLayout
from forcelayout.algorithms import BaseSpringLayout
from forcelayout.forcelayout import _create_algorithm
from sklearn.cluster import KMeans


def tsne_embedding(app_usage, iterations, random_state, metric):
    embedding = TSNE(n_iter=int(iterations/i), random_state=random_state, metric=metric,
                     perplexity=50).fit_transform(app_usage)
    return embedding


options = {
    'true': True,
    'false': False,
}

metrics = ["euclidean", "hamming"]

if len(sys.argv) < 3:
    print(f'\nusage: python3 umap_clustering.py *REQUIRED* <num apps> <dataset size> *OPTIONAL* <metric> <iterations> <high dimensional> <clusters> <intermediate_steps>')
    print('\tApps: see datasets/app_usage')
    print('\tSizes: see datasets/app_usage')
    print('\tMetric: euclidean, hamming')
    print('\tIterations: Multiple of 5 between 250 and 5000. 1250 if next argument is true.')
    print('\tHigh Dimensional Clusters: true, false')
    print('\tClsuters: 1 - 10')
    print('\tIntermediate Steps: true, false')
    exit(1)

if len(sys.argv) > 3 and sys.argv[3].lower() not in metrics:
    print('\tAvailable metrics: euclidean, hamming')

if len(sys.argv) > 4 and (int(sys.argv[4]) < 100 or int(sys.argv[4]) > 5000 or int(sys.argv[4]) % 5 != 0):
    print('\tIterations must be of a multiple of 5 and between 250 and 5000. 1250 if next arguement is true')

if len(sys.argv) > 5 and sys.argv[5].lower() not in options:
    print('\tAvailable options for high dimensional clusters: true, false')

if len(sys.argv) > 6 and (int(sys.argv[6]) > 10 or int(sys.argv[6]) < 1):
    print('\tPlease enter a number of clusters between 1 and 10')
    exit(1)

if len(sys.argv) > 7 and sys.argv[7].lower() not in options:
    print('\tAvailable options for intermediate steps: true, false')
    exit(1)

start = time.time()

top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
metric = sys.argv[3].lower() if len(sys.argv) > 3 else 'euclidean'
iterations = int(sys.argv[4]) if len(sys.argv) > 4 else 1000
high_dimensional_text = sys.argv[5].lower() if len(sys.argv) > 5 else 'false'
clusters = int(sys.argv[6]) if len(sys.argv) > 6 else 4
intermediate_steps_text = sys.argv[7].lower() if len(sys.argv) > 7 else 'false'
high_dimensional = options[high_dimensional_text]
intermediate_steps = options[intermediate_steps_text]
app_usage = load_app_usage(top_apps, data_set_size)
variance = get_variance()

print(
    f"Creating layout of {len(app_usage)} app usage entries using a metric of {metric} with {iterations} iterations. High dimensional clusters - {high_dimensional}, Intermediate Steps - {intermediate_steps}")

plt.figure(figsize=(16.0, 16.0))
if intermediate_steps == True:
    random_state = np.random.randint(0, 100)
    step = iterations/5
    for i in range(1, 6):
        embedding = tsne_embedding(
            app_usage, int(step*i), random_state, metric)
        if high_dimensional:
            k = KMeans(n_clusters=clusters).fit_predict(app_usage)
        else:
            k = KMeans(n_clusters=clusters).fit_predict(embedding)
        spring_layout = _create_algorithm(dataset=app_usage,
                                          algorithm=TSNE,
                                          distance=app_usage_distance, metric=metric)
        draw_layout = DrawLayout(
            dataset=app_usage, spring_layout=spring_layout)
        draw_layout.draw_tsne_facets(
            data=embedding,
            current_plot=i,
            current_iters=int(step*i),
            alpha=0.7,
            point_colors=k,
            annotate=annotate_app_usage,
            algorithm_highlights=True)
else:
    embedding = tsne_embedding(app_usage, iterations, random_state, metric)
    if high_dimensional:
        k = KMeans(n_clusters=clusters).fit_predict(app_usage)
    else:
        k = KMeans(n_clusters=clusters).fit_predict(embedding)
    spring_layout = _create_algorithm(dataset=app_usage,
                                      algorithm=TSNE,
                                      distance=app_usage_distance, metric=metric)
    draw_layout = DrawLayout(
        dataset=app_usage, spring_layout=spring_layout)
    draw_layout.draw_tsne(
        data=embedding,
        alpha=0.7,
        point_colors=k,
        annotate=annotate_app_usage,
        algorithm_highlights=True)

total = time.time() - start

if intermediate_steps == True:
    plt.savefig("../data/outputs/tsne_plots/IntermediateSteps_%dapps_%dentries_%s_%diterations_%r%dclusters_%dperplexity_%.0fs.jpg" %
                (top_apps, data_set_size, metric, iterations, high_dimensional, clusters, 50, total))
else:
    plt.savefig("../data/outputs/tsne_plots/%dapps_%dentries_%s_%diterations_%r%dclusters_%dperplexity_%.0fs.jpg" %
                (top_apps, data_set_size, metric, iterations, high_dimensional, clusters, 50, total))

print(
    f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()
