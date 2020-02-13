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

intermediate_steps_options = {
    'true': True,
    'false': False,
}

metrics = ["euclidean", "hamming"]

if len(sys.argv) < 3:
    print(f'\nusage: python3 umap_clustering.py <num apps> <dataset size> <metric> <iterations> <intermediate_steps>')
    print('\tApps: see datasets/app_usage')
    print('\tSizes: see datasets/app_usage')
    print('\tMetric: euclidean, hamming')
    print('\tIterations: Multiple of 5 between 100 and 5000')
    print('\tIntermediate_steps: true, false')
    exit(1)

if len(sys.argv) > 3 and sys.argv[3].lower() not in metrics:
    print('\tAvailable metrics: euclidean, hamming')

if len(sys.argv) > 4 and (int(sys.argv[4]) < 100 or int(sys.argv[4]) > 5000 or int(sys.argv[4]) % 5 != 0):
    print('\tIterations must be of a multiple of 5 and between 250 and 5000. 1250 if next arguement is true')

if len(sys.argv) > 5 and sys.argv[5] not in intermediate_steps_options:
    print('\tAvailable options for progression: true, false')
    exit(1)

top_apps = int(sys.argv[1])
data_set_size = int(sys.argv[2])
metric = sys.argv[3].lower() if len(sys.argv) > 3 else 'euclidean'
iterations = int(sys.argv[4]) if len(sys.argv) > 4 else 1000
intermediate_steps_text = sys.argv[5].lower() if len(sys.argv) > 5 else 'false'
intermediate_steps = intermediate_steps_options[intermediate_steps_text]
app_usage = load_app_usage(top_apps, data_set_size)
variance = get_variance()

print(
    f"Creating layout of {len(app_usage)} app usage entries using a metric of {metric} with {iterations} iterations. Intermediate Steps - {intermediate_steps}")

plt.figure(figsize=(8.0, 8.0))
start = time.time()

# best one seems to be 50 for 7500
perplex = [20, 30, 40, 50]

if intermediate_steps == True:
    random_state = np.random.randint(0, 100)
    for i in range(5, 0, -1):
        print(i)
        embedding = TSNE(n_iter=int(iterations/i), random_state=random_state, metric=metric,
                         perplexity=50).fit_transform(app_usage)
        k = KMeans(n_clusters=4).fit_predict(app_usage)
        spring_layout = _create_algorithm(dataset=app_usage,
                                          algorithm=TSNE,
                                          distance=app_usage_distance, metric=metric)
        draw_layout = DrawLayout(
            dataset=app_usage, spring_layout=spring_layout)
        draw_layout.draw_tsne_facets(
            data=embedding,
            current_plot=i,
            current_iters=int(iterations/i),
            alpha=0.7,
            point_colors=k,
            annotate=annotate_app_usage,
            algorithm_highlights=True)
else:
    embedding = TSNE(n_iter=5000, metric=metric,
                     perplexity=50).fit_transform(app_usage)

    k = KMeans(n_clusters=4).fit_predict(embedding)
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
    plt.savefig("../data/outputs/tsne_plots/IntermediateSteps_%dapps_%dentries_%s_%diterations_%dperplexity_%.0fs.jpg" %
                (top_apps, data_set_size, metric, iterations, perplex[3], total))
else:
    plt.savefig("../data/outputs/tsne_plots/%dapps_%dentries_%s_%dperplexity_%.0fs.jpg" %
                (top_apps, data_set_size, metric, perplex[3], total))

print(
    f'\nLayout time: {"%.2f" % total}s ({"%.1f" % (total / 60)} mins)')

plt.show()
