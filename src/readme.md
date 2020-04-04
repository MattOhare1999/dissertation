# Dimensionality Reduction Algorithms

This software implements six different dimensionality reduction algorithms in Python:
* [Chalmers' 1996 algorithm](https://ieeexplore.ieee.org/document/567787)
* [Hybrid Layout algorithm](https://ieeexplore.ieee.org/document/1173161)
* [Pivot Layout algorithm](https://ieeexplore.ieee.org/document/1249012)
* [Random Projection](https://scikit-learn.org/stable/modules/random_projection.html)
* [t-SNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#examples-using-sklearn-manifold-tsne)
* [UMAP](https://umap-learn.readthedocs.io/en/latest/basic_usage.html)

All three Spring Model algorithms were adapted from an implementation created from another project - https://github.com/Iain530/force-directed-layout-algorithms

The dataset used is iOS app usage and this can be found in `algorithms/datasets/`  where a sample of subsets are located. This software produces the layouts created by these six algorithms using this data. These layouts are interactive and can be adapted to fit the purpose required through various command line arguments.

## Structure

The structure of this project is as follows:
```
algorithms
├── app_usage_utils.py
├── random_projection_layout.py
├── spring_model_layout.py
├── tsne_layout.py
├── umap_layout.py
├── datasets
│   ├── top_100_apps
│   │   ├── top*_app_usage*.csv
│   ├── top_300_apps
│   ├── top_500_apps
│   ├── top_1000_apps
│   ├── top_10000_apps
│   └── top_45788_apps
└── layout
    ├── spring_models
    │   ├── base_spring_layout.py
    │   ├── hybrid.py
    │   ├── neighbour_sampling.py
    │   ├── node.py
    │   ├── pivot.py
    │   ├── spring_force.py
    │   └── __init__.py
    ├── distance.py
    ├── draw.py
    ├── layout.py
    ├── metrics.py
    ├── utils.py
    └── __init__.py
```

## Setup and Requirements

To run this software, dependencies must first be installed.

```bash
python3 -m pip install -r requirements.txt
```

This will install all the necessary pre-requisites required to set up this project which include:

* Python 3.7
* Packages: listed in 'requirements.txt'
* Tested on Ubuntu 18.04

### Usage

See [manual.md](manual.md) for full documentation on how to use this software.

### Test steps

To ensure that all dependences have installed properly and the software is working as it should, run the following command:

```bash
# python3 umap_layout.py <num apps> <dataset size>
python3 algorithms/umap_layout 100 1000
```

A layout should be produced in ~9s. If successful then everything has installed correctly.

