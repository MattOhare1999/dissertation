from typing import Any, Callable, Dict, List, Optional

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import umap
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.random_projection import GaussianRandomProjection

from forcelayout.metrics import LayoutMetrics

from .algorithms import (BaseSpringLayout, Hybrid, NeighbourSampling, Node,
                         Pivot, SpringForce)
from .draw import DrawLayout


def draw_spring_layout(
        dataset: np.ndarray,
        algorithm: BaseSpringLayout = NeighbourSampling,
        iterations: int = None,
        hybrid_remainder_layout_iterations: int = None,
        hybrid_refine_layout_iterations: int = None,
        hybrid_preset_sample: List[int] = None,
        sample_set_size: int = None,
        neighbour_set_size: int = None,
        pivot_set_size: int = None,
        distance: Callable[[np.ndarray, np.ndarray], float] = None,
        alpha: float = None,
        size: float = None,
        color_by: Callable[[np.ndarray], float] = None,
        color_map: str = None,
        annotate: Callable[[Node, int], str] = None,
        algorithm_highlights: bool = False,
        target_node_speed: float = None,
        high_dimensional: bool = False,
        show_progression: bool = False,
        clusters: int = 4) -> BaseSpringLayout:
    """
    Draw a spring layout diagram of the data using the given algorithm

    dataset: 2d array of the data to lay out
    algorithm: class extending BaseSpringLayout to draw the spring layout diagram
    iterations: number of force iterations to perform on the layout (when using the Hybrid
                algorithm this is the number of force iterations performed on the original sample)
    hybrid_remainder_layout_iterations: number of force iterations to perform on each child of
                                        the remainder subset when using the Hybrid algorithm
    hybrid_refine_layout_iterations: number of force iterations to perform on the whole layout
                                     after the remainder layout stage
    pivot_set_size: number of pivot nodes if algorithm=Pivot
    sample_set_size: size of random sample set
    neighbour_set_size: size of neighbour set for neighbour sampling stages
    distance: function to determine the high dimensional distance between two datapoints
    alpha: opacity of nodes in the diagram in range [0-1]
    size: size of node to draw passed to matplotlib.pyplot.scatter(s=size)
    color_by: function to colour nodes by summarising a datapoint as a float to be expressed through
              color_map
    color_map: string name or matplotlib colour map to use with color_by function
    annotate: callback function for annotating nodes when hovered, given the node being hovered and
              the index in dataset
    algorithm_highlights: allow on click of data point to highlight important nodes for the
                          algorithm
                          NeighbourSampling: neighbour nodes
                          Hybrid: sample set nodes
                          Pivot: pivot nodes
    """
    spring_layout = _create_algorithm(dataset, algorithm, iterations,
                                      hybrid_remainder_layout_iterations,
                                      hybrid_refine_layout_iterations,
                                      hybrid_preset_sample,
                                      pivot_set_size,
                                      sample_set_size,
                                      neighbour_set_size,
                                      distance,
                                      target_node_speed)

    metrics = LayoutMetrics(spring_layout=spring_layout)
    metrics.measure()
    print(" ")
    print("Average Iteration Time: ", metrics.get_average_iteration_time())
    print("Runtime: ", metrics.get_run_time())
    print("Max Memory: ", metrics.get_max_memory())
    print("Stress: ", metrics.get_stress())

    # Plot memory
    # plt.figure(figsize=(8.0, 8.0))
    # plt.plot(metrics.memory.values(), 'b-+', label="Hello")

    # Plot average node speed
    plt.figure(figsize=(8.0, 8.0))
    plt.plot(metrics.avg_node_speed, 'b-+')
    plt.ylabel("Average Node Speed")
    plt.xlabel("Iterations")

    if show_progression:
        for i in range(1, 6):
            current = int(iterations/5)
            draw_layout = DrawLayout(
                dataset=dataset, spring_layout=spring_layout)
            spring_layout.spring_layout(return_after=current)
            if high_dimensional:
                point_colors = KMeans(n_clusters=clusters).fit_predict(dataset)
            else:
                point_colors = KMeans(n_clusters=clusters).fit_predict(
                    spring_layout.get_positions())
            draw_layout.draw_facets(alpha=alpha, current_plot=i, current_iters=current*i, **_create_params(color_by=color_by, color_map=color_map, point_colors=point_colors,
                                                                                                           annotate=annotate, size=size,
                                                                                                           algorithm_highlights=algorithm_highlights))
        return spring_layout

    else:
        plt.figure(figsize=(16.0, 16.0))
        draw_layout = DrawLayout(
            dataset=dataset, spring_layout=spring_layout)
        spring_layout.spring_layout()

        if high_dimensional:
            point_colors = KMeans(n_clusters=clusters).fit_predict(dataset)
        else:
            point_colors = KMeans(n_clusters=clusters).fit_predict(
                spring_layout.get_positions())
        draw_layout.draw(alpha=alpha, **_create_params(color_by=color_by, color_map=color_map, point_colors=point_colors,
                                                       annotate=annotate, size=size,
                                                       algorithm_highlights=algorithm_highlights))
        # draw_layout.save('../data/outputs/spring_models_plots')
        return spring_layout


def draw_spring_layout_animated(
        dataset: np.ndarray,
        algorithm: BaseSpringLayout = NeighbourSampling,
        iterations: int = None,
        hybrid_remainder_layout_iterations: int = None,
        hybrid_refine_layout_iterations: int = None,
        hybrid_preset_sample: List[int] = None,
        sample_set_size: int = None,
        neighbour_set_size: int = None,
        pivot_set_size: int = None,
        distance: Callable[[np.ndarray, np.ndarray], float] = None,
        alpha: float = None,
        size: float = None,
        color_by: Callable[[np.ndarray], float] = None,
        color_map: str = None,
        interval: int = None,
        draw_every: int = None,
        annotate: Callable[[Node, int], str] = None,
        algorithm_highlights: bool = False,
        target_node_speed: float = None) -> matplotlib.animation.FuncAnimation:
    """
    Draw a spring layout diagram of the data using the given algorithm

    dataset: 2d array of the data to lay out
    algorithm: class extending BaseSpringLayout to draw the spring layout diagram
    iterations: number of force iterations to perform on the layout (when using the Hybrid
                algorithm this is the number of force iterations performed on the original sample)
    hybrid_remainder_layout_iterations: number of force iterations to perform on each child of
                                        the remainder subset when using the Hybrid algorithm
    hybrid_refine_layout_iterations: number of force iterations to perform on the whole layout
                                     after the remainder layout stage
    pivot_set_size: number of pivot nodes if algorithm=Pivot
    sample_set_size: size of random sample set
    neighbour_set_size: size of neighbour set for neighbour sampling stages
    distance: function to determine the high dimensional distance between two datapoints
    alpha: opacity of nodes in the diagram in range [0-1]
    size: size of node to draw passed to matplotlib.pyplot.scatter(s=size)
    color_by: function to colour nodes by summarising a datapoint as a float to be expressed through
              color_map
    color_map: string name or matplotlib colour map to use with color_by function
    interval: ms between each frame. If this is set low it will be limited by the run time of the
              algorithm
    algorithm_highlights: allow on click of data point to highlight important nodes for the
                          algorithm
                          NeighbourSampling: neighbour nodes
                          Hybrid: sample set nodes
                          Pivot: pivot nodes
    """
    spring_layout = _create_algorithm(dataset, algorithm, iterations,
                                      hybrid_remainder_layout_iterations,
                                      hybrid_refine_layout_iterations,
                                      hybrid_preset_sample,
                                      pivot_set_size,
                                      sample_set_size,
                                      neighbour_set_size,
                                      distance,
                                      target_node_speed)

    draw_layout = DrawLayout(dataset=dataset, spring_layout=spring_layout)
    return draw_layout.draw_animated(**_create_params(alpha=alpha, color_by=color_by,
                                                      color_map=color_map, interval=interval,
                                                      draw_every=draw_every, annotate=annotate,
                                                      size=size,
                                                      algorithm_highlights=algorithm_highlights))


def spring_layout(
        dataset: np.ndarray,
        algorithm: BaseSpringLayout = NeighbourSampling,
        iterations: int = None,
        hybrid_remainder_layout_iterations: int = None,
        hybrid_refine_layout_iterations: int = None,
        hybrid_preset_sample: List[int] = None,
        pivot_set_size: int = None,
        sample_set_size: int = None,
        neighbour_set_size: int = None,
        distance: Callable[[np.ndarray, np.ndarray], float] = None,
        target_node_speed: float = None) -> BaseSpringLayout:
    """
    Create an istance of a spring layout algorithm

    dataset: 2d array of the data to lay out
    algorithm: class extending BaseSpringLayout to draw the spring layout diagram
    iterations: number of force iterations to perform on the layout (when using the Hybrid
                algorithm this is the number of force iterations performed on the original sample)
    hybrid_remainder_layout_iterations: number of force iterations to perform on each child of
                                        the remainder subset when using the Hybrid algorithm
    hybrid_refine_layout_iterations: number of force iterations to perform on the whole layout
                                     after the remainder layout stage
    pivot_set_size: number of pivot nodes if algorithm=Pivot
    sample_set_size: size of random sample set
    neighbour_set_size: size of neighbour set for neighbour sampling stages
    distance: function to determine the high dimensional distance between two datapoints
    """
    layout = _create_algorithm(dataset, algorithm, iterations,
                               hybrid_remainder_layout_iterations,
                               hybrid_refine_layout_iterations,
                               hybrid_preset_sample,
                               pivot_set_size,
                               sample_set_size,
                               neighbour_set_size,
                               distance,
                               target_node_speed)
    return layout


def _create_algorithm(
        dataset: np.ndarray,
        algorithm: BaseSpringLayout,
        iterations: int = None,
        hybrid_remainder_layout_iterations: int = None,
        hybrid_refine_layout_iterations: int = None,
        hybrid_preset_sample: List[int] = None,
        pivot_set_size: int = None,
        sample_set_size: int = None,
        neighbour_set_size: int = None,
        distance: Callable[[np.ndarray, np.ndarray], float] = None,
        target_node_speed: float = None,
        metric: str = 'euclidean',
        metric_kwds: dict = None) -> BaseSpringLayout:
    """
    Create the spring model algorithm with the given dataset and parameters
    """
    spring_layout: Optional[BaseSpringLayout] = None
    if algorithm is Pivot:
        params = _create_params(distance_fn=distance, sample_layout_iterations=iterations,
                                remainder_layout_iterations=hybrid_remainder_layout_iterations,
                                refine_layout_iterations=hybrid_refine_layout_iterations,
                                preset_sample=hybrid_preset_sample,
                                random_sample_size=sample_set_size,
                                pivot_set_size=pivot_set_size,
                                target_node_speed=target_node_speed)
        spring_layout = Pivot(dataset=dataset, **params)
    elif algorithm is Hybrid:
        params = _create_params(distance_fn=distance, sample_layout_iterations=iterations,
                                remainder_layout_iterations=hybrid_remainder_layout_iterations,
                                refine_layout_iterations=hybrid_refine_layout_iterations,
                                preset_sample=hybrid_preset_sample,
                                random_sample_size=sample_set_size,
                                target_node_speed=target_node_speed)
        spring_layout = Hybrid(dataset=dataset, **params)
    elif algorithm is NeighbourSampling:
        params = _create_params(distance_fn=distance, iterations=iterations,
                                neighbour_set_size=neighbour_set_size,
                                sample_set_size=sample_set_size,
                                target_node_speed=target_node_speed)
        spring_layout = NeighbourSampling(dataset=dataset, **params)
    elif algorithm is TSNE:
        spring_layout = TSNE(
            n_components=2, metric=metric).fit_transform(dataset)
    elif algorithm is umap:
        spring_layout = umap.UMAP(
            metric=metric, min_dist=0.1, spread=0.75, metric_kwds=metric_kwds).fit_transform(dataset)
    elif algorithm is GaussianRandomProjection:
        spring_layout = GaussianRandomProjection(
            n_components=2).fit_transform(dataset)
    else:
        params = _create_params(distance_fn=distance, iterations=iterations,
                                target_node_speed=target_node_speed)
        spring_layout = SpringForce(dataset=dataset, **params)
    return spring_layout


def _create_params(**kwargs) -> Dict[str, Any]:
    if kwargs is not None:
        return {k: v for k, v in kwargs.items() if v is not None}
    return dict()
