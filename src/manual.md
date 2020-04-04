# User manual 

This documents how to use the software in full. If [readme.md](readme.md) has been followed then the following code can executed without issue to create layouts. Firstly, navigate to the correct folder:

'''bash
cd algorithms
'''

Each algorithm has different command line arguments and so they are each split into sections to show their individual implementations.

## Spring Models
Spring Models can have up to a maximum of 7 command line arguments which can be shown by calling:

'''bash
python3 spring_model_layout.py
'''

* num apps: the number of dimensions, available options can be found in `datasets/top_{num apps}_apps` as the first number in the file name; top{num apps}_app_usage{dataset size}.csv
* dataset size: the number of data points, available options can be found in `datasets/top_{num apps}_apps` as the second number in the file name; top{num apps}_app_usage{dataset size}.csv
* algorithm: available options are: `chalmers96`, `hybrid` and `pivot`
* iterations: the number of spring model iterations, multiple of 5 between 50 and 1000
* high dimensional: option to display high-dimensional or low-dimensional clusters, `true` or `false`
* clusters: number of clusters to be visualised, between 1 and 10
* intermediate steps: option to show facets of the layout after every `iterations/5` iterations, `true` or `false`

To create a layout with these arguments, simply run the following.

With required parameters only, using default values for all optional:

'''bash
# python3 spring_model_layout.py *REQUIRED* [num apps] [dataset size] *OPTIONAL* [algorithm] [iterations] [high dimensional] [clusters] [intermediate_steps]
python3 spring_model_layout.py 100 7504
'''

With all required and optional parameters, overwriting default values: 

'''bash
# python3 spring_model_layout.py *REQUIRED* [num apps] [dataset size] *OPTIONAL* [algorithm] [iterations] [high dimensional] [clusters] [intermediate_steps]
python3 spring_model_layout.py 100 7504 hybrid 50 true 2 false
'''

## Random Projection
Random Projection can have up to a maximum of 3 command line arguments which can be shown by calling:

'''bash
python3 random_projection_layout.py
'''

* num apps: the number of dimensions, available options can be found in `datasets/top_{num apps}_apps` as the first number in the file name; top{num apps}_app_usage{dataset size}.csv
* dataset size: the number of data points, available options can be found in `datasets/top_{num apps}_apps` as the second number in the file name; top{num apps}_app_usage{dataset size}.csv
* clusters: number of clusters to be visualised, between 1 and 10

To create a layout with these arguments, simply run the following.

With required parameters only, using default values for all optional:

'''bash
# tsne_layout.py *REQUIRED* [num app][dataset size] *OPTIONAL* [clusters]
python3 random_projection_layout.py 100 7504
'''

With all required and optional parameters, overwriting default values: 

'''bash
# tsne_layout.py *REQUIRED* [num app][dataset size] *OPTIONAL* [clusters]
python3 random_projection_layout.py 100 7504 2
'''


## t-SNE
t-SNE can have up to a maximum of 7 command line arguments which can be shown by calling:

'''bash
python3 tsne_layout.py
'''

* num apps: the number of dimensions, available options can be found in `datasets/top_{num apps}_apps` as the first number in the file name; top{num apps}_app_usage{dataset size}.csv
* dataset size: the number of data points, available options can be found in `datasets/top_{num apps}_apps` as the second number in the file name; top{num apps}_app_usage{dataset size}.csv
* metric: distance metrice to be used, available options are: `seuclidean`, `euclidean` and `hamming`
* iterations: the number of spring model iterations, multiple of 5 between 250 (or 1250 if intermediate steps = True) and 5000
* high dimensional: option to display high-dimensional or low-dimensional clusters, `true` or `false`
* clusters: number of clusters to be visualised, between 1 and 10
* intermediate steps: option to show facets of the layout after every `iterations/5` iterations, `true` or `false`

To create a layout with these arguments, simply run the following.

With required parameters only, using default values for all optional:

'''bash
# tsne_layout.py *REQUIRED* [num app][dataset size] *OPTIONAL* [metric] [iterations] [high dimensional] [clusters] [intermediate steps]
python3 tsne_layout.py 100 7504
'''

With all required and optional parameters, overwriting default values: 

'''bash
# tsne_layout.py *REQUIRED* [num app][dataset size] *OPTIONAL* [metric] [iterations] [high dimensional] [clusters] [intermediate steps]
python3 tsne_layout.py 100 7504 seuclidean 1000 true 2 false
'''


## UMAP
UMAP can have up to a maximum of 7 command line arguments which can be shown by calling:

'''bash
python3 umap_layout.py
'''

* num apps: the number of dimensions, available options can be found in `datasets/top_{num apps}_apps` as the first number in the file name; top{num apps}_app_usage{dataset size}.csv
* dataset size: the number of data points, available options can be found in `datasets/top_{num apps}_apps` as the second number in the file name; top{num apps}_app_usage{dataset size}.csv
* metric: distance metrice to be used, available options are: `seuclidean`, `euclidean` and `hamming`
* type: type of visualisation to be displayed, available options are: `default`, `connectivity`, `diagnostic`, `interactive1`, `interactive2`, `3d`
* high dimensional: option to display high-dimensional or low-dimensional clusters, `true` or `false`
* clusters: number of clusters to be visualised, between 1 and 10

To create a layout with these arguments, simply run the following.

With required parameters only, using default values for all optional:

'''bash
# umap_layout.py *REQUIRED* [num apps] [dataset size] *OPTIONAL* [metric] [type] [high dimensional] [clusters]
python3 tsne_layout.py 100 7504
'''

With all required and optional parameters, overwriting default values: 

'''bash
# umap_layout.py *REQUIRED* [num apps] [dataset size] *OPTIONAL* [metric] [type] [high dimensional] [clusters]
python3 umap_layout.py 100 7504 seuclidean default true 2
'''

All of these layouts are saved to `../../data/outputs`.